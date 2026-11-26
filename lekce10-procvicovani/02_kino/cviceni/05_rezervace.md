# Krok 5 – Rezervace a zrušení

```python
sal = vytvor_sal(2, 4)
print(rezervuj(sal, 2, 3, "Anna"))      # True
print(rezervuj(sal, 2, 3, "Petra"))     # False – už tam sedí Anna
print(zrus(sal, 2, 3))                  # True
print(zrus(sal, 2, 3))                  # False – už je volno
```

## Funkce

Napiš dvě funkce. Obě mají na vstupu sál, řadu a místo, `rezervuj` ještě
jméno. Řadu a místo dostanou tak, jak je řekne člověk, od jedničky.

- `rezervuj` zapíše jméno na volné místo a vrátí `True`. Když je místo
  obsazené, nezmění nic a vrátí `False`.
- `zrus` obsazené místo uvolní a vrátí `True`. Když je volné, vrátí `False`.

Obě funkce nic nevypisují. Co se řekne pokladní, rozhodne až hlavní program
podle toho, co funkce vrátí.

Zasekla ses? Nápověda je v souboru [`napovedy/05_rezervace.md`](../napovedy/05_rezervace.md).

## Program

Proměnné `RAD` a `MIST` nech, kde jsou. Zbytek ukázky z kroku 4 nahraď
voláními z ukázky nahoře.

## Hotovo, když

- [ ] výsledky odpovídají komentářům v ukázce
- [ ] po rezervaci vypíše `zobraz(sal)` na správném místě `X`
