!!! info
    This example will demonstrate how to ...

## Overview

Takes points from a `vtkPolyData` object and constructs a line of those points then builds a polygonal tube around that line with some specified radius and number of sides.

## ParaView Example

!!! failure "Description to come!"
    There are a lot of pages in the documentation and we are trying to fill all content as soon as possible. Stay tuned for updates to this page


<!--- TODO --->

## Python Example

Take a look at `PointsToTube`'s code docs [here](http://docs.pvgeo.org/en/latest/suites/General-Filters.html#PVGeo.filters_general.PointsToTube).

```py
import numpy as np
from PVGeo.filters_general import PointsToPolyData, PointsToTube


############################################
######### GENERATE SOME POINT DATA #########

def path1(y):
    """Equation: x = a(y-h)^2 + k"""
    a = - 110.0 / 160.0**2
    x = a*y**2 + 110.0
    idxs = np.argwhere(x>0)
    return x[idxs][:,0], y[idxs][:,0]

x, y = path1(np.arange(0.0, 200.0, 25.0))
zo = np.linspace(9.0, 11.0, num=len(y))
coords = np.hstack((x,y,zo))
# Shuffle points to demonstrate value of Nearest Neighbor
np.random.shuffle(coords)

# Make a VTK data object for the filter to use
vtkPoints = PointsToPolyData(coords)

############################################

# Use the filter: here is vtkPolyData containing the connected line
tube = PointsToTube(nearestNbr=True).Apply(vtkPoints)

print(tube)
```
