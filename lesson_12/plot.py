"""
=======================
Pie chart on polar axis
=======================

Demo of bar plot on a polar axis.
"""
import numpy as np
import matplotlib.pyplot as plt


# Compute pie slices
N = 20
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)

ax = plt.subplot(111, projection='polar')
bars = ax.bar(theta, radii, width=width, bottom=0.0)

# Use custom colors and opacity
for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.viridis(r / 10.))
    bar.set_alpha(0.5)

plt.show()



# import numpy as np
# import matplotlib.pyplot as plt
# def mandelbrot( h,w, maxit=20 ):
#     """Returns an image of the Mandelbrot fractal of size (h,w)."""
#     y,x = np.ogrid[ -1.4:1.4:h*1j, -2:.8:w*1j ]
#     c = x+y*1j
#     z = c
#     divtime = maxit + np.zeros(z.shape, dtype=int)
#
#     for i in range(maxit):
#         z = z**2 + c
#         diverge = z*np.conj(z) > 2**2            # who is diverging
#         div_now = diverge & (divtime==maxit)  # who is diverging now
#         divtime[div_now] = i                  # note when
#         z[diverge] = 2                        # avoid diverging too much
#
#     return divtime
# plt.imshow(mandelbrot(400,400))
# plt.show()