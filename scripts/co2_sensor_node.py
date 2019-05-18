#!/usr/bin/env python
# -*- coding: utf-8 -*-

# MIT License 2019 (C) Tiryoh<tiryoh@gmail.com>

import rospy
from co2_sensor.MHZ14A import MHZ14A
from co2_sensor_driver.msg import Co2


def main():
    rospy.init_node("co2_sensor_node")
    pub = rospy.Publisher("co2_sensor_raw", Co2, queue_size=10)
    serial_port = rospy.get_param("/co2_sensor/serial_port") if rospy.has_param("/co2_sensor/serial_port") else "/dev/ttyUSB0"
    baudrate = rospy.get_param("/co2_sensor/serial_baudrate") if rospy.has_param("/co2_sensor/serial_baudrate") else 9600
    timeout = rospy.get_param("/co2_sensor/serial_timeout") if rospy.has_param("/co2_sensor/serial_timeout") else 1
    co2_sensor = MHZ14A(serial_port, baud=baudrate, timeout=timeout)
    rospy.loginfo("init sensor on " + serial_port)
    rospy.on_shutdown(co2_sensor.close)
    r = rospy.Rate(1)
    try:
        while not rospy.is_shutdown():
            sensor_data = Co2()
            sensor_data.header.stamp = rospy.Time.now()
            sensor_data.ppm = co2_sensor.get_ppm()
            pub.publish(sensor_data)
            r.sleep()

    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    main()

