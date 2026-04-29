# Search Algorithms

Repositorio con implementaciones sencillas de busqueda lineal y busqueda binaria, junto con pruebas automatizadas.

## Clonar el repositorio

```bash
git clone <URL-del-repositorio>
cd search_algorithms
```

## Preparar el entorno

Se recomienda usar un entorno virtual de Python:

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install pytest
```

## Ejecutar el unit testing

Las pruebas estan en [test_searching.py](test_searching.py) y cubren `linear_search` y `binary_search`.

```bash
pytest
```

Si quieres ejecutar solo ese archivo:

```bash
pytest test_searching.py
```

## Ejecutar el benchmarking

Este repositorio no incluye una herramienta de benchmarking dedicada, pero puedes comparar ambos algoritmos con `timeit` desde la raiz del proyecto:

```bash
python -m timeit -s "from searching import linear_search; data = list(range(10000)); target = 9999" "linear_search(data, target)"
python -m timeit -s "from searching import binary_search; data = list(range(10000)); target = 9999" "binary_search(data, target)"
```

La busqueda binaria requiere una lista ordenada; por eso en el ejemplo se usa `list(range(10000))`.
