**<h2>🏅 API com FastAPI 🏅</h2>**

###

Breve descrição sobre o FastAPI, e como usá-lo.

---

Uma API desenvolvida com FastAPI que retorna informações baseadas em nomes via rota `/name`.

###

**<h2>📂 Organização dos Arquivos</h2>**

###

📦projeto<br>
┣  📂app<br>
┃  ┣  📑main.py<br>
┃  ┣  📑routes.py<br>
┃  ┗  📑models.py<br>
┣  📑requirements.txt<br>
┣  📑README.md<br>
┣  📑.gitignore<br>
┗  📂env/ (virtualenv)<br>

---

**<h2>📌 Instalação das Dependências</h2>**

###

1️⃣- Clone o repositório:

###
```powershell
git clone https://github.com/Kauan19-hub/Projects.git
```

2️⃣- Entre no repositório clonado:

###
```powershell
cd Projects
```

3️⃣- Crie, e ative o Ambiente Virtual `env`:

Windows
```powershell
python -m venv env  ### Cria a env

.\env\Scripts\activate ### Ativa a env
```

MacOS/Linux
```powershell
python3 -m venv env

source env/bin/activate
```

4️⃣- Instale as dependências:

###
```powershell
pip install fastapi uvicorn ### instale diretamente o FastAPI e o Uvicorn (caso não tenha o requirements.txt)
```

**<h2>🛠 Em Andamento</h2>**

###

Após seguir os passos acima, digite:
```powershell
uvicorn main:app --reload
```

A aplicação estará disponível em:
```powershell
http://127.0.0.1:8000/name
```

---

**<h2>😉 Clonagem para Testes</h2>**

###
```powershell
git clone https://github.com/seu-usuario/seu-repositorio.git

cd seu-repositorio

python -m venv env

.\env\Scripts\activate  # ou source env/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload
```

**<h2>📊 Ferramentas Utilizadas</h2>**

###

✅ FastAPI;<br>
✅ Python;<br>
✅ VS Code;<br>
✅ Git/GitHub;<br>
✅ Uvicorn;<br>
✅ Postman;<br>
✅ JSon.<br>

###

⬇ Para testar sua API, você pode usar um desses Softwares: ⬇

###


<div align="left">
  <a href="https://www.postman.com/" target="blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Postman-FF6C37?logo=postman&logoColor=black&style=for-the-badge" height="30" alt="postman logo" title="Download Postman" />
  </a>
  <img width="3" />
  <a href="https://insomnia.rest/download" target="blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/insomnia-5E00D3?logo=insomnia&logoColor=white&style=for-the-badge" height="40" alt="insomnia logo"  title="Download Insomnia" /> 
  </a>
</div>

---

**<h2>🤝 Contribuições</h2>**

###

Sinta-se à vontade para abrir issues ou enviar pull requests, para contribuições ou sugestões! Muito obrigado! 😎








