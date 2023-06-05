path = r"C:\Users\nitta\vsExampleWorkspace\TextFile.txt"
f = open(path)
for i in f:
    #print("Printing TEXT blocks", i)
    print(f.readlines())
f.close()



