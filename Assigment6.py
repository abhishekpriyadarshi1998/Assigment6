#!/usr/bin/env python
# coding: utf-8

# In[6]:


#1. Create a JSON file (employee.json) containing employee information of minimum 5 employees
#Each employee information consists of Name, DOB, Height, City, State
#Write a python program that reads this information from the JSON file and saves the information into a list of objects of Employee class
#Finally print the list of the Employee objects.
#Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.


import json
employee_info=[{"Name":"Abhishek","DOB":"16/01/1995","Height":"5'8","City":"Buxar","State":"Bihar"},
               {"Name":"Siri","DOB":"24/04/1996","Height":"5'6","City":"Vijayawada","State":"Telengana"},
               {"Name":"Renu","DOB":"08/08/1997","Height":"5'5","City":"Nasik","State":"Maharastra"},
               {"Name":"Abhijeet","DOB":"18/07/1999","Height":"5'3","City":"Varanasi","State":"Uttar Pradesh"},
               {"Name":"Suman","DOB":"28/03/2001","Height":"5'4","City":"Ahmedabad","State":"Gujarat"}]
with open("employee.json","w") as f:
    d=json.dump(employee_info,f)
    print('json created')
with open("employee.json","r") as f:
    x=json.load(f)
    print('file loaded')
    print(x)

    
    
    
dict_state={'Bihar':'Patna', 'Uttar Pradesh':'Lucknow','Madhya Pradesh':'Bhopal','Telengana':'Hyderabad','Goa':'Panji','Sikkim':'Gangtok','Gujarat':'Gandhi Nagar'}
with open("state.json","w") as f:
    capitals=json.dump(dict_state,f)
    print('json file for state and their capitals is created')
    
    
    
    
    
    
    
#1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:

#a.It should have a function ‘description()’ which prints the name and age of the dog.
#b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
#d. Create objects and implement the above functionalities.

class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print("Name:", self.name)
        print("Age:", self.age, "years")

    def get_info(self):
        print("Coat color:", self.coat_color)


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, energy_level):
        super().__init__(name, age, coat_color)
        self.energy_level = energy_level

    def breed_description(self):
        print("Jack Russell Terriers are very energetic dogs.")

    def get_breed_info(self):
        print("Energy level:", self.energy_level)


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, drooling_tendency):
        super().__init__(name, age, coat_color)
        self.drooling_tendency = drooling_tendency

    def breed_description(self):
        print("Bulldogs are gentle and loving dogs.")

    def get_breed_info(self):
        print("Drooling tendency:", self.drooling_tendency)


jrt = JackRussellTerrier("Sherlock", 3, "Brown and white", 10)
print("\nJack Russell Terrier")
print("-------------------")
jrt.description()
jrt.get_info()
jrt.breed_description()
jrt.get_breed_info()

b = Bulldog("Bilbo", 5, "Brown", 3)
print("\nBulldog")
print("-------")
b.description()
b.get_info()
b.breed_description()
b.get_breed_info()


# In[ ]:




