🚀 Flask API com CI/CD Pipeline
<div align="center">
https://img.shields.io/badge/Python-3.9%252B-blue
https://img.shields.io/badge/Flask-2.3.3-green
https://img.shields.io/badge/GitHub%2520Actions-CI%252FCD-brightgreen
https://img.shields.io/badge/license-MIT-blue
https://img.shields.io/badge/status-em%2520desenvolvimento-yellow

Uma API RESTful simples construída com Flask e automatizada com GitHub Actions

📋 Funcionalidades •
🛠️ Instalação •
📡 Endpoints •
🧪 Testes •
🔄 CI/CD •
📁 Estrutura

</div>
📋 Sobre o Projeto
Este projeto é uma demonstração prática de como criar uma API REST utilizando Flask e implementar um pipeline de Integração Contínua (CI) usando GitHub Actions. É um exemplo perfeito para:

✅ Aprender os fundamentos de APIs com Flask

✅ Entender como funcionam pipelines de CI/CD

✅ Praticar testes automatizados com pytest

✅ Criar um portfólio profissional no GitHub

🎯 Funcionalidades
API RESTful com endpoints bem definidos

Testes automatizados com pytest

Pipeline CI/CD com GitHub Actions

Código limpo e comentado

Fácil de estender e modificar

🛠️ Instalação
Pré-requisitos
Python 3.9 ou superior

Git

Pip (gerenciador de pacotes Python)

Passo a Passo
1. Clone o repositório

bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
2. Crie um ambiente virtual (recomendado)

bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
3. Instale as dependências

bash
pip install -r requirements.txt
4. Execute a aplicação

bash
python app.py
Acesse: http://localhost:5000 🎉

📡 Endpoints da API
Método	Endpoint	Descrição	Exemplo Resposta
GET	/	Página inicial	{"message": "API Flask funcionando!", "status": "success"}
GET	/api/health	Health check	{"status": "healthy"}
GET	/api/users/<id>	Busca usuário por ID	{"id": 123, "name": "Usuário 123", "email": "user123@example.com"}
GET	/api/sum/<a>/<b>	Soma dois números	{"operation": "sum", "a": 5, "b": 3, "result": 8}
Exemplos de uso com curl
bash
# Endpoint principal
curl http://localhost:5000/

# Health check
curl http://localhost:5000/api/health

# Buscar usuário
curl http://localhost:5000/api/users/42

# Somar números
curl http://localhost:5000/api/sum/10/20
🧪 Testes
O projeto utiliza pytest para testes automatizados.

Executar todos os testes
bash
python -m pytest test_app.py -v
Executar teste específico
bash
python -m pytest test_app.py::test_home_endpoint -v
Verificar cobertura de testes
bash
pip install pytest-cov
python -m pytest --cov=app test_app.py
🔄 CI/CD
GitHub Actions Pipeline
O pipeline é executado automaticamente em cada push ou pull_request para as branches main/master.

Jobs do Pipeline:

Job	Descrição	Quando executa
✅ Test	Executa testes em Python 3.9, 3.10 e 3.11	Sempre
🚀 Deploy-Demo	Testa deploy local	Apenas na branch main
Status do Pipeline
https://github.com/seu-usuario/seu-repositorio/actions/workflows/python-ci.yml/badge.svg

🔗 Ver pipeline em ação

📁 Estrutura do Projeto
text
📦 meu-projeto-flask
├── 📂 .github
│   └── 📂 workflows
│       └── 📄 python-ci.yml     # Configuração do GitHub Actions
├── 📄 app.py                    # Aplicação Flask principal
├── 📄 test_app.py              # Testes automatizados
├── 📄 requirements.txt         # Dependências do projeto
├── 📄 README.md               # Documentação
└── 📄 .gitignore             # Arquivos ignorados pelo Git
💻 Desenvolvimento Local
Pré-requisitos de desenvolvimento
bash
# Instalar dependências de desenvolvimento
pip install flake8 black pytest-cov
Padrões de código
bash
# Verificar estilo de código
flake8 app.py test_app.py --max-line-length=127

# Formatar código automaticamente
black app.py test_app.py
📊 Monitoramento e Logs
A aplicação gera logs que podem ser visualizados:

Localmente: No terminal onde o Flask está rodando

GitHub Actions: Nos artefatos do pipeline (flask.log)

🤝 Como Contribuir
Fork o projeto

Crie uma branch (git checkout -b feature/nova-feature)

Commit suas mudanças (git commit -m 'Adiciona nova feature')

Push para a branch (git push origin feature/nova-feature)

Abra um Pull Request

🎓 Aprendizados
Este projeto demonstra:

✅ Criação de APIs REST com Flask

✅ Testes automatizados com pytest

✅ Versionamento de código com Git

✅ Integração Contínua com GitHub Actions

✅ Boas práticas de documentação

✅ Estrutura organizada de projetos Python