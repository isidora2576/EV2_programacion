import oracledb
import pandas as pd
import hashlib
import numpy as np
import re
from IPython.display import display
import warnings  # <--- 1. Importamos la librería de advertencias

# <--- 2. Le decimos a Python que ignore el Warning de Pandas
warnings.filterwarnings('ignore')

usuario = "system" # Cambia por tu usuario de Oracle
contrasena = "Dulcee16$" 
dsn_tns = "localhost/xe" # o "localhost:1521/XE"

try: 
    conexion = oracledb.connect(user=usuario, password=contrasena, dsn=dsn_tns)
    print("¡Conexión exitosa a la base de datos Oracle (DataFlow Inc.)!")
except Exception as e:
    print(f"Error al conectar: {e}")

#dataframe de liempeza 

df_cliente = df_clientes = pd.read_sql("SELECT * FROM CLIENTES", con=conexion)
print("--- CLIENTES CON DATOS FALTANTES (Nulos) ---")

# df.isnull().any(axis=1) filtra las filas que tienen al menos un NaN en cualquier columna 

clientes_nulos = df_clientes[df_clientes.isnull().any(axis=1)]
display(clientes_nulos)

#limpieza de datos sensibles 

# 1. Creamos una copia para no alterar el DataFrame original extraído
df_procesado = df_clientes.copy()

print("--- INICIANDO LIMPIEZA Y CIFRADO ÉTICO ---")

def cifrar_sensible(dato):
    """Aplica Hash SHA-256 para cumplir con la ética de privacidad"""
    if pd.isna(dato) or str(dato).strip() == "": 
        return None
    return hashlib.sha256(str(dato).encode('utf-8')).hexdigest()

def limpiar_rut(rut):
    """Deja el RUT solo con números y K, y le agrega el guion correcto"""
    if pd.isna(rut): 
        return None
    # Quitar puntos, guiones y cualquier carácter extraño
    limpio = re.sub(r'[^0-9Kk]', '', str(rut).upper())
    if len(limpio) > 1:
        return f"{limpio[:-1]}-{limpio[-1]}"
    return limpio