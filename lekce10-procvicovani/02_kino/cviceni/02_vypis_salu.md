# Krok 2 – Výpis sálu

```text
        1 2 3 4
řada 1  . . . .
řada 2  . . . .
```

## Funkce

Napiš funkci `zobraz`, která sál vypíše. Nad místy jsou jejich čísla a každá
řada má svůj řádek. Zatím je všechno volné, takže každé místo se vypíše jako
tečka.

Zarovnání stačí pro sál s nejvýš 9 řadami a 9 místy v řadě. Dvouciferná čísla
by sloupce posunula.

Zasekla ses? Nápověda je v souboru [`napovedy/02_vypis_salu.md`](../napovedy/02_vypis_salu.md).

## Program

Ukázku z kroku 1 nahraď tímhle:

```python
sal = vytvor_sal(2, 4)
zobraz(sal)
```

## Hotovo, když

- [ ] výpis vypadá jako ukázka nahoře, tečky jsou pod čísly
- [ ] pro `vytvor_sal(3, 8)` vypíše tři řady a nad nimi čísla 1 až 8
