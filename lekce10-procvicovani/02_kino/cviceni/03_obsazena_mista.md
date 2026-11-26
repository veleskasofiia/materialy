# Krok 3 – Obsazená místa

```text
        1 2 3 4
řada 1  . . . .
řada 2  . . X X
```

## Funkce

Uprav funkci `zobraz`, aby obsazené místo vypsala jako `X`. Obsazené místo je
každé, kde není `None`.

## Program

Rezervovat zatím neumíš, tak místa obsaď ručně přiřazením, jako v tématu
[Seznam seznamů](../../01_seznam_seznamu). Lidi číslují řady i místa od
jedničky, indexy začínají nulou. Řada 2, místo 3 je proto `sal[1][2]`. Ukázku
z kroku 2 nahraď tímhle:

```python
sal = vytvor_sal(2, 4)
sal[1][2] = "Anna"
sal[1][3] = "Petra"
zobraz(sal)
```

## Hotovo, když

- [ ] Anna a Petra se ve výpisu ukážou jako dvě `X` ve druhé řadě
- [ ] ostatní místa jsou pořád tečky
