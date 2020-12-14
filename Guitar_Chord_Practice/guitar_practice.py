from pynput import keyboard
import random
import time

def on_press(key):
    print("You can relax now")
    listener.stop()

chords = ['G', 'A', 'Am', 'E', 'Em', 'D', 'C' , 'B', 'Bm', 'F']

delay = int(input("Enter the delay"))


listener = keyboard.Listener(on_press=on_press)
listener.start()

while listener.is_alive():
    print(random.choice(chords))
    time.sleep(delay)
