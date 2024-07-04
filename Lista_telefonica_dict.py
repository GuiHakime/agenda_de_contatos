#Função de exibição do menu

def mostrar_menu():
    print("\nMENU:")
    print("1. Adicionar contato")
    print("2. Atualizar contato")
    print("3. Remover contato")
    print("4. Listar contatos")
    print("5. Sair")

#Função para adicionar contatos
def adicionar_contatos(contatos):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone: ")

    contatos[nome] = telefone
    print("\nContato adicionado com sucesso !")

#Função para atualizar contatos
def atualizar_contatos(contatos):
    nome_atual = input("Digite o nome do contato que deseja alterar: ")
    if nome_atual in contatos:
        novo_nome = input("Digite o novo nome para o contato: (Ou deixe em branco p/ manter) ")
        novo_telefone = input("Digite o novo telefone para o contato: (Ou deixe em branco p/ manter)")
        
        if novo_nome:

            if novo_nome in contatos:
                print("\nO nome informado já está em uso. Por favor, tente um nome diferente")

                return

            #Atualiza o contato no dicionário
            contatos[novo_nome] = contatos[nome_atual]

            del contatos[nome_atual]
        else:
        
            novo_nome = nome_atual

        if novo_telefone:

            contatos[novo_nome] = novo_telefone
            print("\nContato atualizado com sucesso")

    else:
        print("\nContrado não encontrado")


#Funçãp para remover_contatos
def remover_contatos(contatos):
    remover_contato = input("Insira o contato à ser removido: ")

    if remover_contato in contatos:
        del contatos[remover_contato]
        print("Contato removido com sucesso")

    else:
        print("Contato não existente: ")

#Função para listar os contatos
def listar_contatos(contatos):
    if not contatos:
        print("\nNenhum contatos registrado!")
        
    for nome, telefone in contatos.items():
        print(f"Nome: {nome.title()}")
        print(f"Telefone: {telefone}")
    

#Função principal à ser chamada com menu de opções integrado
def main():
    contatos = {}

    while True:
        
        mostrar_menu()

        escolha = input("Escolha uma opção: ")

        if escolha == "1":

            adicionar_contatos(contatos)

        if escolha == "2":

            atualizar_contatos(contatos)

        if escolha == "3":

            remover_contatos(contatos)

        if escolha == "4":

            listar_contatos(contatos)

        elif escolha == "5":
            break

        
main()

    