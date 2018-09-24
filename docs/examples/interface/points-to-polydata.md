# Points to PolyData

!!! info
    This example will demonstrate how to use the `pointsToPolyData` function to convert a 2D NumPy array of points (n by 3) into `vtkPolyData` containing those points.

## Overview
This function is a convenience method to convert a NumPy array of points into a `vtkPolyData` object with the points and cell connectivity properly built.


## ParaView Example

Since this is a convenience function and not as algorithm/plugin, there is not a full ParaView example. However, we use the method in Programmable Sources quite often in the ParaView examples of other algorithms to generate an input data set of points. Check out the following if you're interested:

- [Voxelize Points](../filters-general/voxelize-points.md)
- [Add Cell Connectivity to Points](../filters-general/add-cell-connectivity-to-points.md)
- [Points to Tube](../filters-general/points-to-tube.md)


## Python Example

!!! info "{lookup:PVGeo.interface.pointsToPolyData}"

```py
import numpy as np
from PVGeo import pointsToPolyData

# NumPy array of points for input
points = np.random.random((100,3))

vtkPoints = pointsToPolyData(points)
print(vtkPoints)
```
