import matplotlib.pyplot as plt
import numpy as np

from math import cos, pi, sin


class FlowField2D(object):
    """
    DESCRIPTION
    """
    def __init__(self, points=[], uinf=0., alpha=0., xlim=(-1., 1.), ylim=(-1., 1.), nx=100, ny=100):

        self.points = points
        self.uinf = uinf
        self.alpha = alpha
        self.xlim = xlim
        self.ylim = ylim
        self.nx = nx
        self.ny = ny

    @property
    def flow(self):
        u = np.ones(self.x.shape) * self.freestream[0]
        v = np.ones(self.x.shape) * self.freestream[1]
        for point in self.points:
            point_flow = point.compute_flow(self.x, self.y)
            u += point_flow[0]
            v += point_flow[1]
        return u, v

    @property
    def freestream(self):
        return [self.uinf * cos(self.alpha),
                self.uinf * sin(self.alpha)]

    @property
    def grid(self):
        return np.meshgrid(self.x_values, self.y_values)

    @property
    def psi(self):
        psi = self.uinf * (self.y * cos(self.alpha) - self.x * sin(self.alpha))
        for point in self.points:
            psi += point.compute_psi(self.x, self.y)
        return psi

    @property
    def u(self):
        return self.flow[0]

    @property
    def v(self):
        return self.flow[1]

    @property
    def x(self):
        return self.grid[0]

    @property
    def x_values(self):
        return np.linspace(self.xlim[0], self.xlim[1], self.nx)

    @property
    def y(self):
        return self.grid[1]

    @property
    def y_values(self):
        return np.linspace(self.ylim[0], self.ylim[1], self.ny)

    def plot_streamlines(self,
                         arrowsize=1,
                         arrowstyle='->',
                         axes=None,
                         density=1.,
                         divide_linecolor='r',
                         divide_linewidth=2,
                         grid=True,
                         linewidth=1,
                         scaled=True,
                         show_divide=False,
                         show_points=True,
                         title=None,
                         xlabel='x',
                         ylabel='y'):
        if not axes:
            axes = plt.subplot(111)

        axes.streamplot(self.x, self.y, self.u, self.v,
                        density=density, linewidth=linewidth, arrowsize=arrowsize, arrowstyle=arrowstyle)

        if title:
            axes.set_title(title)
        if xlabel:
            axes.set_xlabel(xlabel)
        if ylabel:
            axes.set_ylabel(ylabel)
        if grid:
            axes.grid()

        axes.set_xlim(self.xlim)
        axes.set_ylim(self.ylim)

        if show_divide:
            axes.contour(self.x, self.y, self.psi,
                         levels=[0.], colors=divide_linecolor,
                         linewidth=divide_linewidth)

        if show_points:
            for point in self.points:
                axes.plot(point.x, point.y, color=point.default_color, marker='o')

        if scaled:
            axes.axis('scaled')

        return axes