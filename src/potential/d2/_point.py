from math import log, pi
from numpy import arctan2


class PointDoublet(object):
    """
    A point doublet for use in 2D potential flow problems.

    Parameters
    ----------
    x: float, optional
        The x-coordinate of the point doublet. Default=0.
    y: float, optional
        The y-coordinate of the point doublet. Default=0.
    strength:
        The strength of the point doublet. Default=1.
    default_color: str, optional
        Matplotlib color for use in plotting. Default='g'.
    """
    def __init__(self, x=0., y=0., strength=1., default_color='g'):
        self.x = x
        self.y = y
        self.strength = strength

        self.default_color = default_color

    def compute_flow(self, x, y):
        """
        Calculate the x and y components of flow due to the point doublet at given point(s) in space.

        Parameters
        ----------
        x: float or array_like
            The Cartesian x-coordinate(s) for flow contributions due to the doublet to be calculated.
        y: float or array_like
            The Cartesian y-coordiante(s) for flow contributions due to the doublet to be calculated.

        Returns
        -------
        u: float or array_like
            X component of flow due to the doublet at given point(s).
        v: float or array_like
            Y component of flow due to the doublet at given point(s).
        """
        xrel = x - self.x
        yrel = y - self.y
        u = -self.strength / 2. / pi * (xrel**2. - y**2.) / (xrel**2. + yrel**2.)**2.
        v = -self.strength / 2. / pi * 2. * xrel * yrel   / (xrel**2. + yrel**2.)**2.
        return u, v

    def compute_psi(self, x, y):
        """
        Compute the stream function contribution of the doublet at given point(s) in space.

        Parameters
        ----------
        x: float or array_like
            The Cartesian x-coordinate(s) for flow contributions due to the doublet to be calculated.
        y: float or array_like
            The Cartesian y-coordiante(s) for flow contributions due to the doublet to be calculated.

        Returns
        -------
        psi: float or array_like
            Stream function due to the source at the given point(s).
        """
        xrel = x - self.x
        yrel = y - self.y
        return -self.strength / 2. / pi * yrel / (xrel**2. + yrel**2.)


class PointSource(object):
    """
    A point source for use in 2D potential flow problems.

    Parameters
    ----------
    x: float, optional
        The x-coordinate of the point source. Default=0.
    y: float, optional
        The y-coordinate of the point source. Default=0.
    strength:
        The strength of the point source. Default=1.
    default_color: str, optional
        Matplotlib color for use in plotting. Default='r'.

    Notes
    -----
    The source can be used as a sink by setting a negative strength.
    """
    def __init__(self, x=0., y=0., strength=1., default_color='r'):
        self.x = x
        self.y = y
        self.strength = strength

        self.default_color = default_color

    def compute_flow(self, x, y):
        """
        Calculate the x and y components of flow due to the point source at given point(s) in space.

        Parameters
        ----------
        x: float or array_like
            The Cartesian x-coordinate(s) for flow contributions due to the source to be calculated.
        y: float or array_like
            The Cartesian y-coordiante(s) for flow contributions due to the source to be calculated.

        Returns
        -------
        u: float or array_like
            X component of flow due to the source at given point(s).
        v: float or array_like
            Y component of flow due to the source at given point(s).
        """
        xrel = x - self.x
        yrel = y - self.y
        u = self.strength / 2. / pi * xrel / (xrel**2. + yrel**2.)
        v = self.strength / 2. / pi * yrel / (xrel**2. + yrel**2.)
        return u, v

    def compute_psi(self, x, y):
        """
        Compute the stream function contribution of the source at given point(s) in space.

        Parameters
        ----------
        x: float or array_like
            The Cartesian x-coordinate(s) for flow contributions due to the source to be calculated.
        y: float or array_like
            The Cartesian y-coordiante(s) for flow contributions due to the source to be calculated.

        Returns
        -------
        psi: float or array_like
            Stream function due to the source at the given point(s).
        """
        xrel = x - self.x
        yrel = y - self.y
        return self.strength / 2. / pi * arctan2(yrel - self.yrel, xrel - self.xrel)


class PointVortex(object):
    """
    A point vortex for use in 2D potential flow problems.

    Parameters
    ----------
    x: float, optional
        The x-coordinate of the point vortex. Default=0.
    y: float, optional
        The y-coordinate of the point vortex. Default=0.
    strength:
        The strength of the point vortex. Default=1.
    default_color: str, optional
        Matplotlib color for use in plotting. Default='c'.

    Notes
    -----
    Positive vortex strength results in left handed rotation within in the x-y plane.
    """
    def __init__(self, x=0., y=0., strength=1., default_color='c'):
        self.x = x
        self.y = y
        self.strength = strength
        self.default_color = default_color

    def compute_flow(self, x, y):
        """
        Calculate the x and y components of flow due to the point vortex at given point(s) in space.

        Parameters
        ----------
        x: float or array_like
            The Cartesian x-coordinate(s) for flow contributions due to the vortex to be calculated.
        y: float or array_like
            The Cartesian y-coordiante(s) for flow contributions due to the vortex to be calculated.

        Returns
        -------
        u: float or array_like
            X component of flow due to the vortex at given point(s).
        v: float or array_like
            Y component of flow due to the vortex at given point(s).
        """
        xrel = x - self.x
        yrel = y - self.y
        u =  self.strength / 2. / pi * yrel / (xrel**2. + yrel**2.)
        v = -self.strength / 2. / pi * xrel / (xrel**2. + yrel**2.)
        return u, v

    def compute_psi(self, x, y):
        """
        Compute the stream function contribution of the vortex at given point(s) in space.

        Parameters
        ----------
        x: float or array_like
            The Cartesian x-coordinate(s) for flow contributions due to the vortex to be calculated.
        y: float or array_like
            The Cartesian y-coordiante(s) for flow contributions due to the vortex to be calculated.

        Returns
        -------
        psi: float or array_like
            Stream function due to the vortex at the given point(s).
        """
        xrel = x - self.x
        yrel = y - self.y
        return self.strength / 4. / pi * log(xrel**2. + yrel**2.)
