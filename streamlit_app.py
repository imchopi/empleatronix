import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
df = pd.read_csv("./dataset/employees_df.csv")

# Título y descripción de la aplicación
st.title("EMPLEATRONIX")
st.write("Todos los datos sobre los empleados en una aplicación")

# Mostrar el DataFrame
st.write(df)

# Línea de separación
st.markdown("---")

# Crear tres columnas para que las opciones estén alineadas horizontalmente
col1, col2, col3 = st.columns(3)

with col1:
    # Elegir color para las barras
    color = st.color_picker("Elige un color para las barras", "#1f77b4")

with col2:
    # Mostrar nombres en el eje Y
    show_names = st.toggle("Mostrar el nombre", value=True)

with col3:
    # Mostrar el sueldo en la barra
    show_salary = st.toggle("Mostrar sueldo en la barra", value=True)

# Crear la gráfica con un tamaño ajustado y mayor resolución
fig, ax = plt.subplots(figsize=(14, 12), dpi=200)  # Aumentar la resolución con dpi=200

# Ajustar el límite máximo del eje X
ax.set_xlim(0, 4500)  # El valor máximo del eje X se fija en 4500

# Crear barras horizontales
ax.barh(df['full name'], df['salary'], color=color)

# Mostrar nombres si se selecciona
if show_names:
    ax.set_yticklabels(df['full name'], fontsize=25)  # Aumentar tamaño de fuente de las etiquetas del eje Y
else:
    ax.set_yticklabels([])  # Si no está activado, ocultar los nombres

# Mostrar sueldo en las barras si se selecciona
if show_salary:
    for index, value in enumerate(df['salary']):
        ax.text(value + 100, index, f"{value}€", va='center', ha='left', fontsize=22)  # Aumentar tamaño de la fuente de los valores del sueldo

# Aumentar tamaño de las etiquetas de los ejes
ax.tick_params(axis='x', labelsize=22)  # Aumentar tamaño de los valores del eje X (salario)
ax.tick_params(axis='y', labelsize=22)  # Aumentar tamaño de los valores del eje Y (empleado)

# Muestra la gráfica
st.pyplot(fig)

# Agregar el texto de copyright debajo de la gráfica
st.markdown("© Adrián Perogil Fernández - CPIFP Alan Turing")
