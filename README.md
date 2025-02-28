# 📊 Pipeline de Dados com IoT e Docker

## 📌 Descrição

Este projeto coleta leituras de temperatura de dispositivos IoT, processa essas informações e as armazena em um banco de dados PostgreSQL.\
Utilizamos um **dashboard interativo com Streamlit** para visualizar os dados.


## 🚀 Tecnologias Utilizadas

- **Python** → Processamento dos dados
- **Pandas** → Manipulação de tabelas
- **SQLAlchemy** → Conexão com PostgreSQL
- **Streamlit** → Criação do Dashboard
- **Plotly** → Gráficos interativos
- **PostgreSQL** → Armazenamento de dados
- **Docker** → Para rodar o banco de dados no container


## Como Instalar e Rodar

### 1. Clone o repositório:

 git clone https://github.com/ViviBorges/Dashboard-iot.git
 cd Painel-iot

### 2. Crie um ambiente virtual:

python -m venv venv


### 3. Ative o ambiente virtual:

📍 No Windows (PowerShell):

.\venv\Scripts\Activate

📍 No Linux/macOS:

source venv/bin/activate


### 4. Instale as dependências:

pip install -r requirements.txt


### 5. Suba o banco de dados PostgreSQL (pode ser com Docker):

docker run --name postgres-iot -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=123456 -p 5432:5432 -d postgres


### 6. Execute o Dashboard:

streamlit run dashboard.py


### 7. Acesse no navegador:

http://localhost:8501


## 📊 Gráficos

[Gráfico 1-](images/Media_temp_por_dispositivo.png)
[Gráfico 2-](images/Leituras_por_hora_do_dia.png")
[Gráfico 3-](images/Temp_max_e_min_por_dia.png)


## 📋 Views SQL Criadas

O projeto usa algumas **views** no banco de dados PostgreSQL para facilitar a análise:

| View                        | Descrição                               |
| --------------------------- | --------------------------------------- |
| avg\_temp\_por\_dispositivo | Média de temperatura por dispositivo    |
| leituras\_por\_hora         | Contagem de leituras agrupadas por hora |
| temp\_max\_min\_por\_dia    | Temperaturas máxima e mínima por dia    |


## Possíveis Insights Obtidos

- Monitorar o desempenho individual de cada dispositivo, identificando sensores com comportamento estranho.
- Entender em quais horários há maior volume de leituras, permitindo otimizar o processo de coleta.
- Identificar tendências e variações climáticas ao longo do tempo.
- Correlacionar mudanças de temperatura com eventos externos (manutenção, clima, etc.).
- Criar alertas automáticos para manutenção preditiva, aumentando a confiabilidade do sistema.

## 💎 Link do Repositório

https://github.com/ViviBorges/Dashboard-iot.git


