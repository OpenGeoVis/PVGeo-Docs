# Points to PolyData

!!! info
    This example will demonstrate how to use the `PointsToPolyData` function to convert a 2D NumPy array of points (n by 3) into `vtkPolyData` containing those points.

## Overview
This function is a convenience method to convert a NumPy array of points into a `vtkPolyData` object with the points and cell connectivity properly built.


## ParaView Example

Since this is a convenience function and not as algorithm/plugin, there is not a full ParaView example. However, we use the method in Programmable Sources quite often in the ParaView examples of other algorithms to generate an input data set of points. Check out the following if you're interested:

- [Voxelize Points](voxelize-points.md)
- [Add Cell Connectivity to Points](add-cell-connectivity-to-points.md)
- [Points to Tube](points-to-tube.md)


## Python Example

!!! info "{lookup:PVGeo.filters.xyz.PointsToPolyData}"

```py
import numpy as np
from PVGeo.filters import PointsToPolyData

# NumPy array of points for input
points = np.random.random((100,3))

vtkPoints = PointsToPolyData(points)
print(vtkPoints)
```
