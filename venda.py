from cupom import isEmpty

class Venda:
  def __init__(self, loja, datahora, ccf, coo):
    self.loja = loja
    self.datahora = datahora
    self.ccf = ccf
    self.coo = coo
    self.itens = []

  def adicionar_item(self, produto, item, quantidade):
    item_venda = ItemVenda(self, item, produto.codigo, produto.descricao, quantidade, produto.unidade, 
                     produto.valor_unitario, produto.substituicao_tributaria)
    for item in self.itens:
      if(produto.codigo == item.codigo):
        raise Exception("Produto duplicado")
    
    if(quantidade <= 0):
      raise Exception("Item com quantidade zero ou negativa")

    if(produto.valor_unitario <= 0):
      raise Exception("Produto com valor unitário zero ou negativo")
      
    self.itens.append(item_venda)



  def dados_venda(self):
    
    texto_data = self.datahora.strftime("%d/%m/%Y")
    texto_hora = self.datahora.strftime("%H:%M:%S")
    return '''{data} {hora}V CCF:{ccf} COO: {coo}'''.format(data=texto_data,
                                                            hora=texto_hora, 
                                                            ccf=self.ccf, 
                                                            coo=self.coo)

  def dados_itens(self):
    dados = ["ITEM CODIGO DESCRICAO QTD UN VL UNIT(R$) ST VL ITEM(R$)\n"]
    for item_linha in self.itens:
      valor_item = item_linha.quantidade * item_linha.valor_unitario
      linha = '''{item} {codigo} {descricao} {qtd} {un} {vl_unit:.2f} {st} {vl_item:.2f}
          '''.format(item=item_linha.item, codigo=item_linha.codigo, 
           descricao=item_linha.descricao, qtd=item_linha.quantidade, 
           un=item_linha.unidade, vl_unit=item_linha.valor_unitario, 
           st=item_linha.substituicao_tributaria, vl_item=valor_item)
      dados.append(linha)
    return ''.join(dados)

  def calcular_total(self):
    totais = []
    for item_linha in self.itens:
      totais.append(item_linha.quantidade * item_linha.valor_unitario)
    return sum(totais)

  def imprimir_cupom(self):

    if(self.itens == []):
      raise Exception ("O campo item da venda é obrigatório")

    dados_loja = self.loja.dados_loja()
    dados_venda = self.dados_venda()
    dados_itens = self.dados_itens()
    total = self.calcular_total()

    cupons_dados = f"{dados_loja}\n"
    cupons_dados += f"{dados_venda}\n"
    cupons_dados += f"{dados_itens}\n"
    cupons_dados += f"{total}"
    return cupons_dados

  def validacao_venda (self):
    self.loja.validacao_loja()
    if (isEmpty(self.ccf)):
      raise Exception("O campo de ccf é obrigatório")
    if (isEmpty(self.coo)):
      raise Exception("O campo de coo é obrigatório")

#-------------------------

class ItemVenda:

  def __init__(self, venda, item, codigo, descricao, quantidade, unidade, 
               valor_unitario, substituicao_tributaria):
    self.venda = venda
    self.item = item
    self.codigo = codigo
    self.descricao = descricao
    self.quantidade = quantidade
    self.unidade = unidade
    self.valor_unitario = valor_unitario
    self.substituicao_tributaria = substituicao_tributaria

class Produto:

  def __init__(self, codigo, descricao, unidade, valor_unitario, substituicao_tributaria):
    self.codigo = codigo
    self.descricao = descricao
    self.unidade = unidade
    self.valor_unitario = valor_unitario
    self.substituicao_tributaria = substituicao_tributaria
