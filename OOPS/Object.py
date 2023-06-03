class car():
    pass
print('this is indide ')
car1=car()
car2=car()
car3=car()
car1.speed=123
car2.speed=456
car3.speed=678
car1.colour='black'
car2.colour='blue'
car3.colour='green'
print('printing class.object/ car1:-',car1.speed,car1.colour)
car1.speed=100
car1.colour='red'
print('After updating class.object/ car1:-',car1.speed,car1.colour)
