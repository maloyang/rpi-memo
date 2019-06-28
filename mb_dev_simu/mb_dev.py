#!/usr/bin/env python
# -*- coding: utf_8 -*-
'''
1. power meter
2. t/h sensor
3. power meter with float
'''
import sys
import time

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_tcp, hooks
import serial
import modbus_tk.modbus_rtu as modbus_rtu

from struct import *


def main():
    """main"""
    logger = modbus_tk.utils.create_logger(name="console", record_format="%(message)s")


    try:
        '''        
        mb_serial = serial.Serial(port=mb_port, baudrate=baudrate
                            , bytesize=databit, parity=parity, stopbits=stopbit)
        server = modbus_rtu.RtuServer(mb_serial)
        '''
        server = modbus_tcp.TcpServer(1502, '0.0.0.0')
        server.start()

        print("running...")
        print("enter 'quit' for closing the server")

        #-- all tag, 30 sec. data
        array_t = [255, 260, 255, 265, 270
                    , 281, 292, 303, 314, 325
                    , 300, 280, 270, 250, 245]
        array_h = [600, 620, 640, 635, 625
                    , 620, 610, 620, 650, 680
                    , 700, 690, 670, 650, 620]
        array_v = [2243, 2229, 2230, 2252, 2241
                    , 2234, 2246, 2243, 2251, 2220
                    , 2225, 2228, 2236, 2239, 2256
                    , 2242, 2241]
        array_vv = [3882, 3857, 3860, 3867, 3871
                    , 3881, 3885, 3855, 3851, 3861
                    , 3859, 3824, 3840, 3850, 3860
                    , 3870, 3880]
        array_i = [4181, 4462, 4771, 4234, 4374
                    , 4245, 4376, 4567, 4672, 4422
                    , 4344, 4316, 4180, 4357, 4680
                    , 4422, 4534]
        idx = 0
        data_n = len(array_t)

        #- add t/h sensor, 1
        slave = server.add_slave(1)
        slave.add_block('AO', cst.HOLDING_REGISTERS, 0, 1000)
        # t/h tag list:
        #0 1, t
        #1 1, h
        slave.set_values('AO', 0, [array_t[idx], array_h[idx]]) #0.1 degree --> 40.5 degree; 600-->60.0%
        # power meter tag list:
        #10~12 1, V1, V2, V3, 0.1V
        #13~15 1, V12, V23, V13, 0.1V
        #16~18 1, I1, I2, I3, 0.001A
        slave.set_values('AO', 10, [array_v[idx], array_v[idx+1], array_v[idx+2]])
        slave.set_values('AO', 13, [array_vv[idx], array_vv[idx+1], array_vv[idx+2]])
        slave.set_values('AO', 16, [array_i[idx], array_i[idx+1], array_i[idx+2]])

        while True:
            idx = idx+1
            if idx>=data_n:
                idx = 0
            # set value
            slave.set_values('AO', 0, [array_t[idx], array_h[idx]])
            slave.set_values('AO', 10, [array_v[idx], array_v[idx+1], array_v[idx+2]])
            slave.set_values('AO', 13, [array_vv[idx], array_vv[idx+1], array_vv[idx+2]])
            slave.set_values('AO', 16, [array_i[idx], array_i[idx+1], array_i[idx+2]])

            time.sleep(2)
            '''
            cmd = sys.stdin.readline()
            args = cmd.split(' ')

            if cmd.find('quit') == 0:
                sys.stdout.write('bye-bye\r\n')
                break
            else:
                sys.stdout.write("unknown command %s\r\n" % args[0])
            '''
    finally:
        server.stop()


if __name__ == "__main__":
    main()