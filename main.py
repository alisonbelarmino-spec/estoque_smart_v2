# Estoque Smart - programa principal (rode este arquivo)
from usuarios import login, cadastrar_cliente
from estoque import cadastrar_produto, listar_produtos
from vendas import registrar_venda, mostrar_venda, listar_historico
from relatorios import mostrar_relatorio


def menu_cliente():
    nome = input("Nome: ")
    email = input("E-mail: ")
    doc = input("CPF ou CNPJ: ")
    cadastrar_cliente(nome, email, doc)
    print("Cliente cadastrado!")


def menu_produto():
    codigo = input("Código: ").strip().upper()
    nome = input("Nome: ")
    preco = float(input("Preço: ").replace(",", "."))
    estoque = int(input("Quantidade em estoque: "))
    cadastrar_produto(codigo, nome, preco, estoque)
    print("Produto cadastrado!")


def menu_venda():
    itens = {}
    while True:
        codigo = input("Código do produto (Enter para finalizar): ").strip().upper()
        if codigo == "":
            break
        qtd = int(input("Quantidade: "))
        itens[codigo] = itens.get(codigo, 0) + qtd
    venda = registrar_venda(itens)
    print("Venda realizada!")
    mostrar_venda(venda)


def menu_relatorio():
    periodo = input("Período (diario / semanal / mensal): ").strip().lower()
    mostrar_relatorio(periodo)


def main():
    print("=== ESTOQUE SMART ===")
    if not login(input("Usuário: "), input("Senha: ")):
        print("Usuário ou senha incorretos.")
        return

    while True:
        print("\n1-Cadastrar produto  2-Estoque  3-Vender  4-Histórico")
        print("5-Relatórios  6-Cadastrar cliente  0-Sair")
        opcao = input("Opção: ")
        if opcao == "0":
            break
        try:
            if opcao == "1":
                menu_produto()
            elif opcao == "2":
                listar_produtos()
            elif opcao == "3":
                menu_venda()
            elif opcao == "4":
                listar_historico()
            elif opcao == "5":
                menu_relatorio()
            elif opcao == "6":
                menu_cliente()
            else:
                print("Opção inválida.")
        except ValueError as erro:
            print("Erro:", erro)


if __name__ == "__main__":
    main()
