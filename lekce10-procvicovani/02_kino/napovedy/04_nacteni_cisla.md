# Nápověda ke kroku 4 – Načtení čísla

Ptát se, dokud to není dobře, je cyklus `while True` a uvnitř `return`, který
ukončí funkci i cyklus.

Než text převedeš na číslo, ověř metodou `isdigit` z lekce 6, že to číslo je.
Jinak by `int("dva")` spadlo na `ValueError`. Teprve pak porovnej, jestli je
v rozsahu.
