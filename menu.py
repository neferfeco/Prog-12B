# IMPORT
from colorama import Fore, Back, Style
import subprocess


# GLOBÁLIS VÁLTOZÓK
darab = 0

# FÜGGVÉNY DEFINÍCIÓK
def menu():
    subprocess.run(["cls"], shell=True)
    
    print(f"{Fore.RED}Válassz menüt!{Fore.RESET}")
    print(f"{'=' * 40}")
    print("A) Big Mac")
    print("B) Pörkölt nokedlivel")
    print("C) Big Tasty")
    print("Q) Kilépés")



# ---------------------------

# PROGRAM
menu()

valasz = input("Mit szeretnél?: ").strip().upper()

if valasz == "A":
    print("500 Ft")
    input("Üss egy billentyűt a folytatáshoz...")
elif valasz == "B":
    print("1000 Ft")
    input("Üss egy billentyűt a folytatáshoz...")
elif valasz == "C":
    print("2000 Ft")
    input("Üss egy billentyűt a folytatáshoz...")
elif valasz == "Q":
    print("Jó étvágyat!")
    exit()


while True:
    menu()
    
    valasz = input("Mit szeretnél?: ").strip().upper()
    
    if valasz == "A":
        print("500 Ft")
        input("Üss egy billentyűt a folytatáshoz...")
    elif valasz == "B":
        print("1000 Ft")
        input("Üss egy billentyűt a folytatáshoz...")
    elif valasz == "C":
        print("2000 Ft")
        input("Üss egy billentyűt a folytatáshoz...")
    elif valasz == "Q":
        exit()




