import random

def generate_random_number(start, end):
    return random.randint(start, end)

if __name__ == "__main__":
    print("Bem-vindo ao Gerador de Números Aleatórios!")
    start = int(input("Digite o número inicial do intervalo: "))
    end = int(input("Digite o número final do intervalo: "))
    while True:
        number = generate_random_number(start, end)
        print(f"Número gerado: {number}")
        again = input("Gerar outro número? (s/n): ").lower()
        if again != 's':
            print("Encerrando o programa. Até logo!")
            break
