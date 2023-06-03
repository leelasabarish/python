#calling with the function
class van():
    def __init__(self,speed=9000,colour='mec'):
     self.velocity=speed
     self.paint=colour
    def display(self,cost):
        self.amount=cost
        print(self.velocity)
        print(self.paint)
        print(self.amount)

car=van(8888,'mec blue')
car.display('30757$')
