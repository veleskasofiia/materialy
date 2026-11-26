# Nápověda ke kroku 2 – Výpis sálu

Řádek se skládá nejlíp ze seznamu kousků a metody `join` z lekce 8:

```python
print(" ".join([".", ".", "."]))    # . . .
```

- Čísla míst jsou `range(1, len(sal[0]) + 1)`. `join` umí spojit jen texty,
  proto každé číslo převeď funkcí `str`.
- Čísla řad od jedničky dá `enumerate(sal, start=1)` z lekce 8.
- Řádek s čísly začni osmi mezerami. Tolik znaků má začátek ostatních řádků,
  `řada 1` a dvě mezery, takže čísla budou stát nad tečkami.
