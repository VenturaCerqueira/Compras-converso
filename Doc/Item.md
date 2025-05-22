## 📦 Tabela: Item

### 🧩 Estrutura da Tabela

| Nº | Campo 🏷️            | Nome no Banco 🗃️     | Tipo de Dado 🔠     | Observações 📌        |
|----|----------------------|-----------------------|----------------------|------------------------|
| 0  | 🔑 ID                | `ID`                  | `INT` (AI, PK)       | Chave Primária         |
| 1  | 🏢 Órgão (FK)        | `FK_ORGAO`            | `INT`                | Chave estrangeira       |
| 2  | 🧩 Unidade do Item   | `FK_UNIDADE_ITEM`     | `INT`                | Chave estrangeira       |
| 3  | 🆔 Código            | `CODIGO`              | `CHAR(20)`           | Código identificador    |
| 4  | 📝 Descrição         | `DESCRICAO`           | `CHAR(255)`          | Nome ou detalhe do item |
