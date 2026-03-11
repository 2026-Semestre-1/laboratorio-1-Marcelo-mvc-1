"""
Nombre: calculadora
Entradas: operacion, op1, op2
Salidas: Calcula el resultado de dichas operaciones
Restricciones: Los parametros deben de ser Enteros
               Los parametros operacion debe permitir valores 1,2,3 y 4
               Los operadores deben de ser Enteros

"""

def calculadora(operacion, op1, op2):
    if not isinstance(operacion, int):
        return "El parametro debe de ser un entero"
    
    if not isinstance(op1, int):
        return "El operador debe de ser un entero"
    
    if not isinstance(op2, int):
        return "El operador debe de ser un entero"

    
    if operacion == 1:  
        return (op1 + op2)
    
    elif operacion == 2:
        return (op1 - op2)
    
    elif operacion == 3:  
        return (op1 * op2)
    
    elif operacion == 4:
        
        if op2 == 0:
            return "Error: división entre 0 no esta permitida"
        
        else:
            return  (op1 // op2)
        
    else:
        return "Esta operacion no es valida"


"""
Nombre: contadorDigitos
Entradas: num, digito
Salida: Retorno del numero de veces que el digito aparece en el numero
Restricciones: Ambos parámetros deben de ser Enteros
               El parámetro digito debe ser menor a 10 y mayor igual a 0
"""

def contadorDigitos(num, digito):
    if not isinstance(num, int):
        return "El parametro num debe de ser entero"

    if not isinstance(digito, int):
        return "El parametro num debe de ser entero"

    
    if digito < 0 or digito > 9:
        return "Error: el parámetro digito debe estar entre 0 y 9"

    if num < 0:
        num = -num
    
    contador = 0
    
    while num > 0:
        if num % 10 == digito:
            contador += 1
        num //= 10
    
    return contador





"""
Nombre: sumatoria_V2
Entradas: inicio, fin, distancia, excepción
Salida: Suma total de los numeros desde el parámetro hasta el final
Restricciones: Todos los parametros deben ser tipo Entero.
               Los parámetros distancia y excepcion deben ser menor a 10 y mayor a 0.
               Los valores inicio y fin deben ser positivos.
               Si la distancia es un número negativo, el valor de fin debe ser menor a inicio.
               Si la distancia es un número positivo, el valor de fin debe ser mayor a inicio.
               Si excepcion es igual a cero, se debe ignorar este valor, lo contrario, todo número dentro de la secuencia
               entre inicio y **final** sea divisible por esta excepción debe omitirse en la suma.
"""


def sumatoria_V2(inicio, fin, distancia, excepcion):
    
    if not isinstance(inicio, int):          
        return "Error: El parametro inicio debe ser entero"

    if not isinstance(fin, int):
         return "Error: El parametro fin debe ser entero"
    
    if not isinstance(distancia, int):
        return "Error: El parametro distancia debe ser entero"
    
    if not isinstance(excepcion, int):
         return "Error: El parametro excepcion debe ser entero"
    
    if distancia == 0 or (distancia >= 10 or distancia <= -10):
        return "Error: El parámetro distancia debe ser mayor a 0 y menor a 10"
    
    if excepcion < 0 or excepcion >= 10:
        return "Error: El parámetro excepcion debe estar entre 0 y 9"

    if inicio <= 0 or fin <= 0:
        return "Error: Los parametros inicio y fin deben ser positivos"
    
    if distancia > 0 and fin < inicio:
        return "Error: El parámetro inicio debe ser menor o igual a fin"
    
    if distancia < 0 and fin > inicio:
        return "Error: El parámetro fin debe ser menor o igual a inicio"
    
    return sumatoria_V2_aux(inicio, fin, distancia, excepcion)
                            

def sumatoria_V2_aux(inicio, fin, distancia, excepcion):
   
    suma = 0
    while (distancia > 0 and inicio <= fin) or (distancia < 0 and inicio >= fin):
        if excepcion == 0 or inicio % excepcion != 0:
            suma += inicio
            
        inicio += distancia

    return suma

