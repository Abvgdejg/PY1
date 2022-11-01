# automatically generated by the FlatBuffers compiler, do not modify

# namespace: fbs

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Dimension(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsDimension(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Dimension()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def DimensionBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x4F\x52\x54\x4D", size_prefixed=size_prefixed)

    # Dimension
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Dimension
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from ort_flatbuffers_py.experimental.fbs.DimensionValue import DimensionValue
            obj = DimensionValue()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Dimension
    def Denotation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def DimensionStart(builder): builder.StartObject(2)
def DimensionAddValue(builder, value): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def DimensionAddDenotation(builder, denotation): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(denotation), 0)
def DimensionEnd(builder): return builder.EndObject()
