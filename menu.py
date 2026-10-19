# IMPORT
from colorama import Fore, Back, Style
import subprocess


# GLOBÁLIS VÁLTOZÓK
menu_elemek = [["A) Big Mac", 0, 500], 
               ["B) Pörkölt nokedlivel", 0, 1000],
               ["C) Big Tasty", 0, 2000],
               ["Q) Kilépés", 0, 0]
]


# FÜGGVÉNY DEFINÍCIÓK
def menu():
    subprocess.run(["cls"], shell=True)
    
    print(f"{Fore.RED}Válassz menüt!{Fore.RESET}")
    print(f"{'=' * 40}")
    
    for m in menu_elemek:
        if m[0].startswith('Q'):
            print(f"{m[0]}")
        else:
            print(f"{m[0]:25} {m[2]:>6} Ft")


def rendeles(mit, db):
    i = 0
    while not menu_elemek[i][0].startswith(mit):
         i += 1

    menu_elemek[i][1] += db


def szamla():
    print(f"{'='*15}\n{'SZÁMLA':^15}\n{'='*15}\n")
    
    total = 0
    
    for i in range(len(menu_elemek) - 1):
        # print() kajanév   mennyiség   részösszeg
        pass
    
    print(f"\nFIZETENDŐ ÖSSZEG: {total} Ft")


# ---------------------------

# PROGRAM
menu()

valasz = input("Mit szeretnél?: ").strip().upper()

if valasz == "A":
    db = int(input("Mennyit kér?: "))
    rendeles("A", db)
      
    input("Üss egy billentyűt a folytatáshoz...")
elif valasz == "B":
    db = int(input("Mennyit kér?: "))
    rendeles("B", db)
    
    input("Üss egy billentyűt a folytatáshoz...")
elif valasz == "C":
    db = int(input("Mennyit kér?: "))
    rendeles("C", db)
    
    input("Üss egy billentyűt a folytatáshoz...")
elif valasz == "Q":
    print("Jó étvágyat!")
    szamla()
    exit()


while True:
    menu()

    valasz = input("Mit szeretnél?: ").strip().upper()

    if valasz == "A":
        db = int(input("Mennyit kér?: "))
        rendeles("A", db)
        
        input("Üss egy billentyűt a folytatáshoz...")
    elif valasz == "B":
        db = int(input("Mennyit kér?: "))
        rendeles("B", db)
        
        input("Üss egy billentyűt a folytatáshoz...")
    elif valasz == "C":
        db = int(input("Mennyit kér?: "))
        rendeles("C", db)
        
        input("Üss egy billentyűt a folytatáshoz...")
    elif valasz == "Q":
        print("Jó étvágyat!")
        szamla()
        exit()




