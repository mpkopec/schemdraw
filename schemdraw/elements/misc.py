''' Other elements '''
from __future__ import annotations
from typing import Optional
from .elements import Element, Element2Term, gap
from .twoterm import resheight
from ..segments import Segment, SegmentPoly, SegmentArc, SegmentCircle


class Speaker(Element):
    ''' Speaker element with two inputs.

        Anchors:
            * in1
            * in2
    '''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        sph = .5
        self.segments.append(Segment([(0, 0), (resheight, 0)]))
        self.segments.append(Segment([(0, -sph), (resheight, -sph)]))
        self.segments.append(SegmentPoly(
            [(resheight, sph/2), (resheight, -sph*1.5),
             (resheight*2, -sph*1.5), (resheight*2, sph/2)]))
        self.segments.append(SegmentPoly(
            [(resheight*2, sph/2), (resheight*3.5, sph*1.25),
             (resheight*3.5, -sph*2.25), (resheight*2, -sph*1.5)],
            closed=False))
        self.anchors['in1'] = (0, 0)
        self.anchors['in2'] = (0, -sph)
        self.params['drop'] = (0, -sph)


class Mic(Element):
    ''' Microphone element with two inputs.

        Anchors:
            * in1
            * in2
    '''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        sph = .5
        self.segments.append(Segment(  # Upper lead
            [(0, 0), (resheight, 0)]))
        self.segments.append(Segment(  # Lower lead
            [(0, -sph), (resheight, -sph)]))
        self.segments.append(Segment(  # Vertical flat
            [(-resheight*2, resheight), (-resheight*2, -resheight*3)]))
        self.segments.append(SegmentArc(
            (-resheight*2, -resheight), theta1=270, theta2=90,
            width=resheight*4, height=resheight*4))
        self.anchors['in1'] = (resheight, 0)
        self.anchors['in2'] = (resheight, -sph)
        self.params['drop'] = (0, -sph)


class Motor(Element2Term):
    ''' Motor '''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        mw = .22
        self.segments.append(Segment(
            [(-mw, 0), (-mw, 0), gap, (1+mw, 0), (1+mw, 0)]))
        self.segments.append(Segment(
            [(0, -mw), (0-mw, -mw), (0-mw, mw), (0, mw)]))
        self.segments.append(Segment(
            [(1, -mw), (1+mw, -mw), (1+mw, mw), (1, mw)]))
        self.segments.append(SegmentCircle((0.5, 0), 0.5))


class AudioJack(Element):
    ''' Audio Jack with 2 or 3 connectors and optional switches.

        Args:
            ring: Show ring (third conductor) contact
            switch: Show switch on tip contact
            ringswitch: Show switch on ring contact
            dots: Show connector dots
            radius: Radius of connector dots [default: 0.075]

        Anchors:
            * tip
            * sleeve
            * ring
            * ringswitch
            * tipswitch
    '''
    _element_defaults = {
        'radius': 0.075,
        'open': True
    }
    def __init__(self,
                 radius: Optional[float] = None,
                 ring: bool = False,
                 ringswitch: bool = False,
                 dots: bool = True,
                 switch: bool = False,
                 open: Optional[bool] = None,
                 **kwargs):
        super().__init__(**kwargs)
        fill = 'bg' if self.params['open'] else None
        r = self.params['radius']

        length = 2.0
        ringlen = .75
        tiplen = .55
        swidth = .2
        sleeveheight = 1.0
        tipy = 1.0
        ringy = .1
        sleevey = .35
        swdy = .4
        swlen = .5

        if switch:
            tipy += .2

        if ring and ringswitch:
            sleevey += .2
            ringy -= .2

        if ring:
            if dots:
                self.segments.append(SegmentCircle((0, -sleevey), r,
                                                   fill=fill, zorder=4))
            self.segments.append(Segment(
                [(-r, -sleevey), (-length, -sleevey),
                 (-length, 0), (-length, sleeveheight),
                 (-length-swidth, sleeveheight),
                 (-length-swidth, 0), (-length, 0)]))
            self.anchors['sleeve'] = (0, -sleevey)

            if dots:
                self.segments.append(SegmentCircle(
                    (0,  ringy), r, fill=fill, zorder=4))
            self.segments.append(Segment(
                [(-r, ringy), (-length*.75, ringy),
                 (-length*ringlen-2*r, ringy+2*r),
                 (-length*ringlen-r*4, ringy)]))
            self.anchors['ring'] = (0, ringy)

        else:
            if dots:
                self.segments.append(SegmentCircle(
                    (0, 0), r, fill=fill, zorder=4))
            self.segments.append(Segment(
                [(-r, 0), (-length, 0), (-length, sleeveheight),
                 (-length+swidth, sleeveheight), (-length+swidth, 0)]))
            self.anchors['sleeve'] = (0, 0)

        if dots:
            self.segments.append(SegmentCircle(
                (0, tipy), r, fill=fill, zorder=4))
        self.segments.append(Segment(
            [(-r, tipy), (-length*.55, tipy),
             (-length*tiplen-2*r, tipy-2*r),
             (-length*tiplen-r*4, tipy)]))
        self.anchors['tip'] = (0, tipy)

        if switch:
            if dots:
                self.segments.append(SegmentCircle(
                    (0, tipy-swdy), r, fill=fill, zorder=4))
            self.segments.append(Segment(
                [(0, tipy-swdy), (-swlen, tipy-swdy)]))
            self.segments.append(Segment([(-swlen, tipy-swdy), (-swlen, tipy)], arrow='->'))
            self.anchors['tipswitch'] = (0, tipy-swdy)

        if ring and ringswitch:
            if dots:
                self.segments.append(SegmentCircle(
                    (0, ringy+swdy), r, fill=fill, zorder=4))
            self.segments.append(Segment(
                [(0, ringy+swdy), (-swlen, ringy+swdy)]))
            self.segments.append(Segment([(-swlen, ringy+swdy), (-swlen, ringy)], arrow='->'))
            self.anchors['ringswitch'] = (0, ringy+swdy)
