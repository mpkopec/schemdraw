''' Operation amplifier '''
from __future__ import annotations
from typing import Optional
import math

from .elements import Element, gap
from ..segments import Segment


oa_back = 2.5
oa_xlen = oa_back * math.sqrt(3)/2
oa_lblx = oa_xlen/8
oa_pluslen = .2


class Opamp(Element):
    ''' Operational Amplifier.

        Keyword Args:
            sign: Draw +/- labels at each input
            leads: Draw short leads on input/output

        Anchors:
            * in1
            * in2
            * out
            * vd
            * vs
            * n1
            * n2
            * n1a
            * n2a
    '''
    _element_defaults = {
        'sign': True,
        'leads': False
    }
    def __init__(self,
                 sign: Optional[bool] = None,
                 leads: Optional[bool] = None,
                 **kwargs):
        super().__init__(**kwargs)
        leadlen = oa_back/4
        x = 0 if not self.params['leads'] else leadlen

        self.segments.append(Segment(
            [(x, 0), (x, oa_back/2), (x+oa_xlen, 0), (x, -oa_back/2), (x, 0),
             gap, (x+oa_xlen, 0)]))

        if self.params['sign']:
            self.segments.append(Segment(
                [(x+oa_lblx-oa_pluslen/2, oa_back/4),
                 (x+oa_lblx+oa_pluslen/2, oa_back/4)]))
            self.segments.append(Segment(
                [(x+oa_lblx-oa_pluslen/2, -oa_back/4),
                 (x+oa_lblx+oa_pluslen/2, -oa_back/4)]))
            self.segments.append(Segment(
                [(x+oa_lblx, -oa_back/4-oa_pluslen/2),
                 (x+oa_lblx, -oa_back/4+oa_pluslen/2)]))

        if self.params['leads']:
            self.segments.append(Segment([(0, oa_back/4), (leadlen, oa_back/4)]))
            self.segments.append(Segment([(0, -oa_back/4), (leadlen, -oa_back/4)]))
            self.segments.append(Segment([(leadlen+oa_xlen, 0), (oa_xlen + 2*leadlen, 0)]))

        self.anchors['out'] = (oa_xlen+2*x, 0)
        self.anchors['in1'] = (0, oa_back/4)
        self.anchors['in2'] = (0, -oa_back/4)
        self.anchors['center'] = (x+oa_xlen/2, 0)
        self.anchors['vd'] = (x+oa_xlen/3, .84)
        self.anchors['vs'] = (x+oa_xlen/3, -.84)
        self.anchors['n1'] = (x+oa_xlen*2/3, -.42)
        self.anchors['n2'] = (x+oa_xlen*2/3, .42)
        self.anchors['n1a'] = (x+oa_xlen*.9, -.13)
        self.anchors['n2a'] = (x+oa_xlen*.9, .13)
        self.elmparams['drop'] = (2*x+oa_xlen, 0)
