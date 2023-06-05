def namecount(Input):
    List = NameInput.split(',')
    Count = len(List)
    return Count

NameInput = input("enter names separated by commas: ")
WordCount = namecount(NameInput)
print(WordCount)
