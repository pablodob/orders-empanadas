import requests
import os
import sqlite3

os.system("clear")
name = input("Ingrese su nombre: ")
cc = input("Ingrese el numero de empanadas de carne: ")
cjyq = input("Ingrese el numero de empanadas de jamon y queso: ")
ch = input("Ingrese el numero de empanadas de humita: ")

cc = int(cc)
cjyq = int(cjyq)
ch = int(ch)


try:
    r = requests.get("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
except:
    print("El servicio de dolarsi se puede conectar. El programa se detendra.")
    exit()

if (r.status_code == 200):
    print("El servicio de dolarsi ha funcionado correctamente")
else:
    print("El servicio de dolarsi ha tenido un error. El error es el numero " + r.status_code + ". El programa se detendra.")
    exit()

dolar =  r.json()[0]["casa"]["venta"]

dolar = float(dolar.replace(",","."))
total = cc + cjyq + ch

print (str(total))
print ("El precio de cada empanada es de $" + str(dolar))
print ("El numero de empanadas totales es de " + str(total) + " y debe abonar un total de $" + str(dolar*total))

cobro=-1
while (cobro<(dolar*total)):
    cobro = input("Ingrese el monto con el que va a abonar el cliente: ")
    try:
        cobro = float(cobro)
    except:
        print("Debe ingresar un numero flotante")
        cobro = -1

print ("El vuelto del cliente es: $" + str(cobro - dolar*total))

#cargar datos en la bd
conn = sqlite3.connect("data.sqlite")
cursor = conn.cursor()

cursor.execute("INSERT INTO empanadas VALUES (?,?,?,?,?)", (name,cc,cjyq,ch,dolar*total))
conn.commit()
