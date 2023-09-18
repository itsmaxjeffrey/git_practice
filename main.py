from random import randint


# challenge: try to resert 
my_list = [1,2,3,4]
my_new_list = [i * ranint(0,10) for i in my_list]

print(f"My list before randomization: {my_list}")
print(f" My list after ranodmization: {my_new_list}")
