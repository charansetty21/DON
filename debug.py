import os
import shutil
import sys

print("Python:", sys.executable)
print("PATH:", os.environ["PATH"])
print("shutil.which('piper'):", shutil.which("piper"))