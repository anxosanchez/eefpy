# Función cun argumento posicional

print("Ola, mundo")
# Función cun argumento posicional e un valor de retorno

nome = input("Como te chamas? ")
print("Ola,")
print(nome)

# Definición dunha función cun parámetro de valor predeterminado

def ola(to="mundo"):
    print("Ola,", to)


ola()
nome = input("Como te chamas? ")
ola(nome)

# Definición dunha función principal

def main():
    nome = input("Como te chamas? ")
    ola(nome)


def ola(to="mundo"):
    print("Ola,", to)


main()

# Concatenación de cadeas de caracteres

nome = input("Como te chamas? ")
print("Ola, " + nome)

# Función con dous argumentos posicionais 

nome = input("Como te chamas? ")
print("Ola,", nome)

# Función con un argumento posicional e un carácter final tuneado

nome = input("Como te chamas? ")
print("Ola, ", end="")
print(nome)

# Formateo dunha cadea de caracteresa 

nome = input("Como te chamas? ")
print(f"Ola, {nome}")

# Métodos da funcións str

nome = input("Como te chamas? ").strip().title()
print(f"Ola, {nome}")

# Métodos da funcións str

nome = input("Como te chamas? ").strip().title()
first, last = nome.split(" ")
print(f"Ola, {first}")

# Definición dunha a función sen parámetros

def ola():
    print("ola")

nome = input("Como te chamas? ")
ola()
print(nome)

# Definición dunhaa function con un parámetro

def ola(to):
    print("Ola,", to)


nome = input("Como te chamas? ")
ola(nome)