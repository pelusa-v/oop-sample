from utils.drink import *

def main():

    drink = Drink(name="Red Bull")
    print(drink.getDetail())

    soda = Soda(name="Sprite", flavor="Lemon", brand="Sprite company", price=200, cost=100)
    print(soda.getDetail())
    print(soda.getGain())

    
if __name__ == "__main__":
    main()