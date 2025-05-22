## 📦 Tabela: Distribuição Item

### 🧾 Campos da Tela

- 📁 **Projeto Lotação (FK)**
- 📜 **Contrato-Item (FK)**
- 🎯 **Quantidade Destinada**
- 📥 **Quantidade Entregue**

---

### 🧱 Estrutura da Tabela no Banco

| Nº | Campo 🏷️                   | Nome no Banco 🗃️            | Tipo de Dado 🔠         | Observações 📌                             |
|----|-----------------------------|------------------------------|--------------------------|--------------------------------------------|
| 0  | 🔑 ID                       | `ID`                         | `INT` (AI, PK)           | Chave Primária                             |
| 1  | 📁 Projeto Lotação (FK)     | `FK_PROJETO_LOTACAO`         | `INT`                    | Chave estrangeira para projeto/lotação    |
| 2  | 📜 Contrato-Item (FK)       | `FK_CONTRATO_HAS_ITEM`       | `INT`                    | Chave estrangeira para contrato_item       |
| 3  | 🎯 Quantidade Destinada     | `QUANTIDADE_DESTINADA`       | `DECIMAL(10,3)`          | Quantidade destinada ao projeto            |
| 4  | 📥 Quantidade Entregue      | `QUANTIDADE_ENTREGUE`        | `DECIMAL(10,3)`          | Quantidade efetivamente entregue           |
