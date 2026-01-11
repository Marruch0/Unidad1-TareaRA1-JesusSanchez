# Apartado 2: Ejecución y Depuración
Lo primero que hice fue intentar ejecutar el archivo `main_app.py`. El programa no arrancaba. Tuve que usar el depurador de VS Code y la terminal para encontrar los siguientes errores de sintaxis y estructura.

## Lista de Errores Encontrados (Ejecución)

### Error 1: Rutas de Importación (ModuleNotFoundError)
* **El Problema:** Al ejecutar los tests desde la terminal, Python no encontraba el archivo `lavadero.py`.
![Error 1](imagenes/Error1.png)
* **La Causa:** La carpeta de tests no "veía" la carpeta `src` donde estaba el código.
* **Solución:** Tuve que añadir un "parche" en el `sys.path` dentro del archivo de test para que incluyera dinámicamente la ruta de la carpeta superior.

### Error 2: Diferencia de Nombres (AttributeError)
* **El Problema:** El archivo `main_app.py` intentaba llamar a una función `lavadero.hacerLavado()`, pero el programa fallaba diciendo que no existía.
* **La Causa:** Al revisar la clase `Lavadero`, vi que el método estaba definido como protegido: `_hacer_lavado` (con guion bajo).
* **Solución:** Corregí la llamada en el main para usar el nombre correcto: `_hacer_lavado`.

### Error 3: Argumentos Faltantes (TypeError)
* **El Problema:** El Ejemplo 4 del main lanzaba un error inmediato al ejecutarse.
* **La Causa:** Se estaba llamando a la función de lavado pasando solo 2 argumentos, cuando la definición exige 3 (faltaba el booleano de `encerado`).
* **Solución:** Añadí `encerado=False` a esa llamada en el main.

### Error 4: Mayúsculas en Linux (ImportError)
* **El Problema:** El archivo se llamaba `Lavadero.py` (con mayúscula) pero el import buscaba `lavadero`. En Windows funcionaba, pero en Linux fallaba.
* **Solución:** Renombré el archivo a minúsculas `lavadero.py` para seguir las buenas prácticas de Python (PEP8).

---

**Evidencia de ejecución correcta tras las correcciones:**
![Captura del Main funcionando](ejecucion_main.png)
*Ahora el programa ejecuta el ciclo visualmente sin errores.*
