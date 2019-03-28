import re

with open("sometext.txt", "r") as file:
    text = file.read()

mylist = sorted(re.findall(r"[\w]+", text))
n = len(mylist)

with open("outputfile.txt", "w") as file:
    for i in range(n - 1):
        if mylist[i] == mylist[i + 1]:
            file.write(mylist[i])
            file.write(' ')									# print(mylist[i], end=' ')
        else:
            file.write(mylist[i])
            file.write('\n')								# print(mylist[i])

    file.write(mylist[n - 1])								# print(mylist[n - 1])
