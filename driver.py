from disk import Disk
from galois_number import GaloisNum as GN
import convert as C

class Driver():
    def __init__(self, num_disk):
        assert num_disk > 0, "num_disk <= 0!"
        self.N = num_disk
        self.disks = []
        for i in range(num_disk):
            self.disks.append(Disk(i))

    def write_data(self, s):
        '''Write data to disks.'''
        data, P, Q = self.preprocess_write_data(s)
        write_data = self.generate_write_data(data, P, Q)
        for i, disk in enumerate(self.disks):
            disk.write_to_file(write_data[i])

    def read_data(self):
        '''Read data from disks.'''
        stat = self.check_disk_status()
        data = [[] for _ in range(self.N)]
        for i, disk in enumerate(self.disks):
            data[i] = disk.read_file(0)
        data, _, _ = self.combine_read_data(data)
        content = []
        for d in data:
            content.append(chr(d))
        return "".join(content)

    def preprocess_write_data(self, s):
        n = len(s) % (self.N - 2)
        data = [GN(ord(c)) for c in s]

        if n > 0:
            data.extend([GN(0) for _ in range(n)])

        assert len(data) % (self.N - 2) == 0, "wrong length!"

        data, P, Q = self.compute_pq(data)

        return data, P, Q

    def combine_read_data(self, _data):
        N = len(_data[0])
        p_pos, q_pos = self.N - 2, self.N - 1
        data = []
        P = []
        Q = []
        for i in range(N):
            for j in range(self.N):
                if j == p_pos:
                    P.append(_data[j][i])
                elif j == q_pos:
                    Q.append(_data[j][i])
                else:
                    data.append(_data[j][i])
            p_pos = self._change_special_pos(p_pos)
            q_pos = self._change_special_pos(q_pos)

        return data, P, Q

    # def generate_matrix_from_data(self, _data):
    #     N = len(data[0])
    #     p_pos, q_pos = self.N - 2, self.N - 1
    #     data = []
    #     P = []
    #     Q = []
    #     for i in range(N):
    #         for j in range(self.N):
    #             if j == p_pos:
    #                 P.append(_data[j][i])
    #             elif j == q_pos:
    #                 Q.append(_data[j][i])
    #             else:
    #                 data.append(_data[j][i])

    #     return data, P, Q

    def generate_write_data(self, data, P, Q):
        '''Generate writing data.'''
        write_data = [[] for _ in range(self.N)]
        p_pos, q_pos = self.N - 2, self.N - 1
        for r, d in enumerate(data):
            offset = 0
            for i in range(self.N):
                pos = i - offset
                if i == p_pos:
                    write_data[i].append(P[r])
                    offset += 1
                elif i == q_pos:
                    write_data[i].append(Q[r])
                    offset += 1
                else:
                    pos = i - offset
                    write_data[i].append(d[pos])
            p_pos = self._change_special_pos(p_pos)
            q_pos = self._change_special_pos(q_pos)
            assert p_pos != q_pos, "p and q have the same position!"

        return write_data

    def _change_special_pos(self, pos):
        pos -= 1
        if pos < 0:
            pos = self.N - 1
        return pos

    def recover_data(self):
        '''Recover data.'''

    def compute_pq(self, data):
        '''Compute pq'''
        m = []
        temp = []
        for i in range(len(data)):
            if (i + 1) % (self.N - 2) == 0:
                temp.append(data[i])
                m.append(temp)
                temp = []
            else:
                temp.append(data[i])

        P = []
        Q = []
        for row in m:
            p = GN(0)
            q = GN(0)
            for i, x in enumerate(row):
                p = p + x
                q = q + GN(GN.power_table[i]) * x
            P.append(p)
            Q.append(q)

        return m, P, Q

    def check_disk_status(self):
        return [False if disk.if_lost else True for disk in self.disks]

if __name__ == "__main__":
    d = Driver(5)
    d.write_data("hello world!")
    print(d.read_data())
