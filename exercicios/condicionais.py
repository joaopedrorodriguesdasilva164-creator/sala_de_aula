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
   
    #Exercício 2
def verificar_maioridade(idade:int):
    if idade> 18:
        return "maior_de_idade"
    else:
        return"menor_de_idade"
    

#exercício 3
def verificar_maioridade(idade:int):
    if idade>18 :
        return"maior_de_idade"
    else:
        return "menor_de_idade"
        
    
#exercício 4
def verificar_paridade(numero:int):
    if numero> 0:
        return "positivo"
    elif numero <0 :
        return "negativo"
    else:
        return "menor_de_idade"
    
#exercício 5
def maior_de_dois(a,b):
    if a > b:
        return "o primeiro é maior" 
    if b > a:
        return "o segundo é maior"
    
    return "são iguais"
    



    
#exercicio 6
def calcular_desconto (valor_compra: float, e_cliente_vip:bool):
 if  e_cliente_vip or valor_compra > 200:
    return f"valor final:"
 return f"Valor final: {valor_compra*0.85}"
    
#exercicio 7
def conceito_nota(nota:float):
    if nota>9 and nota <10:
        return "a"
    if nota>= 7 and nota< 9:
        if nota > 5 and nota <7:
            return "C"
        return "F"
    
    #exercico 8
    def validar_triangulo(a:float,b:float,c:float):
        if a==b==c:
            return "equilatéro" 
        
        if a==b!=c:
            return "isóceles"
        if a!= b!= c:

            return "escaleno"
        else:
            return "não é triangulo"
        
    #exercicio 9
    def calcular_imposto(salario:float):
     excedente= salario- 20000
     if salario >= 20000 and salario< 40000:
         return excedente * 0.1
     if salario  >= 4000:
            return 200 +( excedente *0.2)
    return 0

    #exercicio 10
def validador_ano_bissexto(ano:int):
        if ano%4==0 and ano %400 ==0:
         return False
        return True
        

if __name__=="__ main__":
    teste=fizz_buzz(15)
print(teste)
