import venv
import os

venv_dir = os.path.join(os.getcwd(), "venv2")
print(venv_dir)
venv.create(venv_dir)
full_path = os.path.join("/home", "Scripts/activate")
print("this: " + full_path)
#exec(open(os.path.join(venv_dir, "/Scripts/activate")).read())
