szamok = []

for i in range(5):
    szamok.append(int(input("Adj meg egy számot: ")))
    
atlag = 0.0

for szam in szamok:
    atlag += szam

atlag = atlag / len(szamok)

print(f"Átlag: {atlag}")






