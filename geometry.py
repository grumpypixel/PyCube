

axis_verts = (
    (-7.5, 0.0, 0.0),
    (7.5, 0.0, 0.0),
    (0.0, -7.5, 0.0),
    (0.0, 7.5, 0.0),
    (0.0, 0.0, -7.5),
    (0.0, 0.0, 7.5)
)

axes = (
    (0, 1),
    (2, 3),
    (4, 5)
)

axis_colors = (
    (1.0, 0.0, 0.0),  # Red
    (0.0, 1.0, 0.0),  # Green
    (0.0, 0.0, 1.0)  # Blue
)


'''
    5____________6
    /           /|
   /           / |
 1/__________2/  |
 |           |   |
 |           |   |
 |           |   7
 |           |  /
 |           | /
 0___________3/
'''

edge_pieces = [
    # X
    # 0
    [[[-1, -1, 3],
     [-1, -3, 3],
     [1, -3, 3],
     [1, -1, 3],
     [-1, -1, 1],
     [-1, -3, 1],
     [1, -3, 1],
     [1, -1, 1]],

    # 1
    [[-1, 1, 3],
     [-1, 3, 3],
     [1, 3, 3],
     [1, 1, 3],
     [-1, 1, 1],
     [-1, 3, 1],
     [1, 3, 1],
     [1, 1, 1]],

    # 2
    [[-1, 1, -3],
     [-1, 3, -3],
     [1, 3, -3],
     [1, 1, -3],
     [-1, 1, -1],
     [-1, 3, -1],
     [1, 3, -1],
     [1, 1, -1]],

    # 3
    [[-1, -1, -3],
     [-1, -3, -3],
     [1, -3, -3],
     [1, -1, -3],
     [-1, -1, -1],
     [-1, -3, -1],
     [1, -3, -1],
     [1, -1, -1]]],

    # Y
    # 0
    [[[-3, -1, 3],
     [-3, 1, 3],
     [-1, 1, 3],
     [-1, -1, 3],
     [-3, -1, 1],
     [-3, 1, 1],
     [-1, 1, 1],
     [-1, -1, 1]],

    # 1
    [[-3, -1, -3],
     [-3, 1, -3],
     [-1, 1, -3],
     [-1, -1, -3],
     [-3, -1, -1],
     [-3, 1, -1],
     [-1, 1, -1],
     [-1, -1, -1]],

    # 2
    [[3, -1, -3],
     [3, 1, -3],
     [1, 1, -3],
     [1, -1, -3],
     [3, -1, -1],
     [3, 1, -1],
     [1, 1, -1],
     [1, -1, -1]],

    # 3
    [[3, -1, 3],
     [3, 1, 3],
     [1, 1, 3],
     [1, -1, 3],
     [3, -1, 1],
     [3, 1, 1],
     [1, 1, 1],
     [1, -1, 1]]],

    # Z
    # 0
    [[[-3, -3, 1],
     [-3, -1, 1],
     [-1, -1, 1],
     [-1, -3, 1],
     [-3, -3, -1],
     [-3, -1, -1],
     [-1, -1, -1],
     [-1, -3, -1]],

    # 1
    [[-3, 3, 1],
     [-3, 1, 1],
     [-1, 1, 1],
     [-1, 3, 1],
     [-3, 3, -1],
     [-3, 1, -1],
     [-1, 1, -1],
     [-1, 3, -1]],

    # 2
    [[3, 3, 1],
     [3, 1, 1],
     [1, 1, 1],
     [1, 3, 1],
     [3, 3, -1],
     [3, 1, -1],
     [1, 1, -1],
     [1, 3, -1]],

    # 3
    [[3, -3, 1],
     [3, -1, 1],
     [1, -1, 1],
     [1, -3, 1],
     [3, -3, -1],
     [3, -1, -1],
     [1, -1, -1],
     [1, -3, -1]]],


]

center_pieces = [
    # Front 0
    [[-1, -1, 3],
     [-1, 1, 3],
     [1, 1, 3],
     [1, -1, 3],
     [-1, -1, 1],
     [-1, 1, 1],
     [1, 1, 1],
     [1, -1, 1]],

    # Left 1
    [[-3, -1, 1],
     [-3, 1, 1],
     [-1, 1, 1],
     [-1, -1, 1],
     [-3, -1, -1],
     [-3, 1, -1],
     [-1, 1, -1],
     [-1, -1, -1]],

    # Back 2
    [[-1, -1, -1],
     [-1, 1, -1],
     [1, 1, -1],
     [1, -1, -1],
     [-1, -1, -3],
     [-1, 1, -3],
     [1, 1, -3],
     [1, -1, -3],
     ],

    # Right 3
    [[1, -1, 1],
     [1, 1, 1],
     [3, 1, 1],
     [3, -1, 1],
     [1, -1, -1],
     [1, 1, -1],
     [3, 1, -1],
     [3, -1, -1],

     ],

    # Up 3
    [[-1, 1, 1],
     [-1, 3, 1],
     [1, 3, 1],
     [1, 1, 1],
     [-1, 1, -1],
     [-1, 3, -1],
     [1, 3, -1],
     [1, 1, -1]],

    # Down 4
    [[-1, -3, 1],
     [-1, -1, 1],
     [1, -1, 1],
     [1, -3, 1],
     [-1, -3, -1],
     [-1, -1, -1],
     [1, -1, -1],
     [1, -3, -1]]
]

'''
    These pattern are for each set of edge pieces and corner
    pieces on each face. They will shift when the faces are
    rotated so these patterns will keep track of them.
     _______________
    |  1 |  2 |  2 |
    |____|____|____|
    | 1  |    |  3 |
    |____|____|____|
    |  0 |  0 |  3 |
    |____|____|____|

'''
# face_patterns = [
#     [0, 1, 2, 3],  # 0 Front
#     [0, 1, 2, 3],  # 1 Back
#     [0, 1, 2, 3],  # 2 Left
#     [0, 1, 2, 3],  # 3 Right
#     [0, 1, 2, 3],  # 4 Up
#     [0, 1, 2, 3],  # 5 Down
# ]
#
# front_edges = [
#     [0, 1],  # x
#     [0, 3]   # y
# ]
#
# back_edges = [
#     [2, 3],  # x
#     [1, 2]   # y
# ]
#
# left_edges = [
#     [0, 1],  # y
#     [0, 1]   # z
# ]
#
# right_edges = [
#     [2, 3],  # y
#     [2, 3]   # z
# ]


'''
       5____________6
       /           /|
      /           / |
    1/__________2/  |
    |           |   |
    |           |   |
    |           |   7
    |           |  /
    |           | /
    0___________3/
'''

cube_verts = (
    (-3.0, -3.0, 3.0),      # 0
    (-3.0, 3.0, 3.0),       # 1
    (3.0, 3.0, 3.0),        # 2
    (3.0, -3.0, 3.0),       # 3
    (-3.0, -3.0, -3.0),     # 4
    (-3.0, 3.0, -3.0),      # 5
    (3.0, 3.0, -3.0),       # 6
    (3.0, -3.0, -3.0)       # 7
)


cube_edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 6),
    (5, 1),
    (5, 4),
    (5, 6),
    (7, 3),
    (7, 4),
    (7, 6)
)


'''
    5____________6
    /           /|
   /           / |
 1/__________2/  |
 |           |   |
 |           |   |
 |           |   7
 |           |  /
 |           | /
 0___________3/
'''

cube_surfaces = (
    [0, 1, 2, 3],  # Front
    [4, 5, 1, 0],  # Left
    [7, 6, 5, 4],  # Back
    [3, 2, 6, 7],  # Right
    [1, 5, 6, 2],  # Top
    [4, 0, 3, 7]  # Bottom
)

cube_colors = (
    (1.0, 1.0, 1.0),  # White
    (0.769, 0.118, 0.227),  # Red
    (1.0, 0.835, 0.0),  # Yellow
    (1.0, 0.345, 0.0),  # Orange
    (0.0, 0.62, 0.376),  # Green
    (0.0, 0.318, 0.729)  # Blue
)
