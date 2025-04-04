import os
import csv
import json

# Caminho absoluto do CSV dentro do contêiner Docker
csv_file_path = '/usr/src/workspace/intuitiveweb-api/src/csv/Relatorio_cadop.csv'
json_file_path = '/usr/src/workspace/intuitiveweb-api/src/json/Relatorio_cadop.json'

os.makedirs(os.path.dirname(json_file_path), exist_ok=True)

json_data = []

with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')
    
    for row in csv_reader:
        record = {
            "ans_registration_code": row["Registro_ANS"],
            "cnpj": row["CNPJ"],
            "socialname": row["Razao_Social"],
            "fantasyname": row["Nome_Fantasia"],
            "modality": row["Modalidade"],
            "area_code": row["DDD"],
            "phone": row["Telefone"],
            "fax": row["Fax"],
            "email": row["Endereco_eletronico"],
            "representative": row["Representante"],
            "representative_position": row["Cargo_Representante"],
            "commercialization_region": row["Regiao_de_Comercializacao"],
            "ans_registration_date": row["Data_Registro_ANS"]
        }
        
        json_data.append(record)

with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=4)

print(f"Arquivo JSON gerado em: {json_file_path}")
