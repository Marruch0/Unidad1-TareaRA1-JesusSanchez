# main_app.py

# Importar la clase desde el otro archivo (módulo)
from lavadero import Lavadero

def ejecutarSimulacion(lavadero, prelavado, secado_mano, encerado):
    """
    Simula el proceso de lavado para un vehículo con las opciones dadas.
    """
    
    print(f"\n--- INICIO SIMULACIÓN: [Pre: {prelavado}, Sec: {secado_mano}, Cera: {encerado}] ---")
    
    # 1. Iniciar el lavado
    try:
        # CORREGIDO: Usamos _hacer_lavado (con guion bajo)
        lavadero._hacer_lavado(prelavado, secado_mano, encerado)
        
        print("Coche entra. Estado inicial:")
        lavadero.imprimir_estado()

        # 2. Avanza por las fases
        print("\n>>> AVANZANDO FASES:")
        
        pasos = 0
        while lavadero.ocupado and pasos < 20: 
            lavadero.avanzarFase()
            print(f"   -> ", end="")
            lavadero.imprimir_fase()
            print() 
            pasos += 1
        
        print("\n----------------------------------------")
        print("Lavado completo. Estado final:")
        lavadero.imprimir_estado()
        print("----------------------------------------")
        
    except ValueError as e: 
        print(f"❌ ERROR LÓGICO (Regla de negocio): {e}")
    except RuntimeError as e: 
        print(f"❌ ERROR DE ESTADO: {e}")
    except Exception as e:
        print(f"❌ ERROR INESPERADO: {e}")


# Punto de entrada (main)
if __name__ == "__main__":
    
    lavadero_global = Lavadero() 
    
    # EJEMPLO 1: Completo
    ejecutarSimulacion(lavadero_global, prelavado=True, secado_mano=True, encerado=True)
    
    # EJEMPLO 2: Básico
    ejecutarSimulacion(lavadero_global, prelavado=False, secado_mano=False, encerado=False)

    # EJEMPLO 3: Error (Encerado sin secado)
    ejecutarSimulacion(lavadero_global, prelavado=False, secado_mano=False, encerado=True)

    # EJEMPLO 4: Prelavado (CORREGIDO: Faltaba el argumento encerado)
    ejecutarSimulacion(lavadero_global, prelavado=True, secado_mano=False, encerado=False)