class Prograssion():
    def __init__(self, start, step):
        self._start = start
        self._step = step
        self.cashe = {}



    @property#проперти контролирует чтение атрибута
    def start(self):
        return self._start



    #сеттер контролирует запись атрибута
    @start.setter#чтобы задать старт, нужно очистить кеш
    def start(self, val):
        self._start = val
        self.cashe = {}

    @property  # проперти контролирует чтение атрибута
    def step(self):
        return self._step

    @step.setter
    def step(self, val):
        self._step = val
        self.cashe = {}


    def get(self, positsia):
        if positsia in self.cashe:
            return self.cashe[positsia]#возвращаем число на конкретной позиции, если оно было найдено в кеше
        else:
            num = self.start + self.step*positsia#присваиваем число, находящееся на конкретной позиции новой переменной
            self.cashe[positsia] = num#записываем это число в кеш
            return  num#возвращаем это число в кеше


a = Prograssion(0, 3)
print(a.get(10))
print(a.get(1000))

