# Nápověda ke kroku 1 – Prázdný sál

Kostra funkce. Doplň, co se přidá do řady a co do sálu:

```python
def vytvor_sal(rady, mist):
    sal = []
    for cislo_rady in range(rady):
        rada = []
        for cislo_mista in range(mist):
            ...
        ...
    return sal
```

Pozor, kde je řádek `rada = []`. Musí být uvnitř vnějšího cyklu, aby každá řada
byla nový seznam. Kdyby byl před cyklem, byly by v sále tři jména pro jeden
a ten samý seznam a rezervace jednoho místa by se objevila ve všech řadách.
