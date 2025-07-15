from src.dia2_hola_mundo import calcular_anio_cien

def test_calcular_anio_cien():
    # Suponemos que la edad es 25 y el año actual 2025
    assert calcular_anio_cien(25) == 2100