# For windows
from pynput import keyboard

def on_press(key):
    try:
        k = key.char  # single-char keys
        print(k, end='')
    except:
        w = key.name  # other keys    
        if w == 'enter':
            print('Key pressed: ' + k) 
          
    return True  # stop listener; remove this if want more keys
print('x')
while True:
    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # start to listen on a separate thread
    listener.join()  # remove if main thread is polling self.keys
