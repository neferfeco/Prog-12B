# IMPORT
import subprocess

from colorama import Fore


# GLOBÁLIS VÁLTOZÓK
menu_elemek = [
    [11, "Pepsi citrom 0,5l", 500],
    [12, "Pepsi cseresznye 0,5l", 500],
    [13, "Fanta narancs 1l", 1050],
    [14, "Coca-Cola 1,75l", 1250],
    [31, "Tibi csoki (tábla)", 550],
    [32, "Mars szelet", 350],
    [33, "Kinder Maxi King", 450],
    [34, "Lindt 80% kakaó", 1950]
]


# FÜGGVÉNY DEFINÍCIÓK
def menu():
    subprocess.run(["cls"], shell=True)
    
    print(f"{Fore.RED}A választék:{Fore.RESET}\n")
    
    print(f"{'Kód':4} {'Termék':25} {'Ár':>6} Ft")
    print(f"{'=' * 40}")
    
    for m in menu_elemek:
        print(f"{m[0]:4} {m[1]:25} {m[2]:>6} Ft")




# ---------------------------

# PROGRAM

# 1. Termék választás
menu()
valasz = int(input("\nMit szeretnél?: "))
print(f"{'-' * 40}")

# ELDÖNTÉS
jo_valasztas = False

i = 0
while i < len(menu_elemek) and menu_elemek[i][0] != valasz:
    i += 1 

if i < len(menu_elemek):
    jo_valasztas = True

while not jo_valasztas:
    menu()
    valasz = int(input("\nMit szeretnél?: "))
    print(f"{'-' * 40}")

    # ELDÖNTÉS
    jo_valasztas = False

    i = 0
    while i < len(menu_elemek) and menu_elemek[i][0] != valasz:
        i += 1 

    if i < len(menu_elemek):
        jo_valasztas = True


# FIZETTETÉS
# Termék árának kikeresése
ar = menu_elemek[i][2]

osszeg = 0
while osszeg <= ar:
    osszeg += int(input("Bedobott összeg!: "))

print("Vedd el a választott terméket!")


# VISSZAJÁRÓ
#1000, 500, 200, 100, 50
visszajaro = osszeg - ar

cimletek = [1000, 500, 200, 100, 50]

print(f"Visszajáró összeg: {visszajaro} Ft")

for c in cimletek:
    db = visszajaro // c
    # visszajaro -= (c * db)
    
    if db > 0:
        print(f"  {c} Ft {db} darab")






