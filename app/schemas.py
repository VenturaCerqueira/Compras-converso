from pydantic import BaseModel, EmailStr, condecimal
from typing import Optional
from datetime import date

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

class Licitacao(BaseModel):
    ID: Optional[int]
    FK_ORGAO: int
    MODALIDADE: Optional[str] = None
    NUMERO_LICITACAO: Optional[str] = None
    NUMERO_PROCESSO: Optional[str] = None
    DATA_PUBLICACAO: Optional[date] = None
    DATA_LICITACAO: Optional[date] = None
    OBJETO: Optional[str] = None
    VALOR_TOTAL: Optional[condecimal(max_digits=10, decimal_places=3)] = None
    INFORMACOES_COMPLEMENTARES: Optional[str] = None
    
class Contrato(BaseModel):
    ID: Optional[int]
    FK_FORNECEDOR: int
    FK_LICITACAO: int
    NUMERO: Optional[str] = None
    TIPO_CONTRATO: Optional[str] = None
    DATA: Optional[date] = None
    DATA_ENCERRAMENTO: Optional[date] = None
    DATA_ADITIVADA: Optional[date] = None
    VALOR_TOTAL: Optional[condecimal(max_digits=10, decimal_places=3)] = None
    
