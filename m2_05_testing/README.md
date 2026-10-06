# Actividad Complementaria: Pruebas Unitarias con Unittest

Este repositorio contiene un módulo en Python con funciones matemáticas básicas y su correspondiente conjunto de pruebas unitarias implementadas con el framework nativo `unittest`.

## Estructura del Proyecto

* `math_utils.py`: Contiene las funciones matemáticas (`suma`, `resta`, `multiplicacion`, `division`) con validación estricta de tipos de entrada.
* `test_math_utils.py`: Contiene los casos de prueba divididos en dos clases (`TestMathUtilsValidos` y `TestMathUtilsInvalidos`).

## 🛠️ Requisitos

* Python 3.x instalado.

## Cómo ejecutar las pruebas

Abre la terminal en el directorio del proyecto y ejecuta:

```bash
python3 -m unittest -v test_math_utils.py