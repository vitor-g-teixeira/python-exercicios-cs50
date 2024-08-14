class Jar:
    def __init__(self, capacity = 12):
        if capacity >= 0 and type(capacity) == int:
            self.capacity = capacity
            self.size = 0
        else:
            raise ValueError("Unsuported amount")

    def deposit(self, n):
        if self.size + n <= self.capacity:
            self.size += n
        else:
            raise ValueError("Not enough space to that many cookies")

    def withdraw(self, n):
        if n <= self.size:
            self.size -= n
        else:
            raise ValueError("Not enough cookies in the jar to remove")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, n):
        self._capacity = n

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        self._size = n

    def __str__(self):
        return self.size * "🍪"

def main():
    cookie_jar = Jar(5)
    cookie_jar.deposit(3)
    print(cookie_jar)

if __name__ == "__main__":
    main()
