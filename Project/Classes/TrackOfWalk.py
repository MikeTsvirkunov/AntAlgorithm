class TrackOfWalk:
    def __init__(self, feromon_volume, feromon_erosion_speed) -> None:
        self.feromon_volume = feromon_volume
        self.feromon_erosion_speed = feromon_erosion_speed
    
    def update(self, track, feromon_matrix):
        L = 0
        for i in range(len(track)):
            L += track[0][2]
            feromon_matrix = self.feromon_erosion_speed * feromon_matrix
            feromon_matrix[track[i][0]][track[i][1]] = feromon_matrix[track[i][0]][track[i][1]] + self.feromon_volume / L
            feromon_matrix[track[i][1]][track[i][0]] = feromon_matrix[track[i][1]][track[i][0]] + self.feromon_volume / L
        return feromon_matrix

