class Pasta:
    def __init__(self):
        self.ingredients = {}

    def add_ingredient(self, key, value):
        self.ingredients[key] = value

    def __str__(self):
        return f'Ingredients for pasta: {self.ingredients}'

class Pasta_Builder:
    def __init__(self):
        self.pasta = Pasta()

    def make_sauce(self, sauce):
        self.pasta.add_ingredient('sauce', sauce)
        return self

    def make_cheese(self, cheese):
        self.pasta.add_ingredient('cheese', cheese)
        return self

    def make_meat(self, meat):
        self.pasta.add_ingredient('meat', meat)
        return self

    def maker(self):
        return self.pasta


cook = Pasta_Builder()
carbonara = (cook
             .make_sauce('pecorino')
             .make_cheese('parmesan')
             .make_meat('bacon')
             .maker())

bolognese = (cook
             .make_sauce('bolognese')
             .make_cheese('none')
             .make_meat('beef')
             .maker())

meatballs = (cook
             .make_sauce('tomato sauce')
             .make_cheese('none')
             .make_meat('meatballs')
             .maker())
