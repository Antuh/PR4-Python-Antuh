from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Observation(FileSystemEventHandler):
    def on_modified(self, event):
           with open("file.txt", "r", encoding='utf8') as file:
                print(file.readlines()[-1])
observer = Observer()
observer.schedule(Observation(), path="D:\\Programmirovanie\\PR4. Python")
observer.start()
try:
    while 1:
        pass
except KeyboardInterrupt:
    observer.stop()
    print("Наблюдение было завершено")