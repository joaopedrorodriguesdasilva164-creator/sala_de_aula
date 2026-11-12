
import pytest


# TESTE 1 - CADASTRAR CLASSE
def test_cadastrar_classe(banco):
    banco("""
        INSERT INTO classe
        (nome, vida, mana, dano, escudo, cura)
        VALUES ('Mago', 100, 70, 20, 0, 0)
    """)

    banco.commit()

    resultado = banco.(
        "SELECT nome FROM classe"
    ).fetchone()

    assert resultado[0] == "Mago"


# TESTE 2 - LISTAR CLASSES
def test_listar_classes(banco):
    banco.("""
        INSERT INTO classe
        (nome, vida, mana, dano, escudo, cura)
        VALUES ('Mago', 100, 70, 20, 0, 0)
    """)

    banco.commit()

    resultado = banco.(
        "SELECT * FROM classe"
    ).fetchall()

    assert len(resultado) == 1


# TESTE 3 - ATUALIZAR CLASSE
def test_atualizar_classe(banco):
    banco.("""
        INSERT INTO classe
        (nome, vida, mana, dano, escudo, cura)
        VALUES ('Mago', 100, 70, 20, 0, 0)
    """)

    banco.commit()

    banco.execute("""
        UPDATE classe
        SET vida = 150
        WHERE nome = 'Mago'
    """)

    banco.commit()

    resultado = banco.execute(
        "SELECT vida FROM classe WHERE nome = 'Mago'"
    ).fetchone()

    assert resultado[0] == 150


# TESTE 4 - EXCLUIR CLASSE
def test_excluir_classe(banco):
    banco.execute("""
        INSERT INTO classe
        (nome, vida, mana, dano, escudo, cura)
        VALUES ('Mago', 100, 70, 20, 0, 0)
    """)

    banco.commit()

    banco.execute("""
        DELETE FROM classe WHERE nome = 'Mago'
    """)

    banco.commit()

    resultado = banco.execute(
        "SELECT * FROM classe"
    ).fetchall()

    assert resultado == []

