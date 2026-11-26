# Krok 5 – Ptát se jen občas

```text
1 * 9 = 9
...
5 * 5 = 25
Správně!
Enter = další příklady, n = konec:
```

## Program

Ptát se po každém příkladu zdržuje. Uprav hru tak, aby se ptala jen po každém
pátém. Počítej kola v proměnné `kolo`.

Číslo 5 si dej do proměnné nahoru pod import, třeba `PTAT_SE_PO = 5`. Velkými
písmeny se píšou hodnoty, které se za běhu programu nemění, jako `TAHY`
v lekci 8. Když budeš chtít delší kola, změníš jen tenhle řádek.

Skončit pak jde až po pátém příkladu. To je v pořádku, hra se dřív nezeptá.

### Kratší zápis přičítání

Kolo přičteš tak, jak to znáš od lekce 4:

```python
kolo = kolo + 1
```

Python na to má i kratší zápis. Znamená přesně totéž:

```python
kolo += 1
```

Funguje to i s jiným číslem a s odčítáním: `body += 10`, `zivoty -= 1`.
Kratší neznamená lepší, piš to, co se ti líp čte.

Zasekla ses? Nápověda je v souboru [`napovedy/05_kazde_pate.md`](../napovedy/05_kazde_pate.md).

## Hotovo, když

- [ ] otázka přijde po 5., 10., 15. příkladu
- [ ] po ostatních příkladech hra rovnou pokračuje
- [ ] když změníš `PTAT_SE_PO` třeba na 3, hra se ptá po každém třetím
