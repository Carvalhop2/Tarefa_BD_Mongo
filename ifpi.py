from pymongo import MongoClient

#Conecta ao servido local Mongo
cliente = MongoClient("mongodb://localhost:27017/")

#Cria ou acessa o banco de dados
banco = cliente["IFPI"]

#Cria ou acessa uma tabela
alunos = banco["Alunos"]

#adicionar na tabela
alunos.insert_one({
    "nome": "Ana Maria",
    "Idade": 18,
    "data de nascimento": "10/01/2006"
})