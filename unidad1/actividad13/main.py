import os

directori = os.path.dirname(file)
operacions = os.path.join(directori, "operacions.txt")
resultats = os.path.join(directori, "resultats.txt")

with open(operacions,'r',encoding = 'utf-8') as f:
    operacions = f.readlines()
    with open(resultats,'w',encoding = 'utf-8') as f:
        for linia in operacions:
            num1 = int(linia.split()[0])
            op = linia.split()[1]
            num2 = int(linia.split()[2])
            match (op):
                case '+':
                    res = num1 + num2
                case '-':
                    res = num1 - num2
                case '':
                    res = num1 num2
                case '/':
                    if num2 == 0:
                        res = "No se puede dividir entre 0."
                    else:
                        res = num1 / num2
                case _: # PER DEFECTE
                    res = "Operador Invalido."
            f.write(f"{num1} {op} {num2} = {res}\n")