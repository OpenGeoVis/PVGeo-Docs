
!!! info
    This example will demonstrate how to to merge to `vtkTable` objects with the same number of rows into a single `vtkTable`.


## ParaView Example

!!! failure "Description to come!"
    There are a lot of pages in the documentation and we are trying to fill all content as soon as possible. Stay tuned for updates to this page


<!--- TODO --->


## Python Example

Take a look at `CombineTables`'s code docs [here](http://docs.pvgeo.org/en/latest/suites/General-Filters.html#PVGeo.filters_general.CombineTables).

```py
import numpy as np
import vtk
from vtk.numpy_interface import dataset_adapter as dsa
from PVGeo import _helpers
from PVGeo.filters_general import CombineTables

##################################
# Create some input tables
t0 = vtk.vtkTable()
t1 = vtk.vtkTable()
# Populate the tables
n = 100
titles = ('Array 0', 'Array 1', 'Array 2')
arr0 = np.random.random(n) # Table 0
arr1 = np.random.random(n) # Table 0
t0.AddColumn(_helpers.numToVTK(arr0, titles[0]))
t0.AddColumn(_helpers.numToVTK(arr1, titles[1]))
arr2 = np.random.random(n) # Table 1
t1.AddColumn(_helpers.numToVTK(arr2, titles[2]))
arrs = [arr0, arr1, arr2]

##################################

# Now use the `CombineTables` filter:
f = CombineTables()
f.SetInputDataObject(0, t0)
f.SetInputDataObject(1, t1)
f.Update()

# Get the output:
output = f.GetOutput()

# Here I verify the result
wpdi = dsa.WrapDataObject(output)

for i in range(len(titles)):
    arr = wpdi.RowData[titles[i]]
    assert(np.allclose(arr, arrs[i], rtol=0.0001))
```
