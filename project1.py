import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

choices = ["rock", "paper", "scissors"]

print(Fore.CYAN + "=" * 40)
print(Fore.YELLOW + "      ROCK PAPER SCISSORS")
print(Fore.CYAN + "=" * 40)

while True:
    print("\nChoose one:")
    print(Fore.GREEN + "1. Rock")
    print(Fore.BLUE + "2. Paper")
    print(Fore.MAGENTA + "3. Scissors")

    user = input(Fore.WHITE + "\nEnter your choice: ").lower()

    if user not in choices:
        print(Fore.RED + "❌ Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print(Fore.YELLOW + f"\nYou chose: {user}")
    print(Fore.CYAN + f"Computer chose: {computer}")

    if user == computer:
        print(Fore.YELLOW + "\n🤝 It's a Tie!")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print(Fore.GREEN + "\n🎉 You Win!")

    else:
        print(Fore.RED + "\n💀 Computer Wins!")

    again = input(Fore.WHITE + "\nPlay again? (y/n): ").lower()

    if again != "y":
        print(Fore.CYAN + "\n👋 Thanks for playing!")
        break