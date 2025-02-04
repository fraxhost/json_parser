import sys
from validator import JsonValidator

if __name__ == '__main__' :
    if len(sys.argv) != 2 :
        print('Usage: python main.py <file_path>')
        sys.exit(1)
    
    validator = JsonValidator(sys.argv[1])
    validator.validate()