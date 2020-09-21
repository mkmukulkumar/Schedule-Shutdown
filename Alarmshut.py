import os 
import time
a= input("Type minutes after which your PC should shutdown:")
time.sleep(int(a)*60)
os.system("shutdown")
input()
