from relatorio import Aluguel,total_do_cliente,RelatorioDoMes
def test_todos_alugueis_mesmo_cliente():
    #Cenario
    alugueis= [
        Aluguel("Ana", "fifa", 20),
        Aluguel("Ana", "Skyrim",30),              
        Aluguel ("Ana","Gta",10)
    ]
    #ação
    total= total_do_cliente(alugueis, "Ana")
    # validação
    assert total == 60
    
def test_todos_alugueis_mais_clientes():
    #Cenario
    alugueis= [
        Aluguel("Ana", "fifa", 20),
        Aluguel("Jaõa", "Skyrim",30),              
        Aluguel ("Ana","Gta",10)
    ]
    #ação
    total= total_do_cliente(alugueis, "Ana")
    # validação
    assert total == 30