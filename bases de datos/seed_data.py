import random
from datetime import datetime, timedelta
import sqlite3
import os

# ==========================================
# CONFIGURACIÓN PRINCIPAL
# ==========================================
# 1. ¿Qué base de datos quieres llenar?
# Escribe aquí la ruta de tu archivo .db (ej: "mi_proyecto.db")
ARCHIVO_DB = "taller_bicicletas.db" 

# ==========================================
# 1. LISTAS DE DATOS (CONFIGURACIÓN)
# ==========================================
# Estas listas se usan para generar datos aleatorios.
# Puedes modificarlas según las necesidades de tu proyecto.

nombres = ["Juan", "Maria", "Pedro", "Ana", "Luis", "Carmen", "Jose", "Laura", "Carlos", "Sofia", "Miguel", "Elena", "Javier", "Isabel", "David"]
apellidos = ["Perez", "Gonzalez", "Rodriguez", "Lopez", "Martinez", "Sanchez", "Fernandez", "Gomez", "Diaz", "Torres", "Ramirez", "Flores"]
calles = ["Av. Siempre Viva", "Calle Falsa", "Pasaje Los Olmos", "Av. Libertador", "Calle Central", "Los Aromos", "Las Lilas"]
marcas = ["Trek", "Giant", "Specialized", "Oxford", "Cannondale", "Bianchi", "Scott", "Santa Cruz", "Merida"]
modelos = ["X-Caliber", "Talon", "Rockhopper", "Marlin", "Aspect", "Scale", "Spark", "Epic", "Stumpjumper"]
colores = ["Rojo", "Azul", "Negro", "Verde", "Blanco", "Gris", "Naranja", "Amarillo", "Plateado"]
tipos = ["MTB", "Ruta", "Gravel", "Urbana"]
estados = ["Pendiente", "En reparación", "Listo", "Entregado"]
servicios_base = [
    {"nombre": "Mantención", "precio": 30000},
    {"nombre": "Reparación", "precio": 0}, # Precio variable
    {"nombre": "Ajuste frenos", "precio": 15000, "esOtro": True},
    {"nombre": "Cambio cadena", "precio": 12000, "esOtro": True},
    {"nombre": "Centrado rueda", "precio": 10000, "esOtro": True}
]

# ==========================================
# 2. CLASE GESTOR DE BASE DE DATOS
# ==========================================
class DatabaseManager:
    """
    Clase genérica para manejar la conexión y operaciones con la base de datos.
    Se conecta a una base de datos EXISTENTE.
    """
    def __init__(self, db_path):
        # Verificar que el archivo exista
        if not os.path.exists(db_path):
            raise FileNotFoundError(f"No se encontró el archivo de base de datos: {db_path}\nAsegúrate de que la ruta en 'ARCHIVO_DB' sea correcta.")

        # CAMBIAR AQUÍ PARA OTROS MOTORES (ej. psycopg2 para PostgreSQL)
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        
        print(f"Conectado exitosamente a: {db_path}")

    def verificar_tabla(self, tabla):
        """Verifica si la tabla existe en la base de datos."""
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (tabla,))
        if not self.cursor.fetchone():
            raise ValueError(f"La tabla '{tabla}' no existe en la base de datos. Debes crearla primero.")

    def insertar(self, tabla, datos):
        """
        Inserta un diccionario de datos en la tabla especificada.
        Genera la sentencia SQL dinámicamente.
        """
        columnas = ", ".join(datos.keys())
        placeholders = ", ".join(["?" for _ in datos]) # Usar %s para PostgreSQL
        valores = list(datos.values())
        
        query = f"INSERT INTO {tabla} ({columnas}) VALUES ({placeholders})"
        try:
            self.cursor.execute(query, valores)
        except Exception as e:
            print(f"Error insertando en {tabla}: {e}")

    def guardar_cambios(self):
        self.conn.commit()

    def cerrar(self):
        self.conn.close()

# ==========================================
# 3. FUNCIONES AUXILIARES
# ==========================================
def generar_fecha_aleatoria():
    dias_atras = random.randint(0, 60)
    fecha = datetime.now() - timedelta(days=dias_atras)
    return fecha.strftime("%Y-%m-%d")

def generar_fecha_entrega(fecha_ingreso_str, estado):
    fecha_ingreso = datetime.strptime(fecha_ingreso_str, "%Y-%m-%d")
    if estado == "Entregado":
        dias_despues = random.randint(1, 7)
        return (fecha_ingreso + timedelta(days=dias_despues)).strftime("%d/%m/%Y %H:%M")
    else:
        dias_despues = random.randint(2, 5)
        return (fecha_ingreso + timedelta(days=dias_despues)).strftime("%Y-%m-%d")

# ==========================================
# 4. GENERADORES DE DATOS (PERSONALIZABLE)
# ==========================================
def generar_datos_orden(estado_forzado=None):
    """
    Genera un diccionario con los datos para una fila.
    IMPORTANTE: Las claves del diccionario (ej: "cliente", "telefono") 
    DEBEN coincidir con los nombres de las columnas en tu base de datos.
    """
    cliente = f"{random.choice(nombres)} {random.choice(apellidos)}"
    telefono = "+569" + "".join([str(random.randint(0, 9)) for _ in range(8)])
    
    tipo_bicicleta = random.choice(tipos)
    marca = random.choice(marcas)
    modelo = random.choice(modelos)
    color = random.choice(colores)
    bicicleta = f"{tipo_bicicleta} {marca} {modelo}"
    
    estado = estado_forzado if estado_forzado else random.choice(estados)
    fecha_ingreso = generar_fecha_aleatoria()
    fecha_entrega = generar_fecha_entrega(fecha_ingreso, estado)
    
    # Lógica de servicios y precio
    num_servicios = random.randint(1, 3)
    servicios_seleccionados = random.sample(servicios_base, num_servicios)
    
    precio_total = sum(s["precio"] for s in servicios_seleccionados)
    if any(s["nombre"] == "Reparación" for s in servicios_seleccionados):
        precio_total += random.randint(5000, 50000)
        
    direccion = f"{random.choice(calles)} {random.randint(100, 9999)}"
    correo = f"{cliente.lower().replace(' ', '.')}@email.com"
    
    observaciones = "Cliente solicita revisión extra de frenos" if random.random() > 0.7 else ""
    
    # Retornar diccionario con claves iguales a las columnas de la BD
    return {
        "cliente": cliente,
        "telefono": telefono,
        "bicicleta": bicicleta,
        "descripcion": f"Servicio de {servicios_seleccionados[0]['nombre']}",
        "estado": estado,
        "fecha_ingreso": fecha_ingreso,
        "precio": precio_total,
        "direccion": direccion,
        "correo": correo,
        "tipo_bicicleta": tipo_bicicleta,
        "marca": marca,
        "modelo": modelo,
        "color": color,
        "observaciones": observaciones,
        "fecha_entrega": fecha_entrega
    }

# ==========================================
# 5. EJECUCIÓN PRINCIPAL
# ==========================================
def main():
    # Configuración de qué generar
    CONFIGURACION = [
        {
            "tabla": "ordenes", # Nombre de la tabla existente en tu DB
            # cantidad de datos a generar
            "cantidad": 1000,
            "generador": lambda: generar_datos_orden(estado_forzado=random.choice(["Pendiente", "En reparación", "Listo"]))
        },
        {
            "tabla": "ordenes", 
            # cantidad de datos a generar
            "cantidad": 1000,
            "generador": lambda: generar_datos_orden(estado_forzado="Entregado")
        }
    ]

    print("Iniciando generación de datos...")
    
    try:
        # Inicializar conexión a base de datos existente
        db = DatabaseManager(ARCHIVO_DB)
        
        total_registros = 0
        for config in CONFIGURACION:
            tabla = config["tabla"]
            cantidad = config["cantidad"]
            generador = config["generador"]
            
            # Verificar que la tabla exista antes de empezar
            db.verificar_tabla(tabla)
            
            print(f"Generando {cantidad} registros para '{tabla}'...")
            
            for _ in range(cantidad):
                datos = generador()
                db.insertar(tabla, datos)
                total_registros += 1
                
            print(f"  -> Completado lote para '{tabla}'")
            
        db.guardar_cambios()
        print(f"\n¡Éxito! Se insertaron {total_registros} registros en total en '{ARCHIVO_DB}'.")
        
    except FileNotFoundError as e:
        print(f"\nERROR DE ARCHIVO: {e}")
    except ValueError as e:
        print(f"\nERROR DE TABLA: {e}")
    except Exception as e:
        print(f"\nError durante la ejecución: {e}")
    finally:
        if 'db' in locals():
            db.cerrar()

if __name__ == "__main__":
    main()
