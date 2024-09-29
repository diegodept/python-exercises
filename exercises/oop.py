
# objet = a bundle of related attributes (variables) and methods (functions)
# ex: phone, cup, book
# you need a "class" to create many objects 

# class = (blueprint) used to design the structure and layout of and object

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

car1 = Car("mustang", 2024, "red", False)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

        
