# -*- encoding:utf-8 -*-

"""
author:  Huayu Hu
date:    2022/1/4
contact: huhuayu@bytedance.com
"""
import copy
import json
import os
import numpy as np
from matplotlib import pyplot as plt
from analyse_data import AnalyseData
from plot_graph import plot_graph_pyqtgraph


def split_txt_file(file_path):
    """split .txt file"""
    start_lines = 0
    lines = 20000
    output_path = f'input/Current_{lines}_with_pulse.txt'
    with open(file_path, 'r') as f, open(output_path, 'w') as f2:
        for idx, line in enumerate(f.readlines()):
            if start_lines <= idx <= lines+start_lines:
                f2.write(line)
            elif idx > lines+start_lines:
                break
    print('[INFO] split_txt_file done!')


def get_data(path):
    with open(path, 'r') as f:
        time, value = [], []
        for idx, line in enumerate(f.readlines()):
            line = line.strip().split()
            time.append(float(line[0]))
            value.append(float(line[1]))
    return time, value


def save_data_point(tmp, idx, v):
    t = np.array(copy.deepcopy(tmp[-200:]))
    t = t - t[0]
    if abs(t.sum()) < 5 and v > 250:
        print('idx', idx, v)


def anomaly_detection(input_path):
    tmp = [888]
    with open(input_path, 'r') as f:
        for idx, line in enumerate(f.readlines()):
            line = float(line.split()[1])
            if tmp[-1] == line and tmp[-1] != 0 and idx > 200:
                save_data_point(tmp, idx, line)
            tmp.append(line)


def save_data_to_json(input_path, output_file_name):
    tmp = []
    start_lines = 66595
    lines = 1000
    with open(input_path, 'r') as f, open(os.path.join('output/json_files', output_file_name + '.json'), 'w') as json_f:
        for idx, line in enumerate(f.readlines()[start_lines: start_lines + lines]):
            line = float(line.split()[1])
            tmp.append(line)
        json.dump({output_file_name: tmp}, json_f)


def auto_plot():
    location_file = r'E:\Huayu\Study\Master\TU_Berlin\2.Semester\IAT_Projekt_06_WS_2122\git\iat-project\LSTM\Location.txt'
    with open(location_file, 'r') as f:
        for idx, line in enumerate(f.readlines()):
            loc = int(line.split()[1])
            AnalyseData(file_path, loc).analyse_specific_data()


def build_dataset():
    location_file = r'E:\Huayu\Study\Master\TU_Berlin\2.Semester\IAT_Projekt_06_WS_2122\git\iat-project\LSTM\input\LocationOfZundfehler.txt'
    with open(file_path, 'r') as f:
        data = []
        for idx, line in enumerate(f.readlines()):
            data.append(line.split()[1])

    with open(location_file, 'r') as f2:
        count = 1
        for idx, line in enumerate(f2.readlines()):
            line = line.split()
            if len(line) == 2 and idx != 0:
                with open(rf'E:\Huayu\Study\Master\TU_Berlin\2.Semester\IAT_Projekt_06_WS_2122\git\iat-project\LSTM\dataset\zundfehler\signal\{count}.txt', 'w') as s:
                    print(line)
                    s.write(','.join(data[int(line[0]): int(line[1])]))
                    count += 1


def check_signal():
    dir_path = r'E:\Huayu\Study\Master\TU_Berlin\2.Semester\IAT_Projekt_06_WS_2122\git\iat-project\LSTM\dataset\zundfehler\signal'
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            fp = os.path.join(root, file)
            with open(fp, 'r') as f:
                for line in f.readlines():
                    line = line.split(',')
                    v = [float(v) for v in line]
                    plt.figure(figsize=(18, 10))
                    plt.plot(range(len(v)), v)
                    plt.xlabel(file, fontdict={'weight': 'normal', 'size': 20}, labelpad=20)
                    plt.grid(True)
                    plt.show()


def calculation():
    for i in range(121, 150):
        print(i**2)


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


def remove_zundfehler():
    location_file = r'E:\Huayu\Study\Master\TU_Berlin\2.Semester\IAT_Projekt_06_WS_2122\git\iat-project\LSTM\input\LocationOfZundfehler.txt'
    location_file_enlarge = location_file.replace("LocationOfZundfehler", "LocationOfZundfehlerEnlarge")

    # 扩大zundfehler的范围
    # with open(location_file, 'r') as f, open(location_file_enlarge, 'w') as f2:
    #     for idx, line in enumerate(f.readlines()):
    #         line = line.split()
    #         if len(line) == 2 and idx != 0:
    #             start, end = int(line[0]), int(line[1])
    #             start = start - 20
    #             end = end + 20
    #             f2.write(f"{start} {end}\n")

    zund_path = 'input/standing_query/zund.txt'
    t, zund = get_data(zund_path)
    len_of_zund = len(zund)
    t, v = get_data(file_path)
    with open(location_file_enlarge, 'r') as f, open(f'input/Current_without_zundfehler.txt', 'w') as f2:
        for line in f.readlines():
            line = line.split()
            start, end = int(line[0]), int(line[1])
            len_of_zundfehler = end - start
            tmp = [zund[-1]] * (len_of_zundfehler-len_of_zund)
            zund += tmp
            v[start:end] = zund
        for idx, value in enumerate(v):
            f2.write(f"{idx} {value}\n")


def merge_txt_to_csv():
    pos_path = 'input/others/Current_only_CMT_pos.txt'
    output_path = 'input/others/merge_current.txt'
    with open(file_path, 'r') as f, open(output_path, 'w') as f2, open(pos_path, 'r') as f3:
        tmp = copy.deepcopy(f.readlines())
        for idx, line in enumerate(f3.readlines()):
            line = line.split()
            start_lines, end_lines = int(line[0]), int(line[1])
            # print(tmp[start_lines:end_lines], type(tmp[start_lines:end_lines]))
            f2.write(''.join(tmp[start_lines:end_lines]))


# file_path = r'E:\Huayu\Study\Master\TU_Berlin\2.Semester\IAT_Projekt_06_WS_2122\git\iat-project\input\Datensätze\Kamerasystem 2\V2-Baustahl\Prozessdaten\Current.txt'
file_path = 'input/Current_20000_with_pulse.txt'
# save_data_to_json(file_path, 'Spritzer')
# split_txt_file(file_path)                               # 分割txt
# anomaly_detection(file_path)
# AnalyseData(file_path, 3241).analyse_specific_data()    # 画出特定数据的图片
AnalyseData(file_path, 0).plot_all_data(flag=True)      # 画出所有数据的图片
# auto_plot()
# build_dataset()
# check_signal()
# calculation()
# txt_to_csv(file_path)                                   # txt 转成csv文件
# remove_zundfehler()
# merge_txt_to_csv()                                      # 合并txt




