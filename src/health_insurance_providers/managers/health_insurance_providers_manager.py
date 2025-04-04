from health_insurance_providers.repository.health_insurance_providers_repository import HealthInsuranceProviderRepository

class HealthInsuranceProviderManager:
    def __init__(self, repository=None):
        self.repository = repository or HealthInsuranceProviderRepository()

    def get_all_providers(self):
        return self.repository.find_all()

    def get_provider_by_code(self, code):
        return self.repository.find_by_code(code)

    def create_provider(self, new_data):
        return self.repository.create(new_data)

    def update_provider(self, code, updated_data):
        return self.repository.update(code, updated_data)

    def delete_provider(self, code):
        return self.repository.delete(code)