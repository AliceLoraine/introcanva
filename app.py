import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("Tablero para dibujo")

with st.sidebar:
  st.subheader("Propiedades del Tablero")
  drawing_mode = st.sidebar.selectbox(
    "Herramienta de Dibujo:",
    ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
  )
  
  stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)
  stroke_color = st.color_picker("Color de trazo", "#FFFFFF")
  fill_hex = st.color_picker("Fill", "#FFFFFF")

  # Convert HEX to RGBA with lower opacity (e.g., 0.5)
def hex_to_rgba(hex_color, alpha=0.5):
    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2 ,4))
    return f"rgba({r}, {g}, {b}, {alpha})"

fill_color_rgba = hex_to_rgba(fill_hex, alpha=0.5)
  
bg_color = '#000000'

# Create a canvas component
canvas_result = st_canvas(
    fill_color = fill_color_rgba,  # Transparent fill
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=300,
    width=500,
    drawing_mode=drawing_mode,
    key="canvas",
)
