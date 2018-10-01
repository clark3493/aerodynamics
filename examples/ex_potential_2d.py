import os
import sys
SRC_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src')
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

import argparse
import matplotlib.pyplot as plt
import numpy as np

from potential.d2 import PointDoublet, PointSource, PointVortex, FlowField2D


parser = argparse.ArgumentParser()
parser.add_argument('examples', nargs='*', help='title of examples to run')


def doublet():
    doublet = PointDoublet()

    flow_field = FlowField2D(points=[doublet], uinf=1., nx=300, ny=300)
    ax = flow_field.plot_streamlines(show_divide=True)
    plt.show()


def rankine():
    source = PointSource(x=0., y=0., strength= 1.)
    sink   = PointSource(x=1., y=0., strength=-1.)

    flow_field = FlowField2D(points=[source, sink], xlim=(-1., 2.))
    ax = flow_field.plot_streamlines()
    plt.show()


def simple_freestream():
    source = PointSource(x=0., y=0., strength=1.)
    sink = PointSource(x=1., y=0., strength=-1.)

    flow_field = FlowField2D(points=[source, sink], uinf=1., xlim=(-1., 2.), nx=200, ny=200)
    ax = flow_field.plot_streamlines(show_divide=True)
    plt.show()


def source():
    source = PointSource(x=0., y=0., strength=1.)

    flow_field = FlowField2D(points=[source])
    ax = flow_field.plot_streamlines()
    plt.show()


def vortex():
    vortex = PointVortex()

    flow_field = FlowField2D(points=[vortex])
    ax = flow_field.plot_streamlines()
    plt.show()


def vortex_sheet():
    xmin = -1.
    xmax = 1.
    n = 20

    vortices = [PointVortex(x=xi) for xi in np.linspace(xmin, xmax, n)]

    flow_field = FlowField2D(points=vortices, xlim=(xmin, xmax))
    ax = flow_field.plot_streamlines()
    plt.show()


if __name__ == '__main__':

    args = parser.parse_args()

    for arg in args.examples:
        if arg == 'doublet':
            doublet()
        elif arg == 'rankine':
            rankine()
        elif arg == 'simple_freestream':
            simple_freestream()
        elif arg == 'source':
            source()
        elif arg == 'vortex':
            vortex()
        elif arg == 'vortex_sheet':
            vortex_sheet()
        else:
            raise ValueError("Unrecognized example case: %s" % arg)
