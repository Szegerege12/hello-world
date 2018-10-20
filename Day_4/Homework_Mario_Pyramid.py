"""
Wymagania:
Narysuj na ekranie piramidę Mario
(wypisując odpowiednio znaki #)
jako input podaj wysokość piramidy

Piramida wysokości 3 ma wyglądać:

  #
 ###
#####

1 - użyj jedynie pętli i znaków "#" oraz spacji
2 - przeczytaj https://docs.python.org/3/library/string.html aby ułatwić sobie życie
"""
h = int(input("Pyramid height: "))
for i in range(h):
    print("x"*(h-i-1)+"#"*(2*i+1))
