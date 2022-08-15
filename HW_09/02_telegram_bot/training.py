from datetime import datetime


dt = datetime.now()
time = dt.time()
time.strftime('%H:%M:%S')

print("Now it is",time.strftime('%H:%M:%S'))
print("hello")