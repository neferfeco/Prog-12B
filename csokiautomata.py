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

menu_elem_kodok = []


# FÜGGVÉNY DEFINÍCIÓK
def menu():
    subprocess.run(["cls"], shell=True)
    
    print(f"{Fore.RED}A választék:{Fore.RESET}\n")
    
    print(f"{'Kód':4} {'Termék':25} {'Ár':>6} Ft")
    print(f"{'=' * 40}")
    
    for m in menu_elemek:
        print(f"{m[0]:4} {m[1]:25} {m[2]:>6} Ft")


def menu_kodok():
    kodok = []
    
    for sor in menu_elemek:
        kodok.append(sor[0])

    return kodok


def visszajaro_cimletek(osszeg):
    cimletek = [1000, 500, 200, 100, 50]
    
    for cimlet in cimletek:
        db = osszeg // cimlet
        
        if db > 0:
            print(f"  {cimlet:5} Ft: {db:>3} db")
            osszeg -= (cimlet * db)


# ---------------------------

# PROGRAM
menu_elem_kodok = menu_kodok()

# 1. Termék választás
menu()
valasz = int(input("\nMit szeretnél?: "))
print(f"{'-' * 40}")

while valasz not in menu_elem_kodok:
    menu()
    valasz = int(input("\nMit szeretnél?: "))
    print(f"{'-' * 40}")

index = menu_elem_kodok.index(valasz)


# 2. Készpénz befizetés
subprocess.run(["cls"], shell=True)
fizetendo_osszeg = menu_elemek[index][2]

print(f"A {menu_elemek[index][1]} ára {fizetendo_osszeg} Ft\n")

osszeg = int(input("Add meg a befizetés összegét!: "))

while osszeg < fizetendo_osszeg:
    print(f"Még hiányzik {fizetendo_osszeg - osszeg} Ft!")
    osszeg += int(input("Add meg a befizetés összegét!: "))

print(f"\n{Fore.GREEN}A befizetett összeg OK!{Fore.RESET}\n")
input("Üss ENTER-t a folytatáshoz!")


# 3. Termék kiadás
subprocess.run(["cls"], shell=True)

print(f"\n{Fore.RED}Vedd el a terméket!{Fore.RESET}\n")

input("Üss ENTER-t a folytatáshoz!")


# 4. Visszajáró készpénz kezelése
subprocess.run(["cls"], shell=True)

print(f"A {menu_elemek[index][1]} ára {fizetendo_osszeg} Ft.")
print(f"Befizetett összeg: {osszeg} Ft")
print(f"Max. 50 Ft-os címletig tudok visszadni!")

visszajaro = osszeg - fizetendo_osszeg
visszajaro -= (visszajaro % 50)

print(f"\n{Fore.GREEN}Visszajár: {visszajaro} Ft{Fore.RESET}")

visszajaro_cimletek(visszajaro)

   
