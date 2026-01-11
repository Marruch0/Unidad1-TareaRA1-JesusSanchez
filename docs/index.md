# Tarea RA1: Depuración y Pruebas - Lavadero
**Alumno:** (PON TU NOMBRE AQUÍ)
**Curso:** Especialización Ciberseguridad

---

## 1. Elementos de Python y Código Fuente
El código fuente ha sido documentado utilizando **Docstrings** explicativos en cada método y clase, detallando los parámetros, retornos y excepciones. Se ha refactorizado la estructura para cumplir con los principios de encapsulamiento, utilizando métodos protegidos (`_hacer_lavado`) y propiedades (`@property`).

El código fuente completo se encuentra en la carpeta `src/` del repositorio.

---

## 2. Ejecución y Depuración (Apartado 2)
Al ejecutar inicialmente el programa, se detectaron errores de sintaxis (indentación incorrecta) y errores lógicos en las transiciones de estados que impedían la ejecución fluida.

**Captura de la ejecución del programa principal (`main_app.py`):**

![Ejecución Main](main_run.png)
*En la imagen se observa la simulación de un ciclo de lavado completo pasando por las fases correctas tras la corrección.*

---

## 3. Pruebas Unitarias (Apartado 3)
Se ha implementado una batería de **14 tests unitarios** utilizando la librería `unittest` de Python.

### Fase 1: Detección de Errores (Evidencia de Fallos)
Inicialmente, los tests revelaron fallos críticos en la lógica original proporcionada:
- Cálculo incorrecto de precios (se sumaban importes erróneos en secado y encerado).
- Nombres de métodos inconsistentes que impedían la ejecución de los tests.

**Evidencia de Tests Fallidos:**
![Tests Fallidos](tests_fail.png)

### Fase 2: Corrección y Validación (Tests OK)
Tras corregir la lógica en `lavadero.py` (ajuste de precios y transiciones de fase `if/else`) y actualizar el archivo `main_app.py` para usar los métodos correctos, todos los tests pasaron exitosamente.

**Evidencia de Tests Correctos:**
![Tests OK](tests_ok.png)

---

## 4. Ejecución en Sandbox (Apartado 4)
La aplicación se ha ejecutado en un entorno controlado (Visual Studio Code actuando como entorno de desarrollo aislado) sobre Linux. Se ha verificado que el script no requiere permisos de administrador (`sudo`) y opera estrictamente dentro de su ámbito de usuario.

---

## 5. Reflexión sobre Seguridad en Lenguajes (Apartado 5)
Tras analizar las diferencias entre lenguajes como Python frente a C/C++, concluyo:

1.  **Gestión de Memoria (Memory Safety):**
    * **C/C++** requieren gestión manual (`malloc`/`free`). Esto abre la puerta a vulnerabilidades críticas como *Buffer Overflows* o *Use-After-Free*.
    * **Python** es "Memory Safe" por defecto. Su *Garbage Collector* y la gestión automática de límites en arrays evitan que un programador acceda accidentalmente a memoria de otros procesos, eliminando una gran superficie de ataque.

2.  **Tipado:**
    * El tipado dinámico pero fuerte de Python evita errores de interpretación de bits que ocurren en C con el casting de punteros inseguro.

**Conclusión:** En infraestructuras críticas, lenguajes de alto nivel como Python ofrecen una capa de seguridad base que minimiza errores humanos graves, a costa de un menor rendimiento en comparación con C.
