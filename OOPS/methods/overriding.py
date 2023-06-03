class van():
    def __init__(self,speed=9000,colour='mec'):
     self.velocity=speed
     self.paint=colour
    def display(self):
         print(self.velocity)
         print(self.paint)


car=van(9999,'white')
car.display()