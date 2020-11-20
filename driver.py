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
        self._write_data(write_data)
    
    def _write_data(self, data):
        for i, disk in enumerate(self.disks):
            disk.write_to_file(data[i])

    def read_data(self):
        '''Read data from disks.'''
        data = [[] for _ in range(self.N)]
        for i, disk in enumerate(self.disks):
            data[i] = disk.read_file(0)
        lost = self.check_disk_lost()
        data = self.recover_data(data, lost)

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
        data = []
        P = []
        Q = []
        for r in range(N):
            p_pos, q_pos = self.get_pq_id(r)
            for j in range(self.N):
                if j == p_pos:
                    P.append(_data[j][r])
                elif j == q_pos:
                    Q.append(_data[j][r])
                else:
                    data.append(_data[j][r])

        return data, P, Q

    def generate_write_data(self, data, P, Q):
        '''Generate writing data.'''
        write_data = [[] for _ in range(self.N)]
        for r, d in enumerate(data):
            offset = 0
            p_pos, q_pos = self.get_pq_id(r)
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

        return write_data

    def recover_data(self, data, lost):
        '''Recover data.'''
        if not (True in lost):
            return data

        lost_id = []
        for i, s in enumerate(lost):
            if s:
                lost_id.append(i)

        gn_data = C.data_to_gn(data)

        if len(lost_id) == 1:
            gn_data = self._recover_1(gn_data, lost_id[0])
        else:
            gn_data = self._recover_2(gn_data, lost_id)

        self._write_data(gn_data)
        data = C.gn_to_data(gn_data)

        return data

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

    def check_disk_lost(self):
        return [disk.if_lost for disk in self.disks]

    def _recover_1(self, data, lost_id):
        N_row = len(data[0])
        lost_data = []
        for r in range(N_row):
            p_pos, q_pos = self.get_pq_id(r)
            row_data = [d[r] for d in data]
            temp = GN(0)

            offset = 0
            for i, d in enumerate(row_data):
                if lost_id == p_pos:
                    if i == q_pos:
                        continue
                    temp = temp + d
                elif lost_id == q_pos:
                    if i == lost_id or i == p_pos:
                        offset += 1
                        continue
                    temp = temp + GN(GN.power_table[i-offset]) * d
                else:
                    if i == 0:
                        temp = row_data[p_pos]
                    if i == p_pos or i == q_pos:
                        continue
                    temp = temp - d
            lost_data.append(temp)

        data[lost_id] = lost_data

        return data

    def _recover_2(self, data, lost_id):
        return data

    def get_pq_id(self, r):
        return self.N - 1 - (r + 1) % self.N, self.N - 1 - r % self.N

if __name__ == "__main__":
    d = Driver(5)
    d.write_data("hello world!")
    d.disks[0].lost_data()
    print(d.read_data())
