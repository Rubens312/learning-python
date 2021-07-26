class Person:
    name = 'Rubens Kaiserman'
    age = 17
    weight = 72
    height = 1.92

    def grow_up(self, new_height):
        self.height = new_height


    def get_older(self, new_height):
        self.age = self.age + 1
        if self.age < 21:
            self.grow_up(self.height + 0.5)
            
    
    def get_fetter(self, new_weight):
        self.weight = new_weight

    def get_thinner(self, new_weight):
        self.weight = new_weight
