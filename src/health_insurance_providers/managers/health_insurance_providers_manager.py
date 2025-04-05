from health_insurance_providers.repository.health_insurance_providers_repository import HealthInsuranceProviderRepository

class HealthInsuranceProviderManager:
    def __init__(self, repository=None):
        self.repository = repository or HealthInsuranceProviderRepository()

    def get_all_providers(self, ans_registration_code, cnpj, fantasyname, page, limit):

        all_providers = self.repository.find_all()
        filtered_providers = []
        
        for provider in all_providers:

            if ans_registration_code and str(provider.get('ans_registration_code', '')).find(ans_registration_code) == -1:
                continue
                
            if cnpj and str(provider.get('cnpj', '')).replace('.', '').replace('/', '').replace('-', '').find(
                cnpj.replace('.', '').replace('/', '').replace('-', '')) == -1:
                continue
                
            if fantasyname and provider.get('fantasyname', '').upper().find(fantasyname) == -1:
                continue
                
            filtered_providers.append(provider)
        
        return  filtered_providers
           
    def get_provider_by_code(self, code):
        return self.repository.find_by_code(code)

    def create_provider(self, new_data):
        return self.repository.create(new_data)

    def update_provider(self, code, updated_data):
        return self.repository.update(code, updated_data)

    def delete_provider(self, code):
        return self.repository.delete(code)