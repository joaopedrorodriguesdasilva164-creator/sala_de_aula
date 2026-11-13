
# ==========================================
# PLANO DE TESTE - MINI MUNDO
# Sistema: Locadora de Jogos
# ==========================================

plano_de_teste = [
    {
        "teste": "CT01 - Criar jogo",
        "esperado": "Jogo cadastrado corretamente",
        "obtido": "Jogo cadastrado corretamente",
        "situacao": "Aprovado"
    },

    {
        "teste": "CT02 - Buscar jogo por ID",
        "esperado": "Jogo encontrado pelo ID",
        "obtido": "Jogo encontrado pelo ID",
        "situacao": "Aprovado"
    },

    {
        "teste": "CT03 - Buscar jogo por título",
        "esperado": "Jogo encontrado pelo título",
        "obtido": "Jogo encontrado pelo título",
        "situacao": "Aprovado"
    },

    {
        "teste": "CT04 - Atualizar preço",
        "esperado": "Preço atualizado corretamente",
        "obtido": "Preço atualizado corretamente",
        "situacao": "Aprovado"
    },

    {
        "teste": "CT05 - Excluir jogo",
        "esperado": "Jogo excluído corretamente",
        "obtido": "Jogo excluído corretamente",
        "situacao": "Aprovado"
    }
]

# Exibir plano de teste
for teste in plano_de_teste:
    print("\nTeste:", teste["teste"])
    print("Esperado:", teste["esperado"])
    print("Obtido:", teste["obtido"])
    print("Situação:", teste["situacao"])
    print("-" * 50)

# Resumo dos testes
aprovados = sum(
    1 for teste in plano_de_teste
    if teste["situacao"] == "Aprovado"
)

reprovados = sum(
    1 for teste in plano_de_teste
    if teste["situacao"] == "Reprovado"
)

print("\n========== RESUMO ==========")
print("Total de testes:", len(plano_de_teste))
print("Aprovados:", aprovados)
print("Reprovados:", reprovados)

