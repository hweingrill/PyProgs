from pynput import keyboard
from morse import latin2morse_dict
from morse import txt2morse

# The event listener will be running in this block

with keyboard.Events() as events:
    for event in events:
        print (event.key, ' 1')
        print (event, ' 2')
       
        if event.key == keyboard.Key.esc:
            break
        else:
            pass
#            print(event)
            x=('{}'.format(event))
#            mstring = txt2morse(mstr, latin2morse_dict)    # (Eingabe, Dictionary)
#            print (event)
#       if mstring != ' ':
#            print(mstring)
#            morzei(mstring)
            

            print (x)
             
