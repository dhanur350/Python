import random
def stealdeal():
    play = 'y'
    count = 0
    while play == 'y':
        count = count+1
        computer_choice = random.randint(1, 3)

        if computer_choice == 1:
            computer_choice = "Steal"
        elif computer_choice == 2:
            computer_choice = "Deal"
        else:
            computer_choice = "Draw"

        player_choice = random.randint(1, 3)
        player_choice = int(input("Steal(1), Deal(2), Draw(3)? "))

        print("computer choice", computer_choice)
        print("player choice", player_choice)

        if player_choice == 1:
            player_choice = "Steal"
        elif player_choice == 2:
            player_choice = "Deal"
        else:
            player_choice = "Draw"

        if computer_choice == "Steal" and player_choice == "Deal":
            print("You win - Deal covers the Steal")
        elif computer_choice == "Steal" and player_choice == "Draw":
            print("computer win - Steal beats Draw")

        elif computer_choice == "Deal" and player_choice == "Steal":
            print("computer win- Deal wrap Steal")
        elif computer_choice == "Deal" and player_choice == "Draw":
            print("computer loses- scissor cut the Deal")
        elif computer_choice == "Draw" and player_choice == "Steal":
            print("computer loses-Steal beats scissor")
        elif computer_choice == "Draw" and player_choice == "Deal":
            print("computer win-scissor cut Deal")
        else:
            print("the match draws")
        print()
        play = input('Play again? ')

    print("\n\nYou played", count, "games.")
