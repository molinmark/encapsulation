class sheep:
    def __init__(self):
        self.__health=100
        self.__X = 0
        self.__Y = 0
        self.__name = 'Oвца1'

    @property
    def health(self):
        return self.__health
    @health.setter
    def health(self, val):
        if val<0 or val>100:
            print('Ошибка')
        else:
            self.__health = val
    def movement(self,direction):
        if direction == 'w':
            self.__Y += 1
        elif direction == 'a':
            self.__X -= 1
        elif direction == 's':
            self.__Y -= 1
        elif direction == 'd':
            self.__X += 1
        else:
            print('Некорректное направление')
        print(self.__name,'перемистилась в кординату:','X=',self.__X,'Y=',self.__Y,'текущее здоровье:',self.__health)

def main():
    sheep1 = sheep()
    while True:
        direction = input('Введите напраление "w", "a", "s", "d" или (-) чтобы закончить: ')
        if direction == '-':
            break
        sheep1.movement(direction)

main()
