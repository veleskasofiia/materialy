# Krok 6 – Pokladna

```text
(s)ál, (r)ezervovat, (z)rušit, (k)onec: r
Řada: 2
Místo: 3
Na jméno: Anna
Řada 2, místo 3 je tvoje, Anna.

(s)ál, (r)ezervovat, (z)rušit, (k)onec: r
Řada: 2
Místo: 3
Na jméno: Petra
To místo už je obsazené.
```

## Program

Ukázky z minulých kroků smaž, jen `RAD` a `MIST` nech. Pod ně napiš program pro
pokladnu. Sál vytvoř podle `RAD` a `MIST`. Program se pořád dokola ptá, co chceš
udělat:

- `s` vypíše sál
- `r` se zeptá na řadu, místo a jméno a místo rezervuje. Bez jména rezervovat
  nejde: na prázdné jméno napiš „Bez jména rezervovat nejde.“
- `z` se zeptá na řadu a místo a rezervaci zruší, nebo napíše, že tam žádná
  není
- `k` program ukončí
- na cokoli jiného napiš „Tomu nerozumím.“

Velká písmena a mezery navíc v odpovědi nevadí.

Zasekla ses? Nápověda je v souboru [`napovedy/06_pokladna.md`](../napovedy/06_pokladna.md).

### Na závěr

Podívej se na funkce, které jsi napsala: `zobraz`, `rezervuj` i `zrus` dostávají
jako první vstup sál. Data o sále jsou v jedné proměnné a funkce, které s nimi
pracují, vedle nich. Drží je pohromadě jen to, že na to myslíš. Příští lekce
ukáže, jak data a funkce spojit do jednoho celku.

## Hotovo, když

- [ ] jde rezervovat, zrušit a vypsat sál
- [ ] obsazené místo nejde rezervovat podruhé
- [ ] bez jména nejde rezervovat
- [ ] špatná řada nebo místo program neshodí
- [ ] na `k` program skončí
