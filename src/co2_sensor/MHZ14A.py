#!/usr/bin/env python
# -*- coding: utf-8 -*-

# MIT License 2019 (C) Tiryoh<tiryoh@gmail.com>

# This script is based on https://qiita.com/watiko/items/5cfa2aedd5a67619add0

import rospy
import serial


class MHZ14A():
    PACKET = [0xff, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79]
    ZERO = [0xff, 0x01, 0x87, 0x00, 0x00, 0x00, 0x00, 0x00, 0x78]

    def __init__(self, port, baud=9600, timeout=1):
        try:
            self.serial = serial.Serial(port, baud, timeout=timeout)
            rospy.sleep(2)
        except serial.serialutil.SerialException as e:
            rospy.logerr(e)

    def set_zero(self):
        self.serial.write(bytearray(MHZ14A.ZERO))

    def __get_data(self):
        self.serial.write(bytearray(MHZ14A.PACKET))
        res = self.serial.read(size=9)
        res = bytearray(res)
        checksum = 0xff & (~(res[1] + res[2] + res[3] + res[4] + res[5] + res[6] + res[7]) + 1)
        if res[8] == checksum:
            return (res[2] << 8) | res[3]
        else:
            raise Exception("checksum: " + hex(checksum))

    def get_ppm(self):
        return self.__get_data()

    def get(self):
        return {
            "ppm": self.get_ppm(),
        }

    def close(self):
        try:
            self.serial.close()
        except AttributeError as e:
            rospy.logerr(e)
