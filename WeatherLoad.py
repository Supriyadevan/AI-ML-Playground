import json


try:
    
    path = r"C:\Users\nitta\vsExampleWorkspace\Weather.JSON"

    f = open(path)
    
    try:
        dictionary = json.load(f)
        print(dictionary)
    except:
        print("Unable to load JSON")
    finally:
        print("Entered Finally ")
        

except:
    raise Exception("Unable to open file")

finally:
    f.close()

