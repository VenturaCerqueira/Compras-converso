from fastapi import APIRouter, HTTPException, Query
from app.database import get_connection
from app.schemas import Entidade, UnidadeItem, Fornecedor, Item, Licitacao, Contrato
from typing import List

router = APIRouter()

@router.get("/entidades", response_model=List[Entidade])
def get_entidades():
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM orgao")
            return cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro: {e}")
    finally:
        conn.close()

@router.get("/unidades", response_model=List[UnidadeItem])
def get_unidades(fk_orgao: int = Query(..., description="ID do órgão")):
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM unidade_item WHERE FK_ORGAO = %s", (fk_orgao,))
            return cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro: {e}")
    finally:
        conn.close()

@router.get("/fornecedores", response_model=List[Fornecedor])
def get_fornecedores(fk_orgao: int = Query(..., description="ID do órgão")):
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM fornecedor WHERE FK_ORGAO = %s", (fk_orgao,))
            return cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro: {e}")
    finally:
        conn.close()

@router.get("/itens", response_model=List[Item])
def get_itens(fk_orgao: int = Query(..., description="ID do órgão")):
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM item WHERE FK_ORGAO = %s", (fk_orgao,))
            return cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro: {e}")
    finally:
        conn.close()

@router.get("/licitacao", response_model=List[Licitacao])
def get_licitacao(fk_orgao: int = Query(..., description= "ID do órgão")):
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("Select * from licitacao where FK_ORGAO = %s", (fk_orgao))
            return cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro: {e}")
    finally:
        conn.close()
        
@router.get("/contrato", response_model=List[Contrato])
def get_contratos(fk_licitacao: int = Query(..., description="ID da Licitação consultar em /licitacao")):
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("Select * from contrato where fk_licitacao = %s", (fk_licitacao))
            return cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro: {e}")
    finally:
        conn.close() 