import json
import os

class HealthInsuranceProviderRepository:
    def __init__(self, file_path='/usr/src/workspace/intuitiveweb-api/src/json/Relatorio_cadop.json'):
        self.file_path = file_path

    def _read_data(self):
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _write_data(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def find_all(self):
        return self._read_data()

    def find_by_code(self, code):
        data = self._read_data()
        return next((item for item in data if item["ans_registration_code"] == code), None)

    def create(self, new_data):
        data = self._read_data()
        data.append(new_data)
        self._write_data(data)
        return new_data

    def update(self, code, updated_data):
        data = self._read_data()
        item = next((item for item in data if item["ans_registration_code"] == code), None)
        
        if item:
            item.update(updated_data)
            self._write_data(data)
            return item
        return None

    def delete(self, code):
        data = self._read_data()
        item_to_delete = next((item for item in data if item["ans_registration_code"] == code), None)

        if item_to_delete:
            data = [item for item in data if item["ans_registration_code"] != code]
            self._write_data(data)
            return item_to_delete
        return None