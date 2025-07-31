#===================================================== 1 ===============================================================
"""Task 1

A Person class

Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters and add them as
attributes. Make another method called talk() which makes prints a greeting from the person containing,
for example like this: "Hello, my name is Carl Johnson and I’m 26 years old"."""
class Person:

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.firstname + ' ' + self.lastname} and I’m {self.age} years old")

# TEST
# person_1 = Person('Bek', 'Djeliev', 40)
# person_1.talk()

#===================================================== 2 ===============================================================
"""Task 2

Doggy age

Create a class Dog with class attribute 'age_factor' equals to 7. Make __init__() which takes values for a dog’s age. 
Then create a method `human_age` which returns the dog’s age in human equivalent."""
class Dog:
    AGE_FACTOR = 7

    def __init__(self, dog_age: int):
        self.age = dog_age

    def human_age(self):
        return self.age * Dog.AGE_FACTOR

# TEST
# dog_1 = Dog(10)
# print(dog_1.human_age())

#===================================================== 3 ===============================================================
"""Task 3
TV controller
Create a simple prototype of a TV controller in Python. It’ll use the following commands:

first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
exists(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.
The default channel turned on before all commands is №1.
Your task is to create the TVController class and methods described above.
"""
CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    def __init__(self, channels):
        self.channels_list = channels
        self.cur_channel = 1

    def first_channel(self):
        self.cur_channel = 1
        return self.channels_list[0]

    def last_channel(self):
        self.cur_channel = len(self.channels_list)
        return self.channels_list[self.cur_channel - 1]

    def turn_channel(self, n: int):
        self.cur_channel = n if 1 <= n <= len(self.channels_list) else 1
        return self.channels_list[self.cur_channel - 1]

    def next_channel(self):
        self.cur_channel = self.cur_channel % len(self.channels_list) + 1
        return  self.channels_list[self.cur_channel - 1]

    def previous_channel(self):
        self.cur_channel = len(self.channels_list) if self.cur_channel == 1 else self.cur_channel - 1
        return self.channels_list[self.cur_channel - 1]

    def exists(self, channel):
        # if((type(channel) == int  and channel in range(1, len(self.channels_list) + 1))
                                # or (type(channel) == str and channel in self.channels_list)):
        if channel in range(1, len(self.channels_list) + 1) or channel in self.channels_list:
            return 'Yes'
        else:
            return 'No'

    def current_channel(self):
        return self.channels_list[self.cur_channel - 1]

# TEST
# controller = TVController(CHANNELS)

# print(controller.current_channel())

# print(controller.last_channel())

# print(controller.turn_channel(-1))
# print(controller.turn_channel(100000))
# print(controller.turn_channel(2))

# print(controller.next_channel())
# print(controller.next_channel())
# print(controller.next_channel())

# print(controller.previous_channel())
# print(controller.previous_channel())
# print(controller.previous_channel())
# print(controller.previous_channel())

# print(controller.exists(4))
# print(controller.exists(0))
# print(controller.exists(1))
# print(controller.exists("Discovery"))
# print(controller.exists("BBC"))