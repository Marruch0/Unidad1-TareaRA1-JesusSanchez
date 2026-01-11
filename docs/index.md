# Tarea RA1: Análisis, Depuración y Pruebas
**Alumno:** (TU NOMBRE AQUÍ)
**Módulo:** Puesta en Producción Segura
**Curso:** Especialización en Ciberseguridad

## Introducción
En esta práctica he trabajado sobre una aplicación Python llamada "Lavadero". El objetivo ha sido analizar un código heredado, documentarlo, corregir sus errores de ejecución y, lo más importante, crear una batería de pruebas unitarias para asegurar que cumple con las reglas de negocio.

El código fuente comentado y corregido se encuentra en la carpeta `src/` de este repositorio.

---

## Reflexión: Seguridad en Lenguajes (Python vs C/C++)
Tras realizar la práctica, he analizado las diferencias de seguridad entre lenguajes de alto nivel (Python) y bajo nivel (C/C++):

### 1. Gestión de Memoria (Memory Safety)
Esta es la diferencia clave que he notado.
* **En C/C++:** La gestión es manual. Si reservo memoria (`malloc`) y se me olvida liberarla, o si intento escribir más datos de los que caben en una variable, provoco un **Buffer Overflow**. Este es el fallo clásico que permite a los atacantes inyectar código.
* **En Python:** Es un lenguaje "Memory Safe". El intérprete se encarga de la memoria (Garbage Collector). Si intento acceder a la posición 10 de una lista de 5 elementos, Python me para con un error (`IndexError`) en lugar de leer memoria de otro proceso. Esto evita una gran superficie de ataque.

### 2. Tipado
* **En C:** El "casting" de punteros permite tratar datos de una forma insegura si no se tiene cuidado.
* **En Python:** El tipado fuerte impide mezclar tipos incompatibles (como sumar texto y números) sin conversión explícita, reduciendo comportamientos inesperados.

**Conclusión:** Python ofrece una capa de seguridad "por defecto" ideal para desarrollos rápidos, mientras que C requiere una vigilancia extrema del programador.
