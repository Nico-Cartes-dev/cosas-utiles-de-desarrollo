# Cosas Útiles de Desarrollo

Este repositorio contiene una colección de scripts y utilidades prácticas para el desarrollo de software, enfocadas principalmente en Python. Aquí encontrarás herramientas para validación de seguridad, automatización de desarrollo, pruebas de carga y gestión de bases de datos.

## Contenido

### 1. Comprobación de Seguridad y Creación de Hashes
Ubicación: `comprobacion de seguridad y creacion de hashes/`

Conjunto de scripts para asegurar la integridad de los archivos críticos de tu proyecto mediante hashes SHA-256.

*   **`generate_hashes.py`**: Genera una "huella digital" (hash) de los archivos especificados como críticos y los guarda en un archivo JSON.
*   **`verify_integrity.py`**: Verifica que los archivos no hayan sido modificados comparando su estado actual con los hashes guardados previamente. Útil para detectar cambios no autorizados o corrupciones.

**Uso:**
```bash
# Generar hashes
python "comprobacion de seguridad y creacion de hashes/generate_hashes.py"

# Verificar integridad
python "comprobacion de seguridad y creacion de hashes/verify_integrity.py"
```

### 2. Automatización de Desarrollo (Dev Runner)
Ubicación: `desarrollo de app con py/`

*   **`dev_runner.py`**: Una utilidad que monitorea cambios en tus archivos `.py` y reinicia automáticamente tu aplicación. Es ideal para el desarrollo local, evitando tener que detener y reiniciar el servidor manualmente tras cada cambio.

**Requisitos:**
```bash
pip install watchdog
```

**Uso:**
Edita la variable `APP_FILE` en el script para apuntar a tu archivo principal y ejecuta:
```bash
python "desarrollo de app con py/dev_runner.py"
```

### 3. Testeos de API (Stress Test)
Ubicación: `testeos de api/stress test/`

*   **`load_test.py`**: Script para realizar pruebas de carga (stress testing) contra una API HTTP. Permite simular múltiples peticiones concurrentes para evaluar el rendimiento y la estabilidad del servidor.

**Características:**
*   Configuración de número total de peticiones e hilos concurrentes.
*   Reporte detallado de latencia, peticiones por segundo y tasa de éxito/error.

**Requisitos:**
```bash
pip install requests
```

**Uso:**
Configura la `BASE_URL` y los `ENDPOINTS` dentro del script y ejecuta:
```bash
python "testeos de api/stress test/load_test.py"
```

### 4. Utilidades para Bases de Datos
Ubicación: `bases de datos/`

Herramientas para poblar y analizar bases de datos SQLite de manera rápida y sencilla. Son completamente configurables y agnósticas al proyecto.

*   **`seed_data.py`**: Poblador de bases de datos (Seeder) genérico.
    *   Permite generar miles de registros aleatorios para probar tu aplicación.
    *   Configurable: Define tu archivo `.db`, la estructura de datos y la cantidad de registros.
    *   No crea tablas, solo las llena (ideal para probar sobre una estructura existente).

*   **`contador_de_datos_por_tabla.py`**: Analizador de datos simple.
    *   Genera un reporte visual en consola sobre la distribución de datos en una tabla específica.
    *   Agrupa por columnas (ej: ver cuántos usuarios hay por "estado" o "rol").
    *   Muestra porcentajes y barras gráficas simples.

**Uso:**
1.  Configura las variables al inicio de cada archivo (`ARCHIVO_DB`, `TABLA`, etc.).
2.  Ejecuta:
```bash
# Para llenar la base de datos
python "bases de datos/seed_data.py"

# Para analizar los datos
python "bases de datos/contador_de_datos_por_tabla.py"
```

---
**Nota:** Asegúrate de revisar y ajustar las configuraciones (rutas de archivos, URLs, puertos) dentro de cada script para adaptarlos a tu entorno específico.
