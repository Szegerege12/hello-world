"""
Wymagania:
Stwórz dwuwymiarową listę, w której listy wewnętrzne będą zawierały
3 kolejne liczby naturalne w zakresie do 100 - w każdej kolejnej subliście
pierwza liczba ma być o 1 większa niż PIERWSZA w poprzedniej

Dla chętnych:
List comprehension
https://docs.python.org/3.6/tutorial/datastructures.html#list-comprehensions

Wynik:
[[0, 1, 2], [1, 2, 3], ...
"""
def function(elements=100, lineLen=3):
    numbers = [str(x) for x in range(elements)]
    chunks = [numbers[x:x+lineLen] for x in range(0, len(numbers), lineLen)]
    strContent = "\n".join([" ".join(item) for item in chunks])
    return strContent

some01 = function(elements=100, lineLen=3)
print(some01)