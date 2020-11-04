from cupom import isEmpty
from venda import ItemVenda, Produto, Venda
import cupom
import datetime
import pytest
import venda

NOME_LOJA = "Loja 1"
LOGRADOURO = "Log 1"
NUMERO = 10
COMPLEMENTO = "C1"
BAIRRO = "Bai 1"
MUNICIPIO = "Mun 1"
ESTADO = "E1"
CEP = "11111-111"
TELEFONE = "(11) 1111-1111"
OBSERVACAO = "Obs 1"
CNPJ = "11.111.111/1111-11"
INSCRICAO_ESTADUAL = "123456789"
ccf = "1234"
coo = "123456"

datahora = datetime.datetime(2020, 10, 27, 9, 20, 15)

# Venda sem itens -------------------------
endereco_completo = cupom.Endereco(LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO, MUNICIPIO, ESTADO, CEP)
loja_completa = cupom.Loja(NOME_LOJA, endereco_completo, TELEFONE, OBSERVACAO, CNPJ, INSCRICAO_ESTADUAL)

TEXTO_ESPERADO_VENDA_SEM_ITENS = "O campo item da venda é obrigatório"
v_sem_itens = Venda(loja_completa, datahora, ccf, coo)

def valida_impressao(mensagem_esperada, venda):
    with pytest.raises(Exception) as excinfo:
        venda.imprimir_cupom()
    the_exception = excinfo.value
    assert mensagem_esperada == str(the_exception)

def test_venda_sem_itens():
    valida_impressao(
        TEXTO_ESPERADO_VENDA_SEM_ITENS, 
        v_sem_itens
        )

# Venda com dois itens (mesmo produto) -------------------------

TEXTO_ESPERADO_VENDA_DUPLICADA = "Produto duplicado"

#Produto (1)
codigo1 = 666
descricao1 = "maracujá"
quantidade1 = 2
unidade1 = "uni"
valorUnitario1 = 2.50
substituicaoTributaria1 = ""

def validacao_item(mensagem_esperada, item, produto, quantidade, venda):
    with pytest.raises(Exception) as excinfo:
        venda.adicionar_item(produto, item, quantidade)
    the_exception = excinfo.value
    assert mensagem_esperada == str(the_exception)

def test_venda_duplicacao_item():
    itemUm = Produto(codigo1, descricao1, unidade1, valorUnitario1, substituicaoTributaria1)
    vendaCom2Itens = Venda(loja_completa, ccf, coo, datahora)
    vendaCom2Itens.adicionar_item(itemUm, 1, quantidade1)
    validacao_item(
        TEXTO_ESPERADO_VENDA_DUPLICADA,
        1, 
        itemUm,
        quantidade1,
        vendaCom2Itens
        )

# Produto com valor unitário zero ou negativo -------------------------

TEXTO_ESPERADO_VALOR_ZERO_OU_NEGATIVO = "Produto com valor unitário zero ou negativo"

#Produto (2)
codigo2 = 333
descricao2 = "melancia"
quantidade2 = 1
unidade2 = "uni"
valorUnitario2 = 0
substituicaoTributaria2 = ""



def test_valor_produto():
    itemDois = Produto(codigo2, descricao2, unidade2, valorUnitario2, substituicaoTributaria2)
    vendaCom2ItensNegativos = Venda(loja_completa, ccf, coo, datahora)

    validacao_item(
        TEXTO_ESPERADO_VALOR_ZERO_OU_NEGATIVO,
        1,
        itemDois,
        quantidade2,
        vendaCom2ItensNegativos
    )

# Venda com quantidade zero ou negativa 

#Produto (3)
codigo3 = 222
descricao3 = "laranja"
quantidade3 = 0
unidade3 = "uni"
valorUnitario3 = 1.50
substituicaoTributaria3 = ""

TEXTO_ESPERADO_VALORUNI_ZERO = "Item com quantidade zero ou negativa"

def test_quant_item():
    itemTres = Produto(codigo3, descricao3, unidade3, valorUnitario3, substituicaoTributaria3)
    vendaComQuantNegativa = Venda(loja_completa, ccf, coo, datahora)
    validacao_item(
        TEXTO_ESPERADO_VALORUNI_ZERO, 
        1,
        itemTres,
        quantidade3,
        vendaComQuantNegativa
    )