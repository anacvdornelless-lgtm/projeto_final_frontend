import sys
from pathlib import Path
import streamlit as st

#configuração do diretorio onde o app.py do streamlit esta sendo executado
BASE_DIR = Path(__file__).parent
sys.path.append(BASE_DIR)
#configura as paginas que estao no menu lateral
pagina_aluno = st.Page("menus/pagina_aluno.py", title="Pagina de Alunos", icon=":material/school:")
pagina_endereco = st.Page("menus/pagina_endereco.py", title="Pagina de Endereços", icon=":material/location_on:")
pagina_nota = st.Page("menus/pagina_nota.py", title="Pagina de Notas", icon=":material/grade:")
pagina_disciplina = st.Page("menus/pagina_disciplina.py", title="Pagina de Disciplinas", icon=":material/book:")

#cria o menu lateral do frontend
menus = {
  "Alunos": [pagina_aluno],
  "Endereços": [pagina_endereco],
  "Disciplinas": [pagina_disciplina],
  "Notas": [pagina_nota]
}
pg = st.navigation(menus)
#execcuta o app.py
pg.run()