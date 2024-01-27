import venv
import os
import subprocess
import sys

print("current directory: " + os.getcwd())
#create virtual env
os.system("virtualenv venv --python=python3")

python_path = os.path.join(os.getcwd(), "venv", "bin", "python-script.py")
full_path = os.path.join(os.getcwd(), "venv", "bin", "activate_this.py")
print("full path: " + full_path)
print("python path: " + python_path)

#activate virtual env
exec(open(full_path).read(), {'__file__': full_path})
os.system("which python")

#install django
os.system("pip install -r requirements.txt")
lab2_path = os.path.join(os.getcwd(), "lab2")

#change directory
os.chdir(lab2_path)
print("current directory: " + os.getcwd())

#install emoji-mart and esbuild
os.system("npm install")

#Transpile main.js to the static directory
os.system("npx esbuild main.js --bundle --minify --sourcemap --outfile=./emojis/static/main.min.js")

#runserver
os.system("python3 manage.py runserver 0.0.0.0:8000")
