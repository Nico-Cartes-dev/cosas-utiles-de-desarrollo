# importa tu base de datos
import db
import random
from datetime import datetime, timedelta
# ajusta esta lista a tu caso
# Listas de datos para generar combinaciones aleatorias
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

def generar_fecha_aleatoria():
    dias_atras = random.randint(0, 60)
    fecha = datetime.now() - timedelta(days=dias_atras)
    return fecha.strftime("%Y-%m-%d")

def generar_fecha_entrega(fecha_ingreso_str, estado):
    if estado == "Entregado":
        fecha_ingreso = datetime.strptime(fecha_ingreso_str, "%Y-%m-%d")
        dias_despues = random.randint(1, 7)
        fecha_entrega = fecha_ingreso + timedelta(days=dias_despues)
        # Formato DD/MM/YYYY HH:MM para entregados
        return fecha_entrega.strftime("%d/%m/%Y %H:%M")
    else:
        # Formato YYYY-MM-DD para estimadas
        fecha_ingreso = datetime.strptime(fecha_ingreso_str, "%Y-%m-%d")
        dias_despues = random.randint(2, 5)
        fecha_entrega = fecha_ingreso + timedelta(days=dias_despues)
        return fecha_entrega.strftime("%Y-%m-%d")

def poblar_base_datos(cantidad_activas=1000, cantidad_historial=1000):
    print(f"Generando {cantidad_activas} registros activos y {cantidad_historial} registros históricos...")
    
    # Asegurar que las tablas existan
    db.crear_tablas()
    
    estados_activos = ["Pendiente", "En reparación", "Listo"]
    estados_historial = ["Entregado"]
    
    # Función auxiliar para generar e insertar una orden
    def crear_orden(estado_forzado=None):
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
        
        # Generar servicios aleatorios
        num_servicios = random.randint(1, 3)
        servicios_seleccionados = random.sample(servicios_base, num_servicios)
        
        # Calcular precio
        precio_total = sum(s["precio"] for s in servicios_seleccionados)
        if any(s["nombre"] == "Reparación" for s in servicios_seleccionados):
            precio_total += random.randint(5000, 50000)
            
        direccion = f"{random.choice(calles)} {random.randint(100, 9999)}"
        correo = f"{cliente.lower().replace(' ', '.')}@email.com"
        
        observaciones = ""
        if random.random() > 0.7:
            observaciones = "Cliente solicita revisión extra de frenos"
            
        detalle_orden = ""
        if random.random() > 0.7:
            detalle_orden = "Bicicleta con rayones visibles en cuadro"

        db.insertar_orden(
            cliente=cliente,
            telefono=telefono,
            bicicleta=bicicleta,
            descripcion=f"Servicio de {servicios_seleccionados[0]['nombre']}",
            estado=estado,
            fecha_ingreso=fecha_ingreso,
            precio=precio_total,
            servicios_seleccionados=servicios_seleccionados,
            direccion=direccion,
            correo=correo,
            tipo_telefono="Móvil",
            tipo_bicicleta=tipo_bicicleta,
            marca=marca,
            modelo=modelo,
            color=color,
            observaciones=observaciones,
            detalle_orden=detalle_orden,
            recibido_por="Administrador",
            atendido_por="Mecánico Jefe",
            fecha_entrega=fecha_entrega
        )

    # Generar Activas
    print("Generando órdenes activas...")
    for _ in range(cantidad_activas):
        crear_orden(random.choice(estados_activos))

    # Generar Historial
    print("Generando órdenes históricas...")
    for _ in range(cantidad_historial):
        crear_orden(random.choice(estados_historial))
        
    print("¡Registros insertados correctamente!")

if __name__ == "__main__":
    # cantidad de datos a generar 
    poblar_base_datos(10000,10000)