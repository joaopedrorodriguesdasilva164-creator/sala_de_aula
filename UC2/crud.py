
import sqlite3

con = sqlite3.connect("rpg.db")
cursor = con.cursor()

# CRIAR TABELAS
cursor.executescript("""
CREATE TABLE IF NOT EXISTS classe (
    id_classe INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    vida INTEGER NOT NULL,
    mana INTEGER DEFAULT 0,
    dano INTEGER DEFAULT 0,
    escudo INTEGER DEFAULT 0,
    cura INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS trabalho (
    id_trabalho INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS npc (
    id_npc INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    id_trabalho INTEGER,
    FOREIGN KEY (id_trabalho)
        REFERENCES trabalho(id_trabalho)
);

CREATE TABLE IF NOT EXISTS dialogo (
    id_dialogo INTEGER PRIMARY KEY AUTOINCREMENT,
    texto TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS npc_dialogo (
    id_npc INTEGER,
    id_dialogo INTEGER,
    PRIMARY KEY (id_npc, id_dialogo),
    FOREIGN KEY (id_npc) REFERENCES npc(id_npc),
    FOREIGN KEY (id_dialogo) REFERENCES dialogo(id_dialogo)
);
""")

con.commit()


# =========================
# CRUD DE CLASSES
# =========================

def cadastrar_classe():
    nome = input("Nome da classe: ")
    vida = int(input("Vida: "))
    mana = int(input("Mana: "))
    dano = int(input("Dano: "))
    escudo = int(input("Escudo: "))
    cura = int(input("Cura: "))

    cursor.execute("""
    INSERT INTO classe
    (nome, vida, mana, dano, escudo, cura)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, vida, mana, dano, escudo, cura))

    con.commit()
    print("Classe cadastrada!")


def listar_classes():
    cursor.execute("SELECT * FROM classe")
    for classe in cursor.fetchall():
        print(classe)


def atualizar_classe():
    id_classe = int(input("ID da classe: "))
    nome = input("Novo nome: ")
    vida = int(input("Nova vida: "))
    mana = int(input("Nova mana: "))
    dano = int(input("Novo dano: "))
    escudo = int(input("Novo escudo: "))
    cura = int(input("Nova cura: "))

    cursor.execute("""
    UPDATE classe SET
    nome=?, vida=?, mana=?, dano=?, escudo=?, cura=?
    WHERE id_classe=?
    """, (nome, vida, mana, dano, escudo, cura, id_classe))

    con.commit()
    print("Classe atualizada!")


def excluir_classe():
    id_classe = int(input("ID da classe: "))

    cursor.execute(
        "DELETE FROM classe WHERE id_classe=?",
        (id_classe,)
    )

    con.commit()
    print("Classe excluída!")


# =========================
# CRUD DE TRABALHOS
# =========================

def cadastrar_trabalho():
    nome = input("Nome do trabalho: ")

    cursor.execute(
        "INSERT INTO trabalho (nome) VALUES (?)",
        (nome,)
    )

    con.commit()
    print("Trabalho cadastrado!")


def listar_trabalhos():
    cursor.execute("SELECT * FROM trabalho")
    for trabalho in cursor.fetchall():
        print(trabalho)


# =========================
# CRUD DE NPC
# =========================

def cadastrar_npc():
    nome = input("Nome do NPC: ")
    listar_trabalhos()

    id_trabalho = int(input("ID do trabalho: "))

    cursor.execute("""
    INSERT INTO npc (nome, id_trabalho)
    VALUES (?, ?)
    """, (nome, id_trabalho))

    con.commit()
    print("NPC cadastrado!")


def listar_npcs():
    cursor.execute("""
    SELECT npc.id_npc, npc.nome, trabalho.nome
    FROM npc
    LEFT JOIN trabalho
    ON npc.id_trabalho = trabalho.id_trabalho
    """)

    for npc in cursor.fetchall():
        print(npc)


def excluir_npc():
    id_npc = int(input("ID do NPC: "))

    cursor.execute(
        "DELETE FROM npc_dialogo WHERE id_npc=?",
        (id_npc,)
    )

    cursor.execute(
        "DELETE FROM npc WHERE id_npc=?",
        (id_npc,)
    )

    con.commit()
    print("NPC excluído!")


# =========================
# CRUD DE DIÁLOGOS
# =========================

def cadastrar_dialogo():
    texto = input("Texto do diálogo: ")

    cursor.execute(
        "INSERT INTO dialogo (texto) VALUES (?)",
        (texto,)
    )

    con.commit()
    print("Diálogo cadastrado!")


def listar_dialogos():
    cursor.execute("SELECT * FROM dialogo")
    for dialogo in cursor.fetchall():
        print(dialogo)


def vincular_dialogo():
    listar_npcs()
    id_npc = int(input("ID do NPC: "))

    listar_dialogos()
    id_dialogo = int(input("ID do diálogo: "))

    cursor.execute("""
    INSERT INTO npc_dialogo (id_npc, id_dialogo)
    VALUES (?, ?)
    """, (id_npc, id_dialogo))

    con.commit()
    print("Diálogo vinculado ao NPC!")


def listar_dialogos_npc():
    id_npc = int(input("ID do NPC: "))

    cursor.execute("""
    SELECT npc.nome, dialogo.texto
    FROM npc_dialogo
    JOIN npc ON npc_dialogo.id_npc = npc.id_npc
    JOIN dialogo ON npc_dialogo.id_dialogo = dialogo.id_dialogo
    WHERE npc.id_npc = ?
    """, (id_npc,))

    for resultado in cursor.fetchall():
        print(resultado)


# =========================
# MENU PRINCIPAL
# =========================

while True:
    print("""
===== SISTEMA RPG =====

1 - Cadastrar classe
2 - Listar classes
3 - Atualizar classe
4 - Excluir classe

5 - Cadastrar trabalho
6 - Listar trabalhos

7 - Cadastrar NPC
8 - Listar NPCs
9 - Excluir NPC

10 - Cadastrar diálogo
11 - Listar diálogos
12 - Vincular diálogo ao NPC
13 - Listar diálogos do NPC

0 - Sair
""")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_classe()
    elif opcao == "2":
        listar_classes()
    elif opcao == "3":
        atualizar_classe()
    elif opcao == "4":
        excluir_classe()
    elif opcao == "5":
        cadastrar_trabalho()
    elif opcao == "6":
        listar_trabalhos()
    elif opcao == "7":
        cadastrar_npc()
    elif opcao == "8":
        listar_npcs()
    elif opcao == "9":
        excluir_npc()
    elif opcao == "10":
        cadastrar_dialogo()
    elif opcao == "11":
        listar_dialogos()
    elif opcao == "12":
        vincular_dialogo()
    elif opcao == "13":
        listar_dialogos_npc()
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")

con.close()
