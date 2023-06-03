class van():
    def __init__(self,speed=4000,colour='sky blue'):
     self.velocity=speed
     self.paint=colour
    def display(self):
         print(self.velocity)
         print(self.paint)
car=van()
car.display()