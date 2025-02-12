import os
import subprocess
import sys

def windows():
    exe_path = os.path.join(os.path.dirname(__file__), 'jc.exe')
    subprocess.run([exe_path])

def linux():
    subprocess.run(["python3", "-m", "json_corrector.jc"])

def main():
    if "linux" in sys.platform:
        linux()
    elif "win" in sys.platform:
        windows()

if __name__ == "__main__":
    main()
