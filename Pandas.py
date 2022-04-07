import pandas as pd

datos = pd.read("fuchero.csv", header=0)
print(datos)
print(datos["cable"])
print (datos.ix[0:3])
print (datos.sort_values(by="Teléfono", ascending=False))
print (datos[datos.ix[:,5]<10])
tel = datos["Teléfono"]
print (tel[tel>30])