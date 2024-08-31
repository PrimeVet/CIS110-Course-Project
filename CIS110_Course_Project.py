print(f"Hi, there! Welcome to the adbenture of Barvatos the Viking lord!")
print(f"Before the story begins, I have a few questions I need you to answer.")
print(f"After you type your answer, press enter.")
input(f"\nPress the enter key to continue...")

keepPlaying = "yes"
while keepPlaying.lower() == "yes":

    #5 Questions Before the story begins
    advisor_name = input(f"\nWhat is the name of barvatos advisor?  ")
    while len(advisor_name) == 0:
        advisor_name = input(f"Please enter a valid name:  ")
    #Second Question
    weapon = input(f"What type of weapon does Barvatos wield into battle?  ")
    while len(weapon) == 0:
        weapon = input(f"please enter a valid weapon type:  ")
    #Third Question
    city = input(f"What is the name of the city Barvatos is planning to raid?  ")
    while len(city) == 0:
        city = input(f"Please enter a valid city name:  ")
    #Fourth Question
    treasure = input(f"What type of treasure is barvatos seeking?  ")
    while len(treasure) == 0:
        treasure = input(f"Please enter a valid treasure:  ")
    #Fifth Question
    number_of_warriors = input(f"How many warriors accompany Barvatos?  ")
    while not number_of_warriors.isdigit():
        number_of_warriors = input(f"Value not recognized. Please enter a numeric value:  ")
    
    #Story Starts
    print(f"\nLETS BEGIN THE ADVENTURE!!!")
    print(f"\nBarvatos, the fierce viking lord, prepares for an epic raid on {city}.")
    print(f"With his trusty {weapon} and {number_of_warriors}, Barvatos sets sail.")
    print(f"His advisor, {advisor_name}, stands by his side, ready for the challenge ahead.")

    #Decision 1
    attack_strategy = input(f"\nShould Barvatos launch a surprise attack or demand the city's surrender first? (attack/surrender):  ")
    while attack_strategy not in ["attack", "surrender"]:
        attack_strategy = input("Please choose 'attack' or 'surrender':  ")

    if attack_strategy == "attack":
         print(f"\nBarvatos decides to launch a surprise attack on {city}!")
         print(f"With his {weapon} in hand, he leads his warriors into battle, catching the city off guard.")
         print(f"The fight is fierce, but Barvatos's warriors are victorious, and they seize the city's {treasure}.")
    else:
        print(f"\nBarvatos demands the city's surrender first.")
        print(f"The city's leaders, fearing the might of Barvatos and his {number_of_warriors} warriors, surrender immediately.")
        print(f"As a sign of submission, they offer their precious {treasure} to Barvatos.")
        
    #Decision 2
    rest_after_battle = input(f"\nShould Barvatos and his warriors rest in the city or continue their raids elsewhere? (rest/continue):  ")
    while rest_after_battle not in ["rest", "continue"]:
        rest_after_battle = input("Please choose 'rest' or 'continue':  ")
        
    if rest_after_battle == "rest":
         print(f"\nBarvatos decides to rest in {city}.")
         print(f"He and his warriors enjoy the spoils of their victory, feasting and celebrating.")
         print(f"During their stay, {advisor_name} discovers hidden passages leading to more {treasure}.")
    else:
        print(f"\nBarvatos decides not to rest and continues his raids on neighboring territories.")
        print(f"His relentless pursuit of glory and {treasure} leads to more victories")
        print(f"But the journey is not without cost, as his warriors grow weary.")
        
    #Alternate Endings
    if attack_strategy == "attack" and rest_after_battle == "rest":
         print(f"\nAfter the fierce battle and subsequent rest in {city}, Barvatos and his warriors are well rested and wealthy.")
         print(f"Witht their newfound wealth in {treasure}, they return home as heroes, their names etched in legend.")
    elif attack_strategy == "surrender" and rest_after_battle == "continue":
         print(f"\nBarvatos's cunning in demanding surrender spared his warriors a battle.")
         print(f"His decision to continue the raids, however, brought more challenges and unforeseen dangers.")
         print(f"While they gained more {treasure}, the journey home was fraught with peril.")
    else:
         print(f"\nThe choices of Barvatos, whether through battle or diplomacy, shaped the future of his clan.")
         print(f"Returning with {treasure} and tales of adventure, Barvatos's legacy was secured.")
    print(f"\nThe End")

    keepPlaying = input(f"\nDo you want to play again and alter Barvatos's fate? Enter yes or no:  ")
    while keepPlaying.lower() not in ["yes", "no"]:
        keepPlaying = input(f"Please type yes or no:  ")



