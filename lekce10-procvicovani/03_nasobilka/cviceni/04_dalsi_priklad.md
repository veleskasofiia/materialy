# Krok 4 – Další příklad?

```text
3 * 7 = 21
Správně!
Enter = další příklady, n = konec:
8 * 2 = 16
Správně!
Enter = další příklady, n = konec: n
```

## Funkce

Napiš funkci `pokracovat`, která se zeptá, jestli hrát dál:

- na Enter, tedy prázdnou odpověď, vrátí `True`
- na `n` nebo `ne`, i velkými písmeny, vrátí `False`
- na cokoli jiného se zeptá znovu

## Program

Kolo z kroku 3 dej do cyklu. Po každém příkladu se zeptej funkcí
`pokracovat`. Když hráčka skončí, rozluč se.

Zasekla ses? Nápověda je v souboru [`napovedy/04_dalsi_priklad.md`](../napovedy/04_dalsi_priklad.md).

## Hotovo, když

- [ ] na Enter přijde další příklad
- [ ] `n`, `N`, `ne` i `NE` hru ukončí
- [ ] jiná odpověď vede na novou otázku
