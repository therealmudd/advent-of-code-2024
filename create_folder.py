import os
import shutil

def create_new_folder():
    # Get sorted list of folders starting with "day_"
    day_folders = sorted((folder for folder in os.listdir() if folder.startswith("day_")), key=lambda x: int(x[4:]))
    
    last_folder = day_folders[-1] if day_folders else "day_0"
    new_folder = f"day_{int(last_folder[4:]) + 1}"
    
    os.makedirs(new_folder, exist_ok=True)
    
    shutil.copy("template_solution.py", os.path.join(new_folder, "solution_part_1.py"))
    shutil.copy("template_solution.py", os.path.join(new_folder, "solution_part_2.py"))
    with open(os.path.join(new_folder, "input.txt"), "w"):
        pass

create_new_folder()
