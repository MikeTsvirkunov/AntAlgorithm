import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
import re
import streamlit as st
import pandas as pd
from io import StringIO
import sys
sys.path.append("../Project")
from Project.Classes.Ant import Ant
from Project.Classes.TrackOfWalk import TrackOfWalk
from random import shuffle
from streamlit_modal import Modal
import streamlit.components.v1 as components

def iteration(ant: Ant,
               pos: iter,
               feromon_map_updater: TrackOfWalk, 
               feromon_map: np.ndarray, 
               distance_map: np.ndarray):
    track = ant.walk(pos=pos, 
                     distance_matrix=distance_map, 
                     feromon_matrix=feromon_map)
    feromon_map = feromon_map_updater.update(track=track, 
                                                feromon_matrix=feromon_map)
    return feromon_map

def Dijkstra(N, S, matrix):
	valid = [True]*N        
	weight = [np.inf]*N
	weight[S] = 0
	way = []
	for i in range(N):
		min_weight = np.inf
		ID_min_weight = -1
		for j in range(N):
			if valid[j] and weight[j] < min_weight:
				min_weight = weight[j]
				ID_min_weight = j
		for z in range(N):
			if weight[ID_min_weight] + matrix[ID_min_weight][z] < weight[z]:
				weight[z] = weight[ID_min_weight] + matrix[ID_min_weight][z]
		valid[ID_min_weight] = False
		way.append(ID_min_weight)
	return weight, way


modal = Modal("Demo Modal", key='streamlit-modal-default')
uploaded_file = st.file_uploader("Choose a file")
findout = st.button("Findout")
iterations = st.text_input('Iterations', 10)
alpha = st.text_input('Alpha', 1)
betha = st.text_input('Betha', 1)
ant_walk_distance = st.text_input('Ant walk distance', 'auto')
n_ants = st.text_input('Num of ants', 'auto')
feromon_volume_set = st.text_input('Feromon volume set', 'auto')
feromon_erosion_set = st.text_input('Feromon erosion speed', 'auto')
global res
res = 0

if findout and uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    dataframe = pd.read_csv(uploaded_file, sep=';')
    num_of_iterations = iterations
    distance_map = dataframe.to_numpy()
    feromon_map = np.random.rand(distance_map.shape[0], distance_map.shape[0])
    n_ants = int(n_ants) if n_ants.isnumeric() else max(distance_map.shape[0]//4, 1)
    ants = [Ant(walk_distance=int(ant_walk_distance) if ant_walk_distance.isnumeric() else distance_map.shape[0]+1, a=alpha, b=betha) for _ in range(0, n_ants)]
    positions = [[i, i] for i in range(0, 100, n_ants)]
    try:
        feromon_erosion_set = float(feromon_erosion_set)
    except ValueError:
          feromon_erosion_set = 0.999
    try:
        feromon_volume_set = float(feromon_volume_set)
    except ValueError:
          feromon_volume_set = distance_map.shape[0]
    feromon_map_updater = TrackOfWalk(feromon_volume=feromon_volume_set, feromon_erosion_speed=1-feromon_erosion_set)
    for _ in range(int(num_of_iterations)):
        for ant, pos in zip(ants, positions):
            feromon_map = iteration(ant, pos, feromon_map_updater, feromon_map, distance_map)
    way = Dijkstra(distance_map.shape[0], 1, feromon_map*(-1))[1]
    way = np.array(list(zip(way[:-2], way[1:]))) 
    st.session_state['res'] = sum([distance_map[i[0], i[1]] for i in way])
    # res = sum([distance_map[i[0], i[1]] for i in way])
    # print(distance_map)
    modal.open()

if modal.is_open():
    with modal.container():
        st.write("Results")
        html_string = '''
        <h2>Results:<h2>
        <h1>''' + str(st.session_state['res']) + '''</h1>

        <script language="javascript">
        document.querySelector("h1").style.color = "green";
        document.querySelector("h1").style.fontStyle = "Source Sans";
        document.querySelector("h2").style.fontStyle = "Source Sans";
        </script>
        '''
        components.html(html_string)

    st.write("Some fancy text")
    value = st.checkbox("Check me")
    st.write(f"Checkbox checked: {value}")