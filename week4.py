#create a class named person.
class person:
    def __init__(self, name, age, gender):  #assign name,age,gender to the class person.
        self.name = name
        self.age = age
        self.gender = gender
        
#method called introduce that prints a message introducing the person with their name, age, and gender.
    def introduce(self):
        print(f"Hello my name is {self.name}. I am {self.age} old. I identify as {self.gender}.")
#instance of class person.
person_1 = person("Kennedy Ndiritu", 23, "Male")
#method to display persons information
person_1.introduce()