fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("file name not exist")
    quit()
for line in fh:
    line = line.rstrip()
    print(line.upper())
