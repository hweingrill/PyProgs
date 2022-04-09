import pynput 
from pynput.keyboard import Key, Listener 
   
keys = [] 
char=" "  
def on_press(key): 
    global char 
    keys.append(key)

#    print(keys, 'zeile 9')
#    write_file(keys) 
      
    try:
#        keys +=('key {0}'.format(key.char))
        char +=({0}.format(key.char))
#        char.append(x)
#        print(keys)
#        char +=x
#        print(char, end='')

    except AttributeError: 
#        print('special key {0} pressed'.format(key))
    
        pass
           
def write_file(keys): 
      
    with open('log.txt', 'w') as f: 
        for key in keys:               
            k = str(key).replace("'", "") 
            f.write(k)                                 
            f.write(' ')  
               
def on_release(key): 
                      
#    print('{0} released'.format(key)) 
    if key == Key.enter: 
        
        return False
    
with Listener(on_press = on_press, 
              on_release = on_release) as listener: 
                      
    listener.join()
    
print('keys= ', keys,)
print('char= ', char)
