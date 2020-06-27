class Game:
    variable1 = 'Hello'
    variable2 = 'World!'
#Basic concept of instantiating a class

if __name__=="__main__":
    x = Game()
    print("{} {}".format(x.variable1, x.variable2))
#This is how you access out of a class
#=================================================
#Parent Class
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    dna = "sequenceA"
    origin = "Unknown"
    carbon_based = True #boolean
#defined parent class

    def information(self): #special to classes, want access to information in classes, pass self
        msg ="\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(self.name, self.species, self.legs, self.arms, self.dna, self.origin, self.carbon_based)    
        return msg

    
#Child class instance
class Human(Organism):
    name = 'Sam'
    species = 'Homo Sapien'
    legs = 2
    arms = 2
    origin = 'Earth'

    def ingenuity(self):
        msg = "\nCreates a deadly weapon with a paper clip, gum and a roll of tape!"
        return msg


#another class instance
class Dog(Organism):
    name = 'Spot'
    species = 'K9'
    legs = 4
    arms = 0
    dna = 'SequenceB'
    origin = 'Earth'

    def bit(self):
        msg = "\nEmits a loud growl and bites down on target!"
        return msg

#another class instance
class Bacterium(Organism):
    name = 'Mycelium'
    species = 'Bacteria'
    legs = 0
    arms = 0
    dna = 'SequenceC'
    origin = 'Mars'

    def replication(self):
        msg = "\nThe cell begins to divide into two!"
        return msg


if __name__=="__main__":
    #instantiation
    human = Human()
    print(human.information())#from mother
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bit())

    bacterium = Bacterium()
    print(bacterium.information())
    print(bacterium.replication())



