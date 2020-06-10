# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from robotnik_msgs/RobotnikMotorsStatus.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import robotnik_msgs.msg

class RobotnikMotorsStatus(genpy.Message):
  _md5sum = "40f5305ac2c33d213d54d21bf9ba7fc9"
  _type = "robotnik_msgs/RobotnikMotorsStatus"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Name of each motor drive
string[] name
# CAN ID of each motor drive
int32[] can_id
# Status of the motor drive
robotnik_msgs/MotorStatus[] motor_status


================================================================================
MSG: robotnik_msgs/MotorStatus
string state
string status
string communicationstatus
string statusword
string driveflags
string[] activestatusword
string[] activedriveflags
int32 digitaloutputs
int32 digitalinputs
float32 averagecurrent
float32[] analoginputs

"""
  __slots__ = ['name','can_id','motor_status']
  _slot_types = ['string[]','int32[]','robotnik_msgs/MotorStatus[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       name,can_id,motor_status

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RobotnikMotorsStatus, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.name is None:
        self.name = []
      if self.can_id is None:
        self.can_id = []
      if self.motor_status is None:
        self.motor_status = []
    else:
      self.name = []
      self.can_id = []
      self.motor_status = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.name)
      buff.write(_struct_I.pack(length))
      for val1 in self.name:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.can_id)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.can_id))
      length = len(self.motor_status)
      buff.write(_struct_I.pack(length))
      for val1 in self.motor_status:
        _x = val1.state
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.status
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.communicationstatus
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.statusword
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.driveflags
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.activestatusword)
        buff.write(_struct_I.pack(length))
        for val2 in val1.activestatusword:
          length = len(val2)
          if python3 or type(val2) == unicode:
            val2 = val2.encode('utf-8')
            length = len(val2)
          buff.write(struct.pack('<I%ss'%length, length, val2))
        length = len(val1.activedriveflags)
        buff.write(_struct_I.pack(length))
        for val2 in val1.activedriveflags:
          length = len(val2)
          if python3 or type(val2) == unicode:
            val2 = val2.encode('utf-8')
            length = len(val2)
          buff.write(struct.pack('<I%ss'%length, length, val2))
        _x = val1
        buff.write(_get_struct_2if().pack(_x.digitaloutputs, _x.digitalinputs, _x.averagecurrent))
        length = len(val1.analoginputs)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(struct.pack(pattern, *val1.analoginputs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.motor_status is None:
        self.motor_status = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.name = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.name.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.can_id = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.motor_status = []
      for i in range(0, length):
        val1 = robotnik_msgs.msg.MotorStatus()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.state = str[start:end].decode('utf-8')
        else:
          val1.state = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.status = str[start:end].decode('utf-8')
        else:
          val1.status = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.communicationstatus = str[start:end].decode('utf-8')
        else:
          val1.communicationstatus = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.statusword = str[start:end].decode('utf-8')
        else:
          val1.statusword = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.driveflags = str[start:end].decode('utf-8')
        else:
          val1.driveflags = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.activestatusword = []
        for i in range(0, length):
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2 = str[start:end].decode('utf-8')
          else:
            val2 = str[start:end]
          val1.activestatusword.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.activedriveflags = []
        for i in range(0, length):
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2 = str[start:end].decode('utf-8')
          else:
            val2 = str[start:end]
          val1.activedriveflags.append(val2)
        _x = val1
        start = end
        end += 12
        (_x.digitaloutputs, _x.digitalinputs, _x.averagecurrent,) = _get_struct_2if().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.analoginputs = struct.unpack(pattern, str[start:end])
        self.motor_status.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.name)
      buff.write(_struct_I.pack(length))
      for val1 in self.name:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.can_id)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.can_id.tostring())
      length = len(self.motor_status)
      buff.write(_struct_I.pack(length))
      for val1 in self.motor_status:
        _x = val1.state
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.status
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.communicationstatus
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.statusword
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.driveflags
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.activestatusword)
        buff.write(_struct_I.pack(length))
        for val2 in val1.activestatusword:
          length = len(val2)
          if python3 or type(val2) == unicode:
            val2 = val2.encode('utf-8')
            length = len(val2)
          buff.write(struct.pack('<I%ss'%length, length, val2))
        length = len(val1.activedriveflags)
        buff.write(_struct_I.pack(length))
        for val2 in val1.activedriveflags:
          length = len(val2)
          if python3 or type(val2) == unicode:
            val2 = val2.encode('utf-8')
            length = len(val2)
          buff.write(struct.pack('<I%ss'%length, length, val2))
        _x = val1
        buff.write(_get_struct_2if().pack(_x.digitaloutputs, _x.digitalinputs, _x.averagecurrent))
        length = len(val1.analoginputs)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(val1.analoginputs.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.motor_status is None:
        self.motor_status = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.name = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.name.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.can_id = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.motor_status = []
      for i in range(0, length):
        val1 = robotnik_msgs.msg.MotorStatus()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.state = str[start:end].decode('utf-8')
        else:
          val1.state = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.status = str[start:end].decode('utf-8')
        else:
          val1.status = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.communicationstatus = str[start:end].decode('utf-8')
        else:
          val1.communicationstatus = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.statusword = str[start:end].decode('utf-8')
        else:
          val1.statusword = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.driveflags = str[start:end].decode('utf-8')
        else:
          val1.driveflags = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.activestatusword = []
        for i in range(0, length):
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2 = str[start:end].decode('utf-8')
          else:
            val2 = str[start:end]
          val1.activestatusword.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.activedriveflags = []
        for i in range(0, length):
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2 = str[start:end].decode('utf-8')
          else:
            val2 = str[start:end]
          val1.activedriveflags.append(val2)
        _x = val1
        start = end
        end += 12
        (_x.digitaloutputs, _x.digitalinputs, _x.averagecurrent,) = _get_struct_2if().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.analoginputs = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
        self.motor_status.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2if = None
def _get_struct_2if():
    global _struct_2if
    if _struct_2if is None:
        _struct_2if = struct.Struct("<2if")
    return _struct_2if
