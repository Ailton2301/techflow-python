# 📋 Sistema de Gerenciamento Ágil de Tarefas - TechFlow Solutions

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![GitHub License](https://img.shields.io/github/license/Ailton2301/techflow-python)
![GitHub Issues](https://img.shields.io/github/issues/Ailton2301/techflow-python)

## 📌 Visão Geral
Sistema de gerenciamento de tarefas para startups de logística, desenvolvido com:
- **Backend**: Python + Flask
- **Metodologias Ágeis**: Kanban integrado via GitHub Projects
- **CI/CD**: GitHub Actions
- **Testes**: Pytest

## 🚀 Começando

### Pré-requisitos
- Python 3.10+
- Git
- Conta no GitHub

### Instalação
```bash
# Clone o repositório
git clone https://github.com/Ailton2301/techflow-python.git
cd techflow-python

# Ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

# Instale as dependências
pip install -r requirements.txt
Execução
bash
flask run
Acesse: http://localhost:5000

📚 Documentação da API
Autenticação
POST /auth/login

json
{
  "username": "admin",
  "password": "admin123"
}
Tarefas
Método	Endpoint	Descrição
GET	/api/tasks	Lista todas as tarefas
POST	/api/tasks	Cria nova tarefa
PUT	/api/tasks/id	Atualiza tarefa
DELETE	/api/tasks/id	Remove tarefa
🧪 Testes
bash
pytest -v
🛠️ Tecnologias
Backend: Python + Flask

Testes: Pytest

CI/CD: GitHub Actions

Documentação: Swagger (futuro)

📊 Estrutura
text
src/
├── app.py          # Aplicação principal
├── models.py       # Modelos de dados
└── routes/
    ├── tasks.py    # Endpoints de tarefas
    └── auth.py     # Autenticação
tests/              # Testes automatizados
🤝 Contribuição
Faça um fork

Crie sua branch (git checkout -b feature/nova-feature)

Commit (git commit -m 'Add feature')

Push (git push origin feature)

Abra um Pull Request

✉️ Contato
Ailton Resende

Email: silvaailton578@gmail.com

LinkedIn: linkedin.com/in/ailton-resende

Nota: Projeto desenvolvido para a disciplina de Engenharia de Software da [UNIFECAF].
