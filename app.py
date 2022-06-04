import operator
import tkinter as tk
from datetime import datetime, timedelta

class App:

    def __init__(self, file_path="notes"):
        # initialize the geometry and window positioning to start the app
        self.file_path = file_path
        self.root = tk.Tk()
        self.root.title("PatNotes")
        self.root.geometry('300x400+50+50')
        self.root.resizable(False, False)
        #  self.root.iconbitmap('tbd')  # icon bit map

        # now let's generate the control panel layout
        self.control_pane = tk.Frame(self.root)
        self.control_pane.pack(side=tk.TOP)
        tk.Label(self.control_pane, text="Pat Notes").pack(side=tk.TOP)
        tk.Button(self.control_pane,
                  text="<-",
                  command=lambda: self._load_notes(direction=operator.sub)
                  ).pack(side=tk.LEFT)
        tk.Button(self.control_pane,
                  text="->",
                  command=lambda: self._load_notes(direction=operator.add)
                  ).pack(side=tk.RIGHT)


        self.text_panel = tk.Frame(self.root)
        self.text_panel.pack(side=tk.BOTTOM)

        self.date_label_variable = tk.StringVar(self.root, f"DATE:{datetime.utcnow().date()}", "date")
        self.date_label = tk.Label(self.text_panel, textvariable="date")
        self.date_label.pack(side=tk.TOP)

        # text box
        self.cur_text = tk.Text(self.text_panel, wrap=tk.WORD)
        self.cur_text.pack(expand=True, side=tk.BOTTOM)
        self.cur_text.bind("<KeyRelease>", self._save)

        self.current_date = datetime.utcnow()

        # load notes initially
        self._load_notes(start_up=True)

    def get_file_path(self, date_to_use):
        return f"{self.file_path}/{date_to_use.date()}.note"

    def _clear(self):
        self.cur_text.delete("1.0", tk.END)


    def _load_notes(self, direction=operator.sub, start_up=False):
        if start_up:
            # if we're starting up we don't need to change the date
            pass
        else:
            self.current_date = direction(self.current_date, timedelta(days=1))

        self.date_label_variable.set(f"DATE:{self.current_date.date()} UTC")
        try:
            with open(self.get_file_path(self.current_date), "r") as fp:
                self._clear()
                todays_notes = fp.read()
                self.cur_text.insert(tk.END, todays_notes)
        except FileNotFoundError:
            # if you can't find a date, go back a day and try again, if you go back to far
            # don't do anything at all

            if self.current_date.date() <= datetime(year=2022, month=5, day=1).date():
                # we don't bother with days before 1MAY2022, if you get there, go back
                self._load_notes(direction=operator.add)
            elif self.current_date.date() > datetime.utcnow().date():
                # if it occurs after today, we don't care, we can just make a new note
                self._load_notes(direction=operator.sub)
            elif self.current_date.date() == datetime.utcnow().date():
                self._clear()
            else:
                self._load_notes(direction=direction)

    def run(self):
        self.root.mainloop()

    def _save(self, args):

        with open(f"{self.get_file_path(self.current_date)}", "w") as fp:
            fp.write(self.cur_text.get('1.0', 'end-1c'))