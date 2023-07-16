"""
体现距离与测距周期之间的关系
"""

import cflib.crtp
import numpy as np
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
import time
import logging
import pandas as pd
from multiprocessing import Process
import utils

logging.basicConfig(level=logging.ERROR)

URI0 = 'usb://0'
URI1 = 'radio://0/80/2M/E7E7E7E7E1'
URI2 = 'radio://0/80/2M/E7E7E7E7E2'
URI3 = 'radio://0/3/2M'
URI4 = 'radio://0/4/2M'
URI5 = 'radio://0/5/2M'
URI6 = 'radio://0/6/2M'
URI7 = 'radio://0/7/2M'
URI8 = 'radio://0/8/2M'
URI9 = 'radio://0/9/2M'
URI24 = 'radio://0/24/2M/E7E7E7E7E4'
URI26 = 'radio://0/26/2M/E7E7E7E7E6'

if __name__ == '__main__':
    # log_var = {
    #     'total': 'uint16_t',
    #     'distTo1': 'uint16_t',
    #     'distTo2': 'uint16_t',
    #     'distTo3': 'uint16_t',
    #     'distTo4': 'uint16_t',
    # }
    log_var = {
        # 'index': 'uint8_t',
        # 't0index':'uint8_t',
        # 't0inter':'uint16_t'
        #----------------周期随机化测试------------#
        # 'index0': 'uint8_t',
        # 'interval0': 'uint16_t',
        # 'diff0': 'uint8_t',
        # 'index2': 'uint8_t',
        # 'interval2': 'uint16_t',
        # 'diff2': 'uint8_t',
        # 'discount':'uint8_t',
        # 'disTrue':'uint8_t'
        #----------------周期随机化测试------------#
        #----------------丢包率及距离------------#
        # 'distTo0':'uint16_t',
        # 'lossNum5':'uint32_t',
        # 'recvNum5':'uint32_t',
        # 'distNum5':'uint32_t',
        # 'index3': 'uint8_t',
        # 'interval5': 'uint16_t',
        'diff5': 'uint8_t',
    }

    # utils.log_ranging(link_uri=URI24, log_cfg_name='TSranging', log_save_path='./data/dw1000testNew.csv',
    #                   log_var=log_var, period_in_ms=100, keep_time_in_s=15)
    utils.log_ranging(link_uri=URI1, log_cfg_name='Ranging', log_save_path='./data/dw1000NodeTest4.csv',
                      log_var=log_var, period_in_ms=10, keep_time_in_s=200)
