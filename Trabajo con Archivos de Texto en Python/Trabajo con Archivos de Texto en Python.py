# Escritura de Archivo de Texto

# Creamos un nuevo archivo llamado "my_notes.txt" y abrimos el archivo en modo de escritura ("w")
with open("my_notes.txt", "w") as file:
    # Escribimos tres líneas de notas personales en el archivo
    file.write("Primera nota: Recordar practicar Python todos los días.\n")
    file.write("Segunda nota: Leer un capítulo del libro de algoritmos.\n")
    file.write("Tercera nota: Hacer una pausa para tomar café.\n")

# Lectura de Archivo de Texto

# Abrimos el archivo "my_notes.txt" en modo de lectura ("r")
with open("my_notes.txt", "r") as file:
    # Leemos el contenido del archivo línea por línea usando un bucle
    for line in file:
        # Mostramos en la consola cada línea leída
        print(line.strip())  # strip() elimina los saltos de línea adicionales al final de cada línea

# No es necesario cerrar el archivo manualmente cuando usamos 'with',
# ya que el archivo se cierra automáticamente después de salir del bloque 'with'.
