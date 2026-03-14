import os
os.remove("demofile.txt")

#Check if file exists, then delete it:

if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist") 