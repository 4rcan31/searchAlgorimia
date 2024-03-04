import numpy as np
import string

def generate_and_save_data(num_elements, string_length, filename="data.bin", batch_size=10000):
    with open(filename, "wb") as binary_file:
        for _ in range(num_elements // batch_size):
            batch_data = np.random.choice(list(string.ascii_letters), size=(batch_size, string_length))
            batch_data.tofile(binary_file)

    print(f"Datos generados y guardados en {filename}.")

# Ejemplo de uso: generar 1,000,000 elementos con cadenas de longitud 10,000 en lotes de 10,000
generate_and_save_data(num_elements=1000000, string_length=10000, batch_size=10000)
