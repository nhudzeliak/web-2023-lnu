from collections.abc import Iterable, Iterator


class AlphabeticalOrderIterator(Iterator):
    _position = None
    _reverse = False

    def __init__(self, collection, reverse=False):
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):
    def __init__(self, collection=[]):
        self._collection = collection

    def __iter__(self):
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)

    def add_item(self, item):
        self._collection.append(item)


if __name__ == "__main__":
    collection = WordsCollection()
    collection.add_item("apple")
    collection.add_item("banana")
    collection.add_item("cherry")

    print("Straight traversal:")
    for item in collection:
        print(item)

    print("Reverse traversal:")
    reverse_iterator = collection.get_reverse_iterator()
    for item in reverse_iterator:
        print(item)