# Registro de vendas e histórico (RF03 a RF06)
from datetime import datetime
from estoque import produtos

historico = []


def registrar_venda(itens, data=None):
    """itens: dicionário {codigo: quantidade}"""
    if not itens:
        raise ValueError("A venda precisa ter pelo menos um item.")

    # 1) valida tudo antes de mexer no estoque
    for codigo, qtd in itens.items():
        if codigo not in produtos:
            raise ValueError(f"Produto {codigo} não existe.")
        if qtd <= 0:
            raise ValueError(f"Quantidade inválida para {codigo}.")
        if qtd > produtos[codigo]["estoque"]:
            disp = produtos[codigo]["estoque"]
            raise ValueError(f"Estoque insuficiente para {codigo} (disponível: {disp}).")

    # 2) tudo certo: dá baixa e calcula o total
    total = 0
    lista = []
    for codigo, qtd in itens.items():
        p = produtos[codigo]
        p["estoque"] -= qtd
        subtotal = p["preco"] * qtd
        total += subtotal
        lista.append({"codigo": codigo, "nome": p["nome"], "qtd": qtd, "subtotal": subtotal})

    venda = {
        "id": len(historico) + 1,
        "itens": lista,
        "total": total,
        "data": data or datetime.now(),
    }
    historico.append(venda)
    return venda


def mostrar_venda(venda):
    print(f"\nVenda #{venda['id']} - {venda['data'].strftime('%d/%m/%Y %H:%M')}")
    for i in venda["itens"]:
        print(f"  {i['qtd']} x {i['nome']}: R$ {i['subtotal']:.2f}")
    print(f"  Total: R$ {venda['total']:.2f}")


def listar_historico(lista=None):
    lista = historico if lista is None else lista
    if not lista:
        print("Nenhuma venda registrada.")
    for venda in lista:
        mostrar_venda(venda)
