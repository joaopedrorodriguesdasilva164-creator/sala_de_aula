# Pg personalizados

## introdução
O projeto PG personalizados tem como o obejtivo
desenvolver um sistema para gerenciar a comercialização de produtos personalizados, permitindo cadastrar clientes, controlar produtos disponíveis e registrar e acompanhar encomendas.
## problema
O projeto PG Personalizado busca solucionar a falta de um controle centralizado das informações relacionadas aos produtos personalizados, como camisetas e canecas, e às encomendas realizadas pelos clientes.
Atualmente, o registro dessas informações pode ocorrer de forma manual, por meio de cadernos, planilhas ou mensagens de WhatsApp, dificultando o controle dos produtos disponíveis, das quantidades solicitadas, dos valores, dos pagamentos e das datas de retirada.
Essa falta de organização pode ocasionar erros nos registros, perda de informações e dificuldades no acompanhamento das encomendas
### histórias
A falta de um controle centralizado pode ocasionar erros nos registros, perda de informações e dificuldades para acompanhar as encomendas dos clientes.
O sistema pretende facilitar a organização dos produtos e dos pedidos, reunindo as informações em um único ambiente.

- estória:
- Descrição:Desenvolver funcionalidades para:
•	Cadastrar e gerenciar produtos.
•	Controlar as quantidades disponíveis.
•	Registrar encomendas vinculadas aos clientes.
•	Associar produtos e quantidades às encomendas.
•	Acompanhar valores, pagamentos e datas de retirada.
•	Impedir encomendas com quantidades superiores ao estoque disponível


- tarefas:Camada 1 — Lógica / Modelo
•	Implementar a classe Produto.
•	Implementar a classe Encomenda.
•	Implementar a classe ItemEncomenda.
•	Criar validações de preços e quantidades.
Camada 2 — Persistência / Banco de dados
•	Criar ou revisar as tabelas no PostgreSQL.
•	Verificar os relacionamentos entre cliente, produto e encomenda.
•	Implementar as operações CRUD.
•	Validar a disponibilidade dos produtos antes de registrar uma encomenda.
Camada 3 — Testes
•	Testar o cadastro de produtos.
•	Testar o registro de encomendas.
•	Testar o relacionamento entre cliente, produto e encomenda.
•	Testar a rejeição de quantidades superiores ao estoque.

- quem:
- Oque: •	Classes e regras de negócio implementadas.
•	Banco de dados estruturado.
•	Operações CRUD funcionando.
•	Testes automatizados executados.
•	Validações das regras de negócio

- Milestone:Objetivo: concluir e validar as funcionalidades de cadastro de produtos e registro de encomendas, incluindo as regras de disponibilidade de estoque
- critérios de aceitação:•	Critério 1 — Cadastro de produtos: o sistema deve permitir cadastrar camisetas e canecas com nome, tipo, preço e quantidade disponível.
•	Critério 2 — Registro de encomendas: o sistema deve permitir registrar uma encomenda vinculada a um cliente, contendo os produtos, quantidades e valores correspondentes.
•	Critério 3 — Caso especial: o sistema deve impedir o registro de uma encomenda com quantidade superior à disponibilidade do produto em estoque.

- Suite:Validação dos testes
A suíte de testes deverá verificar se as funcionalidades implementadas atendem aos critérios de aceitação.
•	Testes de cadastro de produtos aprovados.
•	Testes de registro de encomendas aprovados.
•	Testes de validação de estoque aprovados.
•	Todos os testes executados com resultado PASS.
Resultado esperado: suíte de testes GREEN, sem falhas nos testes relacionados à funcionalidade.

** Green**