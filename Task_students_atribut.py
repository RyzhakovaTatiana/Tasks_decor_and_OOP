class Student():
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.full_id = self.name + " - " + str(self.id)

    def get_name(self):
        return self.name



s = Student("Amit", 10)
print(s.name)
print(s.id)
print(s.full_id)

#Добавим новое имя и выведем полученный результат


s.name = "Vasilii"
print(s.name)
print(s.id)
print(s.full_id)

#Можно заметить, что атрибут full_id не обновляется. Чтобы атрибут full_id обновлялся,
#когда обновляется name или id , нужно превратить full_id в метод (см. Task_students_metod_full_id)

