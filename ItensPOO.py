class Item:

    def __init__(self,nome,id,quantidade,preco):
        self.nome = nome
        self.id = id
        self.quantidade = quantidade
        self.preco = preco

    def rename(self,nome):
        self.nome = nome

    def mudarId(self,id):
        self.id = id

    def alterarQuantidade(self,quantidade):
        self.quantidade +=quantidade

    def alterarPreco(self,preco):
        self.preco = preco

itens=[]

while(1):
    opc=int(input("\n\n1-Adicionar Item\n2-Visualizar Itens\n3-Alterar Item\nDigite o numero da operação: "))

    if opc==1:
        cont =""
        while(cont==""):

            nome=input("\nDigite o nome do item: ").upper()
            id=input("Digite o ID do item: ")
            quantidade=int(input("Quantidade de itens: "))
            preco = float(input("Digite o preço do item: "))

            item = Item(nome,id,quantidade,preco)
            itens.append(item)
            print(f"\n**NOVO** NOME:{itens[-1].nome} ID:{itens[-1].id} QNTD:{itens[-1].quantidade} PREÇO:{itens[-1].preco}\n")
            cont=input("Aperte ENTER para continuar adicionando ou outra tecla para sair")

    if opc==2:
        print("\n")
        for i in itens:
            print(f"{itens.index(i)+1}- NOME:{i.nome} ID:{i.id} QNTD:{i.quantidade} PREÇO:{i.preco}")
        p=input("Pressione ENTER para continuar")

    if opc==3:
        print("\n")
        for i in itens:
            print(f"{itens.index(i)+1}- NOME:{i.nome} ID:{i.id} QNTD:{i.quantidade} PREÇO:{i.preco}")
        alt=int(input("Numero do item a ser alterado:"))

        print(f"{itens.index(itens[alt-1]) + 1}- NOME:{itens[alt-1].nome} ID:{itens[alt-1].id} QNTD:{itens[alt-1].quantidade} PREÇO:{itens[alt-1].preco}")
        opc2=int(input("\n1-Renomear\n2-Alterar ID\n3-Alterar Quantidade\n4-Alterar Preco\nDigite o numero da operação:"))

        if opc2==1:
            nomeNovo=input("Digite o nome para ser alterado: ").upper()
            itens[alt-1].rename(nomeNovo)
        if opc2==2:
            idNovo=input("Digite o novo ID para ser alterado: ")
            itens[alt-1].mudarId(idNovo)
        if opc2==3:
            quantidadeNova=int(input("Digite uma valor para ser adicionado ao atual: "))
            itens[alt-1].alterarQuantidade(quantidadeNova)
        if opc2==4:
            precoNovo=float(input("Digite um novo preço para ser alterado: "))
            itens[alt - 1].alterarPreco(precoNovo)

        print(f"\nALTERACÃO CONCLUIDA\n{itens.index(itens[alt-1]) + 1}- NOME:{itens[alt-1].nome} ID:{itens[alt-1].id} QNTD:{itens[alt-1].quantidade} PREÇO:{itens[alt-1].preco}")