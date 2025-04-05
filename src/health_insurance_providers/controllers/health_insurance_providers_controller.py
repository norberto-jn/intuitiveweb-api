from flask import Blueprint, request, jsonify
from health_insurance_providers.managers.health_insurance_providers_manager import HealthInsuranceProviderManager

health_insurance_providers_controller = Blueprint('health-insurance-providers', __name__)
manager = HealthInsuranceProviderManager()

@health_insurance_providers_controller.route('/health-insurance-providers/search', methods=['GET'])
def get_all_providers():
    ans_registration_code = request.args.get('ans_registration_code', '').strip()
    cnpj = request.args.get('cnpj', '').strip()
    fantasyname = request.args.get('fantasyname', '').strip().upper()
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    
    result = manager.get_all_providers(
        ans_registration_code=ans_registration_code,
        cnpj=cnpj,
        fantasyname=fantasyname,
        page=page,
        limit=limit
    )
    
    return jsonify(result)

@health_insurance_providers_controller.route('/health-insurance-providers/<string:code>', methods=['GET'])
def find_one(code):
    provider = manager.get_provider_by_code(code)
    if provider:
        return jsonify(provider)
    else:
        return jsonify({"message": "Registro não encontrado!"}), 404

@health_insurance_providers_controller.route('/health-insurance-providers', methods=['POST'])
def create():
    new_data = request.get_json()
    
    if manager.get_provider_by_code(new_data["ans_registration_code"]):
        return jsonify({"message": "Código de registro já existe!"}), 400
    
    created_data = manager.create_provider(new_data)
    return jsonify({"message": "Registro criado com sucesso!", "data": created_data}), 201

@health_insurance_providers_controller.route('/health-insurance-providers/<string:code>', methods=['PUT'])
def update(code):
    updated_data = request.get_json()
    updated_item = manager.update_provider(code, updated_data)
    
    if updated_item:
        return jsonify({"message": "Registro atualizado com sucesso!", "data": updated_item}), 200
    else:
        return jsonify({"message": "Registro não encontrado!"}), 404

@health_insurance_providers_controller.route('/health-insurance-providers/<string:code>', methods=['DELETE'])
def delete(code):
    deleted_item = manager.delete_provider(code)
    
    if deleted_item:
        return jsonify({"message": "Registro deletado com sucesso!"}), 200
    else:
        return jsonify({"message": "Registro não encontrado!"}), 404