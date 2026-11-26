# Tahák – Lekce 10: Procvičování

Nové je jen jedno: seznam seznamů. Zbytek jsou postupy, které se v kině
a násobilce opakovaly. Klidně si ho vytiskni na A4.

## Seznam seznamů

```python
sal = [
    [None, None, "Anna"],       # řada 1
    [None, None, None],         # řada 2
]

sal[0][2]                       # Anna    čti zleva doprava: řada, pak místo
sal[1]                          # [None, None, None]   celá řada
sal[0][1] = "Petra"             # změna místa

for rada in sal:                # cyklus v cyklu projde všechno
    for jmeno in rada:
        print(jmeno)
```

Stavění cyklem, nový seznam pro každou řadu:

```python
sal = []
for i in range(5):
    rada = []                   # uvnitř cyklu!
    for j in range(8):
        rada.append(None)
    sal.append(rada)
```

Když je `rada = []` před cyklem, je v sále pět jmen pro jeden seznam:
změna jedné řady se objeví ve všech.

## Lidi počítají od jedničky

```python
sal[rada - 1][misto - 1] = jmeno    # řada 2, místo 3 je sal[1][2]
enumerate(sal, start=1)             # čísla řad od jedničky
```

Převáděj na indexy na jednom místě, třeba uvnitř funkce.

## Ptej se, dokud to není dobře

```python
def nacti_cislo(otazka, nejvic):
    while True:
        odpoved = input(otazka).strip()
        if odpoved.isdigit() and int(odpoved) >= 1 and int(odpoved) <= nejvic:
            return int(odpoved)
        print(f"Napiš číslo od 1 do {nejvic}.")
```

## Funkce vrací, program mluví

```python
if rezervuj(sal, rada, misto, jmeno):       # funkce vrátí True / False
    print("Místo je tvoje.")
else:
    print("To místo už je obsazené.")
```

## Nabídka

```python
while True:
    volba = input("(s)ál, (k)onec: ").strip().lower()
    if volba == "k":
        break
    elif volba == "s":
        zobraz(sal)
    else:
        print("Tomu nerozumím.")
```

## Drobnosti

```python
RAD = 5                         # velkými písmeny: hodnota se za běhu nemění
MIST = 8                        # a používá se na víc místech

from random import randrange
randrange(1, 10)                # náhodné číslo od 1 do 9

kolo += 1                       # totéž jako kolo = kolo + 1
kolo % 5 == 0                   # každé páté kolo
f"{procenta:.0f} %"             # procenta bez desetinných míst
f"{priklad['a']}"               # uvnitř f-stringu apostrofy
" ".join(["1", "2", "3"])       # 1 2 3 – spojí jen texty
```

## Časté chyby

| Co se děje | Co se většinou stalo |
|---|---|
| `IndexError: list index out of range` | číslo od 1 použité jako index bez `- 1` |
| změna jedné řady se objeví ve všech | do seznamu se přidal pořád ten samý seznam |
| `TypeError: sequence item 0: expected str instance, int found` | `join` dostal čísla, převeď je `str()` |
| `ValueError: invalid literal for int()` | `int()` na textu, který není číslo – nejdřív `isdigit()` |
| `SyntaxError: f-string: unmatched '['` | uvnitř f-stringu stejné uvozovky jako kolem něj (starší Python) |
