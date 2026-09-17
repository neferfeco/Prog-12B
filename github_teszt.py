szamok = []

for i in range(5):
    szamok.append(int(input("Adj meg egy számot: ")))
    
atlag = 0.0

for szam in szamok:
    atlag += szam

atlag = atlag / len(szamok)

print(f"Átlag: {atlag}")

# Van-e páros szám?
i = 0
while i < len(szamok) and szamok[i] % 2 != 0:
    i += 1

if i < len(szamok):
    print("Van páros szám!")
else:
    print("Nincs páros szám!")


