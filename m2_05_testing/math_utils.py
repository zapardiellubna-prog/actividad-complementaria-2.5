from typing import Union 

Number = Union[int, float] 

def ensure_number(x, y): 
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)): 
        raise TypeError("Ambos argumentos deben ser int o float.") 

def suma(x: Number, y: Number) -> Number: 
    ensure_number(x, y) 
    return x + y 

def resta(x: Number, y: Number) -> Number: 
    ensure_number(x, y) 
    return x - y 

def multiplicacion(x: Number, y: Number) -> Number: 
    ensure_number(x, y) 
    return x * y 

def division(x: Number, y: Number) -> float: 
    ensure_number(x, y) 
    if y == 0: 
        raise ZeroDivisionError("No se puede dividir entre cero.") 
    return x / y