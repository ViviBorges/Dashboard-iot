import os
import pandas as pd
from sqlalchemy import create_engine

# Caminho do arquivo CSV
csv_path = r"C:\Users\vivia\meu_projeto\data\IOT-temp.csv"

# Verificar se o arquivo CSV existe
if not os.path.exists(csv_path):
    print(f"Erro: O arquivo {csv_path} não foi encontrado.")
    exit()

try:
    # Carregar o arquivo CSV
    df = pd.read_csv(csv_path)

    # Renomear colunas para um formato mais amigável ao banco de dados
    df = df.rename(columns={
        "room_id/id": "device_id",
        "noted_date": "timestamp",
        "temp": "temperature"
    })

    # Remover colunas problemáticas
    df = df.drop(columns=["id", "out/in"], errors="ignore")

    # Converter timestamp para o formato correto
    df["timestamp"] = pd.to_datetime(df["timestamp"], format="%d-%m-%Y %H:%M")

    # Criar conexão com PostgreSQL
    DATABASE_URL = "postgresql://postgres:1020@localhost:5432/postgres"
    engine = create_engine(DATABASE_URL)

    # Inserir dados no banco
    df.to_sql("temperature_readings", engine, if_exists="append", index=False)
    print("Dados inseridos com sucesso!")

except Exception as e:
    print(f"Erro ao processar os dados: {e}")
