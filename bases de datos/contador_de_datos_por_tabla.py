import sqlite3
import os
import sys

# ==========================================
# CONFIGURACIÓN
# ==========================================
# Ajusta estos valores según tu proyecto
DB_NAME = "taller_bicicletas.db"  # Nombre de tu base de datos
TABLA = "ordenes"                 # Nombre de la tabla a analizar
COLUMNA_AGRUPACION = "estado"     # Columna por la cual agrupar

def analizar_tabla():
    """
    Conecta a la base de datos y muestra un reporte simple de la tabla configurada.
    """
    # Intentar resolver la ruta de la base de datos
    db_path = os.path.abspath(DB_NAME)
    
    if not os.path.exists(db_path):
        # Intentar buscar en el directorio padre si no está en el actual
        parent_db_path = os.path.join(os.path.dirname(os.getcwd()), DB_NAME)
        if os.path.exists(parent_db_path):
            db_path = parent_db_path
        else:
            print(f"Error: No se encuentra el archivo de base de datos '{DB_NAME}'.")
            print(f"Buscado en: {db_path}")
            print("Asegúrate de ejecutar seed_data.py primero para generar los datos.")
            return

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Verificar tablas disponibles
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tablas_encontradas = [row[0] for row in cursor.fetchall()]
        
        if TABLA not in tablas_encontradas:
            print(f"Error: La tabla '{TABLA}' no existe en la base de datos.")
            print(f"Tablas disponibles: {', '.join(tablas_encontradas) if tablas_encontradas else 'Ninguna'}")
            conn.close()
            return

        # 1. Contar total de registros
        cursor.execute(f"SELECT COUNT(*) FROM {TABLA}")
        total = cursor.fetchone()[0]
        
        print(f"\n=== REPORTE PARA TABLA: {TABLA} ===")
        print(f"Base de datos: {os.path.basename(db_path)}")
        print(f"Total de registros: {total}")

        # 2. Agrupar por la columna seleccionada
        if total > 0:
            print(f"\n=== DESGLOSE POR '{COLUMNA_AGRUPACION}' ===")
            try:
                # Verificar si la columna existe
                cursor.execute(f"PRAGMA table_info({TABLA})")
                columnas = [info[1] for info in cursor.fetchall()]
                
                if COLUMNA_AGRUPACION not in columnas:
                    print(f"Advertencia: La columna '{COLUMNA_AGRUPACION}' no existe en la tabla '{TABLA}'.")
                    print(f"Columnas disponibles: {', '.join(columnas)}")
                else:
                    query = f"SELECT {COLUMNA_AGRUPACION}, COUNT(*) FROM {TABLA} GROUP BY {COLUMNA_AGRUPACION} ORDER BY COUNT(*) DESC"
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    
                    for row in rows:
                        valor = row[0] if row[0] is not None else "Sin definir"
                        cantidad = row[1]
                        porcentaje = (cantidad / total * 100)
                        barra = "█" * int(porcentaje / 5) # Pequeña barra visual
                        print(f" {barra:<20} {valor}: {cantidad} ({porcentaje:.1f}%)")
            except sqlite3.OperationalError as e:
                print(f"Error al agrupar: {e}")
        else:
            print("\nLa tabla está vacía.")

        conn.close()
        
    except sqlite3.Error as e:
        print(f"\nError de base de datos: {e}")
    except Exception as e:
        print(f"\nError inesperado: {e}")

if __name__ == "__main__":
    analizar_tabla()
