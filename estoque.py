# Controle de produtos e estoque (RF01 e RF02)
ESTOQUE_BAIXO = 5

produtos = {
    "P001": {"nome": "Hambúrguer artesanal", "preco": 25.0, "estoque": 20},
    "P002": {"nome": "Refrigerante", "preco": 6.0, "estoque": 15},
    "P003": {"nome": "Batata frita", "preco": 12.0, "estoque": 10},
}


def cadastrar_produto(codigo, nome, preco, estoque):
    if codigo in produtos:
        raise ValueError("Código já cadastrado.")
    if not nome.strip():
        raise ValueError("Nome vazio.")
    if preco < 0 or estoque < 0:
        raise ValueError("Preço e quantidade não podem ser negativos.")
    produtos[codigo] = {"nome": nome, "preco": preco, "estoque": estoque}


def listar_produtos():
    for codigo, p in produtos.items():
        aviso = "  <- ESTOQUE BAIXO" if p["estoque"] <= ESTOQUE_BAIXO else ""
        print(f"{codigo} | {p['nome']} | R$ {p['preco']:.2f} | {p['estoque']} un.{aviso}")
