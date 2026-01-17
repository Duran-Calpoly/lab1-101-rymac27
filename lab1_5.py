def check_multiple(number):
    if number % 3 == 0 and number % 5 == 0:
        return True
    else:
        return False

def check_password(input_string):
    if input_string == "Python123":
        return "access granted"
    else:
        return "access denied"    

def calculate_federal_tax(salary):
    if salary<=(11000):    
        tax = salary * 0.1
    elif salary<(44725):    
        tax = salary * 0.12
    elif salary<(95375):    
        tax = salary * 0.22   
    else:
        tax = salary * 0.24
    return tax
        