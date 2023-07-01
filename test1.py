# 1:37:46
class Person:
    def __init__(self, name, surname, email_id, year_of_birth):
        # Self is a pointer which points towards the class 
        self.name = name 
        self.surname = surname
        self.email_id = email_id
        self.year_of_birth = year_of_birth
    
    def current_age(self, current_year):
        return current_year - self.year_of_birth

# You can use two init functions but only the first one is considered
nikhil = Person("Nikhil ","Shetty", "nikhilshetty00@gmail.com",1999)
print(nikhil.name)
print(nikhil.name + nikhil.surname)
print(nikhil.current_age(2023))
