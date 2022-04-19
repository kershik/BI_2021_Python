class LinkedListItem:
    def __init__(self, value):
        self.value = value
        self.__next = None

    def get_next(self):
        return self.__next

    def set_next(self, next_item):
        self.__next = next_item

    def has_next(self):
        return self.__next is not None


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__len = 0

    def __getitem__(self, index):
        current = self.__head
        for _ in range(index):
            if current is None or not current.has_next():
                raise IndexError
            current = current.get_next()
        return current.value

    def __len__(self):
        return self.__len

    def __contains__(self, value):
        current = self.__head
        for _ in range(self.__len):
            if current.value == value:
                return True
            current = current.get_next()
        return False
    
    def to_list(self):
        return [self[i] for i in range(len(self))]

    def add(self, value, index=None):
        self.__len += 1
        new_item = LinkedListItem(value)
        if index is None:
            if not self.__head:
                self.__head = new_item
            else:
                self.__tail.set_next(new_item)
            self.__tail = new_item
        else:
            current = self.__head
            for _ in range(index-1):
                if current is None or not current.has_next():
                    raise IndexError
                current = current.get_next()
            new_tail = current.get_next()
            current.set_next(new_item)
            new_item.set_next(new_tail)
        return self

    def extend(self, values, index=None):
        if index is None:
            for el in values:
                self.add(el)
        else:
            self.__len += len(values)
            current = self.__head
            for _ in range(index-1):
                if current is None or not current.has_next():
                    raise IndexError
                current = current.get_next()
            new_tail = current.get_next()
            for el in values:
                new_item = LinkedListItem(el)
                current.set_next(new_item)
                current = new_item
            current.set_next(new_tail)
        return self
    
    def pop(self, index=None):
        self.__len -= 1
        current = self.__head
        if index is None or index == self.__len:
            for _ in range(self.__len-1):
                current = current.get_next()
            current.set_next(None)
            pop_value = self.last()
            self.__tail = current
        else:
            for _ in range(index-1):
                if current is None or not current.get_next().has_next():
                    raise IndexError
                current = current.get_next()
            new_tail = current.get_next().get_next()
            pop_value = current.get_next().value
            current.set_next(new_tail)
        return pop_value

    def remove_last_occurence(self, value):
        current = self.__head
        last_occurence_index = None
        for i in range(self.__len):
            if current.value == value:
                last_occurence_index = i
            current = current.get_next()
        if last_occurence_index is None:
            raise ValueError(f'{value} not in list')
        else:
            self.pop(last_occurence_index)
        return self

    def first(self):
        return self.__head.value

    def last(self):
        return self.__tail.value


if __name__ == "__main__":
  items = LinkedList()
  items.add(10)
  items.add(11)
  items.add(12)
  items.add(13)
  items.add(14)
  