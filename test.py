z = "Hello, Ksu, how are you?"
print(z[:10])
print(z[-12:])
print(z[16:-5])
print(z[::2])

print(z[::4])
for letter in z:
    print(letter)

print(z[::-1])
print("Количество букв 'о' в этой строке =", z.count("o"))
print("Hello" in z)
print()
len_ = "%s - главное достоинство программиста. (%s)"
print(len_ % ("Лень", "Larry Wall"))
zif = "{} не лгут, но {} пользуются формулами. ({})"
print(zif.format("Цифры", "лжецы", "Robert A. Heinlein"))
b = "{num} Кб должно хватить для любых задач. ({author})"
print(b.format(num=640, author="Bill Gates"))
print()
subject = "оптимизация"
author = "Donald Knuth"
print(f"Преждевременная {subject} - корень всех зол. ({author})")
