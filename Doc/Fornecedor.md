## 📋 Cadastro de Fornecedor

### 🧩 Estrutura da Tabela

| Nº | Campo 🏷️                      | Nome no Banco 🗃️     | Tipo de Dado 🔠         | Observações 📌             |
|----|-------------------------------|-----------------------|--------------------------|-----------------------------|
| 0  | 🔑 ID                         | `id`                  | `INT` (AI, PK)           | Chave Primária              |
| 1  | 🏢 Órgão (FK)                 | `FK_ORGAO`            | `INT`                    | Exemplo: 25                 |
| 2  | 🧾 CNPJ/CPF                   | `CNPJ`                | `INT`                    |                  |
| 3  | 🏷️ Razão Social              | `RAZAO_SOCIAL`        | `VARCHAR(100)`           |                             |
| 4  | 🔑 CPF do Responsável         | `CPF_RESPONSAVEL`     | `VARCHAR(11)`            |                             |
| 5  | 👤 Nome do Responsável        | `NOME_RESPONSAVEL`    | `VARCHAR(100)`           |                             |
| 6  | ☎️ Telefone                   | `TELEFONE`            | `VARCHAR(100)`           |                             |
| 7  | 🏠 Endereço                   | `ENDERECO`            | `VARCHAR(100)`           |                             |
| 8  | 📧 E-mail                     | `EMAIL`               | `VARCHAR(50)`            |                             |
