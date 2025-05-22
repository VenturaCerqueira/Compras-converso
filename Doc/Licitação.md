## 📑 Tabela: Licitação

### 🧱 Estrutura da Tabela no Banco

| Nº | Campo 🏷️                  | Nome no Banco 🗃️             | Tipo de Dado 🔠          | Observações 📌                   |
|----|----------------------------|-------------------------------|---------------------------|----------------------------------|
| 0  | 🔑 ID                      | `ID`                          | `INT` (AI, PK)            | Chave Primária                   |
| 1  | 🏢 Órgão (FK)              | `FK_ORGAO`                    | `INT`                     | Chave estrangeira                |
| 2  | 🏷️ Modalidade             | `MODALIDADE`                  | `VARCHAR(45)`             | Tipo da licitação (ex: Pregão)  |
| 3  | 🔢 Número da Licitação     | `NUMERO_LICITACAO`            | `VARCHAR(40)`             | Código/identificação da licitação |
| 4  | 🆔 Número do Processo      | `NUMERO_PROCESSO`             | `VARCHAR(20)`             | Número do processo interno       |
| 5  | 📅 Data de Publicação      | `DATA_PUBLICACAO`             | `DATE`                    |                                  |
| 6  | 🗓️ Data da Licitação       | `DATA_LICITACAO`              | `DATE`                    |                                  |
| 7  | 📄 Objeto da Licitação     | `OBJETO`                      | `TEXT`                    | Descrição do objeto              |
| 8  | 💰 Valor Total             | `VALOR_TOTAL`                 | `DECIMAL(10,3)`           | Valor estimado total             |
| 9  | 🧾 Informações Complementares | `INFORMACOES_COMPLEMENTARES` | `TEXT`                    | Opcional                         |

<br>

---

### 🧾 Campos da Tela

- 🏷️ **Modalidade**
- 🔢 **Número da Licitação**
- 🆔 **Número do Processo**
- 📅 **Data da Publicação**
- 🗓️ **Data da Licitação**
- 💰 **Valor Total**
- 📄 **Objeto**

---

![alt text](/src/assets/img/image.png)