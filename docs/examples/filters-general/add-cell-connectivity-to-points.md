[getstart]: ../../overview/getting-started.md#using-outside-modules

!!! info
    This example will demonstrate how to add connectivity along some arbitrary set of points to generate a line or polyline.

!!! warning
    The **Add Cell Connectivity To Points** filter uses the SciPy python package. You may get an error if you do not have SciPy linked to ParaView Python. To work around this, make sure the **Use nearest nbr** parameter is not checked. Since the points file we give you in this example is in sequential order, this will not matter.  [**See details**][getstart] to learn more about enabling the SciPy package in `pvpython`.

## Overview

This filter will add **linear** cell connectivity between scattered points. You have the option to add `VTK_LINE` or `VTK_POLYLINE` connectivity. `VTK_LINE` connectivity makes a straight line between the points in order (either in the order by index or using a nearest neighbor calculation). The `VTK_POLYLINE` adds polyline connectivity between all points as one spline (either in the order by index or using a nearest neighbor calculation).

## ParaView Example

First, lets generate some data on the ParaView pipeline. For this example, we want to generated a series of scattered points that might make up a path using a **Programmable Source**. Select *Sources->Alphabetical->Programmable Source* then paste the following script in the source's *Script* field:

```py
import numpy as np
from PVGeo import pointsToPolyData

def path1(y):
    """Equation: x = a(y-h)^2 + k"""
    a = - 110.0 / 160.0**2
    x = a*y**2 + 110.0
    idxs = np.argwhere(x>0)
    return x[idxs][:,0], y[idxs][:,0]

x, y = path1(np.arange(0.0, 200.0, 25.0))
zo = np.linspace(9.0, 11.0, num=len(y))
coords = np.vstack((x,y,zo)).T
# Shuffle points to demonstrate value of Nearest Neighbor
np.random.shuffle(coords)

pdo = self.GetOutput()
pdo.ShallowCopy(pointsToPolyData(coords))
```

!!! note
    These points are similar to the points used in the file given with the [Many Slices Along Points Example](./many-slices-along-points.md) except we shuffle them to make use of the nearest neighbor approximation.


### Apply the Filter

Now that you have the points generated on the pipeline, lets go ahead and apply the **Add Cell Connectivity To Points** filter from *Filters->PVGeo: General Filters->Add Cell Connectivity To Points*. Go ahead and click *Apply*. The output data should look really wacky and incorrectly built like the image below; this is good.

![Bad Connectivity](images/shuffled-cellconn.png)

Remember that in the script given above we shuffle the points to demonstrate that the points make a useable line but we need to reconstruct the order of the points. We do this by selecting the *Use Nearest Nbr Approx* checkbox; this will ensure that a useable path is generate from the points. Go ahead and select the check box then reapply the filter. Now it looks good (see image below)!

![Good Connectivity](images/cellconn.png)

## Python Example

!!! info "{lookup:PVGeo.filters.xyz.AddCellConnToPoints}"

```py
import numpy as np
from PVGeo import pointsToPolyData, AddCellConnToPoints

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
coords = np.vstack((x,y,zo)).T
# Shuffle points to demonstrate value of Nearest Neighbor
np.random.shuffle(coords)

# Make a VTK data object for the filter to use
vtkPoints = pointsToPolyData(coords)

############################################

# Use the filter: Here is vtkPolyData containing the connected line:
line = AddCellConnToPoints(nearestNbr=True).Apply(vtkPoints)
```
