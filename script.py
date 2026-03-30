class Libro:
    def __init__(self, titulo, paginas, isbn):
        self.titulo = titulo
        self.paginas = paginas
        self.isbn = isbn

    def get_titulo(self):
        return self.titulo

    def get_paginas(self):
        return self.paginas

    def get_isbn(self):
        return self.isbn

    def __gt__(self, other):
        if not isinstance(other, Libro):
            return False

        return self.get_paginas() > other.get_paginas()

    def __ge__(self, other):
        if not isinstance(other, Libro):
            return False

        return self.get_paginas() >= other.get_paginas()

    def __lt__(self, other):
        if not isinstance(other, Libro):
            return False

        return self.get_paginas() < other.get_paginas()

    def __le__(self, other):
        if not isinstance(other, Libro):
            return False

        return self.get_paginas() <= other.get_paginas()

    def __eq__(self, other):
        if not isinstance(other, Libro):
            return False

        return self.get_isbn() == other.get_isbn()

    def __ne__(self, other):
        if not isinstance(other, Libro):
            return True

        return self.get_isbn() != other.get_isbn()

    def __str__(self):
        return f"Título: '{self.get_titulo()}' - Hojas: {self.get_paginas()} - ISBN: '{self.get_isbn()}'"


libro1 = Libro("1984", 352, "9788499890944")
libro2 = Libro("El principito", 96, "9789876373487")
libro3 = Libro("1984", 352, "9789875669284")
libro4 = Libro("La metamorfosis", 128, "9788420651361")
libro5 = Libro("El principito", 96, "9789876373487")

print(libro1)
print(libro2)
print(libro3)
print(libro4)
print(libro5)

if libro3 > libro4:
    print(f"El libro 3 ({libro3.get_titulo()}) es más largo que el libro 4 ({libro4.get_titulo()})")

if libro5 < libro1:
    print(f"El libro 5 ({libro5.get_titulo()}) es más corto que el libro 1 ({libro1.get_titulo()})")

if libro5 == libro2:
    print(f"El libro 5 ({libro5.get_titulo()}) y el libro 2 son iguales")

if libro3 != libro1:
    print(f"El libro 3 ({libro3.get_titulo()}) y el libro 1 ({libro1.get_titulo()}) son distintos")
