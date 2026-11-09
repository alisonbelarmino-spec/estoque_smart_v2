# Clientes e login (Bloco 2)
# Instalar antes: pip install bcrypt validate-docbr
import re
import bcrypt
from validate_docbr import CPF, CNPJ

clientes = [{"nome": "Maria", "email": "maria@gmail.com", "doc": "12345678909"}]
usuarios = {"admin": {"senha": bcrypt.hashpw(b"1234", bcrypt.gensalt()), "ativo": True}}


def validar_cliente(nome, email, doc):
    erros = []
    if not nome.strip():
        erros.append("Nome vazio.")
    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
        erros.append("E-mail inválido.")
    if not (CPF().validate(doc) or CNPJ().validate(doc)):
        erros.append("CPF/CNPJ inválido.")
    elif any(c["doc"] == doc for c in clientes):
        erros.append("CPF/CNPJ já cadastrado.")
    return erros


def cadastrar_cliente(nome, email, doc):
    doc = re.sub(r"\D", "", doc)
    erros = validar_cliente(nome, email, doc)
    if erros:
        raise ValueError("\n- ".join(erros))
    clientes.append({"nome": nome, "email": email, "doc": doc})


def login(usuario, senha):
    u = usuarios.get(usuario)
    if not u:
        return False
    if not u["ativo"]:
        return False
    return bcrypt.checkpw(senha.encode(), u["senha"])
