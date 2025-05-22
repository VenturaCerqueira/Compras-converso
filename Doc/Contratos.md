## 📜 Tabela: Contratos

### 🧱 Estrutura da Tabela no Banco

| Nº | Campo 🏷️                 | Nome no Banco 🗃️        | Tipo de Dado 🔠        | Observações 📌                 |
|----|---------------------------|--------------------------|-------------------------|--------------------------------|
| 0  | 🔑 ID                     | `ID`                     | `INT` (AI, PK)          | Chave Primária                 |
| 1  | 🧑‍💼 Fornecedor (FK)      | `FK_FORNECEDOR`          | `INT`                   | Chave estrangeira              |
| 2  | 📑 Licitação (FK)        | `FK_LICITACAO`           | `INT`                   | Chave estrangeira              |
| 3  | 🔢 Número do Contrato     | `NUMERO`                 | `VARCHAR(16)`           | Código ou número oficial       |
| 4  | 🧾 Tipo do Contrato       | `TIPO_CONTRATO`          | `VARCHAR(45)`           | Ex: Fornecimento, Serviço etc. |
| 5  | 📅 Data de Início         | `DATA`                   | `DATE`                  | Início do contrato             |
| 6  | 📆 Data de Encerramento   | `DATA_ENCERRAMENTO`      | `DATE`                  | Encerramento previsto          |
| 7  | 🔁 Data Aditivada         | `DATA_ADITIVADA`         | `DATE`                  | Se houver prorrogação          |
| 8  | 💰 Valor Total            | `VALOR_TOTAL`            | `DECIMAL(10,3)`         | Valor global do contrato       |

---
 
<br>

### 🧾 Campos da Tela

- 🧑‍💼 **Fornecedor**
- 🧾 **Tipo de Contrato**
- 🔢 **Número do Contrato**
- 💰  **Valor Total**
- 📅 **Data de Início**
- 📆 **Data de Encerramento**
- 🔁 **Data Aditivada** (opcional)
- 📑 **Licitação (FK)** (opcional)

---

![alt text](/src/assets/img/Contratos.png)


## ➕ Tabela: Aditivo

### 🧱 Estrutura da Tabela no Banco

| Nº | Campo 🏷️               | Nome no Banco 🗃️    | Tipo de Dado 🔠    | Observações 📌                  |
|----|-------------------------|----------------------|---------------------|---------------------------------|
| 0  | 🔑 ID                   | `ID`                 | `INT` (AI, PK)      | Chave Primária                  |
| 1  | 📜 Contrato (FK)        | `FK_CONTRATO`        | `INT`               | Chave estrangeira               |
| 2  | 🔢 Número do Aditivo    | `NUMERO`             | `VARCHAR(16)`       | Número sequencial do aditivo    |
| 3  | 📄 Objeto               | `OBJETO`             | `TEXT`              | Descrição do aditivo            |
| 4  | 📅 Data                 | `DATA`               | `DATE`              | Data de assinatura              |
| 5  | 📆 Validade             | `VALIDADE`           | `DATE`              | Data de vencimento              |
| 6  | 💰 Valor                | `VALOR`              | `DECIMAL(10,3)`     | Valor acrescido ou ajustado     |

### 🧾 Campos da Tela

- 🔢 **Número do Aditivo**
- 📅 **Data do Aditivo**
- 💰 **Valor**
- 📆 **Nova data ENC.**
- 📄 **Objeto**

---

![alt text](/src/assets/img/Aditivo.png)