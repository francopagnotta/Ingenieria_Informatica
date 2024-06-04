# 9. Una librería tiene un sistema que guarda los nombres de todos los libros que tienen en una lista de la
# siguiente forma: [“El principito”, “It”, “Sherlock Holmes”...]. Se quiere saber cuántos libros repetidos
# tienen. Hacer código que imprima para cada título, cuántos ejemplares hay.
# Aclaración: No se sabe la cantidad de elementos que tiene la lista, la lista nombrada es solo un ejemplo.


book_list = [
	"Pride and Prejudice",
    "To Kill a Mockingbird",
    "The Catcher in the Rye",
    "The Lord of the Rings",
    "The Adventures of Huckleberry Finn",
    "The Catcher in the Rye",
    "The Catcher in the Rye",
    "The Handmaid's Tale",
    "The Adventures of Huckleberry Finn",
    "The Catcher in the Rye",
    "Moby Dick",
    "Jane Eyre",
]
book_list_copy = []

def checkIfExist(book):
    if book not in book_list_copy:
        return True
    else:
        return False


def getBookVolumes(book_list):
    book_list_copy.extend(filter(checkIfExist, book_list))

    for book in book_list_copy:
        volumes = list(book_list).count(book)

        print(
            f"name: {book}" + "\n"
            f"volumes: {volumes}" + "\n"
        )        
        
getBookVolumes(book_list)


