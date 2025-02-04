import re

class JsonValidator:
    def __init__(self, file_path):
        print(file_path)
        self.file_path = file_path

    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            return None
        
    def is_valid_json(self, content):
        pattern = r'^\{(\s*"\w+":\s*"\w+"\s*)*(,\s*"\w+":\s*"\w+"\s*)*\}$'  # Matches a string that starts and ends with curly braces
        return bool(re.match(pattern, content))
    
    def validate(self):
        content = self.read_file()
        isValidJson = self.is_valid_json(content)
        
        if content is None or not isValidJson:
            return False
        
        return True
