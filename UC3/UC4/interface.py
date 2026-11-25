
import streamlit as st

st.set_page_config(
    page_title="Sistema de Produtos",
    page_icon="📦",
    layout="centered"
)

st.title("📦 Sistema de Produtos")
st.write("Cadastro e gerenciamento de produtos")

# Menu lateral
opcao = st.sidebar.selectbox(
    "Escolha uma opção",
    ["Cadastrar Produto", "Consultar Produtos", "Alterar Produto", "Excluir Produto"]
)

# Banco de dados temporário
if "produtos" not in st.session_state:
    st.session_state.produtos = []

# Cadastro
if opcao == "Cadastrar Produto":
    st.subheader("Cadastrar Produto")

    nome = st.text_input("Nome do produto")
    preco = st.number_input("Preço (R$)", min_value=0.0)
    quantidade = st.number_input("Quantidade", min_value=0, step=1)

    if st.button("Cadastrar"):
        if nome:
            st.session_state.produtos.append({
                "nome": nome,
                "preco": preco,
                "quantidade": quantidade
            })
            st.success("Produto cadastrado com sucesso!")
        else:
            st.error("Informe o nome do produto.")

# Consulta
elif opcao == "Consultar Produtos":
    st.subheader("Lista de Produtos")

    for i, produto in enumerate(st.session_state.produtos):
        st.write(f"**Produto:** {produto['nome']}")
        st.write(f"**Preço:** R$ {produto['preco']:.2f}")
        st.write(f"**Quantidade:** {produto['quantidade']}")
        st.divider()

    if not st.session_state.produtos:
        st.info("Nenhum produto cadastrado.")

# Alteração
elif opcao == "Alterar Produto":
    st.subheader("Alterar Produto")

    if st.session_state.produtos:
        indice = st.selectbox(
            "Selecione o produto",
            range(len(st.session_state.produtos)),
            format_func=lambda i: st.session_state.produtos[i]["nome"]
        )

        produto = st.session_state.produtos[indice]

        novo_nome = st.text_input("Novo nome", value=produto["nome"])
        novo_preco = st.number_input(
            "Novo preço",
            min_value=0.0,
            value=float(produto["preco"])
        )

        nova_quantidade = st.number_input(
            "Nova quantidade",
            min_value=0,
            value=int(produto["quantidade"])
        )

        if st.button("Salvar alterações"):
            produto["nome"] = novo_nome
            produto["preco"] = novo_preco
            produto["quantidade"] = nova_quantidade
            st.success("Produto atualizado!")
    else:
        st.info("Não existem produtos cadastrados.")

# Exclusão
elif opcao == "Excluir Produto":
    st.subheader("Excluir Produto")

    if st.session_state.produtos:
        indice = st.selectbox(
            "Selecione o produto",
            range(len(st.session_state.produtos)),
            format_func=lambda i: st.session_state.produtos[i]["nome"]
        )

        if st.button("Excluir", type="primary"):
            st.session_state.produtos.pop(indice)
            st.success("Produto excluído!")
    else:
        st.info("Não existem produtos cadastrados.")
