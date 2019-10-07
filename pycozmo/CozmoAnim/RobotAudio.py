# automatically generated by the FlatBuffers compiler, do not modify

# namespace: CozmoAnim

import flatbuffers

class RobotAudio(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsRobotAudio(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = RobotAudio()
        x.Init(buf, n + offset)
        return x

    # RobotAudio
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # RobotAudio
    def TriggerTimeMs(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # RobotAudio
    def AudioEventId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # RobotAudio
    def AudioEventIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # RobotAudio
    def AudioEventIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # RobotAudio
    def Volume(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 1.0

    # RobotAudio
    def Probability(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # RobotAudio
    def ProbabilityAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float32Flags, o)
        return 0

    # RobotAudio
    def ProbabilityLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # RobotAudio
    def HasAlts(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return True

def RobotAudioStart(builder): builder.StartObject(5)
def RobotAudioAddTriggerTimeMs(builder, triggerTimeMs): builder.PrependUint32Slot(0, triggerTimeMs, 0)
def RobotAudioAddAudioEventId(builder, audioEventId): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(audioEventId), 0)
def RobotAudioStartAudioEventIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def RobotAudioAddVolume(builder, volume): builder.PrependFloat32Slot(2, volume, 1.0)
def RobotAudioAddProbability(builder, probability): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(probability), 0)
def RobotAudioStartProbabilityVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def RobotAudioAddHasAlts(builder, hasAlts): builder.PrependBoolSlot(4, hasAlts, 1)
def RobotAudioEnd(builder): return builder.EndObject()