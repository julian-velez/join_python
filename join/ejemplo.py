carros = "ferrari, porsche, bugatti, tesla"
marcas = "___"  # ahora sí, el separador deseado

# Convertimos la cadena en una lista usando el separador actual ", "
lista_carros = carros.split(", ")

# Unimos las marcas con 3 guiones bajos
marcas_autos = marcas.join(lista_carros)

print(marcas_autos)
