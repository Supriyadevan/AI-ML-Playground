path = r"C:\Users\nitta\vsExampleWorkspace\TextFile.txt"
f = open(path,"a")
f.write("\nThis is Supriya's line")
f.close()

updatedFile = open(path)
print(updatedFile.read())
updatedFile.close()