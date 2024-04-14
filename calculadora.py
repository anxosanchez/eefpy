# Suma

x = 1
y = 2

z = x + y

print(z)

# Bug: concatenación de cadeas sen querer

# Solicitar ao usuario dous números enteiros
x = input("Canto vale x? ")
y = input("Canto vale y? ")

# Imprimir a suma
z = x + y
print(z)

# Formato despois do lugar decimal

x = int(input("Canto vale x? "))
y = int(input("Canto vale y? "))

z = x / y

print(f"{z:.2f}")

# Definición dunha función cun valor de retorno

def main():
    x = int(input("Canto vale x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()

# Conversión de str a int

x = input("Canto vale x? ")
y = input("Canto vale y? ")

z = int(x) + int(y)

print(z)

# Nidificación de chamadas de función

x = int(input("Canto vale x? "))
y = int(input("Canto vale y? "))

z = x + y

print(z)

# Conversión de str a flotar

x = float(input("Canto vale x? "))
y = float(input("Canto vale y? "))

z = x + y

print(z)

# Redondeando ao enteiro máis próximo

x = float(input("Canto vale x? "))
y = float(input("Canto vale y? "))

z = round(x + y)

print(z)

# Menos variables

x = float(input("Canto vale x? "))
y = float(input("Canto vale y? "))

print(round(x + y))

# Formato con comas

x = float(input("Canto vale x? "))
y = float(input("Canto vale y? "))

z = round(x + y)

print(f"{z:,}")

# División

x = float(input("Canto vale x? "))
y = float(input("Canto vale y? "))

z = x / y

print(z)
# Redondeando despois do punto decimal

x = float(input("Canto vale x? "))
y = float(input("Canto vale y? "))

z = round(x / y, 2)

print(z)