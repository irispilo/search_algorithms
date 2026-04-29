from searching import linear_search, binary_search

LISTA_DESORDENADA = list(range(100000))
LISTA_ORDENADA    = list(range(100000))
TARGET            = -1  # no existe en la lista -> peor caso


def test_benchmark_linear(benchmark):
    benchmark.pedantic(
        linear_search,
        args=(LISTA_DESORDENADA, TARGET),
        rounds=5,
        iterations=5,
    )


def test_benchmark_binary(benchmark):
    benchmark.pedantic(
        binary_search,
        args=(LISTA_ORDENADA, TARGET),
        rounds=5,
        iterations=5,
    )
