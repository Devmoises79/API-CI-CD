### 🚀 Flask API com CI Pipeline

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI/CD-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Status](https://img.shields.io/badge/status-em%20finalização-yellow)

# Overview Architecture

Uma **API RESTful simples construída com Flask** e automatizada com **GitHub Actions** para demonstrar um pipeline básico de **CI/CD**.

</div>

---

# 📋 Funcionalidades

- API RESTful com endpoints bem definidos
- Testes automatizados com **pytest**
- Pipeline de **CI/CD com GitHub Actions**
- Código limpo e organizado
- Estrutura simples e fácil de expandir

---

# 📖 Sobre o Projeto

Este projeto é uma demonstração prática de como:

- Criar uma **API REST com Flask**
- Implementar **testes automatizados com pytest**
- Configurar **Integração Contínua (CI)** com GitHub Actions
- Manter um projeto com **boas práticas de versionamento**

É ideal para quem deseja aprender os **fundamentos de desenvolvimento backend em Python** e criar um **portfólio técnico no GitHub**.

---

# 🛠️ Instalação

## Pré-requisitos

- Python **3.9+**
- Git
- Pip

---

## 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

## 2️⃣ Crie um ambiente virtual

```bash
Windows
python -m venv venv
venv\Scripts\activate
Linux / Mac
python3 -m venv venv
source venv/bin/activate
```

## 3️⃣ Instale as dependências
```bash
pip install -r requirements.txt
```

## 4️⃣ Execute a aplicação

```bash
python app.py
```

* Acesse:
```bash
http://localhost:5000
```

## 📡 Endpoints da API

```text
Método	Endpoint	Descrição
GET	/	Página inicial
GET	/api/health	Health check
GET	/api/users/<id>	Buscar usuário por ID
GET	/api/sum/<a>/<b>	Soma dois números
Exemplo de respostas
Endpoint principal
{
  "message": "API Flask funcionando!",
  "status": "success"
}
Health check
{
  "status": "healthy"
}
```

## 📡 Exemplos com curl
# Endpoint principal

```bash
curl http://localhost:5000/
```

# Health check
```bash
curl http://localhost:5000/api/health
```

# Buscar usuário
```bash
curl http://localhost:5000/api/users/42
```

# Somar números

```bash
curl http://localhost:5000/api/sum/10/20
```

## 🧪 Testes

* O projeto utiliza pytest para testes automatizados.

- Executar todos os testes:

```bash
python -m pytest test_app.py -v
```

- Executar teste específico

```bash
python -m pytest test_app.py::test_home_endpoint -v
```

- Verificar cobertura

```bash
pip install pytest-cov
python -m pytest --cov=app test_app.py
```

## 🔄 CI/CD

- O projeto possui um pipeline de integração contínua utilizando GitHub Actions.

*O pipeline executa automaticamente quando ocorre:

- push

- pull request

*nas branches:

- main

- master

# Jobs do Pipeline

```text
Job	Descrição
Test	Executa testes em Python 3.9, 3.10 e 3.11
Deploy-Demo	Simula um deploy local
```

## 📁 Estrutura do Projeto

```bash
📦 flask-api-ci-cd
 ┣ 📂 .github
 ┃ ┗ 📂 workflows
 ┃ ┗ 📄 python-ci.yml
 ┣ 📄 app.py
 ┣ 📄 test_app.py
 ┣ 📄 requirements.txt
 ┣ 📄 README.md
 ┗ 📄 .gitignore
```

## 💻 Desenvolvimento Local

- Dependências de desenvolvimento:

```bash
pip install flake8 black pytest-cov
```

- Verificar padrão de código

```bash
flake8 app.py test_app.py --max-line-length=127
```

- Formatar código automaticamente:

```bash
black app.py test_app.py
```

## 📊 Monitoramento e Logs

*Os logs da aplicação podem ser visualizados:

- Localmente: no terminal onde o Flask está rodando

- GitHub Actions: nos artefatos do pipeline

## 🤝 Contribuição

- Fork o projeto

- Crie uma branch

- git checkout -b feature/nova-feature

*Commit suas alterações:

```bash
git commit -m "Adiciona nova feature"
```

*Envie para o repositório:

```bash
git push origin feature/nova-feature
```

- Abra um Pull Request

# 🎓 Aprendizados

Este projeto demonstra:

- Desenvolvimento de APIs REST com Flask

- Testes automatizados com pytest

- Versionamento com Git

- Integração contínua com GitHub Actions

- Estrutura organizada de projetos Python

- Boas práticas de documentação

## 👨‍💻 Desenvolvido por Moisés Aniceto
