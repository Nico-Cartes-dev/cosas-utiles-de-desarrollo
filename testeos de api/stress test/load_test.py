import concurrent.futures
import requests
import time
import random
import sys
# previo a iniciar esto instala requests
# pip install requests
# Configuración del Test
# url local de tu api
BASE_URL = "http://127.0.0.1:5000"
TOTAL_REQUESTS = 30000  # Número total de peticiones a lanzar
CONCURRENT_THREADS = 1  # Número de hilos simultáneos (simulando usuarios)

# cambia a los endpoints de tu api
# # Endpoints a probar (Solo lectura para no llenar la base de datos de basura)
# ENDPOINTS = [
#     "/ordenes",
#     "/historial",
#     "/servicios",
#     "/tipos-bicicleta",
#     "/ordenes?page=1&per_page=100",  # Testear paginación pesada
#     "/ordenes?search=a",             # Testear búsqueda
#     "/ordenes?estado=Pendiente"      # Testear filtros
# ]

def make_request(url):
    """Realiza una petición GET y devuelve el resultado."""
    start_time = time.time()
    try:
        response = requests.get(url, timeout=5)
        elapsed_time = time.time() - start_time
        return response.status_code, elapsed_time
    except requests.RequestException as e:
        return None, 0

def run_load_test():
    print(f"🚀 Iniciando prueba de carga (Stress Test) contra {BASE_URL}")
    print(f"📡 Total Peticiones: {TOTAL_REQUESTS}")
    print(f"🧵 Hilos Simultáneos: {CONCURRENT_THREADS}")
    print("-" * 50)

    # Verificar que el servidor esté arriba antes de empezar
    try:
        requests.get(BASE_URL + "/ordenes", timeout=2)
        print("✅ Servidor detectado online. Comenzando ataque de prueba...")
    except:
        print("❌ Error: No se pudo conectar al servidor. Asegúrate de que el backend esté corriendo (puerto 5000).")
        sys.exit(1)

    start_total = time.time()
    
    results = []
    
    # Usar ThreadPoolExecutor para lanzar peticiones concurrentes
    with concurrent.futures.ThreadPoolExecutor(max_workers=CONCURRENT_THREADS) as executor:
        futures = []
        for _ in range(TOTAL_REQUESTS):
            endpoint = random.choice(ENDPOINTS)
            url = BASE_URL + endpoint
            futures.append(executor.submit(make_request, url))
        
        # Recolectar resultados a medida que completan
        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            status, elapsed = future.result()
            results.append((status, elapsed))
            
            # Mostrar progreso cada 100 peticiones
            if (i + 1) % 100 == 0:
                print(f"   ... {i + 1} peticiones completadas")

    total_time = time.time() - start_total
    
    # Análisis de resultados
    successful = [r for r in results if r[0] == 200]
    failed = [r for r in results if r[0] != 200]
    avg_time = sum(r[1] for r in successful) / len(successful) if successful else 0
    req_per_sec = len(results) / total_time

    print("-" * 50)
    print("📊 RESULTADOS DE LA PRUEBA")
    print("-" * 50)
    print(f"⏱️  Tiempo Total:       {total_time:.2f} segundos")
    print(f"✅  Peticiones Exitosas: {len(successful)}")
    print(f"❌  Peticiones Fallidas: {len(failed)}")
    print(f"⚡  Promedio Latencia:   {avg_time:.4f} segundos")
    print(f"🚀  Rendimiento:         {req_per_sec:.2f} peticiones/segundo")
    print("-" * 50)

    if len(failed) > 0:
        print("⚠️  ADVERTENCIA: Hubo fallos. El servidor podría estar saturado.")
    else:
        print("✅  El servidor soportó la carga correctamente.")

if __name__ == "__main__":
    run_load_test()
