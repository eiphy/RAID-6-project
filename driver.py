import galois_filed as GF
import util as U
from disk import Disk
from galois_filed import GaloisNum as GN


class Driver:
    def __init__(self, num_disk, clear=False, block_size=10):
        assert num_disk > 0, "num_disk <= 0!"
        assert num_disk <= 255, "num_disk > 255!"
        self.N = num_disk
        self.B = block_size
        self.disks = []
        for i in range(num_disk):
            self.disks.append(Disk(i, clear=clear))

        GF.generate_recover_table()

    def write_data(self, s):
        """Write data to disks."""
        data = [ord(c) for c in s]
        data = U.padding_data(data, self.N)

        gn_data = U.data_to_gn(data)
        m, P, Q = U.seq_data_to_matrix(gn_data, self.N)

        write_data = U.gn_to_data(U.matrix_to_disk_data(m, P, Q, self.N))

        self._write_data(write_data)

    def _write_data(self, data, ids=[]):
        if len(ids) == 0:
            for i, disk in enumerate(self.disks):
                disk.write_to_file(data[i])
        else:
            for i, i_d in enumerate(ids):
                self.disks[i_d].write_to_file(data[i])

    def read_data(self):
        """Read data from disks."""
        data = [disk.read_file(0) for disk in self.disks]

        lost_ids = self.check_disk_lost()
        data = U.padding_lost_data(data, lost_ids)
        data = self.recover_data(data, lost_ids)

        seq_data = U.disk_data_to_seq(data)

        content = []
        for d in seq_data:
            content.append(chr(d))
        return "".join(content)

    def check_disk_lost(self):
        lost_ids = []
        for i, disk in enumerate(self.disks):
            if disk.if_lost:
                lost_ids.append(i)

        return lost_ids

    def recover_data(self, data, lost_ids):
        """Recover data."""
        if len(lost_ids) == 0:
            return data

        gn_data = U.data_to_gn(data)

        m, P, Q = U.disk_data_to_matrix(gn_data)

        if len(lost_ids) == 1:
            lost_data = [self._recover_1(m, P, Q, lost_ids[0])]
        elif len(lost_ids) == 2:
            lost_data = self._recover_2(m, P, Q, lost_ids)
        else:
            raise ValueError("Not implemented!")

        for i, i_d in enumerate(lost_ids):
            gn_data[i_d] = lost_data[i]

        data = U.gn_to_data(gn_data)
        self._write_data(data, ids=lost_ids)

        for i in lost_ids:
            self.disks[i].recovered()

        return data

    def _recover_1(self, m, P, Q, lost_id):
        R = len(m)
        lost_data = []
        for r in range(R):
            p_pos, q_pos = U.get_pq_pos(r, self.N)
            p, q = GF.compute_pq_row(m[r])

            if lost_id == p_pos:
                temp = p
            elif lost_id == q_pos:
                temp = q
            else:
                temp = GF.recover_data_from_p(p, P[r])

            lost_data.append(temp)

        return lost_data

    def _recover_2(self, m, P, Q, lost_ids):
        R = len(m)
        lost_data = [[], []]

        for r in range(R):
            p_pos, q_pos = U.get_pq_pos(r, self.N)
            p, q = GF.compute_pq_row(m[r])

            if p_pos in lost_ids and q_pos in lost_ids:
                temp = [p, q] if lost_ids[0] == p_pos else [q, p]
            elif p_pos in lost_ids:
                temp = [None, None]
                i_d, i_s, disk_id = U.get_recover_id_1data(lost_ids, p_pos)
                i_m = U.get_matrix_id_from_disk_id(r, disk_id, self.N)

                temp[i_d] = GF.recover_data_from_q(q, Q[r], i_m)
                temp[i_s], _ = GF.compute_pq_row(m[r])
            elif q_pos in lost_ids:
                temp = [None, None]
                i_d, i_s, disk_id = U.get_recover_id_1data(lost_ids, q_pos)

                temp[i_d] = GF.recover_data_from_p(p, P[r])
                _, temp[i_s] = GF.compute_pq_row(m[r])
            else:
                x = U.get_matrix_id_from_disk_id(r, lost_ids[0], self.N)
                y = U.get_matrix_id_from_disk_id(r, lost_ids[1], self.N)
                temp = GF.recover_2data(P[r], Q[r], p, q, x, y)
                m[r][x], m[r][y] = temp[0], temp[1]
                p, q = GF.compute_pq_row(m[r])
                assert p == P[r] and q == Q[r], "Wrong recovery!"

            lost_data[0].append(temp[0])
            lost_data[1].append(temp[1])

        return lost_data


if __name__ == "__main__":
    d = Driver(6, clear=True)
    d.write_data(
        "Singapore Airlines is continuing to build back its North American route network with more flights to more cities across the US, ending an eight-month holding pattern during the pandemic that saw the airline operate only one American route.\nOn the heels of launching its newest route just last week between Singapore and New York, which earned the top spot of the world's longest flight by distance, the flag carrier is doubling down with increased flights to the West Coast. Starting in December, Los Angeles will see an increase in daily flights while San Francisco will see its first scheduled flights since April, both laying the foundation for the airline's post-pandemic recovery.\nThe first flight to San Francisco will depart Singapore on December 15 and return\ntwo days later on December 17. The Bay Area will start with three-times-weekly service departing to Singapore on Mondays, Thursdays, and Saturdays as the airline settles into the new route, which sees a duration of 14 hours and 40 minutes on the outbound leg and 17 hours and 35 minutes on the return. Los Angeles, for its part, will see increased frequencies from three weekly flights to five starting December 2, with service on all days of the week except Thursdays and Saturdays. Singapore Airlines never stopped flying the Singapore-Los Angeles route throughout the pandemic, which became its sole non-stop link to the US. Here!!"
    )
    # d.write_data("hello word! \n This message from nobody.")
    d.disks[4].lost_data()
    d.disks[0].lost_data()
    print(d.read_data())
