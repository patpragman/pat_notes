# Pat Notes

I got sick and tired of writing notes in a plethora of various text files.
I didn't want anything complicated, I wanted one set of notes per day.
That is it.

You can't search with it.  You can't do much of anything, but save notes by day.
## Requirements
I am running Python 3.10.4 at the time of writing this, but it will probably run on lower versions.  It uses only the standard library.


## Basic Install
1. Download or clone the repo
2. make sure theres a folder called `notes` in the same folder as notepad.py
3. run the file `notepad.py`
4. enjoy

If you want your notes to point to a different file than the one in the pat_notes directory, it supports one command line argument.

`--path path/to/notes/folder`

## Permanent Install


To make this work easily make it executable, change to the directory it lives in, then
`chmod u=rwx notepad.py`
then down at the bottom create an alias

`alias notepad='cd ~/path/to/pat_notes && ./notepad.py --path /path/to/notes folder && cd -`

this way when you pull up the notes app, it will run, and when you're done with it you go back to the directory you were in.

