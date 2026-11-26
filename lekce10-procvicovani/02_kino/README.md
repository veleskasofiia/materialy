# Kino

Postavíš rezervační systém pro malé kino. Pokladní v něm uvidí sál, rezervuje
místo na jméno a rezervaci zase zruší:

```text
        1 2 3 4 5 6 7 8
řada 1  . . . . . . . .
řada 2  . . X X . . . .
řada 3  . . . . . X . .

(s)ál, (r)ezervovat, (z)rušit, (k)onec: r
Řada: 3
Místo: 4
Na jméno: Anna
Řada 3, místo 4 je tvoje, Anna.
```

Sál je seznam řad a každá řada je seznam míst. Volné místo je `None`, obsazené
má jméno toho, kdo si ho rezervoval. Práci se seznamem seznamů ukazuje téma
[Seznam seznamů](../01_seznam_seznamu).

## Jak na to

- Program píšeš do souboru [`kino.py`](kino.py). Po každém kroku ho spusť.
- Kroky jsou ve složce `cviceni/` a jdou po sobě. Každý přidá kousek programu.
- Když se zasekneš, každý krok má nápovědu. Zkus to nejdřív sama.
- Hotový program pak můžeš rozšířit o bonusy.
