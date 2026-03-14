#f = open("demofile.txt", "x") # Read - Default value. Opens a file for reading, error if the file does not exist
f = open("demofile.txt") 
#f = open("demofile.txt", "a") # Append - Opens a file for appending, creates the file if it does not exist
#f = open("demofile.txt", "w") # Write - Opens a file for writing, creates the file if it does not exist

with open("demofile.txt") as f:
  print(f.read())

f = open("demofile.txt")
print(f.readline())
f.close()

with open("demofile.txt") as f:
  print(f.read(5))

with open("demofile.txt") as f:
  print(f.readline())
  print(f.readline())

with open("demofile.txt") as f:
  for x in f:
    print(x)