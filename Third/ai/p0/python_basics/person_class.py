class Person:
    population = 0;
    def __init__(self, my_age):
        self.age = my_age;
        Person.population += 1;
    
    def get_population(self):
        return Person.population;
    
    def get_age(self):
        return self.age;
    def __str__(self):
        return 'You have an age Equal to %s' % (self.age);
