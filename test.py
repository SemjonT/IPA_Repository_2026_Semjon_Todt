import random

# Test 2

def intro():
    print("Willkommen zum Mini-Abenteuer!")
    print("Du stehst vor zwei Türen: links oder rechts.")

def choose_door():
    choice = input("Welche Tür wählst du? (links/rechts): ")
    return choice.lower()

def left_room():
    print("Du betrittst den linken Raum...")
    event = random.choice(["schatz", "monster"])
    if event == "schatz":
        print("Du hast einen Schatz gefunden! 🎉")
    else:
        print("Ein Monster erscheint! 😱")
        fight()

def right_room():
    print("Du betrittst den rechten Raum...")
    print("Du findest einen geheimen Ausgang. Du bist frei! 🏃")

def fight():
    action = input("Willst du kämpfen oder fliehen? ")
    if action.lower() == "kämpfen":
        if random.random() > 0.5:
            print("Du hast das Monster besiegt! 💪")
        else:
            print("Das Monster hat dich besiegt... 💀")
    else:
        print("Du bist erfolgreich geflohen! 🏃")

def main():
    intro()
    door = choose_door()
    if door == "links":
        left_room()
    elif door == "rechts":
        right_room()
    else:
        print("Ungültige Wahl.")

if __name__ == "__main__":
    main()