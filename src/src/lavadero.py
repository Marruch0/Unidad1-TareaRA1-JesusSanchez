# lavadero.py

class Lavadero:
    """
    Clase Lavadero:
    Simula el estado y las operaciones de un túnel de lavado de coches.
    Gestiona las transiciones de estados, ingresos y reglas de negocio.
    """

    # Fases del ciclo de lavado
    FASE_INACTIVO = 0
    FASE_COBRANDO = 1
    FASE_PRELAVADO_MANO = 2
    FASE_ECHANDO_AGUA = 3
    FASE_ENJABONANDO = 4
    FASE_RODILLOS = 5
    FASE_SECADO_AUTOMATICO = 6
    FASE_SECADO_MANO = 7
    FASE_ENCERADO = 8

    def __init__(self):
        self.__ingresos = 0.0
        self.__fase = self.FASE_INACTIVO
        self.__ocupado = False
        self.__prelavado_a_mano = False
        self.__secado_a_mano = False
        self.__encerado = False
        self.terminar() 

    # Propiedades
    @property
    def fase(self): return self.__fase

    @property
    def ingresos(self): return self.__ingresos

    @property
    def ocupado(self): return self.__ocupado
    
    @property
    def prelavado_a_mano(self): return self.__prelavado_a_mano

    @property
    def secado_a_mano(self): return self.__secado_a_mano

    @property
    def encerado(self): return self.__encerado

    def terminar(self):
        """Resetea el estado del lavadero a INACTIVO."""
        self.__fase = self.FASE_INACTIVO
        self.__ocupado = False
        self.__prelavado_a_mano = False
        self.__secado_a_mano = False
        self.__encerado = False
    
    def _hacer_lavado(self, prelavado_a_mano, secado_a_mano, encerado):
        """
        Configura un nuevo lavado. 
        Nota: Se llama con guion bajo (_) porque es interno.
        """
        if self.__ocupado:
            raise RuntimeError("No se puede iniciar un nuevo lavado mientras el lavadero está ocupado")
        
        if not secado_a_mano and encerado:
            raise ValueError("No se puede encerar el coche sin secado a mano")
        
        self.__fase = self.FASE_INACTIVO  
        self.__ocupado = True
        self.__prelavado_a_mano = prelavado_a_mano
        self.__secado_a_mano = secado_a_mano
        self.__encerado = encerado

    def _cobrar(self):
        """Calcula el precio y lo suma a los ingresos."""
        coste_lavado = 5.00 # Base
        
        if self.__prelavado_a_mano:
            coste_lavado += 1.50 
        
        if self.__secado_a_mano:
            coste_lavado += 1.00 # CORREGIDO (Antes 1.20)
            
        if self.__encerado:
            coste_lavado += 1.20 # CORREGIDO (Antes 1.00)
            
        self.__ingresos += coste_lavado
        return coste_lavado

    def avanzarFase(self):
        """Avanza el estado del túnel dependiendo de la configuración."""
        if not self.__ocupado:
            return

        if self.__fase == self.FASE_INACTIVO:
            coste = self._cobrar()
            self.__fase = self.FASE_COBRANDO
            print(f" (Cobrado: {coste:.2f}€) ", end="")

        elif self.__fase == self.FASE_COBRANDO:
            if self.__prelavado_a_mano:
                self.__fase = self.FASE_PRELAVADO_MANO
            else:
                self.__fase = self.FASE_ECHANDO_AGUA 
        
        elif self.__fase == self.FASE_PRELAVADO_MANO:
            self.__fase = self.FASE_ECHANDO_AGUA
        
        elif self.__fase == self.FASE_ECHANDO_AGUA:
            self.__fase = self.FASE_ENJABONANDO

        elif self.__fase == self.FASE_ENJABONANDO:
            self.__fase = self.FASE_RODILLOS
        
        elif self.__fase == self.FASE_RODILLOS:
            if self.__secado_a_mano:
                self.__fase = self.FASE_SECADO_MANO # CORREGIDO
            else:
                self.__fase = self.FASE_SECADO_AUTOMATICO # CORREGIDO
        
        elif self.__fase == self.FASE_SECADO_AUTOMATICO:
            self.terminar()
        
        elif self.__fase == self.FASE_SECADO_MANO:
            if self.__encerado:
                self.__fase = self.FASE_ENCERADO # CORREGIDO
            else:
                self.terminar() 
        
        elif self.__fase == self.FASE_ENCERADO:
            self.terminar() 
        
        else:
            raise RuntimeError(f"Fase no válida: {self.__fase}")

    def imprimir_fase(self):
        """Imprime la fase actual."""
        print(f"Fase {self.__fase}", end="")

    def imprimir_estado(self):
        """Imprime el estado completo."""
        print(f"Ingresos: {self.ingresos} | Ocupado: {self.ocupado} | Fase: {self.fase}")

    # --- MÉTODO NECESARIO PARA LOS TESTS ---
    def ejecutar_y_obtener_fases(self, prelavado, secado, encerado):
        """Ejecuta el ciclo completo y devuelve la lista de fases."""
        self._hacer_lavado(prelavado, secado, encerado)
        fases = [self.fase]
        while self.ocupado:
            if len(fases) > 15: return fases # Evitar bucle infinito
            self.avanzarFase()
            fases.append(self.fase)
        return fases