file = []
while(True):
    with open("a.txt","r") as flipper:
        file = flipper.readlines()
        print("Length of the List:", len(file))
        print(file)

    Outcome = input("Throw the coin and enter head or tails:" + "\n")
    file.append(Outcome + "\n")
    print("New Value:",Outcome)

    with open("a.txt","w") as flipper1:
         flipper1.writelines(file)
    print("Added value", file)

    HeadCount = file.count("Head\n")

    print(HeadCount)
    print(len(file))

    Percentage =  HeadCount / len(file) * 100
    print("Percentage:",Percentage)






