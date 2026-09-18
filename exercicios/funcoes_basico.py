def formatar_saudacao(nome:str,cidade:str):
    return f"Olá {nome}, seja bem-vinda(a) a {cidade}!"

    
#exercício 2
def calcular_perimetro(largura:float,altura:float):
    perimetro=2*(largura+altura)
    print("EXERCICIOS========================\N\N")
    saudacao=formatar_saudacao("Alice""Porto alegre")
    print(f"1- {saudacao}")
    perimetro= calcular_perimetro(altura=10,largura=5)
    print(f"2- {perimetro}")

#exercicio 3
def fahrenheit_para_celsius(temp_f: float):
    temp_celsisus= (temp_f- 32)* (5/9)
    return temp_celsisus

#Exercício 4
def calcular_gorjeta_por_pessoa(conta:float,porcentagem_gorjeta:float,pessoas:int):
    gorjeta=(conta*porcentagem_gorjeta/100)/pessoas
    return gorjeta

#Exercicio 5
def resumo_circulo(raio:float): 
    pi=3.14159
    area= pi*(raio**2) 
    return f"um circulo de raio{raio} tem área de {area:.2f}"

#Exercício 6 
def resumo_juros_basico(capital:float,taxa:float):
    pass
  
#Exercício 7


if __name__=='__main__':
    saudacao=formatar_saudacao("Alice","Porto alegre")
    print(saudacao)