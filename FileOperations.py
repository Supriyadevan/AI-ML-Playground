essay = open("essay.txt","w")
text = ["hello\n","world\n","This is me"]
essay.writelines(text)
essay.close()

essay = open("essay.txt","r")
content = essay.readlines()
print(content)
print(len(content))
essay.close()

content2 = "count"
print(len(content2))
