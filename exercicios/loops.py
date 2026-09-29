
def dobrar(numeros:[]):
    for numero in numeros:
        numero= numero* 2
        print(numero)

if __name__ == "__main__":
    dobrar([1,2,3,4,5])

#exercicio 1
def contar_negativos(numeros: list):
    count= 0
    for numero in numero :
        if numero< 0:
            count+=1
            return count
    

#exercicio 2
def contar_negativos(numeros):
    contador= 0
    for numero in numero:
        if numero <0 :
            contador+=1
            return contador 
        print (contar_negativos) [10,-3,0,-5,8,-1]

#exercicio 3
def somar_maiores_que(numeros,limite):
    soma=0

    for numero in numeros:
        if numero > limite:
            soma+=numero

#exercicio 4
def zerar_negativos(numeros):
    nova_lista=[]

    for numero in numeros:
        if numero <0:       
            nova_lista.append(0)
        else:
            nova_lista.append(numero)
    
    return nova_lista

    