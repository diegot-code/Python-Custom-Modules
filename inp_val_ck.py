def check(x):
    if x == str:
        return "Value is a string"
    elif x == int:
        return "Value is an integer"
    elif x == float:
        return "Value is a float"
    elif x == list:
        return "Value is a list"
    elif x == dict:
        return "Value is a dictionary"
    elif x == set:
        return "Value is a set"
    elif x == bool:
        return "Value is a boolean"
    else:
        return "I don't know what you gave..."
    

# fix to type(x)