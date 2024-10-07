import os

directorio = os.path.dirname(file)
operaciones = os.path.join(directorio, "operaciones.txt")
resultados = os.path.join(directorio, "resultados.txt")

with open(operaciones,'r',encoding = 'utf-8') as f:
    operaciones = f.readlines()
    with open(resultados,'w',encoding = 'utf-8') as f:
        for linia in operaciones:
            num1 = int(linia.split()[0])
            op = linia.split()[1]
            num2 = int(linia.split()[2])
            match (op):
                case '+':
                    res = num1 + num2
                case '-':
                    res = num1 - num2
                case '*':
                    res = num1 * num2
                case '/':
                    if num2 == 0:
                        res = "No se puede dividir entre 0."
                    else:
                        res = num1 / num2
                case _: 
                    res = "Operador Invalido."
            f.write(f"{num1} {op} {num2} = {res}\n")