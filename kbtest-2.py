import keyboard  # using module keyboard
char=''
k=''
while True:  # making a loop
    k=keyboard.is_pressed
    try:                # used try so that if user pressed other than the
                        # given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            break  # finishing the loop
        else:
            k=key.char
            print(k)
    finally:
        print(char, k)        
#   except:
        break  # if user pressed a key other than the given key the loop will break

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass



