class Student4():
    def __init__(self, name, id):
        self.name = name
        self.id = id
        # Внимание! Чтобы избежать рекурсии в сеттере, необходимо добавить атрибут класса  _ful_id
        self._full_id = self.name + " - " + str(self.id)

    def get_name(self):
        return self.name

    # Если возникает потребность преобразовать все такие атрибуты в метод и изменить атрибуты в вызовы методов, то
    # проще сделать это с помощью декоратора @property

    # можно будет получать новые значени full_id при изменении self.name или self.id = id, воспользовавшись декоратором
    # т.е. можно писать s.full_id без дополнительных круглых скобок
    # Декоратор свойств @property маскирует метод и обрабатывает так, как будто это свойство класса

    #Чтобы избежать рекурсии в сеттере, необходимо использовать атрибут класса  _ful_id
    @property
    def full_id(self):
        return self._full_id

    # Однако @property позволяет только прочитать данные и не позволяет вносить изменения. Чтобы вносить изменения,
    # необходимо добавить декоратор для full_id с помощью метода setter
    # full_id.setter унаследует все, что есть в исходном full_id, поэтому мы можем добавить его напрямую

    @full_id.setter
    def full_id(self, value):
        # Внимание! Чтобы избежать рекурсии необходимо использовать значение  _ful_id
        self._full_id = value


s = Student4("Amit", 10)
print(s.name)
print(s.id)
print(s.full_id)

# Добавим новое имя и айди, выведем полученный результат

s.name = "Vasilii"
s.id = 32
print(s.name)
print(s.id)
print(s.full_id)

# Можно заметить, что с помощью метода у нас обновляется значение full_id, а теперь, т.к. мы использовали декоратор
# @full_id.setter у нас есть возможность записывать новые значения в full_id

s.full_id = "Jane  - 18"
print(s.name)
print(s.id)
print(s.full_id)

