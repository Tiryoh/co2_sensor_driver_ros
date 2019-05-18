# co2_sensor_driver_ros

CO2 sensor driver e.g.) MH-Z14A, MH-Z19


## Requirements

* ROS
  * tested on ROS Kinetic

## Installation

```sh
cd ~/catkin_ws/src && git clone https://github.com/Tiryoh/co2_sensor_driver_ros.git
rosdep install -r -y --from-paths co2_sensor_driver_ros
```

```
cd ~/catkin_ws && catkin_make
source ~/catkin_ws/devel/setup.bash
```

## Usage

```sh
roslaunch co2_sensor_driver co2_sensor_driver.launch
```

## License

This repository is licensed under the MIT license, see [LICENSE](./LICENSE).

Unless attributed otherwise, everything in this repository is under the MIT license.
