import os
import subprocess
import sys
from json_corrector import jc

def windows():
    exe_path = os.path.join(os.path.dirname(__file__), 'jc.exe')
    for i in sys.argv:
        print(i)
    subprocess.run([exe_path] + sys.argv[1:])

def linux():
    #print(sys.argv[1])
    for i in sys.argv:
        print(i)
    subprocess.run(["python3", "-m", "json_corrector.jc"])
    #jc.main(sys.argv[1:])

def main():
    if "linux" in sys.platform:
        linux()
    elif "win" in sys.platform:
        windows()

if __name__ == "__main__":
    main()
