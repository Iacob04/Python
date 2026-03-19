# ============================================================================
# BOLETÍN 4 - EJERCICIO 9
# ============================================================================
# ENUNCIADO:
# La tabla de tarifas impositivas en España para 2022 es la siguiente:
# (Tabla IRPF 2022)
# - Hasta 12.450 €: 19%
# - De 12.450 € a 20.200 €: 24%
# - De 20.200 € a 35.200 €: 30%
# - De 35.200 € a 60.000 €: 37%
# - De 60.000 € a 300.000 €: 45%
# - Más de 300.000 €: 47%
#
# Escribe un programa que le pida al usuario su sueldo anual (puede ser
# un número con decimales) y le informe qué porcentaje de retención le
# corresponde, el importe de la misma y el importe neto restante.
#
# CONCEPTOS CLAVE:
# - Condicionales if-elif-else
# - Cálculo de porcentajes
# - Formateo de moneda
# ============================================================================

print("=" * 50)
print("EJERCICIO 9: Cálculo de retención IRPF 2022")
print("=" * 50)

# Pedir sueldo anual
sueldo = float(input("Introduce tu sueldo anual (€): "))

print("\n" + "-" * 40)

# Determinar el porcentaje de retención según tramos
if sueldo <= 12450:
    porcentaje = 19
elif sueldo <= 20200:
    porcentaje = 24
elif sueldo <= 35200:
    porcentaje = 30
elif sueldo <= 60000:
    porcentaje = 37
elif sueldo <= 300000:
    porcentaje = 45
else:
    porcentaje = 47

# Calcular retención y neto
retencion = sueldo * (porcentaje / 100)
neto = sueldo - retencion

# Mostrar resultados
print("LIQUIDACIÓN IRPF 2022")
print("-" * 40)
print(f"Sueldo bruto anual:     {sueldo:>12,.2f} €")
print(f"Porcentaje retención:   {porcentaje:>12}%")
print(f"Importe retención:      {retencion:>12,.2f} €")
print("-" * 40)
print(f"Sueldo NETO anual:      {neto:>12,.2f} €")
print(f"Sueldo NETO mensual:    {neto/12:>12,.2f} €")
print("=" * 40)

# TABLA DE TRAMOS IRPF 2022:
# --------------------------------------------------------
# | Desde       | Hasta       | Tipo  |
# |-------------|-------------|-------|
# | 0 €         | 12.450 €    | 19%   |
# | 12.450 €    | 20.200 €    | 24%   |
# | 20.200 €    | 35.200 €    | 30%   |
# | 35.200 €    | 60.000 €    | 37%   |
# | 60.000 €    | 300.000 €   | 45%   |
# | 300.000 €   | En adelante | 47%   |
# --------------------------------------------------------

print("\n" + "=" * 50)
print("FIN DEL EJERCICIO")
print("=" * 50)
