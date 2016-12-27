import os
import subprocess
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for fileName in files:
    parts = fileName.split(".")
    if (parts[-1] != "pdf"):
        continue
    print fileName
    script = "condenseSlides.py " + fileName

    subprocess.Popen(script, shell=True)
