NewPwd = input("Enter a new password: ")

Result = {}

if len(NewPwd) >= 8:
    Result["length"] = True
else:
    Result["length"] = False

digit = False
for item in NewPwd:
    if item.isdigit() == True:
        digit = True

Result["digit"] = digit

Upper = False
for item in NewPwd:
    if item.isupper() == True:
        Upper = True

Result["Upper"] = Upper

print(Result)
print(Result.values())

if all(Result.values()):
    print("Great password there!")
else:
    print("weak password")

