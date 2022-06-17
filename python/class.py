class Pizza:
    def __init__(self,crust,toppings,sauce,cheese):
        self.crust = crust
        self.toppings = toppings
        self.sauce = sauce
        self.cheese = cheese

    def order_pizza(self, drink, appetizer):
        self.drink = drink
        self.appetizer = appetizer
        return f"Zamówienie na pizzę na {self.crust} cieście z dodatkowymi -> {self.toppings},\
sos ->{self.sauce},ser ->{self.cheese},napój -> {drink},przystawka -> {appetizer}."



funghi_pizza = Pizza( "cienkim", "pieczarkami" ,"czosnkowy" ,"mozzarella")
print(funghi_pizza.order_pizza("fanta","frytki"))




class Fridge:
    def __init__(self):
        self.isopen = False
        self.content = []
        
        
    def put_in(self,food):
        self.content.append(food)
    
    def put_out(self,food):
        if self.isopen == True:
            self.content.remove(food)
        else:
            print("Otwórz lodówkę")
  
fridge_1 = Fridge()
fridge_1.isopen = True
fridge_1.put_in("milk")
print(fridge_1.isopen)
print(fridge_1.content)
fridge_1.put_out("milk")
print(fridge_1.content)
fridge_1.isopen = False
fridge_1.put_in("milk")