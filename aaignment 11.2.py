import re
name = input("Enter the file name:")
if len(name)<1:
    name = "Actual-data"
handle = open(name)
num = []
for line in handle:
    line = line.rstrip()
    lst = re.findall('[0-9]+', line)
    if len(lst)<0:
        continue
    for i in lst:
        num.append(i)
print(num)
sum = 0

for i in num:
    sum = sum+int(i)
print(sum,len(num))