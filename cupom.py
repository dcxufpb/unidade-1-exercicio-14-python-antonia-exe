# coding: utf-8

def isEmpty(value: str) -> bool:
    return (value == None) or (len(value) == value.count(" "))

class Endereco:
  
  def __init__(self, logradouro, numero, complemento, bairro, municipio, 
      estado, cep):
    self.logradouro = logradouro
    self.numero = numero
    self.complemento = complemento
    self.bairro = bairro
    self.municipio = municipio
    self.estado = estado
    self.cep = cep

#-------------------------

class Loja:
  
  def __init__(self, nome_loja, endereco, telefone, observacao, cnpj, 
      inscricao_estadual):
    self.nome_loja = nome_loja
    self.endereco = endereco
    self.telefone = telefone
    self.observacao = observacao
    self.cnpj = cnpj
    self.inscricao_estadual = inscricao_estadual

  def dados_loja(self):
    if (isEmpty(self.nome_loja)):
      raise Exception("O campo nome da loja é obrigatório")

    if (isEmpty(self.endereco.logradouro)):
      raise Exception("O campo logradouro do endereço é obrigatório")

    numero = int ()
    try:
      numero = int(self.endereco.numero)
    except Exception:
      numero = 0

    if numero <= 0:
      numero = "s/n"

    if (isEmpty(self.endereco.municipio)):
      raise Exception("O campo município do endereço é obrigatório")

    if (isEmpty(self.endereco.estado)):
      raise Exception("O campo estado do endereço é obrigatório")

    if (isEmpty(self.cnpj)):
      raise Exception("O campo CNPJ da loja é obrigatório")
  
    if (isEmpty(self.inscricao_estadual)):
      raise Exception("O campo inscrição estadual da loja é obrigatório")

    linha2 = f"{self.endereco.logradouro}, {numero}"
    if not isEmpty(self.endereco.complemento):
      linha2 += f" {self.endereco.complemento}"

    linha3 = str()
    if not isEmpty(self.endereco.bairro):
      linha3 += f"{self.endereco.bairro} - "
    linha3 += f"{self.endereco.municipio} - {self.endereco.estado}"

    linha4 = str()
    if not isEmpty(self.endereco.cep):
      linha4 = f"CEP:{self.endereco.cep}"
    if not isEmpty(self.telefone):
      if not isEmpty(linha4):
        linha4 += " "
      linha4 += f"Tel {self.telefone}"
    if not isEmpty(linha4):
      linha4 += "\n"

    linha5 = str()
    if not isEmpty(self.observacao):
      linha5 += f"{self.observacao}"

    output = f"{self.nome_loja}\n"
    output += f"{linha2}\n"
    output += f"{linha3}\n"
    output += f"{linha4}"
    output += f"{linha5}\n"
    output += f"CNPJ: {self.cnpj}\n"
    output += f"IE: {self.inscricao_estadual}"

    return output

#-------------------------