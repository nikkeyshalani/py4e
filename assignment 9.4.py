"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""
d = {}
l = []
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line = line.strip()
    if not line.startswith("From "):
        continue
    words = line.split()
    l.append(words[1])
for i in l:
    d[i] = d.get(i,0)+1
largest = -1
word = None
for i,j in d.items():
    if j>largest:
        largest = j
        word = i
print(word,largest)