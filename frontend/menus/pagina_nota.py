import streamlit as st
from components.base_tela import TelaBase
from connection.base_api import BaseAPI
import pandas as pd

class NotaTela(TelaBase):
  def __init__(self):
    self.base = BaseAPI()
    self.titulo = "Tela de Nota"
    self.descricao = "Essa tela é usada para consultar notas"

  def consultar_por_id(self, id):
    endpoint = f"/notas/pegar-dados-notas-por-id/{id}"
    dados = self.base.get(endpoint)
    return dados

  def criar(self, params):
    endpoint = f"/notas/criar-nota"
    return self.base.post(endpoint, params)

  def atualizar(self, id, params):
    endpoint = f"/notas/atualizar-nota/{id}"
    return self.base.put(endpoint, params)

  def deletar(self, id):
    endpoint = f"/notas/deletar-nota/{id}"
    return self.base.delete(endpoint)

  def criar_dataframe(self, dados):
    df = pd.DataFrame([dados])
    st.dataframe(df)

  def renderizar(self):
    super().cabecalho(self.titulo, self.descricao)
    abas = st.tabs(["Consultar por ID", "Criar Nota", "Atualizar Nota", "Deletar Nota"])
    with abas[0]:
      id = st.text_input("Digite o ID da nota:")
      if st.button("Consultar nota por ID"):
        dados = self.consultar_por_id(id)
        self.criar_dataframe(dados)
    with abas[1]:
      aluno_id = st.text_input("Digite o ID do aluno")
      disciplina_id = st.text_input("Digite o ID da disciplina")
      nota = st.text_input("Digite a nota")
      if st.button("Criar nota"):
        params = {
          "nome_id": aluno_id,
          "disciplina_id": disciplina_id,
          "nota": nota
        }
        retorno = self.criar(params)
        if retorno.status_code == 200:
          st.success("Nota criada com sucesso")
        else:
          st.error(retorno.text)
    with abas[2]:
      id = st.text_input("Digite o ID da nota")
      aluno_id = st.text_input("Digite o novo ID do aluno")
      disciplina_id = st.text_input("Digite o novo ID da disciplina")
      nota = st.text_input("Digite a nova nota")
      if st.button("Atualizar nota"):
        params = {
          "aluno_id": aluno_id,
          "disciplina_id": disciplina_id,
          "nota": nota
        }
        params = {chave: valor for chave, valor in params.items() if valor not in ("", None)}
        retorno = self.atualizar(id, params)
        if retorno.status_code == 200:
          st.success("Nota atualizada com sucesso")
        else:
          st.error(retorno.text)
    with abas[3]:
      id = st.text_input("Digite o ID da nota que deseja deletar")
      if st.button("Deletar nota"):
        retorno = self.deletar(id)
        if retorno.status_code == 200:
          st.success("Nota deletada com sucesso")
        else:
          st.error(retorno.text)
    super().rodape()

NotaTela().renderizar()