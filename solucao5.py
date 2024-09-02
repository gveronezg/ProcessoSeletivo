def inverter_string(texto):
    invertida = ""
    for char in texto:
        invertida = char + invertida
    return invertida

# Informe a string desejada
string = input("Informe uma string: ")
print(f"String invertida: {inverter_string(string)}")