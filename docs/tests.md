# Apartado 3: Pruebas Unitarias y Lógica
Una vez conseguí que el código arrancara, creé una batería de **14 tests unitarios** con `unittest` para verificar si el lavadero cobraba bien y hacía los ciclos correctos.

Al principio, **casi todos los tests fallaron**. El código tenía "trampas" o errores lógicos intencionados.

**Estado Inicial (Evidencia de Fallos):**
![Tests en Rojo](fallos_rojos.png)

## Errores Lógicos Detectados y Solucionados

### Error 5: Falta de Métodos de Testeo
* **El Fallo:** Los tests necesitaban comprobar el historial de fases, pero la clase no tenía forma de devolverlo.
* **Solución:** Implementé el método auxiliar `ejecutar_y_obtener_fases` dentro de la clase `Lavadero`, añadiendo un límite de seguridad (`while` con contador) para evitar bucles infinitos.

### Error 6: Precio del Secado a Mano
* **El Fallo:** Al pedir "Secado a mano", el sistema cobraba de más y no cuadraba con los 6.00€ esperados.
* **Solución:** Fui al método `_cobrar` y ajusté el condicional para sumar exactamente **1.00€** (antes sumaba una cantidad errónea).

### Error 7: Precio del Encerado
* **El Fallo:** Ocurría lo mismo con el encerado; el total no llegaba a los 7.20€ estipulados.
* **Solución:** Corregí el coste del extra de encerado a **1.20€** en la lógica de cobro.

### Error 8: Transición Incorrecta (Rodillos -> Secado)
* **El Fallo:** El método `avanzarFase` tenía un error en los `if/else`. Si el cliente pagaba "Secado a mano", el sistema lo ignoraba y lo mandaba a la fase de "Secado automático".
* **Solución:** Modifiqué la condición: si `self.secado_a_mano` es True, fuerza el paso a la fase 7.

### Error 9: El Encerado no se ejecutaba
* **El Fallo:** Al terminar el secado manual, el programa llamaba a `terminar()` directamente, saltándose el encerado aunque el cliente lo hubiera pagado.
* **Solución:** Añadí una comprobación extra: si `self.encerado` es True, pasamos a la fase 8. Solo terminamos si no hay cera contratada.

### Error 10: Validaciones de Negocio
* **El Fallo:** El sistema permitía iniciar un lavado aunque ya hubiera uno en marcha (no lanzaba excepción).
* **Solución:** Aseguré que el método `_hacer_lavado` compruebe `if self.ocupado` y lance un `RuntimeError` antes de aceptar el coche.

---

**Resultado Final (Tests OK):**
Tras aplicar estas correcciones lógicas en `src/lavadero.py`, volví a lanzar los tests.

![Tests en Verde](tests_verdes.png)
*Todos los requisitos funcionales se cumplen ahora.*
