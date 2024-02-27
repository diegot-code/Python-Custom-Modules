def dataCheck(x: str):
    if type(x) != str:
        return f'{x} is not a string.'
    else:
        return x.casefold().capitalize()