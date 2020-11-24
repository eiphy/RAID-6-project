from copy import deepcopy

import algorithm as ALG
import galois_filed as GF
from galois_filed import GaloisNum as GN


def data_to_gn(data):
    """Recursively transfer data to GF(2^8)."""
    return ALG.transfer_data_list(data, lambda x: GN(x))


def gn_to_data(data):
    """Recursively transfer data to ordinary integers."""
    return ALG.transfer_data_list(data, lambda x: x.value)


def strip_data(_data, B):
    """Strip data into different blocks."""
    data = []
    block = []
    for i, d in enumerate(_data):
        if i % B == 0 and i != 0:
            data.append(block)
            block = []
        block.append(d)

    if len(block) != 0:
        data.append(block)

    return data


def block_data_to_seq(data):
    N = len(data)
    B = len(data[0])
    _data = []
    for i in range(N):
        for j in range(B):
            _data.append(data[i][j])

    return _data


def block_data_to_matrix(data, N, B):
    """Generate matrix from stripped data."""
    data = padding_data_block(data, N, B)
    m = []
    for i in range(0, len(data), N - 2):
        temp_block_row = []
        for j in range(B):
            temp_row = []
            for m in range(N - 2):
                temp_row.append(data[i + m][j])
            temp_block_row.append(temp_row)
        m.extend(temp_block_row)

    P, Q = GF.compute_pq(m)

    return m, P, Q


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


def seq_data_to_matrix_block(data, N, B):
    m = []
    temp = []
    for i in range(0, len(data), N - 2):
        temp = []
        for j in range(B):
            temp_b = []
            for m in range(N - 2):
                temp_b.append(data[i + m][j])
            temp.append(temp)
        m.extend(temp)

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


def get_matrix_id_from_disk_id(r, _i, N):
    p, q = get_pq_pos(r, N)
    assert _i not in (p, q), "Index is P or Q!"
    offset = 0
    if p < _i:
        offset += 1
    if q < _i:
        offset += 1
    return _i - offset


def get_recover_id_1data(lost_ids, s_pos1):
    disk_id = lost_ids[0] if lost_ids[1] == s_pos1 else lost_ids[1]
    i_d = lost_ids.index(disk_id)
    i_s = 0 if i_d == 1 else 1
    return i_d, i_s, disk_id


def padding_data(_data, N):
    data = deepcopy(_data)
    n = len(data) % (N - 2)
    if n > 0:
        data.extend([0 for _ in range(N - 2 - n)])

    assert len(data) % (N - 2) == 0, "Wrong padding!"

    return data


def padding_data_block(_data, N, B):
    data = deepcopy(_data)
    n = len(data) % (N - 2)
    if n > 0:
        data.extend([[0 for _ in range(B)] for _ in range(N - 2 - n)])

    assert len(data) % (N - 2) == 0, "Wrong padding!"

    return data


def padding_lost_data(_data, lost_ids):
    N = len(_data[1]) if 0 in lost_ids else len(_data[0])
    data = deepcopy(_data)
    for i in lost_ids:
        data[i] = [0 for _ in range(N)]
    return data
