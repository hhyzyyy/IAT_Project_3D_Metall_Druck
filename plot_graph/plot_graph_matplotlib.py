"""
author:  Huayu Hu
date:    2021/12/27
contact: huayu.hu@campus.tu-berlin.de
"""
import os.path
import numpy as np
import matplotlib.pyplot as plt


class IAT:

    def show_whole_data(self, file_path):
        with open(file_path, 'r') as f:
            tmp_time = []
            tmp_value = []
            for idx, line in enumerate(f.readlines()):
                line = line.strip().split()
                tmp_time.append(float(line[0]))
                tmp_value.append(float(line[1]))

        start_idx = 20000
        end_idx = start_idx + 10000
        print(len(tmp_time), len(tmp_value))
        time, value = tmp_time[start_idx:end_idx], tmp_value[start_idx:end_idx]

        plt.ion()
        step = 200
        for i in range(len(time)):
            if i % step == 0 and i != 0:
                print(i, len(time))
                plt.plot(time[i - step:i], value[i - step:i], c='r')
                plt.pause(0.1)
                plt.draw()
        plt.close('all')

    def plot_graph(self, file_path):
        with open(file_path, 'r') as f:
            tmp_time = []
            tmp_value = []
            for line in f.readlines():
                line = line.strip().split()
                tmp_time.append(float(line[0]))
                tmp_value.append(float(line[1]))
        #         tmp_time = np.array(tmp_time)
        #         tmp_value = np.array(tmp_value)

        fig1, ax1 = plt.subplots(figsize=(500, 15))
        ax1.plot(tmp_time, tmp_value)
        ax1.set_title(os.path.splitext(os.path.basename(file_path))[0])

        fig2, ax2 = plt.subplots(figsize=(10, 5))
        range_start = 10000
        range_end = range_start + 500
        small_time = tmp_time[range_start:range_end]
        small_value = tmp_value[range_start:range_end]
        local_max, local_max_idx = [], []
        step = 30
        for i, v in enumerate(small_value):
            if i % step == 0 and i != 0:
                # ndarray
                #                 local_max.append(small_value[np.argmax(small_value[i-step:i])])
                #                 local_max_idx.append(small_time[np.argmax(small_value[i-step:i])+i])
                # list
                local_max.append(max(small_value[i - step:i]))
                local_max_idx.append(small_time[small_value[i - step:i].index(max(small_value[i - step:i])) + i])

        print(local_max)
        print(local_max_idx)
        ax2.plot(small_time, small_value)
        ax2.set_title(os.path.splitext(os.path.basename(file_path))[0])
        # local_max
        ax2.scatter(local_max_idx, local_max, c='r', label='local_max')
        ax2.legend()

        plt.grid()
        plt.show()

    def run(self):
        file_path = '../input/Current.txt'
        self.show_whole_data(file_path)
        # self.plot_graph(file_path)


if __name__ == '__main__':
    IAT().run()
