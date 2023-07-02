# 1:37:46
class Person:
    # def __init__(self, name, surname, email_id, year_of_birth):
    #     # Self is a pointer which points towards the class 
    #     # self.name = name 
    #     # self.surname = surname
    #     # self.email_id = email_id
    #     # self.year_of_birth = year_of_birth
    
    def age(self, current_year,year_of_birth):
        return current_year - year_of_birth
    
    def name(self):
        name = input("What is you Name: ")
        return name 
    
    def height(self):
        height = float(input("Enter height in Inches: "))
        return height

    def weight(self):
        weight = int(input("What is your weight: "))
        return weight

         


# You can use two init functions but only the first one is considered
nikhil = Person()
# print(nikhil.age(current_year=2023,year_of_birth=1999))

print(nikhil.height())