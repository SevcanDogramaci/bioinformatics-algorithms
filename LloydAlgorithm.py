
from math import sqrt
from random import randrange

# constant definitions
COMPARISON_THRESHOLD = 0.00001
MATRIX_DIM = 10
K = 3


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def find_distance_to(self, other_point):
        squared_distance = (self.x - other_point.x)**2 + (self.y - other_point.y)**2
        return sqrt(squared_distance)
    
    def __repr__(self):
        return f"Point x={self.x} y={self.y}"
    
    def __value_eq(self, self_value, other_value):
        return abs(self_value - other_value) < COMPARISON_THRESHOLD
    
    def __eq__(self, other_point):
        if (isinstance(other_point, Point)):
            return self.__value_eq(self.x, other_point.x) and self.__value_eq(self.y, other_point.y)
        return False


def calculate_center_of_gravity_point(points):
    
    def format_point_value(val):
        return float("{:.5f}".format(val))
    
    points_size = len(points)
    x = 0
    y = 0
    
    for point in points:
        x += point.x
        y += point.y
    
    x /= points_size
    y /= points_size
    
    return Point(format_point_value(x), format_point_value(y))


def create_random_data(matrix_dim):
    lower_threshold_for_point_x_y = -10
    upper_threshold_for_point_x_y = 30

    # create a 2D matrix with random points
    data = [[0] * matrix_dim for i in range(matrix_dim)]

    for i in range(matrix_dim):
        for j in range(matrix_dim):
            point_x = randrange(lower_threshold_for_point_x_y, upper_threshold_for_point_x_y)
            point_y = randrange(lower_threshold_for_point_x_y, upper_threshold_for_point_x_y)
            point = Point(point_x, point_y)
            data[i][j] = point
    return data


def assign_points_to_clusters(data, data_matrix_dim, centers, clusters):
    # assign each data point to its nearest center
    for i in range(data_matrix_dim):
        for j in range(data_matrix_dim):
            point = data[i][j]
            nearest_center = None
            nearest_distance = None

            for k in range(len(centers)):
                center = centers[k]
                distance = point.find_distance_to(center)

                if (nearest_distance == None) or (distance < nearest_distance):
                    nearest_center = k
                    nearest_distance = distance

            clusters[nearest_center].append(point)
            
        return clusters


def update_centers(clusters, centers):
    # create new centers using center of gravity principle
    for cluster in clusters:
        
        cluster_points = clusters[cluster]
        cluster_points_size = len(cluster_points)

        if cluster_points_size > 0:
            centers[cluster] = calculate_center_of_gravity_point(cluster_points)
        
        return centers


def centers_change(old_centers, new_centers):
    return not (old_centers == new_centers)


def llyod_algorithm(data, data_matrix_dim, center_number):
    centers = {}
    old_centers = {}
    
    # select k random data points as centers
    for i in range(center_number):
        data_i = randrange(0, data_matrix_dim)
        data_j = randrange(0, data_matrix_dim)
        centers[i] = data[data_i][data_j]
    
    clusters = {}
    for k in centers:
        clusters[k] = []
        
    while centers_change(old_centers, centers):
        clusters = assign_points_to_clusters(data, data_matrix_dim, centers, clusters)
        old_centers = centers.copy()
        centers = update_centers(clusters, centers)
    
    return centers


data = create_random_data(MATRIX_DIM)
centers = llyod_algorithm(data, MATRIX_DIM, K)

print("Centers:\n", centers)
