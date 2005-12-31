from java.awt import Color
from edu.mines.jtk.dsp import *
from edu.mines.jtk.mosaic import *
from edu.mines.jtk.util import *

True = 1
False = 0

n1 = 101;  d1 = 0.1;  f1 = 0.0
n2 = 101;  d2 = 0.1;  f2 = 0.0
f = Array.sin(Array.rampfloat(0.0,d1,d2,n1,n2))
s1 = Sampling(n1,d1,f1)
s2 = Sampling(n2,d2,f2)

ax = 0.5*d2*(n2-1);
x1 = Array.rampfloat(f1,d1,n1);
x2 = Array.add(ax,Array.mul(ax,Array.sin(x1)));

def makePlotPanel():
  pp = PlotPanel(1,2,PlotPanel.Orientation.X1DOWN_X2RIGHT)

  pxv0 = pp.addPixels(0,0,s1,s2,f)
  pxv1 = pp.addPixels(0,1,s1,s2,f)
  pxv0.setColorMap(PixelsView.ColorMap.GRAY)
  pxv1.setColorMap(PixelsView.ColorMap.JET)

  gv0 = pp.addGrid(0,0)
  gv1 = pp.addGrid(0,1)
  gv0.setVertical(GridView.Vertical.ZERO);
  gv0.setColor(Color.YELLOW);
  gv1.setParameters("HVw-.");

  ptv0 = pp.addPoints(0,0,s1,x2);
  ptv1 = pp.addPoints(0,1,x1,x2);
  ptv0.setStyle("r--.");
  ptv1.setStyle("k-o");

  pp.addColorBar("amplitude")
  pp.title = "A Test of PlotFrame"
  pp.setHLabel(0,"offset (km)")
  pp.setHLabel(1,"velocity (km/s)")
  pp.setVLabel("depth (km)")

  return pp

pp1 = makePlotPanel()
pp2 = makePlotPanel()
pf = PlotFrame(pp1,pp2,PlotFrame.Split.VERTICAL)
pf.setVisible(True)
pf.paintToPng(300,6,"junk.png")