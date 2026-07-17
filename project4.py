import pyautogui
import time

print("Open your chat window.")
print("The bot will start in 5 seconds...")

time.sleep(5)

while True:
    message = input("Enter reply (or type 'exit' to stop): ")

    if message == "exit":
        print("Bot stopped.")
        break

    pyautogui.write(message, interval=0.05)
    pyautogui.press("enter")