#!/usr/bin/env python3
"""
Día 3 – Script interactivo refactorizado.

• La entrada/salida (input / print) está separada de la lógica de cálculo.
• Cada función incluye un docstring corto.
• Todos los mensajes usan f-strings.
"""

from datetime import datetime

CURRENT_YEAR = datetime.now().year


# ──────────────────────────────────────────────────────────────────────
# Funciones de entrada
# ──────────────────────────────────────────────────────────────────────
def pedir_nombre() -> str:
    """Pregunta el nombre y lo devuelve sin espacios extra."""
    return input("¿Cómo te llamas? ").strip()


def pedir_edad() -> int:
    """Pregunta la edad y valida que sea un número entero positivo."""
    while True:
        edad_str = input("¿Cuántos años tienes? ").strip()
        try:
            edad = int(edad_str)
            if edad <= 0:
                raise ValueError
            return edad
        except ValueError:
            print("❌  Introduce un número entero positivo para la edad.")


# ──────────────────────────────────────────────────────────────────────
# Lógica de negocio (cálculo)
# ──────────────────────────────────────────────────────────────────────
def calcular_anio_cien(edad: int, anio_actual: int = CURRENT_YEAR) -> int:
    """Devuelve el año en que el usuario cumplirá 100 años."""
    return anio_actual + (100 - edad)


# ──────────────────────────────────────────────────────────────────────
# Funciones de salida
# ──────────────────────────────────────────────────────────────────────
def construir_mensaje(nombre: str, anio_cien: int) -> str:
    """Crea el mensaje final para el usuario."""
    return (
        f"\n👋 ¡Hola, {nombre}!\n"
        f"En el año {anio_cien} cumplirás 100 años.\n"
        "¡Sigue vibe-codeando! 🚀"
    )


# ──────────────────────────────────────────────────────────────────────
# Orquestador
# ──────────────────────────────────────────────────────────────────────
def main() -> None:
    """Flujo principal del programa."""
    nombre = pedir_nombre()
    edad = pedir_edad()
    anio_cien = calcular_anio_cien(edad)
    mensaje = construir_mensaje(nombre, anio_cien)
    print(mensaje)


if __name__ == "__main__":
    main()