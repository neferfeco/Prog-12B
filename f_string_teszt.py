import random


# DEC 2 BIN
def dec_2_bin(szam):
    return f"{szam:b}"

# DEC 2 HEX
def dec_2_hex(szam):
    return f"{szam:x}"  


ip_cim = ""

for i in range(4):
    if i == 3:
        ip_cim += f"{str(random.randint(0, 255))}"
    else:
        ip_cim += f"{str(random.randint(0, 255))}."

#print(f"IP: {ip_cim}")

#for sz in ip_cim.split("."):
#    print(dec_2_bin(int(sz)), end="")

#print()
#print(dec_2_hex(1000))
#print(f"{1234.456789:.1f}")

tablazat = [
    ["Riki", "Magyar nyelv és irodalom", 5],
    ["Simon", "Matematika", 4],
    ["Huba", "Fizika", 3]
]

for sor in tablazat:
    print(f"{sor[0]:8}{sor[1]:26}{sor[2]:>3}")



