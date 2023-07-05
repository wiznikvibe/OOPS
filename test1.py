# 1:32:46 Krish Naik OOPS
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
# nikhil = Person()
# # print(nikhil.age(current_year=2023,year_of_birth=1999))

# print(nikhil.height())

# Bank Schema using OOPS
class Bank:
    def __init__(self,first_name,last_name,balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance


    def deposit(self, amount: int):
        self.balance += amount
        

    def withdraw(self, amount: int):
        if amount < self.balance:
            self.balance -= amount


# sbi = Bank("Nikhil", "Shetty")

# sbi.deposit(50000)
# sbi.withdraw(3500)
# print(sbi.balance)

class ToDoList:

    def __init__(self, owner):
        self.owner = owner 
        self.tasks = []

    def add_task(self,task):
        self.tasks.append(task)
    
    def complete_task(self, task):
        for task in self.tasks:
            self.tasks.remove(task)
            print(f"Task: {task} Completed")
    
    def display_task(self):
        print(f"The TODO tasks of {self.owner}:")
        for task in self.tasks:
            print(task)
        else: 
            print("Task was not found")


goals = ToDoList("Nikhil")

goals.add_task("Complete the OOPS concepts and implement using it on real world applications")
goals.add_task("Study the SQL concepts")
goals.add_task("Build a Interactive Project to showcase your skills")
goals.add_task("Improve your Resume and Apply for relevant jobs")

goals.complete_task("Complete the OOPS concepts and implement using it on real world applications")
goals.display_task()