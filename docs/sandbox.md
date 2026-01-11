# Apartado 4: Ejecución en Entorno Controlado (Sandbox)

Para esta práctica, he utilizado **Visual Studio Code** ejecutándose sobre un sistema Linux. He considerado esto como mi entorno "Sandbox" por las siguientes razones:

1.  **Espacio de Usuario:** He ejecutado todos los scripts (`python main_app.py`) con mi usuario estándar, sin utilizar permisos de administrador (`sudo`). Esto garantiza que, si el código tuviera un error grave que intentara borrar archivos del sistema, el sistema operativo lo bloquearía por falta de permisos.
2.  **Entorno Virtual:** Aunque para esta tarea simple no era obligatorio, Python permite usar `venv` para aislar las librerías de este proyecto de las del resto del sistema.

He verificado que el programa puede escribir en su propia carpeta (logs, etc.) pero no tiene acceso a modificar configuraciones del sistema operativo, cumpliendo el principio de mínimo privilegio.
