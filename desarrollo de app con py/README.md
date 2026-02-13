# Dev Runner - Auto Restart para Desarrollo en Python

Este directorio contiene una herramienta de utilidad llamada `dev_runner.py` diseñada para mejorar tu flujo de trabajo al desarrollar aplicaciones en Python.

## ¿Qué hace este script?

`dev_runner.py` actúa como un "monitor" o "watcher" para tu proyecto. Sus funciones principales son:
1.  **Monitoreo de Archivos:** Vigila constantemente todos los archivos dentro del directorio actual y subdirectorios.
2.  **Detección de Cambios:** Detecta cuando guardas cambios en cualquier archivo con extensión `.py`.
3.  **Reinicio Automático:** Cuando detecta un cambio, detiene automáticamente el proceso de tu aplicación y lo vuelve a iniciar.

Esto es similar a herramientas como `nodemon` en Node.js, permitiéndote ver los cambios reflejados inmediatamente sin tener que detener y reiniciar tu script manualmente una y otra vez.

## Requisitos Previos

Este script depende de la librería `watchdog` para monitorear el sistema de archivos. Debes instalarla antes de usarlo:

```bash
pip install watchdog
```

## Configuración

Antes de ejecutarlo, asegúrate de que el script sepa cuál es el archivo principal de tu aplicación.

1.  Abre `dev_runner.py` en tu editor.
2.  Busca la línea:
    ```python
    APP_FILE = "main.py"
    ```
3.  Cambia `"main.py"` por el nombre de tu archivo principal (ej. `"app.py"`, `"server.py"`, etc.).

## Cómo Usarlo

1.  Abre una terminal en esta carpeta.
2.  Ejecuta el runner:

```bash
python dev_runner.py
```

3.  Verás que tu aplicación se inicia.
4.  Ahora, prueba hacer un cambio en cualquier archivo `.py` de tu proyecto y guárdalo. Verás en la terminal un mensaje como:
    `🔄 Cambio detectado → reiniciando app`

Para detener el runner, simplemente presiona `Ctrl + C` en la terminal.
