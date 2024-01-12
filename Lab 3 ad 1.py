# a
lista_osob = ['Anna', 'Jan', 'Kamil', 'Zofia']
posortowana_lista = sorted(lista_osob)
print("Posortowana lista alfabetycznie:", posortowana_lista)

# b
lista_osob.extend(['Marta', 'Tomasz'])
ostatnia_osoba = lista_osob.pop()
print("Lista po dodaniu dwóch osób:", lista_osob)
print("Ostatnia dodana osoba:", ostatnia_osoba)

# c
lista_osob.insert(2, 'Alicja')
print("Lista po dodaniu kolejnej osoby na pozycji 3:", lista_osob)

# d
lista_osob.reverse()
zduplikowana_lista = lista_osob * 2
print("Odwrócona lista:", lista_osob)
print("Zduplikowana odwrócona lista:", zduplikowana_lista)