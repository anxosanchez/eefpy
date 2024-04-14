# Demostración dunha función cun argumento posicional

print("Ola, mundo")
# Demostración dunha función cun argumento posicional e un valor de retorno

nome = input("Como te chamas? ")
print("Ola,")
print(nome)

# Demostración da definición dunha función cun parámetro de valor predeterminado


def ola(to="mundo"):
    print("Ola,", to)


ola()
nome = input("Como te chamas? ")
ola(nome)

# Demostración da efinición dunha función principal

def main():
    nome = input("Como te chamas? ")
    ola(nome)


def ola(to="mundo"):
    print("Ola,", to)


main()

# Demostración da concatenación de cadeas de caracteres

nome = input("Como te chamas? ")
print("Ola, " + nome)

# Demostración dunha función con dous argumentos posicionais 

nome = input("Como te chamas? ")
print("Ola,", nome)

# Demostración dunha función cun argumento posicional e un argumento nomeado

nome = input("Como te chamas? ")
print("Ola, ", end="")
print(nome)

# Demostración do formateo dunha cadea de caracteresa 

nome = input("Como te chamas? ")
print(f"Ola, {nome}")

# Demostración das funcións str

nome = input("Como te chamas? ").strip().title()
print(f"Ola, {nome}")

# Demostración das funcións str

nome = input("Como te chamas? ").strip().title()
first, last = nome.split(" ")
print(f"Ola, {first}")

# Demostración dad definición dunha a función sen parámetros

def ola():
    print("ola")

nome = input("Como te chamas? ")
ola()
print(nome)

# Demostración da definición dunhaa function con un parámetro

def ola(to):
    print("Ola,", to)


nome = input("Como te chamas? ")
ola(nome)