import os

def verificar_tipo_arquivo(file_path):
    _, ext = os.path.splitext(file_path)
    
    tipos_suportados = {
        '.txt': 'Arquivo de texto',
        '.bmp': 'Imagem BMP'
    }
    
    if ext.lower() in tipos_suportados:
        return tipos_suportados[ext.lower()]
    else:
        raise ValueError(f"Tipo de arquivo não suportado: {ext}")
    
try:
    tipo = verificar_tipo_arquivo("imagem.bmp")
    print(f"Tipo do arquivo: {tipo}")
except ValueError as e:
    print(e)

try:
    tipo = verificar_tipo_arquivo("test.txt")
    print(f"Tipo do arquivo: {tipo}")
except ValueError as e:
    print(e)

try:
    tipo = verificar_tipo_arquivo("trabalhoeconomia.pdf")
    print(f"Tipo do arquivo: {tipo}")
except ValueError as e:
    print(e)


