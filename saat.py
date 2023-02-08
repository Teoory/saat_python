import time
import os

while True:
    time.sleep(1 - time.monotonic() % 1)
    named_tuple = time.localtime()
    time_string = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
    os.system('cls')
    print("Anlık zaman:", time_string)
    
