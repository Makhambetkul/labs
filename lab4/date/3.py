from datetime import datetime
time = datetime.now()
micro = time.replace(microsecond=0)
print(micro)