import sys
sys.path.insert(0, '../../')
import SchemDraw as schem
import SchemDraw.elements as e

d = schem.Drawing()
o = d.add( e.OPAMP )
d.add( e.LINE, xy=o.out, l=.75 )
d.add( e.LINE, xy=o.in1, d='left', l=.75 )
d.add( e.LINE, d='up', l=1.5)
d.add( e.DOT )
R1 = d.add( e.RES, d='left', label='$R_1$')
d.add( e.GND )
Rf = d.add( e.RES, d='right', xy=R1.start, tox=o.out+.5, label='$R_f$')
d.add( e.LINE, d='down', toy=o.out )
dot = d.add( e.DOT )
d.add( e.LINE, d='left', xy=o.in2, l=.75 )
d.add( e.DOT )
R3 = d.add( e.RES, d='down', label='$R_3$' )
d.add( e.DOT )
d.add( e.GND )
R2 = d.add( e.RES, d='left', xy=R3.start, label='$R_2$' )
d.add( e.SOURCE_V, d='down', reverse=True, label='$v_{in}$' )
d.add( e.LINE, d='right', tox=Rf.end )#tox=R3.end )
d.add( e.GAP_LABEL, d='down', xy=dot.start, toy=R3.end, label=['+','$v_o$','$-$'] )
d.draw(showplot=False)
d.save('opamp.png')