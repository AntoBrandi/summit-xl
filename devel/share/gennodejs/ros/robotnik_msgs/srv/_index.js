
"use strict";

let SetElevator = require('./SetElevator.js')
let ack_alarm = require('./ack_alarm.js')
let SetMotorMode = require('./SetMotorMode.js')
let ResetFromSubState = require('./ResetFromSubState.js')
let SetByte = require('./SetByte.js')
let GetMotorsHeadingOffset = require('./GetMotorsHeadingOffset.js')
let enable_disable = require('./enable_disable.js')
let SetNamedDigitalOutput = require('./SetNamedDigitalOutput.js')
let SetMotorStatus = require('./SetMotorStatus.js')
let axis_record = require('./axis_record.js')
let get_digital_input = require('./get_digital_input.js')
let get_modbus_register = require('./get_modbus_register.js')
let set_digital_output = require('./set_digital_output.js')
let InsertTask = require('./InsertTask.js')
let SetBuzzer = require('./SetBuzzer.js')
let SetLaserMode = require('./SetLaserMode.js')
let get_alarms = require('./get_alarms.js')
let set_ptz = require('./set_ptz.js')
let SetEncoderTurns = require('./SetEncoderTurns.js')
let set_odometry = require('./set_odometry.js')
let set_analog_output = require('./set_analog_output.js')
let get_mode = require('./get_mode.js')
let GetBool = require('./GetBool.js')
let set_CartesianEuler_pose = require('./set_CartesianEuler_pose.js')
let set_modbus_register = require('./set_modbus_register.js')
let home = require('./home.js')
let set_height = require('./set_height.js')
let SetMotorPID = require('./SetMotorPID.js')
let set_float_value = require('./set_float_value.js')
let set_named_digital_output = require('./set_named_digital_output.js')
let set_mode = require('./set_mode.js')
let QueryAlarms = require('./QueryAlarms.js')

module.exports = {
  SetElevator: SetElevator,
  ack_alarm: ack_alarm,
  SetMotorMode: SetMotorMode,
  ResetFromSubState: ResetFromSubState,
  SetByte: SetByte,
  GetMotorsHeadingOffset: GetMotorsHeadingOffset,
  enable_disable: enable_disable,
  SetNamedDigitalOutput: SetNamedDigitalOutput,
  SetMotorStatus: SetMotorStatus,
  axis_record: axis_record,
  get_digital_input: get_digital_input,
  get_modbus_register: get_modbus_register,
  set_digital_output: set_digital_output,
  InsertTask: InsertTask,
  SetBuzzer: SetBuzzer,
  SetLaserMode: SetLaserMode,
  get_alarms: get_alarms,
  set_ptz: set_ptz,
  SetEncoderTurns: SetEncoderTurns,
  set_odometry: set_odometry,
  set_analog_output: set_analog_output,
  get_mode: get_mode,
  GetBool: GetBool,
  set_CartesianEuler_pose: set_CartesianEuler_pose,
  set_modbus_register: set_modbus_register,
  home: home,
  set_height: set_height,
  SetMotorPID: SetMotorPID,
  set_float_value: set_float_value,
  set_named_digital_output: set_named_digital_output,
  set_mode: set_mode,
  QueryAlarms: QueryAlarms,
};
