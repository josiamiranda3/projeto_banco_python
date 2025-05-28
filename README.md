# 💰 Sistema Bancário em Python

Este projeto implementa um **Sistema Bancário Simples** em Python, com funcionalidades básicas como criação de usuários, abertura de contas, depósitos, saques e visualização de extratos. O sistema utiliza conceitos de **Programação Orientada a Objetos (POO)** e **boas práticas com abstrações e herança**.

---

## 📋 Funcionalidades

- Criar novo usuário (Pessoa Física)
- Criar nova conta corrente
- Listar contas criadas
- Realizar depósitos e saques
- Visualizar extrato da conta
- Limite de saque por operação e quantidade
- Histórico de transações

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Paradigma de Programação Orientada a Objetos
- Módulo `abc` (Abstract Base Classes)
- `textwrap` para formatar menus

---

## 🧱 Estrutura de Classes

- **Cliente** (classe base)
- **PessoaFisica** (herda de Cliente)
- **Conta** (classe base para contas bancárias)
- **ContaCorrente** (herda de Conta, com limites)
- **Historico** (registra todas as transações)
- **Transacao** (classe abstrata)
  - **Saque**
  - **Deposito**

---

## ▶️ Como Usar

1. Certifique-se de ter o **Python 3.x** instalado.
2. Salve o código em um arquivo `banco.py`.
3. Execute o script:
   ```bash
   python banco.py
   ```
4. Utilize o menu para interagir com o sistema:

```text
=============== MENU ===============
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q] Sair
```

---

## 🧪 Exemplo de Uso

1. Crie um novo usuário (`nu`)
2. Crie uma conta associada a esse usuário (`nc`)
3. Faça depósitos (`d`) e saques (`s`)
4. Visualize o extrato da conta (`e`)
5. Liste todas as contas cadastradas (`lc`)

---

## 🧠 Conceitos Envolvidos

- Encapsulamento com propriedades privadas
- Abstração com classes abstratas
- Herança e polimorfismo
- Registro e histórico de transações
- Regras de negócio para saques e depósitos

---

## 📌 Regras do Sistema

- O saque só é permitido se:
  - O número de saques for menor que 3
  - O valor for menor ou igual a R$500
  - O saldo for suficiente
- O depósito e saque não aceitam valores menores ou iguais a 0
- Cada transação é registrada no histórico da conta

---

## 📂 Organização do Código

- O menu principal está na função `main()`
- As interações são feitas por meio de entrada do usuário via terminal
- As operações são organizadas em funções e métodos, promovendo legibilidade e manutenibilidade

---

## ✅ Requisitos

- Python 3.7 ou superior

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
