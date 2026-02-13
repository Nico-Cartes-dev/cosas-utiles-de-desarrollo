# Utilidades de Base de Datos

Esta carpeta contiene scripts diseñados para facilitar la gestión, población y análisis de datos en bases de datos SQLite (extensible a otros motores). Son herramientas agnósticas diseñadas para integrarse rápidamente en cualquier proyecto.

## 1. Poblador de Datos (`seed_data.py`)

Este script permite insertar cantidades masivas de datos de prueba (dummy data) en una base de datos **existente**. A diferencia de otros seeders, este script no crea la estructura de la base de datos, sino que se adapta a las tablas que ya tienes.

### Características
*   **Conexión Flexible**: Configura fácilmente la ruta a tu archivo `.db`.
*   **Datos Realistas**: Incluye listas predefinidas de nombres, apellidos, calles, marcas, etc., para generar registros que parecen reales.
*   **Totalmente Configurable**: Puedes definir exactamente qué campos llenar y cómo se generan.
*   **Seguro**: Verifica que la tabla destino exista antes de intentar insertar datos.

### Configuración Rápida
Abre el archivo `seed_data.py` y busca la sección de configuración al inicio:

```python
# 1. ¿Qué base de datos quieres llenar?
ARCHIVO_DB = "mi_proyecto.db" 
```

### Personalización
Para adaptar los datos a tu tabla, modifica la función `generar_datos_orden()`:

```python
def generar_datos_orden(estado_forzado=None):
    # ... lógica de generación ...
    return {
        "nombre_columna_db": valor_generado,
        "otra_columna": otro_valor,
        # Asegúrate de que las claves coincidan con tus columnas reales
    }
```

Luego, en la función `main()`, define cuántos registros quieres:

```python
CONFIGURACION = [
    {
        "tabla": "usuarios", # Nombre real de tu tabla
        "cantidad": 500,     # Cantidad de registros a crear
        "generador": generar_datos_usuario # Tu función generadora
    }
]
```

### Uso
```bash
python seed_data.py
```

---

## 2. Analizador de Datos (`contador_de_datos_por_tabla.py`)

Una herramienta de reporte rápido para visualizar la distribución de datos en tus tablas sin necesidad de abrir un cliente SQL complejo. Ideal para verificar si tu seeder funcionó correctamente o para obtener métricas rápidas.

### Características
*   **Reporte Visual**: Muestra barras de progreso ASCII para visualizar porcentajes.
*   **Agrupación Dinámica**: Puedes contar registros agrupados por cualquier columna (ej: Estado, Categoría, Rol, Fecha).
*   **Validación Automática**: Detecta si la base de datos, la tabla o la columna no existen y sugiere correcciones.

### Configuración
Abre el archivo y ajusta las tres variables principales:

```python
DB_NAME = "mi_proyecto.db"      # Archivo de base de datos
TABLA = "ordenes"               # Tabla a analizar
COLUMNA_AGRUPACION = "estado"   # Columna para agrupar el conteo
```

### Ejemplo de Salida
```text
=== REPORTE PARA TABLA: ordenes ===
Base de datos: taller_bicicletas.db
Total de registros: 2000

=== DESGLOSE POR 'estado' ===
 ██████████           Entregado: 1000 (50.0%)
 ███                  En reparación: 339 (17.0%)
 ███                  Pendiente: 336 (16.8%)
 ███                  Listo: 325 (16.2%)
```

### Uso
```bash
python contador_de_datos_por_tabla.py
```
