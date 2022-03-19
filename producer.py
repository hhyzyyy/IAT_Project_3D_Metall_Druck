# -*- coding: utf-8 -*-

import os
import time
from kafka import KafkaProducer
from kafka import KafkaClient


def start_zookeeper_kafka():
    os.system(r"E:\zookeeper\apache-zookeeper-3.8.0-bin\bin\zkServer.cmd")
    os.system(r"E:\kafka\kafka_2.12-3.1.0\bin\windows\kafka-server-start.bat E:\kafka\kafka_2.12-3.1.0\config\server.properties")


class IatProducer:

    def __init__(self, bootstrap_servers, topic1, topic2):
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers)  # 实例化一个KafkaProducer示例，用于向Kafka投递消息
        # self.client = KafkaClient(bootstrap_servers=bootstrap_servers, request_timeout_ms=3000)
        self.topic1 = topic1
        self.topic2 = topic2

    @staticmethod
    def get_data():
        file_path1 = 'input/Current_20000_with_pulse.txt'
        file_path2 = 'input/Voltage_20000_with_pulse.txt'
        values1, values2 = [], []
        with open(file_path1, 'r') as f, open(file_path2, 'r') as f2:
            tmp = f2.readlines()
            for idx, line in enumerate(f.readlines()):
                line1 = line.strip().split()
                # print(idx, len(tmp))
                line2 = tmp[idx].strip().split()
                values1.append(float(line1[1]))
                values2.append(float(line2[1]))
        return values1, values2

    def send_msg(self):
        print('[INFO] send_msg run!')
        values1, values2 = self.get_data()
        for i, v in enumerate(values1):
            if i % 1 == 0:
                time.sleep(0.001)  # Senden einer Datenzeile alle 0,001 Sekunden (1 Millisekunde)
                time_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                msg1 = str(i) + '&' + str(time_now) + '&' + str(v)
                # msg2 = str(i) + '&' + str(time_now) + '&' + str(v)  # LSTM
                msg2 = str(i) + '&' + str(time_now) + '&' + str(values2[i])
                self.producer.send(topic=self.topic1, value=msg1.encode())  # Daten mit dem Thema 'Current' senden
                self.producer.send(topic=self.topic2, value=msg2.encode())  # Daten mit dem Thema 'Voltage' senden

    def run(self):
        # self.client.delete_topics([self.topic1, self.topic2])
        time.sleep(5)
        self.send_msg()


if __name__ == '__main__':
    print('[INFO] -------------------- Producer run! --------------------')
    IatProducer('localhost:9092', 'Current', 'Voltage').run()
    print('[INFO] -------------------- Consumer done! --------------------')

