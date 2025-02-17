"""Primer ejericio de repaso - teoria"""
import os
import pandas as pd  
import datapane as dp  

# se crea un DataFrame a partir del fichero cvs que tenemos que nos
# servirá como origen para los primeros informes
base_path = os.path.dirname(__file__)
csv_path = os.path.join(base_path, "data.csv")
df = pd.read_csv(csv_path)

# continuando, creamos un informe con el componentTable y un DataTable
# a partir del DataFrame que teníamos preparado
# En las dos primeras líneas se crean las 2 tablas de diferentes tipos
# En la tercera se crea un nuevo informe que incluye las 2 tablas
# En la última línea se guarda el informe en un fichero local, 
# indicando además que queremos abrir el informe en un navegador
# con el open=True (lo cual es opcional)
table = dp.Table(df)
data_table = dp.DataTable(df)
report = dp.Report(table, data_table)
report_path = os.path.join(base_path, "informe.html")
report.save(path=report_path, open=True)


