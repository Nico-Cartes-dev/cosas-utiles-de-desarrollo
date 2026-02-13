# Comprobación de Seguridad e Integridad de Archivos

Este directorio contiene herramientas esenciales para proteger la integridad de tu código y realizar auditorías de seguridad básicas.

## 🛡️ 1. Sistema de Verificación de Integridad

El objetivo de estos scripts es detectar si algún archivo crítico de tu proyecto ha sido modificado sin autorización o por error (corrupción de datos, ataques, etc.). Funciona generando una "huella digital" (hash SHA-256) de tus archivos y comparándola posteriormente.

### 📋 Paso 1: Configuración Inicial (¡Importante!)

Antes de usar los scripts, debes definir qué archivos son "críticos" para tu proyecto.

1.  Abre el archivo `generate_hashes.py`.
2.  Busca la lista `CRITICAL_FILES` (al principio del archivo).
3.  **Descomenta la lista y añade las rutas relativas de los archivos que quieres monitorear.**
    *   Ejemplo:
        ```python
        CRITICAL_FILES = [
            'main.py',
            'utils/database.py',
            'requirements.txt',
            'env_config.py'
        ]
        ```

### 🚀 Paso 2: Generar la Línea Base

Una vez configurados los archivos, ejecuta este script cuando estés seguro de que tu código está limpio y en una versión estable.

```bash
python generate_hashes.py
```

*   **Resultado**: Se creará un archivo `integrity_hashes.json` (o similar, según configuración) que contiene los hashes originales de tus archivos.

### 🔍 Paso 3: Verificar Integridad

Ejecuta este script periódicamente (por ejemplo, en tu proceso de despliegue o arranque del servidor) para confirmar que nada ha cambiado.

```bash
python verify_integrity.py
```

*   **✅ Todo en orden**: Si los archivos coinciden, el script terminará silenciosamente o con un mensaje de éxito.
*   **⚠️ Alerta**: Si algún archivo ha sido modificado o eliminado, el script mostrará una advertencia y (opcionalmente) detendrá la ejecución.

---

## 🕵️ 2. Auditoría de Seguridad (Bandit)

Bandit es una herramienta diseñada para encontrar problemas de seguridad comunes en código Python.

### Instalación

Para usarla, primero debes instalarla en tu entorno:

```bash
pip install bandit
```

### Cómo realizar un análisis

Ejecuta el siguiente comando desde la raíz de tu proyecto para analizar todos tus archivos recursivamente:

```bash
bandit -r .
```

*   **`-r`**: Indica que el análisis debe ser recursivo (incluir subcarpetas).
*   **`.`**: Indica el directorio actual (puedes cambiarlo por una carpeta específica, ej: `bandit -r ./src`).

Bandit te mostrará un reporte con posibles vulnerabilidades clasificadas por severidad (Baja, Media, Alta). Revisa estos hallazgos para asegurar tu código.
