import random
import os
import time

def luhn_checksum(card_number):
    """Luhn algorithm to validate card numbers"""
    digits = [int(d) for d in card_number]
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    total = sum(odd_digits)
    for d in even_digits:
        total += sum(divmod(d * 2, 10))
    return total % 10 == 0

def generate_card(bin_format):
    """Generates a valid card number based on BIN"""
    card = bin_format
    while 'x' in card:
        card = card.replace('x', str(random.randint(0, 9)), 1)
    while len(card) < 15:
        card += str(random.randint(0, 9))
    for i in range(10):
        if luhn_checksum(card + str(i)):
            return card + str(i)
    return generate_card(bin_format)

def ui():
    os.system('clear')
    # Top Branding
    print("\033[1;33m" + "By SmSystems".center(60))
    print("\033[1;35m" + "="*60)
    print("  ██████╗███╗   ███╗     ██████╗ ███████╗███╗   ██╗")
    print("  ██╔════╝████╗ ████║    ██╔════╝ ██╔════╝████╗  ██║")
    print("  ███████╗██╔████╔██║    ██║  ███╗█████╗  ██╔██╗ ██║")
    print("  ╚════██║██║╚██╔╝██║    ██║   ██║██╔══╝  ██║╚██╗██║")
    print("  ███████║██║ ╚═╝ ██║    ╚██████╔╝███████╗██║ ╚████║")
    print("  ╚══════╝╚═╝     ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝")
    print("\033[1;36m" + "           >> ULTIMATE CARD GENERATOR v3.0 <<")
    print("\033[1;35m" + "="*60)
    
    # Information Panel with your BTC and Telegram
    print("\033[1;32m [Dev: By SmSystems] \033[0m".ljust(30) + "\033[1;33m [DONATE BTC] \033[0m")
    print("\033[1;34m TG: t.me/SmSystems01 \033[0m".ljust(25) + "\033[1;37m bc1qhcuka00nes3cvhc3uzzu9rcqtvwd5ju686c3gg \033[0m")
    print("\033[1;35m" + "-"*60 + "\033[0m")

def start_gen():
    ui()
    
    # Input Fields
    bin_num = input("\033[1;34m[?] Enter BIN (Ex: 414720): \033[0m")
    month = input("\033[1;34m[?] Month (Enter for Random): \033[0m")
    year = input("\033[1;34m[?] Year (Enter for Random): \033[0m")
    cvv = input("\033[1;34m[?] CVV (Enter for Random): \033[0m")
    amount = int(input("\033[1;34m[?] How many cards?: \033[0m"))
    
    print("\n\033[1;33m[!] Select Save Location:")
    print(" 1 - Termux Folder (cards.txt)")
    print(" 2 - Phone Storage (sdcard/cards.txt)")
    print(" 3 - Custom Path\033[0m")
    
    choice = input("\033[1;34m[?] Choice (1/2/3): \033[0m")
    
    if choice == "1":
        file_path = "cards.txt"
    elif choice == "2":
        file_path = "/sdcard/cards.txt"
    elif choice == "3":
        file_path = input("\033[1;34m[?] Enter Full Path: \033[0m")
    else:
        file_path = "cards.txt"

    print(f"\n\033[1;36m[*] By SmSystems is generating {amount} cards...\033[0m")
    
    start_time = time.time()
    
    try:
        with open(file_path, "w") as f:
            for i in range(amount):
                cc = generate_card(bin_num)
                m = month if month else str(random.randint(1, 12)).zfill(2)
                y = year if year else str(random.randint(2025, 2033))
                c = cvv if cvv else str(random.randint(100, 999))
                f.write(f"{cc}|{m}|{y}|{c}\n")
                
                if (i+1) % 10000 == 0:
                    print(f"\033[1;32m[+] {i+1} cards completed...\033[0m")

        end_time = time.time()
        
        print("\033[1;35m" + "="*60)
        print(f"\033[1;32m [SUCCESS] {amount} Cards Saved!")
        print(f" [PATH] {file_path}")
        print(f" [TIME] {round(end_time - start_time, 2)} Seconds")
        print(f" \033[1;33mSupport: bc1qhcuka00nes3cvhc3uzzu9rcqtvwd5ju686c3gg \033[0m")
        print("\033[1;35m" + "="*60 + "\033[0m")
        print("\033[1;33m" + "By SmSystems".center(60) + "\033[0m")

    except PermissionError:
        print("\033[1;31m[!] Error: Storage Permission Denied!\033[0m")
    except Exception as e:
        print(f"\033[1;31m[!] Error: {e}\033[0m")

if __name__ == "__main__":
    start_gen()

