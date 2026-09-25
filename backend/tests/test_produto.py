from backend.entity.produto import Produto
import pytest
from backend.exceptions.excecoes import NomeInvalidoError

def test_criar_produto_com_sucesso():
    """Garante que o Produto seja criado com dados válidos."""
    cafe = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert cafe._nome == "cafe"
    assert cafe._preco == 18 and cafe._quant_estoque == 50 and \
        cafe._validade == 3 and cafe._codigo_barras == 1234567890 and \
        cafe._categoria == "alimenticio" and cafe._peso == 250

def test_criar_produto_sem_nome():
    """Garante que o Produto rejeite um nome vazio."""
    with pytest.raises(NomeInvalidoError, match='Nome não pode ser vazio'):
        Produto("", 18, 50, 3, 1234567890, "alimenticio", 250)

def test_preco_vazio():
    with pytest.raises(ValueError):
        Produto("Banana", None, 50, 3, 1234567890, "alimenticio", 250)

def test_estoque_vazio():
    with pytest.raises(ValueError):
        Produto("Maça", 18, None, 3, 1234567890, "alimenticio", 250)

def test_validade_vazio():
    with pytest.raises(ValueError):
        Produto("Uva", 18, 50, None, 1234567890, "alimenticio", 250)

def test_codigo_barras_vazio():
    with pytest.raises(ValueError):
        Produto("Jabuticaba", 18, 50, 3, None, "alimenticio", 250)

def test_categoria_vazio():
    with pytest.raises(ValueError):
        Produto("Melancia", 18, 50, 3, 1234567890, None, 250)

def test_peso_vazio():
    with pytest.raises(ValueError):
        Produto("Jaca", 18, 50, 3, 1234567890, "alimenticio", None)

def test_getter_nome():
    bebida = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert bebida.nome == "cafe"
    bebida.valida_nome("cafe")

def test_getter_preco():
    fruta = Produto("Maça", 10, 30, 5, 987654321, 'alimenticio', 20)
    assert fruta.preco == 10
    fruta.valida_preco(10)

def test_getter_estoque():
    fruta = Produto("Maça", 10, 30, 5, 987654321, 'alimenticio', 20)
    assert fruta.quant_estoque == 30
    fruta.valida_quant_estoque(30)

def test_getter_validade():
    fruta = Produto("Maça", 10, 30, 5, 987654321, 'alimenticio', 20)
    assert fruta.validade == 5
    fruta.valida_validade(5)

def test_getter_codigo_barras():
    fruta = Produto("Maça", 10, 30, 5, 987654321, 'alimenticio', 20)
    assert fruta.codigo_barras == 987654321
    fruta.valida_codigo_barras(987654321)

def test_getter_categoria():
    fruta = Produto("Maça", 10, 30, 5, 987654321, 'alimenticio', 20)
    assert fruta.categoria == 'alimenticio'
    fruta.valida_categoria('alimenticio')

def test_getter_peso():
    fruta = Produto("Maça", 10, 30, 5, 987654321, 'alimenticio', 20)
    assert fruta.peso == 20
    fruta.valida_peso(20)

def test_atualizar_nome():
    produto = Produto("Maça", 10, 30, 5, 987654321, 'alimenticio', 20)
    produto.nome = "banana"
    assert produto.nome == "banana"

def test_atualizar_preco():
    produto = Produto("Maça", 10, 30, 5, 987654321, 'alimenticio', 20)
    produto.preco = 15
    assert produto.preco == 15

def test_atualizar_estoque():
    produto = Produto("Maça", 10, 30, 5, 987654321, 'alimenticio', 20)
    produto.quant_estoque = 40
    assert produto.quant_estoque == 40

def test_atualizar_validade():
    produto = Produto("Maça", 10, 30, 5, 987654321, 'alimenticio', 20)
    produto.validade = 4
    assert produto.validade == 4

def test_atualizar_codigo_barras():
    produto = Produto("Maça", 10, 30, 5, 987654321, 'alimenticio', 20)
    produto.codigo_barras = 34567890
    assert produto.codigo_barras == 34567890

def test_atualizar_categoria():
    produto = Produto("Maça", 10, 30, 5, 987654321, 'alimenticio', 20)
    produto.categoria = 'hortifruti'
    assert produto.categoria == 'hortifruti'

def test_atualizar_peso():
    produto = Produto("Maça", 10, 30, 5, 987654321, 'alimenticio', 20)
    produto.peso = 15
    assert produto.peso == 15
