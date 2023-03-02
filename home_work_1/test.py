import os

with open(os.path.dirname(__file__) + "/requirements.txt", encoding="utf-8") as requirements_file:
  if (os.path.isdir(os.path.dirname(__file__) + "/env/Lib/site-packages/pynput")
  and "pynput==" in requirements_file.read()):
    print("execution t")
  else:
    print("termination")
