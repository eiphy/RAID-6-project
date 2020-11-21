from copy import deepcopy

import galois_filed as GF
from galois_filed import GaloisNum as GN


def data_to_gn(data):
    C = len(data)
    R = len(data[0])
    _data = [[] for _ in range(C)]
    for i in range(C):
        for j in range(R):
            _data[i].append(GN(data[i][j]))

    return _data


def data_to_gn_seq(data):
    _data = []
    for x in data:
        _data.append(GN(x))

    return _data


def gn_to_data(data):
    C = len(data)
    R = len(data[0])
    _data = [[] for _ in range(C)]
    for i in range(C):
        for j in range(R):
            _data[i].append(data[i][j].value)

    return _data


def seq_data_to_matrix(data, N):
    m = []
    temp = []
    for i in range(len(data)):
        if (i + 1) % (N - 2) == 0:
            temp.append(data[i])
            m.append(temp)
            temp = []
        else:
            temp.append(data[i])

    P, Q = GF.compute_pq(m)

    return m, P, Q


def matrix_to_disk_data(m, p, q, N):
    data = [[] for _ in range(N)]
    R = len(p)
    for i in range(R):
        p_pos, q_pos = get_pq_pos(i, N)
        offset = 0
        for j in range(N):
            if j == p_pos:
                data[j].append(p[i])
                offset += 1
            elif j == q_pos:
                data[j].append(q[i])
                offset += 1
            else:
                data[j].append(m[i][j - offset])
    return data


def disk_data_to_matrix(data):
    R = len(data[0])
    N = len(data)
    m = []
    P = []
    Q = []
    for r in range(R):
        p_pos, q_pos = get_pq_pos(r, N)
        offset = 0
        temp = []
        for i in range(N):
            if i == p_pos:
                P.append(data[i][r])
                offset = offset + 1
            elif i == q_pos:
                Q.append(data[i][r])
                offset = offset + 1
            else:
                temp.append(data[i][r])
        m.append(temp)
    return m, P, Q


def disk_data_to_seq(_data):
    m, _, _ = disk_data_to_matrix(_data)
    R = len(m[0])
    N = len(m)
    data = [m[i][r] for i in range(N) for r in range(R)]
    # for r in range(R):
    #     for i in range(N):
    #         data.append(m[i][r])
    return data


def get_pq_pos(r, N):
    return N - 1 - (r + 1) % N, N - 1 - r % N


def padding_data(_data, N):
    data = deepcopy(_data)
    n = len(data) % (N - 2)
    if n > 0:
        data.extend([0 for _ in range(N - 2 - n)])

    assert len(data) % (N - 2) == 0, "Wrong padding!"

    return data
