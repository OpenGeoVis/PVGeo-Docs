!!! info
    This example will demonstrate how to connect a set of points defined on a regular grid to create a `vtkUnstructuredGrid` which can be used to perform volumetric operations.

## Overview


## ParaView Example

!!! failure "Description to come!"
    There are a lot of pages in the documentation and we are trying to fill all content as soon as possible. Stay tuned for updates to this page

Below is a demonstration of this filter transforming point data (XYZ + attribute) to a gridded data set which is thresholded in the center.

!!! success "Example"
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
            <iframe src="http://viewer.pvgeo.org/?fileURL=https://dl.dropbox.com/s/apimhoglo4595kw/voxelize-demo.vtkjs?dl=0" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

<!--- TODO --->




## Python Example

!!! info "{lookup:PVGeo.filters.voxelize.VoxelizePoints}"

```py
import numpy as np
from vtk.numpy_interface import dataset_adapter as dsa
import PVGeo
from PVGeo import pointsToPolyData, VoxelizePoints


# Make a mesh grid
dd = 5
x = y = z = np.arange(0, 100, dd)
g = np.meshgrid(x, y, z)

# Convert to XYZ points
points = np.vstack(map(np.ravel, g)).T
rand = np.random.random(len(points))
vtkpoints = pointsToPolyData(points)
vtkpoints.GetPointData().AddArray(PVGeo.convertArray(rand, 'Random'))

# Use filter
v = VoxelizePoints()
v.SetInputDataObject(vtkpoints)
v.SetEstimateGrid(False) # Cell size is explicitly set
v.SetDeltaX(10)
v.SetDeltaY(10)
v.SetDeltaZ(10)
v.Update()

grid = v.GetOutput()
wgrd = dsa.WrapDataObject(grid)
celldata = wgrd.CellData['Random']

# Checkout output:
assert(grid.GetNumberOfCells() == 8*10**3)
numPts = (len(x)+2)**3
assert(grid.GetNumberOfPoints() == numPts)
assert(np.allclose(celldata, rand))

# Now check that we can set the spacing for every cell
spac = np.full((len(points)), 10.0)
v.SetDeltas(spac, spac, spac)
v.Update()

grid = v.GetOutput()
wgrd = dsa.WrapDataObject(grid)
celldata = wgrd.CellData['Random']

assert(grid.GetNumberOfCells() == 8*10**3)
assert(grid.GetNumberOfPoints() == numPts)
assert(np.allclose(celldata, rand))


```
