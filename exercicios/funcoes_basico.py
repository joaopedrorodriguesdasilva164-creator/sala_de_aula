def formatar_saudacao(nome:str,cidade:str):
    return f"Olá {nome}, seja bem-vinda(a) a {cidade}!"

if __name__=='__main__':
    saudacao=formatar_saudacao("Alice","Porto alegre")
    print(saudacao)