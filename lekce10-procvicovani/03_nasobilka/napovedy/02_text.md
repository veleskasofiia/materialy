# Nápověda ke kroku 2 – Příklad jako text

Text se nejlíp skládá f-stringem z lekce 6. Klíče slovníku piš uvnitř
f-stringu do apostrofů, protože celý f-string je v uvozovkách:

```python
f"{priklad['a']} ..."
```

Starší verze Pythonu (do 3.11) stejné uvozovky uvnitř f-stringu nedovolí
a skončí chybou `SyntaxError: f-string: unmatched '['`.
