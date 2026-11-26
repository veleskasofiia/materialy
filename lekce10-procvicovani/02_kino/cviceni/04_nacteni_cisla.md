# Krok 4 – Načtení čísla

```text
Řada: 9
Napiš číslo od 1 do 5.
Řada: dva
Napiš číslo od 1 do 5.
Řada: 2
Místo: 3
Vybrala sis řadu 2, místo 3.
```

## Funkce

Napiš funkci `nacti_cislo`. Má na vstupu otázku a nejvyšší povolené číslo.
Ptá se tak dlouho, dokud nedostane číslo od 1 do toho nejvyššího, a vrátí ho
jako `int`.

Zasekla ses? Nápověda je v souboru [`napovedy/04_nacteni_cisla.md`](../napovedy/04_nacteni_cisla.md).

## Program

Sál bude mít 5 řad po 8 místech. Ta čísla budeš potřebovat na víc místech,
tak si je dej do proměnných hned pod funkce. Velkými písmeny se píšou
hodnoty, které se za běhu programu nemění, jako `TAHY` v lekci 8.

Ukázku z kroku 3 nahraď tímhle a funkci vyzkoušej:

```python
RAD = 5
MIST = 8

rada = nacti_cislo("Řada: ", RAD)
misto = nacti_cislo("Místo: ", MIST)
print(f"Vybrala sis řadu {rada}, místo {misto}.")
```

## Hotovo, když

- [ ] číslo mimo rozsah, text i prázdná odpověď vedou na novou otázku
- [ ] mezery okolo čísla nevadí
- [ ] funkce vrací číslo, ne text
