class Ant:
    def __init__(self, walk_distance, a, b) -> None:
        self.walk_distance = walk_distance
        self.a = a
        self.b = b
    
    def walk(self, pos, distance_matrix, feromon_matrix):
        way = list()
        for _ in range(self.walk_distance):
            res = max([(pos[0], j, distance_matrix[pos[0]][j], feromon_matrix[pos[0]][j]) 
                       for j in range(distance_matrix.shape[0]) 
                       if j != pos[1]], 
                      key=lambda a: a[2] * a[3])
            pos = res[0:2][::-1]
            way.append(res)
        return way

