def check_francais(input_text):
    while True:
        answer = input(input_text)
        if answer.lower() in ["yes", "y", "no", "n"]:
            print("En francais!!!!!!")
        elif answer.lower() == "non":
            return False
        elif answer.lower() == "oui":
            return True
        else:
            print("Simple question, OUI OU NON!!!")

print('''
Goupy Deux was the most frightening and terrifying fighter plane in all of France (in 1920).
Other fighter planes quivered before it.
''')

answer = check_francais("Do you want to hear more about Goupy?")
if not answer:
    print("Boo you suck")
    exit()

print("HON HON HON you have accepted your mission. Very well monsieur")
print("WAit un champion must eat breakfast first!!")
answer = input("Pain au chocolat or donut?")

if answer.lower() == "donut":
    print("Americain! YOu are an enemy of the state! Spy detected! YOur mission ends here")
    exit()
elif answer.lower() == "pain au chocolat":
    print("Bon choix monsieur")
    print("You wipe the crumbs from your moustache")
else:
    print("fine go hungry then")

answer = check_francais("Are you ready to fly monsieur?")

if not answer:
    print("THen what are you doing here?! FLEE monsieur. s'il vous plait.")
    exit()

answer = check_francais("Do you have everything you need?")

