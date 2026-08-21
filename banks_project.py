import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import numpy as np
from datetime import datetime

# URLs e caminhos globais
url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ['Name', 'MC_USD_Billion']
db_name = 'Banks.db'
table_name = 'Largest_banks'
csv_path = 'Largest_banks_data.csv'
exchange_rate_path = 'exchange_rate.csv'

def log_progress(message):
    """Registra uma mensagem com timestamp no arquivo de auditoria."""
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("code_log.txt", "a") as f:
        f.write(f"{timestamp} : {message}\n")

def extract(url, table_attribs):
    """Extrai os dados da web com User-Agent para evitar bloqueios HTTP."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    page = response.text
    data = BeautifulSoup(page, 'html.parser')
    
    # Busca a tag tbody ou table
    tables = data.find_all('tbody')
    if not tables:
        tables = data.find_all('table')
        
    rows = tables[0].find_all('tr')
    
    data_list = []
    for row in rows:
        col = row.find_all('td')
        if len(col) != 0:
            bank_name = col[1].find_all('a')[1]['title'] if len(col[1].find_all('a')) > 1 else col[1].text.strip()
            market_cap = float(col[2].contents[0].replace('\n', '').strip())
            data_list.append({
                table_attribs[0]: bank_name,
                table_attribs[1]: market_cap
            })
            
    df = pd.DataFrame(data_list)
    return df.head(10)

def transform(df, exchange_rate_path):
    """Calcula a capitalização de mercado em GBP, EUR e INR com base no CSV de câmbio."""
    exchange_rate_df = pd.read_csv(exchange_rate_path)
    dict_rates = exchange_rate_df.set_index('Currency').to_dict()['Rate']

    df['MC_GBP_Billion'] = [np.round(x * dict_rates['GBP'], 2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x * dict_rates['EUR'], 2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x * dict_rates['INR'], 2) for x in df['MC_USD_Billion']]

    return df

def load_to_csv(df, output_path):
    """Persiste os dados em arquivo CSV sem o índice numérico."""
    df.to_csv(output_path, index=False)

def load_to_db(df, sql_connection, table_name):
    """Carrega o DataFrame como tabela em banco de dados relacional SQLite."""
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

def run_query(query_statement, sql_connection):
    """Executa e imprime consultas SQL de validação."""
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)
    log_progress('Process Query Execution completed')

if __name__ == '__main__':
    # 1. Início do Pipeline
    log_progress('Preliminaries complete. Initiating ETL process')

    # 2. Extração
    df = extract(url, table_attribs)
    log_progress('Data extraction complete. Initiating Transformation process')

    # 3. Transformação
    df = transform(df, exchange_rate_path)
    log_progress('Data transformation complete. Initiating Loading process')

    # 4. Carga em CSV e Banco
    load_to_csv(df, csv_path)
    log_progress('Data saved to CSV file')

    sql_connection = sqlite3.connect(db_name)
    log_progress('SQL Connection initiated')

    load_to_db(df, sql_connection, table_name)
    log_progress('Data loaded to Database as a table, Executing queries')

    # 5. Queries de verificação
    run_query('SELECT * FROM Largest_banks', sql_connection)
    run_query('SELECT AVG(MC_GBP_Billion) FROM Largest_banks', sql_connection)
    run_query('SELECT Name from Largest_banks LIMIT 5', sql_connection)

    # 6. Finalização
    log_progress('Process Complete')
    sql_connection.close()
    log_progress('Server Connection closed')
