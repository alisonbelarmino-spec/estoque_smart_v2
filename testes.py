# Testes obrigatórios da apresentação (rode: python testes.py)
from datetime import datetime, timedelta
from estoque import produtos, cadastrar_produto, listar_produtos
from vendas import historico, registrar_venda, listar_historico
from relatorios import mostrar_relatorio
from usuarios import login


def tentar(descricao, itens):
    try:
        registrar_venda(itens)
        print(f"{descricao}: venda aceita")
    except ValueError as erro:
        print(f"{descricao}: recusada -> {erro}")


print("--- 1. Cadastrar produto e consultar quantidade")
cadastrar_produto("P004", "Suco", 8.0, 10)
listar_produtos()

print("\n--- 2. Venda válida (2 hambúrgueres, 2 refrigerantes, 1 batata)")
registrar_venda({"P001": 2, "P002": 2, "P003": 1})
print("Estoque:", {c: p["estoque"] for c, p in produtos.items()})

print("\n--- 3. Quantidade maior que o estoque")
tentar("P003 x 50", {"P003": 50})

print("\n--- 4. Produto inexistente")
tentar("P999 x 1", {"P999": 1})

print("\n--- 5. Dois produtos, só um com estoque")
antes = {c: p["estoque"] for c, p in produtos.items()}
tentar("P001 x 1 + P003 x 50", {"P001": 1, "P003": 50})
depois = {c: p["estoque"] for c, p in produtos.items()}
print("Estoque inalterado?", antes == depois)

print("\n--- 6. Histórico")
listar_historico()

print("\n--- Relatórios (vendas antigas só para testar os períodos)")
registrar_venda({"P001": 3}, data=datetime.now() - timedelta(days=3))
registrar_venda({"P002": 4}, data=datetime.now() - timedelta(days=40))
for periodo in ("diario", "semanal", "mensal"):
    mostrar_relatorio(periodo)

print("\n--- Login")
print("admin/1234:", login("admin", "1234"), "| admin/errada:", login("admin", "errada"))
