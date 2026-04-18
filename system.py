import os
import datetime
import time
import sys

# =========================
# EFFECTS
# =========================

def type_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_bar(task, duration=2):
    print(f"{task} ", end="")
    for _ in range(20):
        time.sleep(duration / 20)
        print("█", end="", flush=True)
    print()

def system_scan():
    type_text("Scanning system...")
    time.sleep(1)
    type_text("Checking permissions...")
    time.sleep(1)
    type_text("No threats detected\n")


# =========================
# LOGIN
# =========================

PASSWORD = "MothLogic314"

type_text("Enter password: ", 0.05)
entry = input()

if entry != PASSWORD:
    type_text("Access denied")
    exit()
else:
    type_text("Access granted\n")


# =========================
# SYSTEM BOOT
# =========================

type_text("Initializing system...")
loading_bar("Loading modules...", 2)

type_text("Accessing database...")
loading_bar("Connecting...", 2)

system_scan()

type_text("✔ System ready\n")


# =========================
# DATABASE
# =========================

FILE_NAME = "secret_data.txt"


# =========================
# ENCRYPTION
# =========================

def encrypt(text):
    return "".join(chr(ord(c) + 3) for c in text)

def decrypt(text):
    return "".join(chr(ord(c) - 3) for c in text)


# =========================
# CORE FUNCTIONS
# =========================

def save_entry(text):
    text = encrypt(text)
    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.datetime.now()}] {text}\n")
    print("✔ Saved\n")


def read_entries():
    if os.path.exists(FILE_NAME):
        print("\n📜 STORED DATA:\n")
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                print(decrypt(line))
    else:
        print("No data found\n")


# =========================
# MENU
# =========================

def menu():
    print("=== PRIVATE SYSTEM ===")
    print("1. Save thought")
    print("2. Read thoughts")
    print("3. Exit")
    print("Hidden commands available: root, scan\n")


# =========================
# MAIN LOOP
# =========================

while True:
    menu()
    option = input("> ")

    if option == "1":
        text = input("Write your thought: ")
        save_entry(text)

    elif option == "2":
        read_entries()

    elif option == "3":
        type_text("Shutting down system...")
        break

    # ROOT COMMAND
    elif option == "root":
        type_text("⚠ ROOT ACCESS GRANTED")
        print("Options: delete")

        sub = input("root> ")

        if sub == "delete":
            if os.path.exists(FILE_NAME):
                os.remove(FILE_NAME)
                print("💀 Database deleted\n")

    # SCAN COMMAND
    elif option == "scan":
        system_scan()

    else:
        print("Unknown command\n")