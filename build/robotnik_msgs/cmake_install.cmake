# Install script for directory: /home/legion/summit-xl/src/robotnik_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/legion/summit-xl/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robotnik_msgs/msg" TYPE FILE FILES
    "/home/legion/summit-xl/src/robotnik_msgs/msg/encoders.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/inputs_outputs.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/ptz.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/Data.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/Interfaces.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/Axis.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/AlarmSensor.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/Alarms.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/MotorStatus.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/MotorsStatus.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/State.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/BatteryStatus.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/BatteryStatusStamped.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/MotorHeadingOffset.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/MotorsStatusDifferential.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/InverterStatus.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/RobotnikMotorsStatus.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/ElevatorAction.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/ElevatorStatus.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/Cartesian_Euler_pose.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/alarmmonitor.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/alarmsmonitor.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/named_inputs_outputs.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/named_input_output.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/Register.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/Registers.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/StringArray.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/LaserMode.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/LaserStatus.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/SafetyModuleStatus.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/SubState.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/QueryAlarm.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/BatteryDockingStatus.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/BatteryDockingStatusStamped.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/BoolArray.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/MotorPID.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/Pose2DArray.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/Pose2DStamped.msg"
    "/home/legion/summit-xl/src/robotnik_msgs/msg/ReturnMessage.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robotnik_msgs/srv" TYPE FILE FILES
    "/home/legion/summit-xl/src/robotnik_msgs/srv/get_digital_input.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/set_analog_output.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/set_mode.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/set_ptz.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/get_mode.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/set_digital_output.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/set_odometry.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/set_height.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/enable_disable.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/home.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/axis_record.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/set_float_value.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/SetMotorStatus.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/SetElevator.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/get_alarms.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/ack_alarm.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/set_modbus_register.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/get_modbus_register.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/GetBool.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/set_CartesianEuler_pose.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/set_named_digital_output.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/SetLaserMode.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/ResetFromSubState.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/QueryAlarms.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/SetNamedDigitalOutput.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/InsertTask.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/SetMotorPID.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/SetMotorMode.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/SetBuzzer.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/SetEncoderTurns.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/GetMotorsHeadingOffset.srv"
    "/home/legion/summit-xl/src/robotnik_msgs/srv/SetByte.srv"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robotnik_msgs/action" TYPE FILE FILES "/home/legion/summit-xl/src/robotnik_msgs/action/SetElevator.action")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robotnik_msgs/msg" TYPE FILE FILES
    "/home/legion/summit-xl/devel/share/robotnik_msgs/msg/SetElevatorAction.msg"
    "/home/legion/summit-xl/devel/share/robotnik_msgs/msg/SetElevatorActionGoal.msg"
    "/home/legion/summit-xl/devel/share/robotnik_msgs/msg/SetElevatorActionResult.msg"
    "/home/legion/summit-xl/devel/share/robotnik_msgs/msg/SetElevatorActionFeedback.msg"
    "/home/legion/summit-xl/devel/share/robotnik_msgs/msg/SetElevatorGoal.msg"
    "/home/legion/summit-xl/devel/share/robotnik_msgs/msg/SetElevatorResult.msg"
    "/home/legion/summit-xl/devel/share/robotnik_msgs/msg/SetElevatorFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robotnik_msgs/cmake" TYPE FILE FILES "/home/legion/summit-xl/build/robotnik_msgs/catkin_generated/installspace/robotnik_msgs-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/legion/summit-xl/devel/include/robotnik_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/legion/summit-xl/devel/share/roseus/ros/robotnik_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/legion/summit-xl/devel/share/common-lisp/ros/robotnik_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/legion/summit-xl/devel/share/gennodejs/ros/robotnik_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/legion/summit-xl/devel/lib/python2.7/dist-packages/robotnik_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/legion/summit-xl/devel/lib/python2.7/dist-packages/robotnik_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/legion/summit-xl/build/robotnik_msgs/catkin_generated/installspace/robotnik_msgs.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robotnik_msgs/cmake" TYPE FILE FILES "/home/legion/summit-xl/build/robotnik_msgs/catkin_generated/installspace/robotnik_msgs-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robotnik_msgs/cmake" TYPE FILE FILES
    "/home/legion/summit-xl/build/robotnik_msgs/catkin_generated/installspace/robotnik_msgsConfig.cmake"
    "/home/legion/summit-xl/build/robotnik_msgs/catkin_generated/installspace/robotnik_msgsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robotnik_msgs" TYPE FILE FILES "/home/legion/summit-xl/src/robotnik_msgs/package.xml")
endif()

