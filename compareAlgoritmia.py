import timeit
from searchLineal import search_data_in_json as lineal_search
from searchSplit import split_and_search_data_in_json as split_search

# Definir la función que ejecutará las mediciones
def compare_search_functions():
    # Medir el tiempo de ejecución de search_data_in_json (búsqueda lineal)
    lineal_time = timeit.timeit(lambda: 
        lineal_search(filename="data.json", search_data="dff")
    , number=5)

    # Medir el tiempo de ejecución de split_and_search_data_in_json (búsqueda dividida)
    split_time = timeit.timeit(lambda: 
        split_search(filename="data.json", search_data="dfd")
    , number=5)

    # Imprimir los resultados
    print(f"Tiempo de ejecución para búsqueda lineal: {lineal_time} segundos")
    print(f"Tiempo de ejecución para búsqueda dividida: {split_time} segundos")

# Llamar a la función de comparación
compare_search_functions()
