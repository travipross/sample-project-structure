

class Animal:
    def __init__(self, species, num_legs=4):
        self.species = species
        self.num_legs = num_legs

    def __repr__(self):
        return f"<Animal (species={self.species}, num_legs={self.num_legs})>"

    def run(self):
        print(f"I am a {self.species}, and I am running.")



class Dog(Animal):
    def __init__(self, breed="Pug"):
        super().__init__(species="dog", num_legs=4)
        self.breed = breed
    
    def __repr__(self):
        return f"<Dog (breed={self.breed})>"

    # semi-advanced, can be avoided but is nice
    @staticmethod
    def pant():
        print(f"I'm a dog and I'm panting")


    # advanced; not necessary
    @classmethod
    def print_info(cls):
        print("I'm a dog")




my_animal1 = Animal('cat')
my_animal2 = Animal(species='ant', num_legs=6)

print(my_animal1)
print(my_animal2)

my_animal1.run()
my_animal2.run()

my_dog = Dog()

my_dog.pant()
my_dog.run()

print(my_dog)

print(Dog('mutt'))

Dog.print_info()



class MicrophoneStats:
    def __init__(self, df):
        self.df = df
        self.std_dev = None
        self.skew = None
        self.kurtosis = None
    
    def compute_stats(self):
        self.std_dev = self.df.std()
        self.skew = self.df.skew()
        self.kurtosis = self.df.kurtosis()

    def to_dict(self):
        stats = {
            "std_dev": self.std_dev,
            "skewness": self.skew,
            "kurtosis": self.kurtosis
        }
        return stats

    def __repr__(self):
        return "<Generic stats object>"

import pandas as pd 

my_stats_chunk_1 = MicrophoneStats(pd.read_csv("sample_data.txt", sep="\t", header=None) )

print(my_stats_chunk_1)
print(my_stats_chunk_1.to_dict())
my_stats_chunk_1.compute_stats()
print(my_stats_chunk_1.to_dict())