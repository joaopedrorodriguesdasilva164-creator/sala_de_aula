def calcular_multa(dias_atraso):
    multa = dias_atraso * 2

    if multa > 50:
        multa = 50

    return multa