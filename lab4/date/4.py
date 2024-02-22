from datetime import datetime
x=datetime(2024, 2, 21, 18, 0, 0)
y=datetime(2024, 2, 21, 17, 45, 0)

dif=x-y
difsec=dif.total_seconds()
print(difsec)