import os
from pathlib import Path

def list_directory_structure(startpath, exclude_dirs={'.git', '__pycache__', '.pytest_cache', 'venv'}):
    for root, dirs, files in os.walk(startpath):
        # Remove diretórios que queremos excluir
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        # Calcula o nível de indentação
        level = root.replace(startpath, '').count(os.sep)
        indent = '  ' * level
        
        # Mostra o nome do diretório atual
        folder = os.path.basename(root)
        if level > 0:  # Não mostra o diretório raiz
            print(f'{indent}📁 {folder}')
        
        # Mostra os arquivos
        sub_indent = '  ' * (level + 1)
        for f in files:
            if not f.startswith('.'):  # Ignora arquivos ocultos
                print(f'{sub_indent}📄 {f}')

# Obtém o diretório atual
current_dir = os.getcwd()

print("Estrutura do Projeto:")
print("===================")
list_directory_structure(current_dir)
