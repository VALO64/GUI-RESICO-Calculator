#This file is to set the logic of the program 
#In Mexico there's IVA tax, but this depends of the estado fiscal of each person
#This program will just calculate the RESICO tax 

#ingreso = 0     #This is a variable ingreso or subtotal (in case you're watching the factura)
#ivaCausado = 799.36  #This is a variable Iva causado or Impuestos trasladados (in case you're watching the factura)
#ivaRetenido = 533.00 #This is a variable Iva retenido or Impuestos retenidos (in case you're watching the factura)
#aPagar = ivaCausado - ivaRetenido #aPagar will substract the Iva causado - Iva retenido and will show how much you have to pay
#print(aPagar)

ivaCausado = float(input("Ingrese el IVA causado (impuestos trasladados): "))
ivaRetenido = float(input("Ingrese el IVA retenido (impuestos retenidos): "))
aPagar = ivaCausado - ivaRetenido

if aPagar >= 0:
    print("El IVA a pagar es: ", aPagar)
elif aPagar < 0:
    print("Error")
