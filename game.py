from colorama import Back,Style, Fore
"""
Python crash course A hands on project based on
 introduction to programming by Eric Mathes
"""
"""
My initial program was a simple number guessing game, which looked something like this:
I'm thinking of a number! Try to guess the number 
I'm thinking of: 25 Too low! Guess again: 50 Too high! Guess again: 
42 That's it! Would you like to play again? (yes/no) no Thanks for playing!
"""
num = 42
ent_num = int(input("I'm thinking of a number! Try to guess the number: "))
if ent_num < num:
    print(Fore.GREEN + f"I'm thinking of: {ent_num} Too low!")
    print("Guess again:")

    ent_num = int(input("I'm thinking of a number! Try to guess the number: "))
    if ent_num > num:
        print(Fore.BLUE + f"I'm thinking of: {ent_num} Too high")
        print("Guess again:")

        ent_num = int(input("I'm thinking of a number! Try to guess the number: "))
        if ent_num == num:
            print(Fore.RED + f"{ent_num} That's it!")
            
            ent_num = str(Fore.YELLOW + input("would you like to play again (yes/no): "))
            #if ent_num != num:
            print("Thanks for playing")
