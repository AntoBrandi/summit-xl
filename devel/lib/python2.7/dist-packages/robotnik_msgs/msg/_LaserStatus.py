# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from robotnik_msgs/LaserStatus.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class LaserStatus(genpy.Message):
  _md5sum = "59f57d3a0c4aa9b97dcd8bd40152ebb4"
  _type = "robotnik_msgs/LaserStatus"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """string name
bool detecting_obstacles
bool contaminated
bool free_warning
# one input per each warning zone.
# first areas are closer to the robot (i.e. more restrictive)
bool[] warning_zones 
"""
  __slots__ = ['name','detecting_obstacles','contaminated','free_warning','warning_zones']
  _slot_types = ['string','bool','bool','bool','bool[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       name,detecting_obstacles,contaminated,free_warning,warning_zones

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LaserStatus, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.name is None:
        self.name = ''
      if self.detecting_obstacles is None:
        self.detecting_obstacles = False
      if self.contaminated is None:
        self.contaminated = False
      if self.free_warning is None:
        self.free_warning = False
      if self.warning_zones is None:
        self.warning_zones = []
    else:
      self.name = ''
      self.detecting_obstacles = False
      self.contaminated = False
      self.free_warning = False
      self.warning_zones = []

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
      _x = self.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3B().pack(_x.detecting_obstacles, _x.contaminated, _x.free_warning))
      length = len(self.warning_zones)
      buff.write(_struct_I.pack(length))
      pattern = '<%sB'%length
      buff.write(struct.pack(pattern, *self.warning_zones))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.name = str[start:end].decode('utf-8')
      else:
        self.name = str[start:end]
      _x = self
      start = end
      end += 3
      (_x.detecting_obstacles, _x.contaminated, _x.free_warning,) = _get_struct_3B().unpack(str[start:end])
      self.detecting_obstacles = bool(self.detecting_obstacles)
      self.contaminated = bool(self.contaminated)
      self.free_warning = bool(self.free_warning)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sB'%length
      start = end
      end += struct.calcsize(pattern)
      self.warning_zones = struct.unpack(pattern, str[start:end])
      self.warning_zones = list(map(bool, self.warning_zones))
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
      _x = self.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3B().pack(_x.detecting_obstacles, _x.contaminated, _x.free_warning))
      length = len(self.warning_zones)
      buff.write(_struct_I.pack(length))
      pattern = '<%sB'%length
      buff.write(self.warning_zones.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.name = str[start:end].decode('utf-8')
      else:
        self.name = str[start:end]
      _x = self
      start = end
      end += 3
      (_x.detecting_obstacles, _x.contaminated, _x.free_warning,) = _get_struct_3B().unpack(str[start:end])
      self.detecting_obstacles = bool(self.detecting_obstacles)
      self.contaminated = bool(self.contaminated)
      self.free_warning = bool(self.free_warning)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sB'%length
      start = end
      end += struct.calcsize(pattern)
      self.warning_zones = numpy.frombuffer(str[start:end], dtype=numpy.bool, count=length)
      self.warning_zones = list(map(bool, self.warning_zones))
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3B = None
def _get_struct_3B():
    global _struct_3B
    if _struct_3B is None:
        _struct_3B = struct.Struct("<3B")
    return _struct_3B
