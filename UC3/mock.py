
from unittest.mock import Mock
from datetime import date
from cobranca import Cobrador


def test_jogador_atrasado():
    whatsapp = Mock()
    relogio = Mock()

    relogio.hoje.return_value = date(2026, 11, 10)

    cobrador = Cobrador(whatsapp, relogio)

    resultado = cobrador.cobrar(
        "Mago",
        50,
        date(2026, 11, 9)
    )

    assert resultado == "atrasado"
    whatsapp.enviar.assert_called_once()


def test_jogador_no_prazo():
    whatsapp = Mock()
    relogio = Mock()

    relogio.hoje.return_value = date(2026, 11, 10)

    cobrador = Cobrador(whatsapp, relogio)

    resultado = cobrador.cobrar(
        "Arqueiro",
        30,
        date(2026, 11, 11)
    )

    assert resultado == "no prazo"
    whatsapp.enviar.assert_not_called()

