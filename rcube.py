__version__ = '1.0.3.1'
__author__ = 'Vi Grey (http://pariahvi.com)'


def get_centres(mem):
    centres = []
    for i in range(6):
        centres.append(mem[i][4])
    return centres


def get_full_mem(mem):
    full_mem = []
    for x in mem:
        for i in x:
            full_mem.append(i)
    return full_mem


def colour_check(mem):
    full_mem = get_full_mem(mem)
    colours = list(set(full_mem))
    centres = get_centres(mem)
    checksum = 0
    if len(colours) == 6 and len(centres) == 6:
        for colour in colours:
            if full_mem.count(colour) == 9:
                checksum += 1
            if checksum == 6:
                return 1
    return 0


def get_corners(mem):
    corners = [
        [mem[0][0], mem[1][0], mem[4][2]], [mem[0][2], mem[4][0], mem[3][2]],
        [mem[0][8], mem[3][0], mem[2][2]], [mem[0][6], mem[2][0], mem[1][2]],
        [mem[5][0], mem[1][8], mem[2][6]], [mem[5][2], mem[2][8], mem[3][6]],
        [mem[5][8], mem[3][8], mem[4][6]], [mem[5][6], mem[4][8], mem[1][6]]
    ]
    return corners


def finished_corners(mem):
    corners_finish = [
        [
            [mem[0][4], mem[1][4], mem[4][4]],
            [mem[1][4], mem[4][4], mem[0][4]],
            [mem[4][4], mem[0][4], mem[1][4]]
        ],
        [
            [mem[0][4], mem[4][4], mem[3][4]],
            [mem[4][4], mem[3][4], mem[0][4]],
            [mem[3][4], mem[0][4], mem[4][4]]
        ],
        [
            [mem[0][4], mem[3][4], mem[2][4]],
            [mem[3][4], mem[2][4], mem[0][4]],
            [mem[2][4], mem[0][4], mem[3][4]]
        ],
        [
            [mem[0][4], mem[2][4], mem[1][4]],
            [mem[2][4], mem[1][4], mem[0][4]],
            [mem[1][4], mem[0][4], mem[2][4]]
        ],
        [
            [mem[5][4], mem[1][4], mem[2][4]],
            [mem[1][4], mem[2][4], mem[5][4]],
            [mem[2][4], mem[5][4], mem[1][4]]
        ],
        [
            [mem[5][4], mem[2][4], mem[3][4]],
            [mem[2][4], mem[3][4], mem[5][4]],
            [mem[3][4], mem[5][4], mem[2][4]]
        ],
        [
            [mem[5][4], mem[3][4], mem[4][4]],
            [mem[3][4], mem[4][4], mem[5][4]],
            [mem[4][4], mem[5][4], mem[3][4]]
        ],
        [
            [mem[5][4], mem[4][4], mem[1][4]],
            [mem[4][4], mem[1][4], mem[5][4]],
            [mem[1][4], mem[5][4], mem[4][4]]
        ]
    ]
    return corners_finish


def get_edges(mem):
    edges = [
        [mem[0][1], mem[4][1]], [mem[0][5], mem[3][1]], [mem[0][7], mem[2][1]],
        [mem[0][3], mem[1][1]], [mem[4][5], mem[1][3]], [mem[4][3], mem[3][5]],
        [mem[2][5], mem[3][3]], [mem[2][3], mem[1][5]], [mem[5][1], mem[2][7]],
        [mem[5][5], mem[3][7]], [mem[5][7], mem[4][7]], [mem[5][3], mem[1][7]]
    ]
    return edges


def finished_edges(mem):
    edges_finish = [
        [[mem[0][4], mem[4][4]], [mem[4][4], mem[0][4]]],
        [[mem[0][4], mem[3][4]], [mem[3][4], mem[0][4]]],
        [[mem[0][4], mem[2][4]], [mem[2][4], mem[0][4]]],
        [[mem[0][4], mem[1][4]], [mem[1][4], mem[0][4]]],
        [[mem[4][4], mem[1][4]], [mem[1][4], mem[4][4]]],
        [[mem[4][4], mem[3][4]], [mem[3][4], mem[4][4]]],
        [[mem[2][4], mem[3][4]], [mem[3][4], mem[2][4]]],
        [[mem[2][4], mem[1][4]], [mem[1][4], mem[2][4]]],
        [[mem[5][4], mem[2][4]], [mem[2][4], mem[5][4]]],
        [[mem[5][4], mem[3][4]], [mem[3][4], mem[5][4]]],
        [[mem[5][4], mem[4][4]], [mem[4][4], mem[5][4]]],
        [[mem[5][4], mem[1][4]], [mem[1][4], mem[5][4]]]
    ]
    return edges_finish


def unique_check(edges, corners, f_edges, f_corners):
    unique_corners = []
    unique_edges = []
    for i in corners:
        for j in range(len(corners)):
            if i in f_corners[j]:
                unique_corners.append(j)
    for i in edges:
        for j in range(len(edges)):
            if i in f_edges[j]:
                unique_edges.append(j)
    unique_corners = list(set(unique_corners))
    unique_edges = list(set(unique_edges))
    if len(unique_corners) == 8 and len(unique_edges) == 12:
        return 1
    return 0


def swap(list, left, right):
    rightbackup = list[right]
    list[right] = list[left]
    list[left] = rightbackup
    return list


def list_error(x_list, x_list_finish):
    y_list = []
    for x in x_list:
        error = 1
        for i in range(len(x_list_finish)):
            if x in x_list_finish[i]:
                error = 0
                y_list.append(i)
    if not error:
        return y_list
    return 0


def permutation_check(edges, corners, f_edges, f_corners):
    c_check = 0
    e_check = 0
    c_list = list_error(corners, f_corners)
    e_list = list_error(edges, f_edges)
    if c_list and e_list:
        for i in range(len(c_list) - 1):
            min = i
            for j in range(i + 1, len(c_list)):
                if c_list[j] < c_list[min]:
                    min = j
            if i != min:
                c_list = swap(c_list, i, min)
                c_check += 1
        for i in range(len(e_list) - 1):
            min = i
            for j in range(i + 1, len(e_list)):
                if e_list[j] < e_list[min]:
                    min = j
            if i != min:
                e_list = swap(e_list, i, min)
                e_check += 1
        if (c_check + e_check) % 2 == 0:
            return 1
    return 0


def corner_check(corners, f_corners):
    corner_b = 0
    corner_c = 0
    for corner in corners:
        for i in range(len(corners)):
            if corner in f_corners[i]:
                if f_corners[i].index(corner) == 1:
                    corner_b += 1
                elif f_corners[i].index(corner) == 2:
                    corner_c += 1
    if (corner_b + (2 * corner_c)) % 3 == 0:
        return 1
    return 0


def edge_check(mem):
    checksum = 0

    edge_list = [
        [mem[0][1], mem[4][1]], [mem[0][3], mem[1][1]], [mem[0][5], mem[3][2]],
        [mem[0][7], mem[2][1]], [mem[5][1], mem[2][7]], [mem[5][3], mem[1][7]],
        [mem[5][5], mem[3][7]], [mem[5][7], mem[4][7]], [mem[2][3], mem[1][5]],
        [mem[2][5], mem[3][3]], [mem[4][3], mem[3][5]], [mem[4][5], mem[1][3]]
    ]
    for x in edge_list:
        if x[0] == mem[0][4] or x[0] == mem[5][4] or (
            x[1] != mem[0][4] and x[1] != mem[5][4] and (
                x[0] == mem[2][4] or x[0] == mem[4][4])):
            checksum += 1
    if checksum % 2 == 0:
        return 1
    return 0


def edge_solve(edges, f_edges):
    temp = -1
    temp2 = -2
    piece = edges[8]
    flip = 0
    i = -1
    solved_edges = []
    counter = 0
    finished_solve = ''
    e_chart = [[0, 16], [1, 12], [2, 8], [3, 4], [17, 7], [19, 13], [9, 15],
               [11, 5], [20, 10], [21, 14], [22, 18], [23, 6]]
    move = [
        'M2 ', 'R\' U R U\' M2 U R\' U\' R ', 'U2 M\' U2 M\' ',
        'L U\' L\' U M2 U\' L U L\' ', 'B L\' B\' M2 B L B\' ',
        'B L2 B\' M2 B L2 B\' ', 'B L B\' M2 B L\' B\' ',
        'L\' B L B\' M2 B L\' B\' L ', 'D M\' U R2 U\' M U R2 U\' D\' M2 ',
        'U R U\' M2 U R\' U\' ', 'Set', 'U\' L\' U M2 U\' L U ',
        'B\' R B M2 B\' R\' B ', 'R B\' R\' B M2 B\' R B R\' ',
        'B\' R\' B M2 B\' R B ', 'B\' R2 B M2 B\' R2 B ',
        'B\' R B U R2 U\' M2 U R2 U\' B\' R\' B ', 'U\' L U M2 U\' L\' U ',
        'M2 D U R2 U\' M\' U R2 U\' M D\' ', 'U R\' U\' M2 U R U\' ',
        'Set', 'U R2 U\' M2 U R2 U\' ', 'M U2 M U2 ', 'U\' L2 U M2 U\' L2 U '
    ]
    for x in edges:
        i += 1
        if x in f_edges[i]:
            if x != f_edges[i][0]:
                if i == 2 or i == 10:
                    if i == 2:
                        finished_solve += (move[e_chart[i][1]] +
                                           move[e_chart[10][0]])
                    else:
                        finished_solve += (move[e_chart[i][1]] +
                                           move[e_chart[2][0]])
                elif i != 8:
                    finished_solve += (move[e_chart[i][1]] +
                                       move[e_chart[i][0]])
                if i != 8:
                    flip += 1
                    flip % 2
            if i != 8:
                solved_edges.append(i)
    while len(solved_edges) != 11:
        for i in range(12):
            if piece in f_edges[i]:
                if i != 8 and temp != temp2:
                    temp2 = i
                    j = f_edges[i].index(piece)
                    if (i == 2 or i == 10) and counter % 2 == 1:
                        if i == 2:
                            finished_solve += move[e_chart[10][(
                                j + flip) % 2]]
                        else:
                            finished_solve += move[e_chart[2][(
                                j + flip) % 2]]
                    else:
                        finished_solve += move[e_chart[i][(j + flip) % 2]]
                    piece = edges[i]
                    if (j + flip) % 2 == 0:
                        flip = 0
                    else:
                        flip = 1
                    solved_edges.append(i)
                    counter += 1
                else:
                    for x in range(12):
                        if x not in solved_edges and x != 8:
                            if (x == 2 or x == 10) and counter % 2 == 1:
                                if x == 2:
                                    finished_solve += move[e_chart[10][0]]
                                else:
                                    finished_solve += move[e_chart[2][0]]
                            else:
                                finished_solve += move[e_chart[x][0]]
                            piece = edges[x]
                            temp = x
                            flip = 0
                            counter += 1
                            break
                break
    return finished_solve, counter


def parity_fix(counter):
    if counter % 2 == 1:
        return 'D\' L2 D M2 D\' L2 D '
    return ''


def corner_solve(corners, f_corners):
    temp = -1
    temp2 = -2
    piece = corners[0]
    flip = 0
    i = -1
    solved_corners = []
    finished_solve = ''
    c_chart = [[0, 4, 17], [1, 16, 13], [2, 12, 9], [3, 8, 5], [20, 6, 11],
               [21, 10, 15], [22, 14, 19], [23, 18, 7]]
    setup = [
        'Set', 'R D\' ', 'F ', 'F R\' ', 'Set', 'F2 ', 'D2 R ', 'D2 ',
        'F\' D ', 'F2 D ', 'F D ', 'D ', 'R\' ', 'R2 ', 'R ', '', 'R\' F ',
        'Set', 'D\' R ', 'D\' ', 'F\' ', 'D\' F\' ', 'D2 F\' ', 'D F\' '
    ]
    reverse_setup = [
        'Set', 'D R\' ', 'F\' ', 'R F\' ', 'Set', 'F2 ', 'R\' D2 ', 'D2 ',
        'D\' F ', 'D\' F2 ', 'D\' F\' ', 'D\' ', 'R ', 'R2 ', 'R\' ', '',
        'F\' R ', 'Set', 'R\' D ', 'D ', 'F ', 'F D ', 'F D2 ', 'F D\' '
    ]
    mod_y_perm = 'R U\' R\' U\' R U R\' F\' R U R\' U\' R\' F R '
    for x in corners:
        i += 1
        if x in f_corners[i]:
            if x != f_corners[i][0]:
                if i != 0:
                    if x == f_corners[i][1]:
                        finished_solve += (setup[c_chart[i][1]] + mod_y_perm +
                                           reverse_setup[c_chart[i][1]] +
                                           setup[c_chart[i][2]] + mod_y_perm +
                                           reverse_setup[c_chart[i][2]])
                        flip += 1
                        flip %= 3
                    elif x == f_corners[i][2]:
                        finished_solve += (setup[c_chart[i][2]] + mod_y_perm +
                                           reverse_setup[c_chart[i][2]] +
                                           setup[c_chart[i][1]] + mod_y_perm +
                                           reverse_setup[c_chart[i][1]])
                        flip += 2
                        flip %= 3
            if i != 0:
                solved_corners.append(i)
    while len(solved_corners) != 7:
        for i in range(8):
            if piece in f_corners[i]:
                if i != 0 and temp != temp2:
                    temp2 = i
                    j = f_corners[i].index(piece)
                    finished_solve += (setup[c_chart[i][(j + flip) % 3]] +
                                       mod_y_perm +
                                       reverse_setup[c_chart[i][(
                                           j + flip) % 3]])
                    piece = corners[i]
                    if (j + flip) % 3 == 0:
                        flip = 0
                    elif (j + flip) % 3 == 1:
                        flip = 1
                    else:
                        flip = 2
                    solved_corners.append(i)
                else:
                    for x in range(8):
                        if x not in solved_corners and x != 0:
                            finished_solve += (setup[c_chart[x][0]] +
                                               mod_y_perm +
                                               reverse_setup[c_chart[x][0]])
                            piece = corners[x]
                            temp = x
                            flip = 0
                            break
                break
    return finished_solve


def optimize(f):
    allfaces = ['U', 'L', 'F', 'R', 'B', 'D', 'M']
    for i in range(4):
        for z in allfaces:
            f = f.replace(z + '2 ' + z + '2 ', '')
            f = f.replace(z + '2 ' + z + '\' ', z + ' ')
            f = f.replace(z + '\' ' + z + '2 ', z + ' ')
            f = f.replace(z + '2 ' + z + ' ', z + '\' ')
            f = f.replace(z + ' ' + z + '2 ', z + '\' ')
            f = f.replace(z + '\' ' + z + ' ', '')
            f = f.replace(z + ' ' + z + '\' ', '')
            f = f.replace(z + '\' ' + z + '\' ', z + '2 ')
            f = f.replace(z + ' ' + z + ' ', z + '2 ')
    return f[:-1]


def mem_check(mem):
    i = 0
    for x in mem:
        i += 1
        if len(x) != 9:
            return 0
    if i == 6:
        return 1
    return 0


def solve(mem):
    if not mem_check(mem):
        raise Exception('Incorrect layout of piece list')
    corners = get_corners(mem)
    corners_finished = finished_corners(mem)
    edges = get_edges(mem)
    edges_finished = finished_edges(mem)
    if colour_check(mem):
        if unique_check(edges, corners, edges_finished, corners_finished):
            if permutation_check(edges, corners, edges_finished,
                                 corners_finished):
                if corner_check(corners, corners_finished):
                    if edge_check(mem):
                        solution, counter = edge_solve(edges, edges_finished)
                        solution += parity_fix(counter)
                        solution += corner_solve(corners, corners_finished)
                        solution = optimize(solution)
                        return solution
    raise Exception('The cube is in an unsolvable state')
