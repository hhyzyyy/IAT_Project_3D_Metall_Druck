# -*- encoding:utf-8 -*-

"""
author:  Huayu Hu
date:    2022/1/5
contact: huhuayu@bytedance.com
"""

import os
from functools import reduce
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator


class AnalyseData:

    def __init__(self, input_path, location):
        self.input_path = input_path
        self.location = location
        self.range = 2000

    @staticmethod
    def calc_energy(lt):
        return reduce(lambda x, y: x + y, map(lambda x: x ** 2, lt))

    @staticmethod
    def txt_to_csv(txt_path):
        root, file_name = os.path.split(txt_path)[0], os.path.split(txt_path)[1]
        file_name = os.path.splitext(file_name)[0] + '.csv'
        new_file_path = os.path.join(root, file_name)
        with open(txt_path, 'r') as f, open(new_file_path, 'w') as f2:
            f2.write("time,value\n")
            for idx, line in enumerate(f.readlines()):
                line = line.split()
                f2.write(','.join(line))
                f2.write("\n")
        return new_file_path

    def plot_all_data(self, flag=True):
        new_file_path = self.txt_to_csv(self.input_path)
        dataset = pd.read_csv(new_file_path)
        if flag is True:
            plt.figure(figsize=(22, 15))
            plt.plot(dataset['value'], color='black', linewidth=1, label='True value')
            plt.ylabel("value")
            plt.xlabel("signal")
            plt.title(f"All data")
            # x_major_locator = MultipleLocator(1000)
            # ax = plt.gca()
            # ax.xaxis.set_major_locator(x_major_locator)
            plt.show()
        else:
            for i in range(0, len(dataset['value']), 10000):
                plt.figure(figsize=(22, 15))
                plt.plot(dataset['value'][i-10000:i], color='black', linewidth=1, label='True value')
                plt.ylabel("value")
                plt.xlabel("signal")
                plt.title(f"All data{i}")
                x_major_locator = MultipleLocator(1000)
                ax = plt.gca()
                ax.xaxis.set_major_locator(x_major_locator)
                plt.show()

    def analyse_specific_data(self):
        with open(self.input_path, 'r') as f:
            t = []
            value = []
            start_idx = int(self.location - self.range / 2)
            end_idx = int(self.location + self.range / 2)
            target_area = f.readlines()[start_idx:end_idx]
            for line in target_area:
                line = line.strip().split()
                t.append(line[0])
                value.append(float(line[1]))
        max_value = max(value)
        max_value_idx = value.index(max_value)
        energy = self.calc_energy(value)

        plt.figure(figsize=(18, 10))
        plt.ticklabel_format(style='plain')
        plt.title(os.path.splitext(os.path.basename(self.input_path))[0],
                  fontdict={'weight': 'normal', 'size': 25}, pad=20)

        plt.xlim(start_idx, end_idx)
        plt.plot(range(start_idx, end_idx), value, label='signal, energy=%.f' % energy)

        x_major_locator = MultipleLocator(100)
        ax = plt.gca()
        ax.xaxis.set_major_locator(x_major_locator)

        plt.xlabel(self.location, fontdict={'weight': 'normal', 'size': 20}, labelpad=20)
        plt.ylabel('Amplitude', fontdict={'weight': 'normal', 'size': 20}, labelpad=20)
        plt.scatter(max_value_idx, max_value, c='r', label=f'local_max={max_value}')
        plt.legend(loc='upper right', fontsize='x-large')
        plt.grid(True)
        plt.show()

    def analyse_all_data(self):
        with open(self.input_path, 'r') as f:
            all_lines = f.readlines()
            length_file = len(all_lines)
            energy, sign, v = [''] * (length_file - 1), [''] * (length_file - 1), []
            for idx, line in enumerate(all_lines):
                if idx != 0:
                    line = line.strip().split(',')
                    v.append(float(line[2]))
                    if len(v) % 200 == 0 and len(v) != 0:
                        data = v[-200:]
                        e = self.calc_energy(data)
                        max_idx, min_idx = np.argmax(data), np.argmin(data)
                        # max_value, min_value = data[max_idx], data[min_idx]
                        energy[idx - 100] = e
                        sign[idx - 200 + min_idx] = '-'
                        sign[idx - 200 + max_idx] = '+'
        df = pd.read_csv(self.input_path)
        df['energy'] = energy
        df['min_max'] = sign
        df.to_csv(os.path.join('./output/test.csv'), index=0)


# AnalyseData('/Users/bytedance/iat-project/output/Current.csv', 4000).analyse_specific_data()
# AnalyseData('/Users/bytedance/iat-project/output/Current.csv', 5000).analyse_all_data()
