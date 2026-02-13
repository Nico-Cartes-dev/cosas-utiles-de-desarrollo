# Stress Test - Prueba de Carga para API

Este directorio contiene una herramienta básica pero efectiva para realizar pruebas de carga (stress testing) a tu API. El script principal es `load_test.py`.

## ¿Qué hace este script?

El script `load_test.py` simula múltiples usuarios accediendo a tu API simultáneamente. Su objetivo es:
1.  **Generar tráfico:** Envía una gran cantidad de peticiones HTTP GET a los endpoints que definas.
2.  **Concurrencia:** Utiliza hilos (threads) para realizar peticiones en paralelo, simulando carga real.
3.  **Medir rendimiento:** Calcula métricas clave como el tiempo total, peticiones por segundo y latencia promedio.
4.  **Detectar fallos:** Identifica si el servidor responde con errores (códigos diferentes a 200 OK) o si se cae bajo presión.

## Requisitos Previos

Antes de ejecutar el script, necesitas instalar la librería `requests`:

```bash
pip install requests
```

## Configuración

Para que el script funcione correctamente con **tu** API, debes editar el archivo `load_test.py` y ajustar las siguientes variables al principio del archivo:

1.  **URL de la API (`BASE_URL`)**:
    Cambia la dirección IP y el puerto donde está corriendo tu servidor.
    ```python
    BASE_URL = "http://127.0.0.1:5000"  # Ejemplo: http://localhost:8000
    ```

2.  **Endpoints (`ENDPOINTS`)**:
    **IMPORTANTE:** Debes descomentar y modificar la lista `ENDPOINTS` con las rutas reales de tu API que quieras probar.
    ```python
    ENDPOINTS = [
        "/usuarios",
        "/productos",
        "/ordenes?limit=10",
        # ... añade tus rutas aquí
    ]
    ```

3.  **Intensidad de la Prueba**:
    Ajusta la carga según lo que quieras probar:
    ```python
    TOTAL_REQUESTS = 1000  # Número total de peticiones a enviar
    CONCURRENT_THREADS = 10 # Número de usuarios simultáneos simulados
    ```

## Cómo Ejecutarlo

1.  Asegúrate de que tu API/Backend esté en ejecución.
2.  Abre una terminal en esta carpeta.
3.  Ejecuta el comando:

```bash
python load_test.py
```

## Interpretación de Resultados

Al finalizar, el script te mostrará un resumen como este:

*   **Peticiones Exitosas:** Cuántas devolvieron código 200 OK.
*   **Peticiones Fallidas:** Cuántas fallaron (errores 404, 500, timeouts, etc.).
*   **Promedio Latencia:** Cuánto tardó en promedio responder cada petición.
*   **Rendimiento (req/s):** Cuántas peticiones por segundo pudo manejar tu servidor.

> **Nota:** Si ves muchas peticiones fallidas o el servidor se detiene, significa que has alcanzado el límite de carga actual de tu infraestructura o código.
