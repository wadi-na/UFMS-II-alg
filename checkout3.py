

class Fila:
    def __init__(self, tamanho):
        self.tamanho = tamanho 
        self.dados = [None] * tamanho 
        self.inicio = 0 
        self.fim = 0 
        self.quantidade = 0
    
    def enfileirar(self, elemento):
        if self.quantidade < self.tamanho: 
            self.dados[self.fim] = elemento
            self.fim += 1 
            self.quantidade += 1
            print(f"valor inserido:  {elemento}")
        else: 
            print("a fila está cheia")
        
    def desenfileirar(self):
        if self.quantidade > 0:
            elemento = self.dados[self.inicio]
            self.dados[self.inicio] = None
            self.inicio += 1
            self.quantidade -= 1 
            print(f'valor excluido: {elemento}')
        else: 
            print("erro")

    def consultar(self):
        if self.quantidade > 0: 
            print(self.dados[self.inicio])
        else: 
            print("nada a exibir")
    
    def contar(self):
        if self.quantidade > 0: 
            print(self.quantidade)
        else: 
            print("nada a exibir")



print("insira o tamanho máximo da fila: ")
tamanho = int(input())
fila = Fila(tamanho)
print(f"voce fará uma lista com {tamanho} itens")


def menu():

    while True:
    
        print ("digite o numero da ação desejada: \n ")
        print("\n 1 - enfileirar() para inserir elementos no final da fila.")
        print("\n 2 - desenfileirar() para remover elementos no início da fila.")
        print("\n 3 - consultar() para exibir o elemento do início da fila, sem removê-lo.")
        print("\n 4 - contar() para exibir a quantidade de elementos na fila.")
        print("\n 5 - sair")

        opcao = int(input())

        match(opcao):
            case 1:
                cont = 0

                if cont == 0:
                    while cont != tamanho:
                        print(f"insira {tamanho} itens para preencher a fila")
                        itens = input()
                        fila.enfileirar(itens)
                        cont += 1
            case 2: 
                fila.desenfileirar()
            case 3: 
                fila.consultar()
            case 4: 
                fila.contar()
            case 5:
                if opcao == 5:
                    print("saindo do programa...")
                    break
            case _: 
                print("inválido")

def main():
        menu()    

if __name__ == "__main__":
    main() 