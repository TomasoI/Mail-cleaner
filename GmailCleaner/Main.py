from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time
import datetime
import json
import warnings
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# Date & Time
DateTime = '{:[%d-%m-%Y %H:%M:%S]}'.format(datetime.datetime.now())

# Title
title = """
   ______                _ __            ________
  / ____/___ ___  ____ _(_) /           / ____/ /__  ____ _____  ___  _____
 / / __/ __ `__ \/ __ `/ / /  ______   / /   / / _ \/ __ `/ __ \/ _ \/ ___/
/ /_/ / / / / / / /_/ / / /  /_____/  / /___/ /  __/ /_/ / / / /  __/ /
\____/_/ /_/ /_/\__,_/_/_/            \____/_/\___/\__,_/_/ /_/\___/_/
"""
print(Fore.RED + title)
print()

Author = "| Made by TomasoI"
print(Fore.CYAN + f"{DateTime} {Author}")
Version = "| In use version 0.0.1"
print(Fore.CYAN + f"{DateTime} {Version}")
print()
print()

# Warn exception
warnings.filterwarnings("ignore", category=DeprecationWarning)
sys.tracebacklimit = 0

# Json opener & reader
settings = json.load(open("Settings.json"))
EmailJSON = settings["Settings"][0]["Email"]
PasswordJSON = settings["Settings"][0]["Password"]
InputRetry = float(PasswordJSON)

# Menu


def menu():
    print("[1] Start login tasks")
    print("[2] Start cleaning tasks")
    print("[0] Exit program.")


menu()
print()
option = int(input("Enter your option: "))

print()

while option != 0:

    # Option 1
    if option == 1:

        print(Fore.YELLOW + "Login tasks are starting...")

        # Path
        driver = webdriver.Chrome("chromedriver.exe")

        # Login trought OAuth2.0
        driver.get("https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f")
        press_login_w_google = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[2]/button[1]")
        press_login_w_google.click()

        search_email_bar = driver.find_element_by_id("identifierId")
        search_email_bar.send_keys(EmailJSON)

        press_email_confirm = driver.find_element_by_id("identifierNext")
        press_email_confirm.click()

        time.sleep(20)

    # Option 2
    elif option == 2:
        print("Cleaning tasks are starting...")
    else:
        print("Invalid option...")

# Option 0
print(Fore.RED + "Program is closing.")
time.sleep(2)
sys.exit()
