# Relatórios e consultas gerenciais (Bloco 29/10)
from datetime import datetime, timedelta
from estoque import produtos
from vendas import historico


def filtrar_por_periodo(periodo):
    """periodo: 'diario', 'semanal' ou 'mensal'"""
    agora = datetime.now()
    if periodo == "diario":
        return [v for v in historico if v["data"].date() == agora.date()]
    if periodo == "semanal":
        inicio = agora - timedelta(days=7)
        return [v for v in historico if v["data"] >= inicio]
    if periodo == "mensal":
        return [v for v in historico
                if (v["data"].month, v["data"].year) == (agora.month, agora.year)]
    raise ValueError("Período inválido. Use diario, semanal ou mensal.")


def resumo(vendas):
    """Retorna (quantidade de vendas, faturamento total)."""
    return len(vendas), sum(v["total"] for v in vendas)


def quantidade_por_produto(vendas):
    """Soma as unidades vendidas de cada produto (inclui os que não venderam = 0)."""
    qtds = {codigo: 0 for codigo in produtos}
    for v in vendas:
        for i in v["itens"]:
            qtds[i["codigo"]] += i["qtd"]
    return qtds


def ranking(vendas):
    """Lista [(codigo, qtd)] do mais vendido para o menos vendido."""
    qtds = quantidade_por_produto(vendas)
    return sorted(qtds.items(), key=lambda par: par[1], reverse=True)


def mostrar_relatorio(periodo):
    vendas = filtrar_por_periodo(periodo)
    n, faturamento = resumo(vendas)
    print(f"\n=== RELATÓRIO {periodo.upper()} ===")
    print(f"Vendas realizadas: {n}")
    print(f"Faturamento total: R$ {faturamento:.2f}")
    if n == 0:
        return

    rank = ranking(vendas)
    print("\nProdutos mais vendidos")
    print(f"{'Produto':<22}{'Qtd':>5}  Gráfico")
    for codigo, qtd in rank:
        print(f"{produtos[codigo]['nome']:<22}{qtd:>5}  {'█' * qtd}")

    mais, menos = rank[0], rank[-1]
    print(f"\nMaior saída: {produtos[mais[0]]['nome']} ({mais[1]} un.)")
    print(f"Menor saída: {produtos[menos[0]]['nome']} ({menos[1]} un.)")
