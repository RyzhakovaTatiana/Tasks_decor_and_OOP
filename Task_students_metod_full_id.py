class Student2():
    def __init__(self, name, id):
        self.name = name
        self.id = id


    def get_name(self):
        return self.name

    # Теперь добавим метод full_id, с помощью которого
    # можно будет получать новые значени full_id при изменении self.name или self.id = id
    def full_id(self):
        return self.name + " - " + str(self.id)



s = Student2("Amit", 10)
print(s.name)
print(s.id)
print(s.full_id())

#Добавим новое имя и айди, выведем полученный результат

s.name = "Vasilii"
s.id = 32
print(s.name)
print(s.id)
print(s.full_id())

#Можно заметить, что с помощью метода у нас обновляется значение full_id

