import sys

class JsonValidator:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            return None
        
    def is_valid_json(self, content):
        return content == '{}'
    
    def validate(self):
        content = self.read_file()
        isValidJson = self.is_valid_json(content)

        if content is None or not isValidJson:
            print('Invalid JSON')
            sys.exit(1)
        
        print('Valid JSON')
        sys.exit(0)
