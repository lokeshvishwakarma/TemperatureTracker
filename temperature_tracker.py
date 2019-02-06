class TempTracker:
    def __init__(self):
        self.temp_list = []

    def insert(self, new_temp):
        self.temp_list.append(new_temp)

    def get_max(self):
        _max = 0.0
        for temp in self.temp_list:
            if temp > _max:
                _max = temp
        return round(_max,2)

    def get_min(self):
        _min = 110.0
        for temp in self.temp_list:
            if temp < _min:
                _min = temp
        return round(_min,2)

    def get_mean(self):
        total = 0.0
        for temp in self.temp_list:
            total += temp
        return round(total/len(self.temp_list))
