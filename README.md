# DataFlow Inc. - Sistema de Migración y Procesamiento de Datos (ETL)

Este proyecto forma parte de la **Evaluación Parcial 2** de la asignatura **IDY1101 - Programación para la Ingeniería de Datos**. Consiste en el desarrollo de un pipeline ETL (Extracción, Transformación y Carga) para la empresa DataFlow Inc., migrando datos desde una infraestructura heredada a una base de datos optimizada.

Características del Sistema

- **Procesamiento Masivo:** Gestión y limpieza de más de 5,000 registros de clientes.
- **Validaciones Éticas:** Implementación de cifrado irreversible (SHA-256) para datos sensibles (Teléfono y Email).
- **Reglas de Negocio Dinámicas:** - Estandarización de RUTs chilenos.
  - Normalización de fechas a estándar ISO (YYYY-MM-DD).
  - Limpieza y segmentación de nombres desde formatos CSV complejos.
  - Manejo de valores nulos y registros inconsistentes.
- **Arquitectura Optimizada:** Cumplimiento estricto del límite de 4 componentes clave en la arquitectura.

Arquitectura de la Solución (4 Componentes)

De acuerdo con los requerimientos del proyecto, el sistema se compone de:
1. **Base de Datos Origen (Oracle 21c):** Esquema local que contiene la tabla `CLIENTES` con datos crudos.
2. **Base de Datos Destino (Oracle 21c):** Esquema optimizado con integridad referencial y tipos de datos correctos.
3. **Microservicio de Extracción y Transformación (Python/Pandas):** Lógica encargada de la limpieza y aplicación de reglas éticas.
4. **Microservicio de Carga (Python/Oracledb):** Módulo encargado de la inserción incremental y manejo de errores transaccionales.

## 🛠️ Tecnologías Utilizadas

- **Base de Datos:** Oracle Database 21c (Local).
- **Lenguaje:** Python 3.x.
- **Librerías Clave:**
  - `pandas`: Procesamiento de datos de alto rendimiento.
  - `oracledb`: Driver nativo de comunicación con Oracle.
  - `hashlib`: Aplicación de estándares de seguridad y ética.
  - `re`: Expresiones regulares para limpieza de strings.

## 📋 Requisitos e Instalación

1.  **Configuración de Base de Datos:**
    - Ejecutar el script `IDY1101 INSERTS CLIENTES.sql` para poblar la base de origen.
    - Crear la tabla de destino utilizando el script SQL proporcionado en la documentación.

2.  **Instalación de Dependencias:**
    ```bash
    pip install oracledb pandas
    ```

3.  **Configuración de Conexión:**
    Editar las variables de conexión en el Notebook/Script:
    ```python
    usuario = "tu_usuario"
    password = "tu_password"
    dsn = "localhost/xe"
    ```

Defensa Oral y Estadísticas

El sistema genera automáticamente un reporte de ejecución que debe ser utilizado durante la defensa:
- **Total Leídos:** 5,004 registros.
- **Registros Descartados:** Identificación de nulos críticos.
- **Registros Transformados:** Conteo de datos normalizados.
- **Registros Exitosos:** Confirmación de carga en destino.

Consideraciones Éticas

Bajo los estándares de la industria financiera, este sistema asegura que:
- Los datos de contacto no se almacenan en texto plano (Uso de **SHA-256**).
- Se garantiza la calidad de la información migrada, eliminando ruido que afecte la toma de decisiones.

---
**Curso:** IDY1101 - Programación para la Ingeniería de Datos  
**Institución:** Duoc UC  
**Equipo:** [Nombres de los integrantes]
