class Test:
    def __init__(self):
        self.name = 'имя'

    def __repr__(self, atr) -> str:
        return f'{self.name} и {atr}'


class Test1(Test):
    def __init__(self):
        super().__init__()
        self.nickname = 'Прозвище'

    def __repr__(self) -> str:
        return super().__repr__(self.nickname)


s = Test1()

print(s)
