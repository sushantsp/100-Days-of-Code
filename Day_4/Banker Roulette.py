import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
length = len(names)

random_banker = random.randint(0,length-1)
print(f"{names[random_banker]} is going to buy the meal today!")

###
print(f"{random.choice(names)} is going to buy the meal today!")
