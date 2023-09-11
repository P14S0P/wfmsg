import keyboard
import time

#put your message here
message = ""

while True:
    try:
        time.sleep(3) # <--- time to alt+tab into the game with the chat opened
        keyboard.write(message)
        time.sleep(1) 
        keyboard.press_and_release("enter")
        time.sleep(120) # <--- time to wait until next message on the warframe trading chat
    except KeyboardInterrupt:
        break
keyboard.unhook_all()

