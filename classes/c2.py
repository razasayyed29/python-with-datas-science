class Animal:

    def __init__ (self, name, age,color,region):  #init means to create a classes(constructor)
        self.name = name
        self.age = age
        self.color = color
        self.region = region 
        self.is_domestic = False

    def info(self):
        print('Animal Details')
        print('Name: ', self.name)
        print('Age: ',  self.age)
        print('color: ', self.color)
        print('region: ', self.region)


o1 = Animal("Elephant",10,"gray","Africa")  
o2 = Animal("Lion",5,"yellow","Africa")      

o1.info()
o2.info()