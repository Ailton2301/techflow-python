📋 Sistema de Gerenciamento Ágil de Tarefas - TechFlow Solutions

📌 Visão Geral
Sistema de gerenciamento de tarefas desenvolvido para startups de logística, implementando metodologias ágeis com Python e Flask. O projeto inclui:

CRUD completo de tarefas com priorização

Autenticação básica de usuários

Quadro Kanban integrado (GitHub Projects)

Pipeline CI/CD com GitHub Actions

Testes automatizados com pytest

🚀 Começando
Pré-requisitos
Python 3.10+

Git

Conta no GitHub

Instalação
bash
# Clone o repositório
git clone https://github.com/seu-usuario/techflow-python.git
cd techflow-python

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

# Instale as dependências
pip install -r requirements.txt
Executando a Aplicação
bash
flask run
A API estará disponível em http://localhost:5000

📚 Documentação da API
Autenticação
POST /auth/login

json
{
  "username": "admin",
  "password": "admin123"
}
Tarefas
GET /api/tasks - Lista todas as tarefas

POST /api/tasks - Cria nova tarefa

json
{
  "titulo": "Revisar contrato",
  "descricao": "Verificar cláusulas de entrega",
  "prioridade": "alta"
}
PUT /api/tasks/<id> - Atualiza tarefa

DELETE /api/tasks/<id> - Remove tarefa

🧪 Testes
Execute todos os testes:

bash
pytest -v
🛠️ Tecnologias
Backend: Python + Flask

Testes: pytest

CI/CD: GitHub Actions

Documentação: Swagger (Futura implementação)

📊 Estrutura do Código
text
src/
├── app.py                # Aplicação principal
├── models.py             # Modelos de dados
└── routes/
    ├── tasks.py          # Endpoints de tarefas
    └── auth.py           # Endpoints de autenticação
tests/
├── test_models.py        # Testes de modelos
├── test_tasks.py         # Testes de tarefas
└── test_auth.py          # Testes de autenticação
🤝 Contribuição
Faça um fork do projeto

Crie sua branch (git checkout -b feature/nova-feature)

Commit suas mudanças (git commit -m 'Adiciona nova feature')

Push para a branch (git push origin feature/nova-feature)

Abra um Pull Request


✉️ Contato
[Ailton Resende] - [silvaailton578@gmail.com]
[www.linkedin.com/in/ailton-resende-8a4815199]

Nota: Este projeto foi desenvolvido como parte da disciplina de Engenharia de Software da [UNIFECAF].

