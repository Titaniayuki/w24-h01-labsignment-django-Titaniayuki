import venv
import os
import subprocess

venv_dir = os.path.join(os.getcwd(), "venv")
full_path = os.path.join(os.getcwd(), "venv", "bin", "activate")
print("FULL PATH: "+ full_path)
#venv.create(venv_dir)

subprocess.Popen("virtualenv venv --python=python3", shell=True)
print("CREATED VIRTUALENV")
#subprocess.run("source venv/bin/activate")

subprocess.Popen("source " + full_path, shell=True)
subprocess.Popen("pip install -r requirements.txt", shell=True)
print("INSTALL DJANGO")

lab2_path = os.path.join(os.getcwd(), "lab2")
os.chdir(lab2_path)
print("CHANGED DIRECTORIES? :" + os.getcwd())
subprocess.Popen("npm install express", shell=True)
#os.system("npm install express")
print("RAN NPM INSTALL")

subprocess.Popen("npx esbuild main.js --bundle --minify --sourcemap --outfile=./emojis/static/main.min.js", shell=True)
#subprocess.Popen("python manage.py makemigrations", shell=True)
#subprocess.Popen("python manage.py migrate", shell=True)
subprocess.Popen("python3 manage.py runserver 0.0.0.0:8000", shell=True)
#

