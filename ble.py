# 2-EXT Extractor Blender
def ble(x3,x2,x1,x0,y3,y2,y1,y0):
    out0 = x3*y3 ^ x2*y2 ^ x1*y1 ^ x0*y0
    out1 = x2*y3 ^ x1*y2 ^ x3*x0*y1 ^ x3*y0
    out2 = x1*y3 ^ x3*x0*y2 ^ x3*x2*x1 ^ x2*y0
    out3 = x3*x0*y3 ^ x3*x2*y2 ^ x2*x1*x1 ^ x1*y0
    return (out3, out2, out1, out0)

