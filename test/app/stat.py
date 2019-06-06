#Reducing boiler plate and cleaning up

from collections import defaultdict

class Starlist(list):
    def mean(self):
        return sum(self)/len(self)

    def median(self):
        if len(self) % 2:
            return self[int(len(self)/2)]
        else:
            idx = int(len(self)/2)
            return (self[idx] + self[idx -1])/2

    def mode(self):
        freqs = defaultdict(int)
        for item in self:
            freqs[item] += 1

        mode_freqs = max(freqs.values())
        modes = []
        for item, value in freqs.items():
            if value == mode_freqs:
                modes.append(item)
                return modes
 