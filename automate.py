import venv
import os
import subprocess

venv_dir = os.path.join(os.getcwd(), "venv")
full_path = os.path.join("venv", "bin", "activate")
print("first: "+ full_path)
#venv.create(venv_dir)

subprocess.Popen("virtualenv venv --python=python3", shell=True)

#subprocess.run("source venv/bin/activate")

subprocess.Popen(full_path, shell=True)
subprocess.Popen("pip install -r requirements.txt", shell=True);
lab2_path = os.path.join(os.getcwd(), "lab2")
subprocess.Popen("npm install", shell=True, cwd=lab2_path);
subprocess.Popen("npx esbuild main.js --bundle --minify --sourcemap --outfile=./emojis/static/main.min.js", shell=True, cwd=lab2_path);


