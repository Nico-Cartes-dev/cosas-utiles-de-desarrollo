import hashlib
import json
import os
# import tanto el readme para ejecutar esto como el archivo integrity_hashes.json

# Archivos críticos para monitorear
# Esto cambia a tu caso, por ejemplo si tienes archivos en otro directorio
# CRITICAL_FILES = [
#     'backend/api.py',
#     'backend/db.py',
#     'electron/main.js',
#     'electron/preload.js',
#     'package.json',
#     'backend/requirements.txt'
# ]

HASH_FILE = 'security/integrity_hashes.json'

def calculate_hash(file_path):
    """Calcula el hash SHA-256 de un archivo."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            # Leer el archivo en bloques de 4K
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"Advertencia: Archivo no encontrado: {file_path}")
        return None
    except Exception as e:
        print(f"Error al leer {file_path}: {e}")
        return None

def generate_hashes():
    """Genera hashes para los archivos críticos y los guarda."""
    hashes = {}
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    print(f"Generando hashes de integridad desde: {base_dir}")
    
    for relative_path in CRITICAL_FILES:
        full_path = os.path.join(base_dir, relative_path)
        file_hash = calculate_hash(full_path)
        if file_hash:
            hashes[relative_path] = file_hash
            print(f"Hash generado para: {relative_path}")
    
    with open(HASH_FILE, 'w') as f:
        json.dump(hashes, f, indent=4)
    
    print(f"\nHashes guardados exitosamente en {HASH_FILE}")

if __name__ == "__main__":
    generate_hashes()
