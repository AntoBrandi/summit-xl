
"use strict";

let Axis = require('./Axis.js');
let BatteryDockingStatus = require('./BatteryDockingStatus.js');
let Register = require('./Register.js');
let SubState = require('./SubState.js');
let ptz = require('./ptz.js');
let Pose2DArray = require('./Pose2DArray.js');
let BoolArray = require('./BoolArray.js');
let ReturnMessage = require('./ReturnMessage.js');
let ElevatorStatus = require('./ElevatorStatus.js');
let Interfaces = require('./Interfaces.js');
let alarmmonitor = require('./alarmmonitor.js');
let Alarms = require('./Alarms.js');
let StringArray = require('./StringArray.js');
let MotorsStatus = require('./MotorsStatus.js');
let RobotnikMotorsStatus = require('./RobotnikMotorsStatus.js');
let QueryAlarm = require('./QueryAlarm.js');
let MotorStatus = require('./MotorStatus.js');
let BatteryDockingStatusStamped = require('./BatteryDockingStatusStamped.js');
let Pose2DStamped = require('./Pose2DStamped.js');
let AlarmSensor = require('./AlarmSensor.js');
let inputs_outputs = require('./inputs_outputs.js');
let Cartesian_Euler_pose = require('./Cartesian_Euler_pose.js');
let SafetyModuleStatus = require('./SafetyModuleStatus.js');
let LaserStatus = require('./LaserStatus.js');
let MotorHeadingOffset = require('./MotorHeadingOffset.js');
let MotorPID = require('./MotorPID.js');
let InverterStatus = require('./InverterStatus.js');
let BatteryStatus = require('./BatteryStatus.js');
let LaserMode = require('./LaserMode.js');
let Registers = require('./Registers.js');
let alarmsmonitor = require('./alarmsmonitor.js');
let named_input_output = require('./named_input_output.js');
let encoders = require('./encoders.js');
let named_inputs_outputs = require('./named_inputs_outputs.js');
let State = require('./State.js');
let Data = require('./Data.js');
let BatteryStatusStamped = require('./BatteryStatusStamped.js');
let ElevatorAction = require('./ElevatorAction.js');
let MotorsStatusDifferential = require('./MotorsStatusDifferential.js');
let SetElevatorResult = require('./SetElevatorResult.js');
let SetElevatorFeedback = require('./SetElevatorFeedback.js');
let SetElevatorActionGoal = require('./SetElevatorActionGoal.js');
let SetElevatorGoal = require('./SetElevatorGoal.js');
let SetElevatorActionResult = require('./SetElevatorActionResult.js');
let SetElevatorAction = require('./SetElevatorAction.js');
let SetElevatorActionFeedback = require('./SetElevatorActionFeedback.js');

module.exports = {
  Axis: Axis,
  BatteryDockingStatus: BatteryDockingStatus,
  Register: Register,
  SubState: SubState,
  ptz: ptz,
  Pose2DArray: Pose2DArray,
  BoolArray: BoolArray,
  ReturnMessage: ReturnMessage,
  ElevatorStatus: ElevatorStatus,
  Interfaces: Interfaces,
  alarmmonitor: alarmmonitor,
  Alarms: Alarms,
  StringArray: StringArray,
  MotorsStatus: MotorsStatus,
  RobotnikMotorsStatus: RobotnikMotorsStatus,
  QueryAlarm: QueryAlarm,
  MotorStatus: MotorStatus,
  BatteryDockingStatusStamped: BatteryDockingStatusStamped,
  Pose2DStamped: Pose2DStamped,
  AlarmSensor: AlarmSensor,
  inputs_outputs: inputs_outputs,
  Cartesian_Euler_pose: Cartesian_Euler_pose,
  SafetyModuleStatus: SafetyModuleStatus,
  LaserStatus: LaserStatus,
  MotorHeadingOffset: MotorHeadingOffset,
  MotorPID: MotorPID,
  InverterStatus: InverterStatus,
  BatteryStatus: BatteryStatus,
  LaserMode: LaserMode,
  Registers: Registers,
  alarmsmonitor: alarmsmonitor,
  named_input_output: named_input_output,
  encoders: encoders,
  named_inputs_outputs: named_inputs_outputs,
  State: State,
  Data: Data,
  BatteryStatusStamped: BatteryStatusStamped,
  ElevatorAction: ElevatorAction,
  MotorsStatusDifferential: MotorsStatusDifferential,
  SetElevatorResult: SetElevatorResult,
  SetElevatorFeedback: SetElevatorFeedback,
  SetElevatorActionGoal: SetElevatorActionGoal,
  SetElevatorGoal: SetElevatorGoal,
  SetElevatorActionResult: SetElevatorActionResult,
  SetElevatorAction: SetElevatorAction,
  SetElevatorActionFeedback: SetElevatorActionFeedback,
};
