from demographic_data_analyzer import calculate_demographic_data

# Llamar a la función y guardar los resultados
results = calculate_demographic_data()

# Imprimir los resultados
for key, value in results.items():
    print(f"{key}: {value}")
