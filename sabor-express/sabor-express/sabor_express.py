import os

restaurantes = [
                {'Nome': 'Praca', 'Categoria': 'Japonesa', 'Ativo': False}, 
                {'Nome': 'Do beco', 'Categoria': 'Pizzaria', 'Ativo': True},
                {'Nome': 'Los hermanos', 'Categoria': 'Hamburgueria', 'Ativo': True}
               ]
#FUNÇÕES

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(f'{texto}\n')
    print(linha)
def voltar_menu():
    input("\nDigite uma tecla para voltar ao menu principal ")
    main()
def exibir_nome_do_programa():   
    print('\n')   
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')
def finalizar_app():
    exibir_subtitulo('Programa Finalizado')
def opcao_invalida():
    print('Opcao invalida!\n')
    voltar_menu()
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar Restaurantes')
    nome_do_restaurante = input('Nome do restaurante: ')
    categoria = input('Digite o nome da Categoria: ')
    dados_do_restaurante = {'Nome': nome_do_restaurante, 'Categoria': categoria, 'Ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_menu()

    
def listar_restaurantes():
    exibir_subtitulo('Lista de Restaurantes')
    for rest in restaurantes:
        nome_rest = rest['Nome']
        categoria_rest = rest['Categoria']
        ativo_rest = 'Ativado' if rest['Ativo'] else 'Desativado'
        print(f'Nome: {nome_rest.ljust(15)}\nCategoria: {categoria_rest.ljust(15)}\nEstado Atual: {ativo_rest.ljust(15)}\n')
    voltar_menu()

def alternar_estado_rest():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o estado: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['Nome']:
            restaurante_encontrado = True
            restaurante['Ativo'] = not restaurante['Ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['Ativo'] else f'O Restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_menu()

#Menu
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolhe uma opcao: '))


        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_rest()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()



def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
if __name__ == '__main__':
    main()

