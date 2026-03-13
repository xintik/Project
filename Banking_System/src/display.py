import ast
from config import CONFIG

def print_transactions(file_path, headers):
    try:
        with open(file_path, "r") as f:
            data = [ast.literal_eval(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        print("No data found.")
        return
    
    if not data:
        print("No records available.")
        return
    
    print(" | ".join(headers))
    print("-" * 50)
    for i, row in enumerate(data, 1):
        print(i, row)