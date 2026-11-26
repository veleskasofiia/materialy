# ---------------------------------------------
#  Seznam seznamů
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.
#
# Položkou seznamu může být cokoli, i další seznam. Hodí se to na data,
# která mají řádky a sloupce, třeba na teploty za dva týdny. Každý týden
# je seznam sedmi čísel a oba týdny jsou v jednom seznamu:

teploty = [
    [12, 14, 11, 9, 10, 13, 15],
    [8, 7, 9, 12, 14, 16, 15],
]

print(len(teploty))         # 2 – dva týdny
print(teploty[1])           # [8, 7, 9, 12, 14, 16, 15] – druhý týden


# Jedno číslo dostaneš dvěma indexy za sebou:
print(teploty[1][0])        # 8

# Čti zleva doprava: teploty[1] je druhý týden, a z něj [0] pondělí.
# Stejně se četlo hoste[0]["jmeno"] v lekci 9, jen tady jsou oba
# indexy čísla.
#
# (Ukazuje to obrázek seznam_seznamu.png.)


# Změna funguje jako u každého seznamu, jen s dvěma indexy:
teploty[0][3] = 10
print(teploty[0])           # [12, 14, 11, 10, 10, 13, 15]


# Všechna čísla projdeš cyklem v cyklu. Vnější cyklus bere týdny,
# vnitřní dny v tom týdnu:
nejtepleji = teploty[0][0]
for tyden in teploty:
    for teplota in tyden:
        if teplota > nejtepleji:
            nejtepleji = teplota

print(nejtepleji)           # 16

# Vnitřní cyklus proběhne celý pro každý týden, takže se postupně
# porovnají všechna čísla. Hledání největšího čísla znáš z lekce 3.


# Seznam seznamů se dá taky postavit cyklem. Pro každý řádek vznikne
# nový prázdný seznam, naplní se a přidá se do velkého seznamu:
tabulka = []
for radek in range(2):
    novy_radek = []
    for sloupec in range(3):
        novy_radek.append(0)
    tabulka.append(novy_radek)

print(tabulka)              # [[0, 0, 0], [0, 0, 0]]

# Řádek novy_radek = [] musí být uvnitř vnějšího cyklu. Kdyby byl před
# ním, přidal by se do tabulky pořád ten samý seznam: dvě jména pro
# jeden seznam z lekce 8. Změna jednoho řádku by se pak objevila ve
# všech.
