# Cálculo de intereses de un CDT

# Entrada de datos
cantidad = float(input("Ingrese la cantidad de dinero invertida: "))
porcentaje_interes = float(input("Ingrese el porcentaje de interés anual (%): "))
periodo = int(input("Ingrese el periodo de tiempo (en días): "))

# Proceso
# Convertir el porcentaje a decimal
tasa = porcentaje_interes / 100

# Calcular los intereses generados
valor_intereses = (cantidad * tasa * periodo) / 360

# Calcular el descuento por retención en la fuente (7%)
retencion = valor_intereses * 0.07

# Calcular el valor total a retirar
total_retirar = cantidad + (valor_intereses - retencion)

# Salida de datos
print("\n--- Resultados ---")
print(f"Intereses generados: ${valor_intereses:.2f}")
print(f"Descuento por retención (7%): ${retencion:.2f}")

print(f"Total a retirar al final del periodo: ${total_retirar:.2f}")
