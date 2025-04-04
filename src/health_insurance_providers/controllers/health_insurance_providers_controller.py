from flask import Blueprint, request, jsonify

response_data = [
    {
        "ans_registration_code": "123456789",
        "cnpj": "12.345.678/0001-90",
        "socialname": "Seguros Saúde S.A.",
        "fantasyname": "Saúde Plus",
        "modality": "Coletivo",
        "area_code": "11",
        "phone": "1234-5678",
        "fax": "1234-5679",
        "email": "contato@saudeplus.com.br",
        "representative": "João Silva",
        "representative_position": "Diretor Comercial",
        "commercialization_region": "São Paulo",
        "ans_registration_date": "2022-01-01"
    },
    {
        "ans_registration_code": "987654321",
        "cnpj": "98.765.432/0001-09",
        "socialname": "Saúde Total S.A.",
        "fantasyname": "Total Saúde",
        "modality": "Individual",
        "area_code": "21",
        "phone": "9876-5432",
        "fax": "9876-5433",
        "email": "contato@totalsaude.com.br",
        "representative": "Maria Souza",
        "representative_position": "CEO",
        "commercialization_region": "Rio de Janeiro",
        "ans_registration_date": "2023-01-01"
    },
]

health_insurance_providers_controller = Blueprint('health-insurance-providers', __name__)

@health_insurance_providers_controller.route('/health-insurance-providers/search', methods=['GET'])
def findAll():
    return jsonify(response_data)

@health_insurance_providers_controller.route('/health-insurance-providers/<string:code>', methods=['GET'])
def findOne(code):
    item = next((item for item in response_data if item["ans_registration_code"] == code), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"message": "Registro não encontrado!"}), 404

@health_insurance_providers_controller.route('/health-insurance-providers', methods=['POST'])
def create():
    new_data = request.get_json()

    if any(item["ans_registration_code"] == new_data["ans_registration_code"] for item in response_data):
        return jsonify({"message": "Código de registro já existe!"}), 400

    response_data.append(new_data)
    return jsonify({"message": "Registro criado com sucesso!"}), 201

@health_insurance_providers_controller.route('/health-insurance-providers/<string:code>', methods=['PUT'])
def update(code):
    updated_data = request.get_json()
    item = next((item for item in response_data if item["ans_registration_code"] == code), None)
    
    if item:
        item.update(updated_data)
        return jsonify({"message": "Registro atualizado com sucesso!"}), 200
    else:
        return jsonify({"message": "Registro não encontrado!"}), 404

@health_insurance_providers_controller.route('/health-insurance-providers/<string:code>', methods=['DELETE'])
def delete(code):
    global response_data
    item_to_delete = next((item for item in response_data if item["ans_registration_code"] == code), None)

    if item_to_delete:
        response_data = [item for item in response_data if item["ans_registration_code"] != code]
        return jsonify({"message": "Registro deletado com sucesso!"}), 200
    else:
        return jsonify({"message": "Registro não encontrado!"}), 404
