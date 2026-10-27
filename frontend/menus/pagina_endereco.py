import streamlit as st
from components.base_tela import TelaBase
from connection.base_api import BaseAPI
import pandas as pd

class EnderecoTela(TelaBase):

  def __init__(self):
    self.base = BaseAPI()
    self.titulo = "Tela de Endereço"
    self.descricao = "Essa tela é usada para consultar endereços"

  def consultar(self):
    endpoint = "/enderecos/pegar-dados-endereco"
    dados = self.base.get(endpoint)
    return dados
  
  def consultar_por_id(self, id):
    endpoint = f"/enderecos/pegar-dados-endereco-por-id/{id}"
    dados = self.base.get(endpoint)
    return dados

  def criar(self, params):
    endpoint = f"/enderecos/criar-endereco"
    return self.base.post(endpoint, params)

  def atualizar(self, id, params):
    endpoint = f"/enderecos/atualizar-endereco/{id}"
    return self.base.put(endpoint, params)

  def deletar(self, id):
    endpoint = f"/enderecos/deletar-endereco/{id}"
    return self.base.delete(endpoint)

  def criar_dataframe(self, dados):
    df = pd.DataFrame(dados)
    st.dataframe(df)

  def renderizar(self):
    super().cabecalho(self.titulo, self.descricao)
    abas = st.tabs(["Consultar todos", "Consultar por ID", "Criar Endereço", "Atualizar Endereço", "Deletar Endereço"])
    with abas[0]:
      dados = self.consultar()
      self.criar_dataframe(dados)
    with abas[1]:
      id = st.text_input("Digite o ID do endereço:")
      if id:
        id = int(id)
        dados = self.consultar_por_id(id)
        df = pd.DataFrame([dados])
        st.dataframe(df)
    with abas[2]:
      cep = st.text_input("Digite o CEP do endereço")
      endereco = st.text_input("Digite o endereço")
      bairro = st.text_input("Digite o bairro")
      cidade = st.text_input("Digite a cidade")
      estado = st.text_input("Digite o estado")
      regiao = st.text_input("Digite a região")
      if st.button("Criar endereço"):
        params = {
          "cep": cep,
          "endereco": endereco,
          "bairro": bairro,
          "cidade": cidade,
          "estado": estado,
          "regiao": regiao
        }
        retorno = self.criar(params)
        if retorno.status_code == 200:
          st.success("Endereço criado com sucesso")
        else:
          st.error(retorno.text)

    with abas[3]:
      id = st.text_input("Digite o ID do endereço que deseja atualizar")
      cep = st.text_input("Digite o CEP do endereço que deseja atualizar")
      endereco = st.text_input("Digite o endereço que deseja atualizar")
      bairro = st.text_input("Digite o bairro que deseja atualizar")
      cidade = st.text_input("Digite a cidade que deseja atualizar")
      estado = st.text_input("Digite o estado que deseja atualizar")
      regiao = st.text_input("Digite a região que deseja atualizar")
      if st.button("Atualizar endereço"):
        params = {
          "cep": cep,
          "endereco": endereco,
          "bairro": bairro,
          "cidade": cidade,
          "estado": estado,
          "regiao": regiao
        }
        params = {chave : valor for chave, valor in params.items() if valor not in ("", None)}
        retorno = self.atualizar(int(id), params)
        if retorno.status_code == 200:
          st.success("Endereço atualizado com sucesso")
        else:
          st.error(retorno.text)
    with abas[4]:
      id = st.text_input("Digite o ID do endereço que deseja deletar")
      if st.button("Deletar endereço"):
        retorno = self.deletar(int(id))
        if retorno.status_code == 200:
          st.success("Endereço deletado com sucesso")
        else:
          st.error(retorno.text)
    super().rodape()

EnderecoTela().renderizar()