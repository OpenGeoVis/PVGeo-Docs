!!! info
    This example will demonstrate how to ...

## Overview
This filter will flip ImageData on any of the three cartesian axes. A checkbox is provided for each axis on which you may desire to flip the data.

## ParaView Example

!!! failure "Description to come!"
    There are a lot of pages in the documentation and we are trying to fill all content as soon as possible. Stay tuned for updates to this page


<!--- TODO --->

## Python Example

!!! info "{lookup:PVGeo.grids.transform.ReverseImageDataAxii}"

```py
import numpy as np
import vtk
from vtk.util import numpy_support as nps
from vtk.numpy_interface import dataset_adapter as dsa
import PVGeo
from PVGeo.grids import ReverseImageDataAxii

###############################
# Create input vtkImageData:
nx, ny, nz = 10, 11, 12
arr = np.random.random((nz, ny, nx))
arrCells = np.random.random((nz-1, ny-1, nx-1)) # Note fortran ordering
image = vtk.vtkImageData()
image.SetDimensions(nx, ny, nz)
image.SetSpacing(2, 2, 2)
image.SetOrigin(0, 0, 0)
data = nps.numpy_to_vtk(num_array=arr.flatten(), deep=True)
data.SetName('Data')
cellData = nps.numpy_to_vtk(num_array=arrCells.flatten(), deep=True)
cellData.SetName('CellData')
image.GetPointData().AddArray(data)
image.GetCellData().AddArray(cellData)
###############################

# Now perfrom the reverse for only X:
ido = ReverseImageDataAxii(axes=[1, 0, 0]).Apply(image)

# Now check the output
assert(ido.GetNumberOfPoints() == len(arr.flatten()))
# Check that x-axis was reversed
wido = dsa.WrapDataObject(ido)
testPointData = wido.PointData['Data']
testCellData = wido.CellData['CellData']
assert(np.allclose(testPointData, np.flip(arr, axis=2).flatten()))
assert(np.allclose(testCellData, np.flip(arrCells, axis=2).flatten()))
```
