# set up variable
owner = "Sesame"
secret = "secret0001"

comer = input("who are you?")

if comer == owner:
    password = input("what is the password?")
    print(f"Hi, {owner}")
    if comer == owner and password == secret:
        print("Sesame door is opening...")
    else:
        print("Nothing here.")
print("Nice view around her...")
