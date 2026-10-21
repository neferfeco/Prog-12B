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
    print(f"{Fore.RED}", end="")
    print(f"\n{'=' * 60}\n{'SZÁMLA':^60}\n{'=' * 60}\n")
    print(f"{Fore.RESET}", end="")
    
    print(f"{'Étel':25}{'Mennyiség':>10}{'Részösszeg':>12}")
    print(f"{'-' * 50}")
    
    total = 0
    
    for i in range(len(menu_elemek) - 1):
        # print() kajanév   mennyiség   részösszeg
        if menu_elemek[i][1] > 0:
            etel_nev = menu_elemek[i][0]
            db = menu_elemek[i][1]
            resz_osszeg = db  * menu_elemek[i][2]
            print(f"{etel_nev[3:]:25}{db:>10}{resz_osszeg:>12} Ft")
            
            total += resz_osszeg
    
    print(f"\n{'-' * 50}")
    print(f"{Fore.RED}FIZETENDŐ ÖSSZEG: {total} Ft{Fore.RESET}\n")


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




