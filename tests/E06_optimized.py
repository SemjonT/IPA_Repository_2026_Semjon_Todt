"""A simple text-based adventure game with random events."""

import random


def intro() -> None:
    """Print the game introduction and scenario."""
    print("Willkommen zum Mini-Abenteuer!")
    print("Du stehst vor zwei Türen: links oder rechts.")


def choose_door() -> str:
    """Prompt the user to choose a door.

    Returns:
        The user's choice as a lowercase string.
    """
    choice = input("Welche Tür wählst du? (links/rechts): ")
    return choice.lower()


def left_room() -> None:
    """Handle the left room scenario with random events."""
    print("Du betrittst den linken Raum...")
    event = random.choice(["schatz", "monster"])
    if event == "schatz":
        print("Du hast einen Schatz gefunden! 🎉")
    else:
        print("Ein Monster erscheint! 😱")
        fight()


def right_room() -> None:
    """Handle the right room scenario (safe exit)."""
    print("Du betrittst den rechten Raum...")
    print("Du findest einen geheimen Ausgang. Du bist frei! 🏃")


def fight() -> None:
    """Handle combat mechanics with random outcomes."""
    action = input("Willst du kämpfen oder fliehen? ")
    if action.lower() == "kämpfen":
        if random.random() > 0.5:
            print("Du hast das Monster besiegt! 💪")
        else:
            print("Das Monster hat dich besiegt... 💀")
    else:
        print("Du bist erfolgreich geflohen! 🏃")


def main() -> None:
    """Main game loop orchestrating the adventure."""
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