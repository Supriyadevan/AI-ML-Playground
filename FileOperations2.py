filenames = ["a.txt","b.txt","c.txt"]

for files in filenames:
    file = open(files,"r")
    fileread = file.readlines()
    file.close()
    print(fileread,"\n")

user_entries = ['10', '19.1', '20']

total = []
for item in user_entries:
    total.append(float(item))
grand = (sum(total))
print(grand)

with open("a.txt", 'r') as file:
    X = file.read()
    print(X)
print(len(X))















