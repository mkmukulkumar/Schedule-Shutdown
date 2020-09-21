import os 
import time
a= input("Type minutes after which your PC should shutdown:")
time.sleep(a*60)
os.system("shutdown /l")
input()
