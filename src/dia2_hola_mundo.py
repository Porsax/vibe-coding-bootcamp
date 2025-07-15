#!/usr/bin/env python3
"""
Script interactivo Día 2 – Hola Mundo vibe-codificado

- Solicita nombre y edad al usuario.
- Calcula el año en que cumplirá 100 años.
- Maneja errores si la edad no es un número positivo.

Uso:
    python3 src/dia2_hola_mundo.py
"""

from datetime import datetime

CURRENT_YEAR = datetime.now().year


def pedir_datos() -> tuple[str, int]:
    """Pregunta nombre y edad; valida que edad sea un entero positivo."""
    nombre = input("¿Cómo te llamas? ").strip()

    while True:
        edad_str = input("¿Cuántos años tienes? ").strip()
        try:
            edad = int(edad_str)
            if edad <= 0:
                raise ValueError
            return nombre, edad
        except ValueError:
            print("❌  Por favor introduce un número entero positivo para la edad.")


def calcular_anio_cien(edad_actual: int) -> int:
    """Devuelve el año en que el usuario cumplirá 100 años."""
    return CURRENT_YEAR + (100 - edad_actual)


def main() -> None:
    nombre, edad = pedir_datos()
    anio_cien = calcular_anio_cien(edad)

    print(
        f"\n👋 ¡Hola, {nombre}!\n"
        f"En el año {anio_cien} cumplirás 100 años.\n"
        "¡Sigue vibe-codeando! 🚀"
    )


if __name__ == "__main__":
    main()