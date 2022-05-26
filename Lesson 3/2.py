"""
2. Разработать класс SuperStr, который наследует функциональность
стандартного типа str и содержит 2 новых метода:
● метод is_repeatance (s), который принимает 1 аргумент s и
возвращает True или False в зависимости от того, может ли
текущая строку быть получена целым количеством повторов
строки s. Вернуть False, если s не является строкой. Считать, что
пустая строка не содержит повторов.
● метод is_palindrom (), который возвращает True или False в
зависимости от того, является ли строка палиндромом. Регистрами
символов пренебрегать. Пустую строку считать палиндромом.
"""


class SuperStr(str):
    def __init__(self, string):
        self.string = string

    def is_repeatance(self, s):
        self.s = s
        self.compare = ''
        if type(self.s) == str:
            if self.s == self.string:
                return True
            elif len(self.s) == len(self.string) and self.s != self.string:
                return False
            else:
                while len(self.compare) <= len(self.string):
                    if self.s != self.string:
                        self.compare += self.s
                        if self.compare == self.string:
                            return True
                        elif len(self.compare) == len(self.string) and self.compare != self.string:
                            return False
                        elif len(self.compare) > len(self.string):
                            return False
        else:
            return False

    def is_palindrom(self):
        if self.string == self.string[::-1]:
            return True
        else:
            return False


s = SuperStr('123123123123')
print(s.is_repeatance('123'))
print(s.is_repeatance('123123'))
print(s.is_repeatance('123123123123'))
print(s.is_repeatance('12312'))
print(s.is_repeatance(123))
print(s.is_palindrom())
print(s)
print(int(s))
print(s + 'qwe')
p = SuperStr('123_321')
print(p.is_palindrom())
