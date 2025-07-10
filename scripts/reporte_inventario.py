import pandas as pd

# Leer el archivo Excel
archivo = "../data/github.xlsx"
df = pd.read_excel(archivo)

# Calcular valores
df["Vr.Parcial"] = df["Cantidad"] * df["Vr. Unitario"]
df["Vr.Parcial con IVA"] = df["Vr.Parcial"] * 1.19

# Guardar nuevo archivo
df.to_excel("../reports/reporte_inventario_rhema.xlsx", index=False)

print("✅ Informe generado con éxito.")
