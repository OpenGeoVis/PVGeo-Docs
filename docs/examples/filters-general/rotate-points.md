!!! info
    This example will demonstrate how to rotate points in a `vtkPolyData` object around some origin on the XY plane.

## Overview


## ParaView Example

!!! failure "Description to come!"
    There are a lot of pages in the documentation and we are trying to fill all content as soon as possible. Stay tuned for updates to this page


<!--- TODO --->

## Python Example

Take a look at `RotatePoints`'s code docs [here](http://docs.pvgeo.org/en/latest/suites/General-Filters.html#PVGeo.filters.RotatePoints).

```py
import numpy as np
from PVGeo.filters import PointsToPolyData, RotatePoints

##############
# Create some input points as `vtkPolyData`
RTOL = 0.00001 # As high as rotation precision can get
x = np.array([0.0,1.0,0.0])
y = np.array([0.0,0.0,1.0])
z = np.array([0.0,0.0,0.0])
x = np.reshape(x, (len(x), -1))
y = np.reshape(y, (len(y), -1))
z = np.reshape(z, (len(z), -1))
pts = np.concatenate((x, y, z), axis=1)
pdi = PointsToPolyData(pts)
##############

# Use the filter:
rotated = RotatePoints(angle=33.3).Apply(pdi)

print(rotated)
```
