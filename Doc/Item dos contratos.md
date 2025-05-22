## 📦 Tabela: Contrato Item

### 🧱 Estrutura da Tabela no Banco

| Nº | Campo 🏷️                  | Nome no Banco 🗃️         | Tipo de Dado 🔠        | Observações 📌                        |
|----|----------------------------|---------------------------|-------------------------|---------------------------------------|
| 0  | 🔑 ID                      | `ID`                      | `INT` (AI, PK)          | Chave Primária                        |
| 1  | 📦 Item (FK)               | `FK_ITEM`                 | `INT`                   | Chave estrangeira da tabela `item`    |
| 2  | 📜 Contrato (FK)           | `FK_CONTRATO`             | `INT`                   | Chave estrangeira da tabela `contrato`|
| 3  | 🔢 Quantidade Total        | `QUANTIDADE_TOTAL`        | `DECIMAL(10,3)`         | Quantidade total contratada           |
| 4  | 📥 Quantidade Entregue     | `QUANTIDADE_ENTREGUE`     | `DECIMAL(10,3)`         | Total já entregue                     |
| 5  | 💲 Valor Unitário          | `VALOR_UNITARIO`          | `DECIMAL(10,3)`         | Valor por unidade                     |
| 6  | 💰 Valor Total             | `VALOR_TOTAL`             | `DECIMAL(10,3)`         | Valor total do item no contrato       |


### 🧾 Campos da Tela

- 📦 **Item (FK)**
- 💲 **Valor Unitário**
- 🔢 **Quantidade Total**
- 💰 **Valor Total**
---

