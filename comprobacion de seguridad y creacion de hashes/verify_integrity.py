import hashlib
import json
import os
import sys

HASH_FILE = 'security/integrity_hashes.json'

def calculate_hash(file_path):
    """Calcula el hash SHA-256 de un archivo."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None
    except Exception as e:
        return None

def verify_integrity():
    """Verifica la integridad de los archivos contra los hashes guardados."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    hash_file_path = os.path.join(base_dir, HASH_FILE)

    if not os.path.exists(hash_file_path):
        print(f"Error: No se encontró el archivo de hashes {HASH_FILE}")
        print("Ejecuta primero 'python security/generate_hashes.py'")
        sys.exit(1)

    with open(hash_file_path, 'r') as f:
        stored_hashes = json.load(f)

    print(f"Verificando integridad de {len(stored_hashes)} archivos...\n")
    
    issues_found = False
    
    for relative_path, stored_hash in stored_hashes.items():
        full_path = os.path.join(base_dir, relative_path)
        current_hash = calculate_hash(full_path)
        
        if current_hash is None:
            print(f"[FALTA] {relative_path} - El archivo no existe o no se puede leer.")
            issues_found = True
        elif current_hash != stored_hash:
            print(f"[MODIFICADO] {relative_path} - El hash no coincide!")
            print(f"  Esperado: {stored_hash}")
            print(f"  Actual:   {current_hash}")
            issues_found = True
        else:
            print(f"[OK] {relative_path}")

    if issues_found:
        print("\n⚠️  ADVERTENCIA: Se encontraron problemas de integridad.")
        sys.exit(1)
    else:
        print("\n✅  INTEGRIDAD VERIFICADA: Todos los archivos coinciden.")
        sys.exit(0)

if __name__ == "__main__":
    verify_integrity()
