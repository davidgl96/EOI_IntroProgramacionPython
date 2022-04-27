from datetime import datetime #el from es para optimizar
datenow1 = datetime.now().date()
print("fecha:",datenow1)
datenow2 = datetime.now()
print("Fecha:",datenow2)
print("Año:",datenow2.year)
print("Mes:",datenow2.month)
print("Dia:",datenow2.day)
print(f"Hora: {datenow2.hour}:{datenow2.minute}")

fecha = "10-11-2022"
obj = datetime.strptime(fecha, '%m-%d-%Y').date()
print(obj)
print(f"{obj.day}-{obj.month}-{obj.year}") #f es para concatenar todo