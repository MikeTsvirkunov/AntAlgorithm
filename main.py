import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas

drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("point", "line")
)

stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
element_color = 'rgba(52, 235, 229, 0.9)'
if drawing_mode == 'point':
    point_display_radius = st.sidebar.slider("Point display radius: ", 1, 25, 3)
if drawing_mode == 'line':
    element_color = 'rgba(0, 0, 0, 0.9)'
# stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
realtime_update = st.sidebar.checkbox("Update in realtime", True)

    

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color='rgba(52, 235, 229, 0.9)' if drawing_mode == 'point' else 'rgba(0, 0, 0, 0.9)',
    background_color=bg_color,
    background_image=None,
    update_streamlit=realtime_update,
    height=150,
    drawing_mode=drawing_mode,
    point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
    key="canvas",
)

if canvas_result.json_data is not None:
    objects = pd.json_normalize(canvas_result.json_data["objects"])
    js = canvas_result.json_data
    for i in js['objects']:
        if (i['type'] == 'circle'):
            i['left'] = 10
    canvas_result.json_data = js
    canvas_result.image_data
    for col in objects.select_dtypes(include=['object']).columns:
        objects[col] = objects[col].astype("str")
    st.dataframe(objects)