class Supermercado: #Definir a classe do supermercado

    def __init__(self):
        self.catalogo = {'Arroz': 15.0, 'Feijão': 12.8, 'Torneira': 27.0, 'Carne': 53.3} #Catálogo de produtos
        self.carrinho = {} #Lista vazia
        self.total = 0.0 #Total de compra

    def comprar(self): #Definir (comprar)
        while True: #Enquanto for verdade...
            print("\nBem-vindo ao meu Supermercado!")
            print("-" * 30)
            print("CATÁLOGO DE PRODUTOS:") #Exibe o catálogo de produtos
            for produto, preco in self.catalogo.items(): #Para cada produto e preço dentro do catálogo
                print(f"{produto.capitalize()} - R${preco:.2f}") #Exibe o produto e o preço formatado em duas casas decimais. Captalize() Para a letra inicial maiúscula

            escolher = input("\nDiga o nome do produto que deseja comprar, ou (SAIR) para sair: ").strip().capitalize() #Escolha do produto

            if escolher.lower() == "sair": #Caso o cliente queira sair da compra sem nenhuma compra, exibe a mensagem e o código quebra
                if not self.carrinho:
                    print("\nNenhuma compra foi efetuada. Obrigado pela sua visita!")
                    return
                break

            if escolher in self.catalogo: #Se escolher um produto dentro do catálogo, exibe a mensagem
                quantidade_str = input("\nQual é a quantidade de produtos que deseja comprar? ") #Solicita a quantidade do produto desejado
                if quantidade_str.isdigit(): #Se a quantidade for uma string, o código não vai quebrar
                    quantidade = int(quantidade_str)
                    if escolher in self.carrinho:
                        self.carrinho[escolher] += quantidade

                    else:
                        self.carrinho[escolher] = quantidade
                    print(f"\n{quantidade} unidades de {escolher.capitalize()} adicionadas ao carrinho.") #A quantidade do produto selecionado, será adicionado ao carrinho
                else:
                    print("Quantidade inválida. Digite apenas números.")
            else:
                print("\nProduto não foi encontrado em nosso catálogo. Por favor, tente novamente.") #Se o produto não se encontrar dentro do catálogo, ele quebra novamente

        print("\nCOMPRA RESUMIDA:") #Resumo da sua compra ao sair
        print("-" * 30)
        for produto, quantidade in self.carrinho.items():
            preco_unitario = self.catalogo[produto]
            preco_total = preco_unitario * quantidade
            print(f"{quantidade} unidades de {produto.capitalize()} - R${preco_total:.2f}") #Preço total a se pagar
            self.total += preco_total

        print(f"Total da compra: R${self.total:.2f}") #Preço total a se pagar
        self.pagar() #Chama a classe (pagar)

    def pagar(self): #Definir a classe de pagamento
        while True:
            print("\nFormas de pagamento: dinheiro, crédito, débito ou pix.") #Formas de pagamento disponíveis
            pagamento = input("\nQual a forma de pagamento?  Caso deseje, digite 'CANCELAR' para cancelar sua compra: ").strip().lower() #Solicita a forma de pagamento, e pode cancelar a compra

            if pagamento == "cancelar":
                print("\nCompra cancelada com sucesso.")
                print("\nAgradecemos pela sua visita em nosso mercado. Volte sempre!") #Caso seja cancelada, essas duas mensagens serão exibidas no final
                print("-" * 30)
                return

            elif pagamento in ["crédito", "débito", "cartão de débito", "cartão de crédito", "pix"]: #Se a forma de pagamento estiver dentro da lista
                print(f"\nSua compra foi paga no {pagamento.capitalize()}. Obrigado pela sua preferência.") #Exibe a sua compra efetuada na forma que o cliente pagou
                break

            elif pagamento == "dinheiro": #Se o pagamento for em dinheiro
                while True:
                    valor_recebido = input(f"\nTotal: R${self.total:.2f} - Escreva o valor recebido: R$ ") #Exibe o valor total da compra, e solicita o valor que o cliente irá pagar
                    try:
                        valor_recebido = float(valor_recebido) #Converte o valor recebido para float
                        if valor_recebido < self.total: #Se o valor recebido for menor que o valor da compra, exibe a mensagem abaixo
                            print(f"\nValor insuficiente. Faltam R${self.total - valor_recebido:.2f}.")

                        else:
                            troco = valor_recebido - self.total
                            print(f"\nObrigado! Compra paga em dinheiro. Troco: R${troco:.2f}") #Compra efetuada em dinheiro, o troco será exibido
                            print("-" * 30)
                            break
                    except ValueError:
                        print("\nValor inválido. Por favor, digite apenas números.") #Valor inválido, caso o cliente digite uma str
                break

            else:
                print("\nForma de pagamento não reconhecida. Tente novamente.") #Forma de pagamento não reconhecida caso ela não esteja dentro da lista
                print("-" * 30)

        cpf_na_nota = input("\nCPF na nota? ").strip().lower() #Solicita o CPF
        if cpf_na_nota == "sim":
            cpf = input("\nDigite seu CPF: ") #Digite o CPF caso o cliente queira
            print(f"\nNota fiscal: Total de compra - R${self.total:.2f} | CPF - {cpf}") #Nota fiscal impressa (com) CPF
        else:
            print(f"\nNota fiscal: Total de compra - R${self.total:.2f}") #Nota fiscal impressa (sem) CPF

        print("-" * 30)
        print("\nObrigado por comprar em nosso supermercado! Volte sempre!")
        print("-" * 30)


        self.catalogo = {'Arroz': 12.0, 'Feijão': 10.5, 'Torneira': 20.7, 'Carne': 45.9}   #Atualização de catálogo (opcional)
        self.carrinho = {}
        self.total = 0.0

mercado = Supermercado() #Execução do sistema
mercado.comprar() #Execução do sistema