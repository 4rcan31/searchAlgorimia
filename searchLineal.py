import json

def search_data_in_json(filename, search_data):
    try:
        # Cargar el archivo JSON
        with open(filename, "r") as json_file:
            data = json.load(json_file)

        # Obtener el array de datos
        data_in_array = data.get("dataInArray", [])

        # Buscar el dato específico en el array
        for item in data_in_array:
            if item == search_data:
                print(f"Se encontró el dato '{search_data}' en el archivo {filename}. en lineal")
                return True

        print(f"No se encontró el dato '{search_data}' en el archivo {filename}. en lineal")
        return False

    except FileNotFoundError:
        print(f"Error: El archivo {filename} no fue encontrado. en lineal")
        return False
    except json.JSONDecodeError:
        print(f"Error: No se pudo decodificar el JSON en el archivo {filename}. en lineal")
        return False

# Ejemplo de uso: buscar el dato "data3" en el archivo "data.json"

