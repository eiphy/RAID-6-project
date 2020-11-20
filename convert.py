from galois_number import GaloisNum as GN

def decode(s):
    return [ord(c) for c in s]

def data_to_gn(data):
    C = len(data)
    R = len(data[0])
    _data = [[] for _ in range(C)]
    for i in range(C):
        for j in range(R):
            _data[i].append(GN(data[i][j]))

    return _data

def gn_to_data(data):
    C = len(data)
    R = len(data[0])
    _data = [[] for _ in range(C)]
    for i in range(C):
        for j in range(R):
            _data[i].append(data[i][j].value)

    return _data
