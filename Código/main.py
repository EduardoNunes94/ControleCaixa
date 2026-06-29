estoque = []

def linha1():
    print('------SUA LISTA DE PRODUTOS------')


def linha2():
    print('-' * 33)


def linha3():
    print('---------- LISTA MENU ----------\n 1 - Cadastrar Produtos \n 2 - Ver Lista \n 3 - Sair')


while True:
    linha3()
    linha2()
    opmenu = input('Qual das opções deseja? ').strip()
    if opmenu == '1':
         while True:
            nome_prod = input('Digite o produto que deseja cadastrar: ').strip()
            preço_prod = float(input(f'Digite o preço de {nome_prod}: R$ '))
            registro = {'Produto':nome_prod, 'Preço R$':preço_prod}
            estoque.append(registro)
            opcao = input('Deseja cadastrar um novo produto? (S/N): ').strip()
            if opcao == 's':
                continue
            elif opcao == 'n':
                print('PRODUTOS CADASTRADOS')

                break
    elif opmenu == '2':
        linha1()

        for item in estoque:
            print(f'Produto: {item['Produto']} | Preço R$: {item['Preço R$']}')

        linha2()           
    elif opmenu == '3':
        print('Até mais!')
        break
    
    