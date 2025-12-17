from fastapi import APIRouter
from config.database import conexao
from models.jogador import Jogador
from schemas.jogador import jogadorEntidade, listaJogadoresEntidade
from bson import ObjectId

jogador_router = APIRouter()

@jogador_router.get("/")
async def inicio():
    return {"mensagem": "API de Jogadores está funcionando!"}

@jogador_router.get("/jogadores")
async def listar_jogadores():
    return listaJogadoresEntidade(conexao.local.jogadores.find())

@jogador_router.get("/jogadores/{jogador_id}")
async def listar_jogador(jogador_id: str):
    jogador = conexao.local.jogadores.find_one({"_id": ObjectId(jogador_id)})
    return jogadorEntidade(jogador)

@jogador_router.post("/jogadores")
async def cadastra_jogadores(jogador: Jogador):
    conexao.local.jogadores.insert_one(dict(jogador))
    return listaJogadoresEntidade(conexao.local.jogadores.find()) 

@jogador_router.put("/jogadores/{jogador_id}")
async def atualizar_jogador(jogador_id: str, jogador: Jogador):
    conexao.local.jogadores.update_one(
        {"_id": ObjectId(jogador_id)},
        {"$set": dict(jogador)}
    )
    return jogadorEntidade(conexao.local.jogadores.find_one({"_id": ObjectId(jogador_id)}))

@jogador_router.delete("/jogadores/{jogador_id}")
async def deletar_jogador(jogador_id: str):
    return jogadorEntidade(conexao.local.jogadores.find_one_and_delete({"_id": ObjectId(jogador_id)}))