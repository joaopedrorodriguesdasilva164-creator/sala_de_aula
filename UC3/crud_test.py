
def criar_jogo(conn, titulo, plataforma, preco):
    if not titulo or preco < 0:
        return False

    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO jogo (titulo, plataforma, preco)
        VALUES (?, ?, ?)
        """,
        (titulo, plataforma, preco)
    )
    conn.commit()
    return cursor.lastrowid


def buscar_por_id(conn, id_jogo):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM jogo WHERE id_jogo = ?",
        (id_jogo,)
    )
    return cursor.fetchone()


def buscar_por_titulo(conn, titulo):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM jogo WHERE titulo LIKE ?",
        (f"%{titulo}%",)
    )
    return cursor.fetchall()


def atualizar_preco(conn, id_jogo, preco):
    if preco < 0:
        return False

    cursor = conn.cursor()
    cursor.execute(
        "UPDATE jogo SET preco = ? WHERE id_jogo = ?",
        (preco, id_jogo)
    )
    conn.commit()
    return cursor.rowcount > 0


def excluir_jogo(conn, id_jogo):
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM jogo WHERE id_jogo = ?",
        (id_jogo,)
    )
    conn.commit()
    return cursor.rowcount > 0
