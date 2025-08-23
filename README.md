# 📋 Sistema de Gerenciamento Ágil de Tarefas - TechFlow Solutions

## 🎯 Objetivo e Escopo
O objetivo deste projeto é desenvolver um sistema de gerenciamento de tarefas para startups de logística, com foco em simplicidade, agilidade e integração com metodologias ágeis.  

O escopo inclui:
- Criação, edição e remoção de tarefas.  
- Autenticação de usuários.  
- Visualização de tarefas em formato de lista.  
- Integração futura com quadro Kanban no GitHub Projects.  

---

## ⚙️ Metodologia Adotada
Durante o desenvolvimento, utilizamos práticas de **Engenharia de Software** e **Metodologias Ágeis**:

- **Kanban (GitHub Projects):** Organização das tarefas em colunas (To Do, Doing, Done).  
- **Controle de Versão (Git + GitHub):** Cada mudança registrada em commits atômicos.  
- **Integração Contínua (GitHub Actions):** Execução automática dos testes (Pytest) em cada push.  

---

## 🚀 Instruções para Execução do Sistema

### Pré-requisitos
- Python 3.10+  
- Git  
- Conta no GitHub  

### Instalação
```bash
# Clone o repositório
git clone https://github.com/Ailton2301/techflow-python.git
cd techflow-python/src

# Criação do ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
.\venv\Scripts\activate    # Windows

# Instalação das dependências
pip install -r requirements.txt
Execução
bash
Copiar
Editar
flask run
Acesse em: http://localhost:5000

📊 Justificativas de Mudanças no Escopo
Durante o desenvolvimento foram realizadas algumas mudanças no escopo inicial:

A integração com Swagger foi adiada para uma versão futura.

O sistema foi ajustado para uso acadêmico, priorizando clareza e simplicidade sobre escalabilidade.

O foco foi dado em tarefas CRUD básicas em vez de funcionalidades avançadas (notificações, dashboard, relatórios).

Essas decisões foram tomadas para manter a viabilidade dentro do prazo da disciplina de Engenharia de Software (UNIFECAF).

🧪 Testes
Para rodar os testes automatizados:

bash
Copiar
Editar
pytest -v
🛠️ Tecnologias
Backend: Python + Flask

Testes: Pytest

CI/CD: GitHub Actions

Documentação: Markdown (README), Swagger (planejado)

🤝 Contribuição
Faça um fork do repositório.

Crie uma branch (git checkout -b feature/nova-feature).

Realize commits (git commit -m 'Adiciona nova funcionalidade').

Envie para o repositório remoto (git push origin feature/nova-feature).

Abra um Pull Request.

✉️ Contato
Autor: Ailton Resende

Email: silvaailton578@gmail.com

LinkedIn: linkedin.com/in/ailton-resende
