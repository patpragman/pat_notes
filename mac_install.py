from pathlib import Path
import os
import argparse
import shutil

parser = argparse.ArgumentParser()
path_to_app_folder_arg_name = "path_to_app_folder"
path_to_notes_folder_arg_name = "path_to_notes_folder"

parser.add_argument("--path_to_app_folder_arg_name", default=os.getcwd())
parser.add_argument("--path_to_notes_folder_arg_name", default=os.getcwd())



if __name__ == "__main__":
    # run me in sudo please!
    args = parser.parse_args()
    print("Opening launcher_template")
    with open("launch_template.sh", "r") as launch_template:
        raw_launcher_script = launch_template.read().replace(
            f"<{path_to_notes_folder_arg_name}>", args.path_to_app_folder_arg_name
        ).replace(
            f"<{path_to_app_folder_arg_name}>", args.path_to_app_folder_arg_name)

        print(f"creating launcher at:  {args.path_to_app_folder_arg_name}/launch.sh")
        with open(f"{args.path_to_app_folder_arg_name}/launch.sh", "w") as launcher_script:
            launcher_script.write(raw_launcher_script)

    print('changing permissions for notepad.py...')
    os.system(f"chmod u+rwx {args.path_to_app_folder_arg_name}/notepad.py")
    print('changing permissions for launch.sh')
    os.system(f"chmod u+rwx {args.path_to_app_folder_arg_name}/launch.sh")

    print("changing .bash_profile file...")
    with open(f"{Path.home()}/.bash_profile", "a") as bash_profile_file:
        alias = f"alias notepad='{args.path_to_app_folder_arg_name}/launch.sh'"
        print(alias)
        bash_profile_file.write("\n")
        bash_profile_file.write(alias)

    with open(f"{args.path_to_app_folder_arg_name}/notepad.py", "r") as app:
        s = app.read().replace("/usr/bin/env python", shutil.which("python3"))

    with open(f"{args.path_to_app_folder_arg_name}/notepad.py", "w") as app:
        app.write(s)

    os.system(f"source {Path.home()}/.bash_profile")
