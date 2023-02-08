import time
import os

while True:
    time.sleep(1 - time.monotonic() % 1)
    local_zaman = time.localtime()
    time_str = time.strftime("%d/%m/%Y, %H:%M:%S", local_zaman)
    os.system('cls')
    print("Anlık zaman:", time_str)
    
