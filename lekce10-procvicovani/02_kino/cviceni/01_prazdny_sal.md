# Krok 1 – Prázdný sál

```python
print(vytvor_sal(2, 3))     # [[None, None, None], [None, None, None]]
```

## Funkce

Napiš funkci `vytvor_sal`. Má na vstupu počet řad a počet míst v řadě a vrátí
sál, kde jsou všechna místa volná, tedy `None`.

Postav ho cyklem v cyklu: pro každou řadu nový seznam míst, a ten přidej do
sálu.

Zasekla ses? Nápověda je v souboru [`napovedy/01_prazdny_sal.md`](../napovedy/01_prazdny_sal.md).

## Program

Pod funkci napiš volání z ukázky nahoře a program spusť. Zkus i jiné rozměry,
třeba `vytvor_sal(3, 2)`.

## Hotovo, když

- [ ] `vytvor_sal(2, 3)` vypíše dvě řady po třech `None`
- [ ] `vytvor_sal(3, 2)` vypíše tři řady po dvou `None`
