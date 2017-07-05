import numpy
# From: https://stackoverflow.com/questions/14177744/how-does-perspective-transformation-work-in-pil
from PIL import Image

def find_coeffs(pa, pb):
    """
    pa and pb contain 4 corresponding points on image in order UL,UR,LR,LL
    UL=(0,0), UR=(w,0), LR=(w,h), LL=(0,h)
    
    Units for pa and pb are pixels.
    pa is target plane (e.g. [(0, 0), (256, 0), (256, 256), (0, 256)])
    pb is source plane (e.g. [(0, 0), (256, 0), (new_width, height), (xshift, height)])
    """
    matrix = []
    for p1, p2 in zip(pa, pb):
        matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0]*p1[0], -p2[0]*p1[1]])
        matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1]*p1[0], -p2[1]*p1[1]])

    A = numpy.matrix(matrix, dtype=numpy.float)
    B = numpy.array(pb).reshape(8)

    res = numpy.dot(numpy.linalg.inv(A.T * A) * A.T, B)
    # take commenters advice to avoid A.T
    #res = numpy.linalg.solve(A, B)
    return numpy.array(res).reshape(8)

def fix_plot_img( UL, UR, LR, LL, img):
    """
    Correct plot so that xmin and xmax have same y value.
    And, ymin/ymax have same x value
    """
    
    # source points
    pb = [UL,UR,LR,LL]
    
    xlo = (LL[0]+UL[0])/2
    xhi = (UR[0]+LR[0])/2
    
    yhi = (UL[1]+UL[1])/2
    ylo = (LL[1]+LR[1])/2
    
    # make target points
    UL = (xlo, yhi)
    UR = (xhi, yhi)
    LR = (xhi, ylo)
    LL = (xlo, ylo)
    pa = [UL,UR,LR,LL]
    
    coeffs = find_coeffs(pa, pb)
    return img.transform(img.size, Image.PERSPECTIVE, coeffs, Image.BICUBIC)
    
if __name__=="__main__":
    
    img_name = "rot_poly_p3.jpg"
    UL = (105., 93.)
    UR = (848., 51.)
    LR = (877., 627.)
    LL = (135., 666.)
    img = Image.open(img_name)
    print('img.size =',img.size)
    
    img_und = fix_plot_img( UL, UR, LR, LL, img)
    img_und.save('undistort_'+img_name)
    
    
    
    