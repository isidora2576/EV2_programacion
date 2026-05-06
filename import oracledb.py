import oracledb
import pandas as pd
import hashlib
import numpy as pd
import re
from IPython.display import display

usuario = "system" # Cambia por tu usuario de Oracle
contrasena = "Dulcee16$" 
dsn_tns = "localhost/xe" # o "localhost:1521/XE"

try: 
    conexion = oracledb.connect(user=usuario, password=contrasena, dsn=dsn_tns)
    print("¡Conexión exitosa a la base de datos Oracle (DataFlow Inc.)!")
except Exception as e:
    print(f"Error al conectar: {e}")