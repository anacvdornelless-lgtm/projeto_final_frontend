import streamlit as st
from components.base_tela import TelaBase
from connection.base_api import BaseAPI
import pandas as pd

class DisciplinaTela(TelaBase):

  def __init__(self):
    self.base = BaseAPI()
    self.titulo = "Tela de Disciplina"
    self.descricao = "Essa tela é usada para consultar disciplinas"

  def consultar(self):
    endpoint = "/disciplinas/pegar-dados-disciplina"
    dados = self.base.get(endpoint)
    return dados

  def criar(self, params):
    endpoint = "/disciplinas/criar-disciplina"
    return self.base.post(endpoint, params)

  def atualizar(self, id, params):
    endpoint = f"/disciplinas/atualizar-disciplina/{id}"
    return self.base.put(endpoint, params)

  def excluir(self, id):
    endpoint = f"/disciplinas/deletar-disciplina/{id}"
    return self.base.delete(endpoint)

  def criar_dataframe(self, dados):
    df = pd.DataFrame(dados)
    st.dataframe(df)

  def renderizar(self):
    super().cabecalho(self.titulo, self.descricao)
    abas = st.tabs(["Consultar todos", "Criar Disciplina", "Atualizar Disciplina", "Excluir Disciplina"])
    with abas[0]:
      dados = self.consultar()
      self.criar_dataframe(dados)
    with abas[1]:
      nome = st.text_input("Digite o nome da nova disciplina")
      carga_horaria = st.text_input("Digite a carga horária da nova disciplina")
      semestre = st.text_input("Digite o semestre da nova disciplina")
      if st.button("Criar disciplina"):
        params = {
          "nome_disciplina": nome,
          "carga": carga_horaria,
          "semestre": semestre
        }
        retorno = self.criar(params)
        if retorno.status_code == 200:
          st.success("Disciplina criada com sucesso")
        else:
          st.error(retorno.text)
    with abas[2]:
      id = st.text_input("Digite o ID da disciplina")
      nome = st.text_input("Digite o novo nome da disciplina")
      carga_horaria = st.text_input("Digite a nova carga horária da disciplina")
      semestre = st.text_input("Digite o novo semestre da disciplina")
      if st.button("Atualizar disciplina"):
        params = {
          "nome_disciplina": nome,
          "carga": carga_horaria,
          "semestre": semestre
        }
        params = {chave : valor for chave, valor in params.items() if valor not in ("", None)}
        retorno = self.atualizar(int(id), params)
        if retorno.status_code == 200:
          st.success("Disciplina atualizada com sucesso")
        else:
          st.error(retorno.text)
    with abas[3]:
      id = st.text_input("Digite o ID da disciplina que deseja excluir")
      if st.button("Excluir disciplina"):
        retorno = self.excluir(int(id))
        if retorno.status_code == 200:
          st.success("Disciplina excluída com sucesso")
        else:
          st.error(retorno.text)
    super().rodape()

DisciplinaTela().renderizar()