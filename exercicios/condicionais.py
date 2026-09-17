#Exercicio 1

def fizz_buzz(numero:int):
    if numero % 3 == 0:
        return "fizz"
    elif numero% 5 == 0:
        return"buzz"
    elif numero % 3 == 0 and numero % 5== 0:
        return "fizz"
    else:
            return numero
    
    if__name__=="__main__:"
    teste= fizz_buzz(15)
    print(teste)