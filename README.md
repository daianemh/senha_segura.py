
# 🔐 Verificador de Senhas Seguras

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3" />
  <img src="https://img.shields.io/badge/Cybersecurity-Defensive-red?style=for-the-badge" alt="Cybersecurity" />
  <img src="https://img.shields.io/badge/Regex-Nativa-blue?style=for-the-badge" alt="RegEx" />
</p>

## 🔍 Sobre o Projeto

O **Verificador de Senhas Seguras** é um script desenvolvido em Python focado na aplicação prática de conceitos de **Cibersegurança (Defensiva)** e criptografia comportamental (boas práticas de credenciais). 

O sistema analisa a estrutura da senha fornecida pelo usuário, valida a presença de múltiplos fatores de complexidade via Expressões Regulares (RegEx) e classifica a robustez da credencial, fornecendo um feedback imediato de mitigação de riscos (dicas de melhoria).

Este projeto faz parte dos meus estudos contínuos na área de Cibersegurança, Infraestrutura e Programação Back-end, unindo o desenvolvimento de software à mentalidade de segurança por design.

---

## ⚙️ Funcionalidades e Critérios de Análise

A ferramenta avalia a segurança com base nos principais frameworks de conformidade do mercado, verificando:

* **📏 Comprimento Mínimo:** Exigência de pelo menos 8 caracteres.
* **🔠 Diversidade de Caixa:** Presença de letras maiúsculas e minúsculas.
* **🔢 Caracteres Numéricos:** Inclusão de números de 0 a 9.
* **✨ Caracteres Especiais:** Validação de símbolos de pontuação e segurança (`@`, `$`, `%`, `&`, `*`, `!`, `?`, etc.).
* **📊 Classificação Dinâmica:** Categorização instantânea em **Fraca**, **Média** ou **Forte**.
* **💡 Feedback Educativo:** Exibição de recomendações específicas para os critérios que não foram atendidos.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3:** Linguagem base para a construção do script.
* **Biblioteca `re`:** Módulo nativo do Python para manipulação de Expressões Regulares, utilizado para a validação matemática e estrutural dos padrões da senha.
* **Terminal Interativo:** Interface de linha de comando (CLI) leve, focada em performance e consumo mínimo de recursos.

---

## 🖥️ Exemplo de Execução (Console)

```text
Sua Senha: 123
[❌] Força da Senha: FRACA
Dicas para melhoria:
- A senha deve ter pelo menos 8 caracteres.
- Adicione letras maiúsculas e minúsculas.
- Adicione pelo menos um caractere especial (@, $, %, etc.).

Sua Senha: P@ssword2026!
[✅] Força da Senha: FORTE
Senha segura! Excelente combinação de caracteres.

```

---

## 💻 Como Rodar o Projeto

### Pré-requisitos

* Ter o **Python 3.x** instalado na sua máquina.
* O projeto não possui dependências externas (apenas bibliotecas nativas).

### Passo a Passo

1. **Clone o repositório:**
```bash
git clone [https://github.com/daianemh/nome-do-seu-repositorio.git](https://github.com/daianemh/nome-do-seu-repositorio.git)

```


2. **Navegue até o diretório do script:**
```bash
cd nome-do-seu-repositorio

```


3. **Execute o script pelo terminal:**
```bash
python verificador.py

```


*(Substitua `verificador.py` pelo nome exato do seu arquivo Python)*

---

## 👤 Autora

Desenvolvido por **Daiane Horbach**.
Se este projeto te ajudou a entender mais sobre validação de segurança, sinta-se à vontade para deixar uma ⭐ no repositório!

```

```
