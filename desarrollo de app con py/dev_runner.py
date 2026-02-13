# dev_runner.py
# para correr la app comando abajo
# py dev_runner.py
import subprocess
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

APP_FILE = "main.py"   # cambialo si tu archivo principal tiene otro nombre
# no tocar más allá de esta línea solo chat gpt y yo en un momento sabiamos que haciamos

class RestartOnChange(FileSystemEventHandler):
    def __init__(self):
        self.process = None
        self.start_app()

    def start_app(self):
        if self.process:
            self.process.kill()
        self.process = subprocess.Popen([sys.executable, APP_FILE])

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print("🔄 Cambio detectado → reiniciando app")
            self.start_app()

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(RestartOnChange(), ".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
