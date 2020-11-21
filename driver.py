import galois_filed as GF
import util as U
from disk import Disk
from galois_filed import GaloisNum as GN


class Driver:
    def __init__(self, num_disk):
        assert num_disk > 0, "num_disk <= 0!"
        self.N = num_disk
        self.disks = []
        for i in range(num_disk):
            self.disks.append(Disk(i))

    def write_data(self, s):
        """Write data to disks."""
        data = [ord(c) for c in s]
        data = U.padding_data(data, self.N)

        m, P, Q = U.seq_data_to_matrix(U.data_to_gn_seq(data), self.N)

        write_data = U.gn_to_data(U.matrix_to_disk_data(m, P, Q, self.N))

        self._write_data(write_data)

    def _write_data(self, data):
        for i, disk in enumerate(self.disks):
            disk.write_to_file(data[i])

    def read_data(self):
        """Read data from disks."""
        data = [disk.read_file(0) for disk in self.disks]

        lost_ids = self.check_disk_lost()
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
            lost_data = self._recover_1(m, P, Q, lost_ids[0])
        elif len(lost_ids) == 2:
            lost_data = self._recover_2(m, P, Q, lost_ids)
        else:
            raise ValueError("Not implemented!")

        for i in lost_ids:
            gn_data[i] = lost_data

        data = U.gn_to_data(gn_data)
        self._write_data(data)

        for i in lost_ids:
            self.disks[i].recovered()

        return data

    def _recover_1(self, m, P, Q, lost_id):
        R = len(m)
        lost_data = []
        for r in range(R):
            p_pos, q_pos = U.get_pq_pos(r, self.N)
            temp = GN(0)

            if lost_id == p_pos:
                temp, _ = GF.compute_pq_row(m[r])
            elif lost_id == q_pos:
                _, temp = GF.compute_pq_row(m[r])
            else:
                temp_sum = GN(0)
                for x in m[r]:
                    temp_sum += x
                temp = P[r] - temp_sum

            lost_data.append(temp)

        return lost_data

    def _recover_2(self, m, P, Q, lost_id):
        N_row = len(m[0])
        lost_data = [[] for _ in lost_id]
        offet = 0

        for r in range(N_row):
            temp_p, temp_q = GN(0), GN(0)
            p_pos, q_pos = U.get_pq_pos(r, self.N)
            row_data = [d[r] for d in m]

            for i, d in enumerate(row_data):
                if p_pos in lost_id and q_pos in lost_id:
                    if i == p_pos or i == q_pos:
                        offset += 1
                        continue
                    temp_p = temp_p + d
                    temp_q = temp_q + GN(GN.power_table[i - offset]) * d
                    temp = [temp_p, temp_q] if lost_id[0] == p_pos else [temp_q, temp_p]

            lost_data[0].append(temp[0])
            lost_data[1].append(temp[1])
        return m


if __name__ == "__main__":
    d = Driver(5)
    d.write_data(
        "Singapore Airlines is continuing to build back its North American route network with more flights to more cities across the US, ending an eight-month holding pattern during the pandemic that saw the airline operate only one American route.\nOn the heels of launching its newest route just last week between Singapore and New York, which earned the top spot of the world's longest flight by distance, the flag carrier is doubling down with increased flights to the West Coast. Starting in December, Los Angeles will see an increase in daily flights while San Francisco will see its first scheduled flights since April, both laying the foundation for the airline's post-pandemic recovery.\nThe first flight to San Francisco will depart Singapore on December 15 and return\ntwo days later on December 17. The Bay Area will start with three-times-weekly service departing to Singapore on Mondays, Thursdays, and Saturdays as the airline settles into the new route, which sees a duration of 14 hours and 40 minutes on the outbound leg and 17 hours and 35 minutes on the return. Los Angeles, for its part, will see increased frequencies from three weekly flights to five starting December 2, with service on all days of the week except Thursdays and Saturdays. Singapore Airlines never stopped flying the Singapore-Los Angeles route throughout the pandemic, which became its sole non-stop link to the US. Here!!"
    )
    # d.write_data("hello word!")
    d.disks[0].lost_data()
    print(d.read_data())
