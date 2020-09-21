import os 
import time
input("Type minutes after which your PC should shutdown:")
time.sleep(30*60)
os.system("shutdown /l")
input()
