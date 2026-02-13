# Cosas Útiles de Desarrollo

Este repositorio contiene una colección de scripts y utilidades prácticas para el desarrollo de software, enfocadas principalmente en Python. Aquí encontrarás herramientas para validación de seguridad, automatización de desarrollo y pruebas de carga para APIs.

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

---
**Nota:** Asegúrate de revisar y ajustar las configuraciones (rutas de archivos, URLs, puertos) dentro de cada script para adaptarlos a tu entorno específico.
