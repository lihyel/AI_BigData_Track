class Car():
    def run(self):
        print("Car 달림")
class Sonata ( Car ):
    def run(self):
        print("Sonata 달림")
class Genesis ( Car ):
    def run(self):
        print("Genesis 달림")
        
def drive(c):
    c.run()
    
c1 = Car() 
c2 = Sonata() 
c3 = Genesis()  
drive(c1)
drive(c2)
drive(c3)