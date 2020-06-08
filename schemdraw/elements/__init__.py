from .elements import Element, ElementDrawing, Element2Term
from .twoterm import Line, Resistor, ResistorBox, ResistorVar, Capacitor, Capacitor2, CapacitorVar, Diode, Schottky, DiodeTunnel, Zener, LED, LED2, Photodiode, Potentiometer, Diac, Triac, SCR, Memristor, Memristor2, Josephson, Fuse, Arrow, LineDot, Gap, Inductor, Inductor2, Crystal
from .oneterm import Ground, GroundSignal, GroundChassis, Antenna, Vss, Vdd, Dot, Arrowhead, DotDotDot, Label
from .opamp import Opamp
from .sources import Source, SourceV, SourceI, SourceSin, SourceControlled, SourceControlledV, SourceControlledI, BatteryCell, Battery, MeterV, MeterI, MeterA, MeterOhm, Lamp
from .switches import Switch, SwitchSpdt, SwitchSpdt2, Button
from .transistors import NFet, PFet, JFet, JFetN, JFetP, Bjt, BjtNpn, BjtPnp, BjtPnp2c
from .misc import Speaker, Mic, CurrentLabel, CurrentLabelInline, LoopCurrent, Motor
from .xform import Transformer
from .cables import Coax, Triax
from .intcircuits import IcPin, Ic, Multiplexer


from . import legacy
import warnings

def __getattr__(name):
    e = getattr(legacy, name)
    warnings.warn('Dictionary-based elements are deprecated. Update to class-based elements or import from schemdraw.elements.legacy.', DeprecationWarning)
    return e
