def calculate_average(num1:float, num2:float, num3:float):
    total = num1 + num2 + num3
    average = total / 3
    return average

def add_tax(bill_total:float):
    total = bill_total * 1.1
    return total

def greet_user(name:str):
    greeting = "Hello " + name
    return greeting