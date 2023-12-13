class Product:

    def __init__(self, cost, price) -> None:
        self.cost = cost
        self.price = price
    
    def getGain(self):
        return "Gain is: " + str(self.price - self.cost) + " coins"


class Drink:

    def __init__(self, name):
        self.name = name
    
    def getDetail(self):
        return "Drink's name is " + self.name


class Soda(Drink, Product):

    count = 0

    def __init__(self, name, flavor, brand, cost, price) -> None:
        Drink.__init__(self, name)
        Product.__init__(self, cost, price)
        self.__flavor = flavor
        self.__brand = brand
    
    def getDetail(self):
        return "Soda's detail: name: " + self.name + ", flavor: " + self.__flavor + ", brand: " + self.__brand
    
    @staticmethod
    def countCreatedInstances(self):
        return self.count