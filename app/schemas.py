from pydantic import BaseModel, EmailStr
from typing import Optional

class Entidade(BaseModel):
    ID: int
    NOME: str

class UnidadeItem(BaseModel):
    ID: int
    FK_ORGAO: int
    SIGLA: str

class Fornecedor(BaseModel):
    ID: int
    FK_ORGAO: int
    CNPJ: str
    CPF_RESPONSAVEL: Optional[str]
    RAZAO_SOCIAL: str
    NOME_RESPONSAVEL: Optional[str]
    TELEFONE: Optional[str]
    ENDERECO: Optional[str]
    EMAIL: Optional[EmailStr]

class Item(BaseModel):
    ID: int
    FK_ORGAO: int
    FK_UNIDADE_ITEM: int
    CODIGO: str
    DESCRICAO: str
