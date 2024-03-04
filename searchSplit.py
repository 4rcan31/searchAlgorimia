import json

def recursive_binary_search(data_array, search_data):
    # Verificar si el array está vacío
    if not data_array:
        return False

    # Calcular el índice medio
    mid = len(data_array) // 2

    # Obtener el valor en el índice medio
    mid_value = data_array[mid]

    # Comparar con el dato buscado
    if mid_value == search_data:
        return True
    elif mid_value < search_data:
        # Realizar búsqueda en la mitad derecha
        return recursive_binary_search(data_array[mid + 1:], search_data)
    else:
        # Realizar búsqueda en la mitad izquierda
        return recursive_binary_search(data_array[:mid], search_data)

def split_and_search_data_in_json(filename, search_data):
    try:
        # Cargar el archivo JSON
        with open(filename, "r") as json_file:
            data = json.load(json_file)["dataInArray"]

        # Convertir el dataInArray a un array
        if not isinstance(data, list):
            print(f"Error: El contenido del archivo {filename} no es un array. en split")
            return False

        # Realizar la búsqueda recursiva
        result = recursive_binary_search(data, search_data)

        if result:
            print(f"Se encontró el dato '{search_data}' en el archivo {filename}. en split")
        else:
            print(f"No se encontró el dato '{search_data}' en el archivo {filename}. en split")

        return result

    except FileNotFoundError:
        print(f"Error: El archivo {filename} no fue encontrado. en split")
        return False
    except json.JSONDecodeError:
        print(f"Error: No se pudo decodificar el JSON en el archivo {filename}. en split")
        return False

# Ejemplo de uso: buscar el dato "data3" en el archivo "data.json"
 # split_and_search_data_in_json(filename="data.json", search_data="BFVsloJvxcXMIJxQvLccpKPGSMpzFrnhOdlzicuJTMXIDAXNTVHDGjlpJltkXDTXlHwfRBYQbExEUYVYBbpJyQcbGiStnqhKOvdYzXNWhfdlsYGBULPVJyxfEboWPDBCHyxSULJuLWclGGXJSwyxfdTAOxEOfIqcHIXbvaTBItxOjsSnVGersfemQnTxvNbOMyyYmInOoHqyVCcqeXQPFoONOxhisgnWpZfquoxsiAESHKRFwTGBqNYywHwjBkIxsURKXycXWkYeBlSOzIEYVgivlwlrhwlUhWAfRbJZBAbnejsKSSnJbXFbrUMrRLIMitzHFHZKPGzkfAfhvLPztNMFSypetnJZpPoNGhjyMyEMORuSzjbjWUGXyXKrlkJJbIfhKPRnulQGvuhCNJUFWAglZaFvXmYynTexPiYCJmnOsHBfsuKLvMaAOYIxPWHHmkeVmpjFyCXKaDFnnEgoglITpWliCVYlRerFXJsZACJHysoclxkXJqmfjlDnvpmAzYQabLxLeEVRKjRLQpByGxJMNWejhIGahrSnQLurLqFQBjXGfFJKcWiUahHijPNttsNtmxiotUFbzmCylWlbHZDUtdktSksKgnajfbtvYEMnSWVbrCvmtlhTaFcJUHqCwmBXOcYJYHcKcXvkkSUdNKYrKXggCIUzkuLrqMBHxNePDPBwFKorqbgGisfaYmhGcQcLFKDnFulWhJfqkQZWUWKhGzdBtYxmLzQSluUFqxUknlZqrhckJuRDrHGAiTXZOGVcHZIeuLewktRhrFbGHGrqEiSRkuHPBPokHEnKlpjUHmabVpFiWBUkKcCOXEatKWJsepxNGzTVzLwSTuxaoFmvhsmJWTTDMHhebFDNkSrSmtzVozXEvUVYOSKSvPHqIdhIygQuMtsGAESxNaEueWEBTErkyjPGIijZqcZgZxKJzdCYoHzgMSVERgibAQcyLiHEGTQszXftKIGaaoyMnZapHRoSIfqwPFctwLlt")
