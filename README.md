# Sistema Productor-Consumidor con Semáforos en Python

Este proyecto implementa el clásico problema **Productor-Consumidor** utilizando la **programación concurrente** en **Python** con la ayuda de **semáforos**, hilos (`threading`), y colas (`queue`).

---

## **Descripción del Proyecto**

El código simula un sistema donde:

1. **Productor**: Llena "casilleros" con datos.
2. **Consumidor**: Vacía los "casilleros" llenos.

La idea principal es sincronizar los accesos concurrentes a los casilleros mediante **semáforos** y garantizar que tanto el productor como el consumidor trabajen de manera coordinada y no interfieran entre sí.

### **¿Qué hace el programa?**

- **Produce y consume datos** de manera controlada utilizando **semáforos**.
- Evita que el **Productor** llene más casilleros de los permitidos.
- Evita que el **Consumidor** retire más datos de los que existen.
- Utiliza una **cinta transportadora** simulada mediante una **cola** (`Queue`) para transferir casilleros entre productor y consumidor.

---

## **Tecnologías Utilizadas**

- **Lenguaje**: Python 3  
- **Módulos**:
   - `threading`: Para la creación y sincronización de hilos.
   - `queue`: Para la implementación de la cinta transportadora.
   - `time.sleep`: Para simular el tiempo de espera en producción y consumo.
   - `random`: *(Opcional)* Puede usarse para generar tiempos aleatorios.

---

## **Funcionamiento del Código**

1. **Variables Globales**:
   - `casillerosVacios`: Semáforo para controlar casilleros disponibles.
   - `casillerosLibres`: Semáforo para controlar casilleros llenos.
   - `cinta`: Semáforo para sincronizar acceso a secciones críticas.
   - `Ca_Llenos`, `Tot_Llenos`, `Tot_Vacios`: Contadores globales.

2. **Hilos Principales**:
   - **Productor**:
     - Llena casilleros hasta el límite permitido (9).
     - Se queda en espera si hay demasiados casilleros llenos.
   - **Consumidor**:
     - Vacía casilleros hasta que todos están vacíos.
     - Se queda en espera si no hay casilleros disponibles para vaciar.

3. **Colas**:
   - Se utilizan dos **colas** (`Queue`):
     - Una para **casilleros vacíos**.
     - Otra para **casilleros llenos** (simulación de la cinta transportadora).

4. **Finalización**:
   - El productor y el consumidor se detienen después de procesar un total de **15 casilleros** cada uno.

---

## **Ejecutar el Proyecto**

1. Asegúrate de tener **Python 3** instalado.
2. Guarda el código en un archivo llamado `productor_consumidor.py`.
3. Ejecuta el script desde la terminal:

   ```bash
   python productor_consumidor.py
