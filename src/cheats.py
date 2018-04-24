import threading
import src.game as game2
import time

class markBombs(object):
    def __init__(self):
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        while game2.generated:
            cheat = input()
            if cheat == 'xyzzy':
                print("Cheat enabled!")

