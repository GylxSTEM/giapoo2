class CalculaCuenta:
    """
    Representa una cuenta individual para calcular el total
    incluyendo IVA y propina.
    """
    def __init__(self, precio_original):
        # --- Propiedades o Atributos ---
        self.precio_original = precio_original
        self.iva = 0.05  # 5% de IVA
        self.propina = 0.10  # 10% de propina

    def calcula_total(self):
        """
        Calcula el monto total sumando el IVA y la propina
        al precio original.
        """
        # --- Comportamiento o Método ---
        total = self.precio_original * (1 + self.iva + self.propina)
        return total

# --- Gestor Principal (Equivalente al GestorCuenta.java) ---
if __name__ == "__main__":
    
    # Creamos una instancia para la "Persona 1" de la tabla
    # que tenía un consumo de $10000.
    calc_persona1 = CalculaCuenta(10000)

    # Llamamos al método para que haga el cálculo.
    total_persona1 = calc_persona1.calcula_total()

    # Imprimimos el resultado con un formato de moneda.
    # El :.2f en el f-string se asegura de que tenga 2 decimales.
    print(f"El total para la Persona 1 es: ${total_persona1:,.2f}")

    # --- Ejemplo para otra persona ---
    
    # Creamos otra instancia para la "Persona 2" ($12000)
    calc_persona2 = CalculaCuenta(12000)
    total_persona2 = calc_persona2.calcula_total()
    print(f"El total para la Persona 2 es: ${total_persona2:,.2f}")