!!! info
    This example will demonstrate how to to powerful a mathematical operation between to input arrays for any given source.

## Overview

This filter allows the user to select two input data arrays on which to perform math operations. The input arrays are used in their order of selection for the operations.

## ParaView Example

!!! failure "Description to come!"
    There are a lot of pages in the documentation and we are trying to fill all content as soon as possible. Stay tuned for updates to this page


<!--- TODO --->


## Python Example

!!! info "{lookup:PVGeo.filters.math.ArrayMath}"

```py
import numpy as np
import vtk
from vtk.numpy_interface import dataset_adapter as dsa
import PVGeo
from PVGeo.filters import ArrayMath

# Create some input data. This can be any `vtkDataObject`
inp = vtk.vtkTable()
# Populate the tables
n = 400
arr0 = np.random.random(n)
arr1 = np.random.random(n)
inp.AddColumn(PVGeo.convertArray(arr0, 'Array 0'))
inp.AddColumn(PVGeo.convertArray(arr1, 'Array 1'))
```

```py
# Use the filter:
f = ArrayMath(operation='add', newName='foo')
f.SetInputArrayToProcess(0, 0, 0, 6, 'Array 0') # field 6 is row data
f.SetInputArrayToProcess(1, 0, 0, 6, 'Array 1') # field 6 is row data
# Now get the result
output = f.Apply(inp)

wout = dsa.WrapDataObject(output)
arr = wout.RowData['foo']
assert(np.allclose(arr, arr0+arr1))

```

```py
# Use a custom math operation:
def power(arr0, arr1):
    return arr0**arr1

# Use filter generated above
f.SetOperation(power)
f.SetNewArrayName('powered')
f.Update()

# Now get the result
output = f.GetOutput()
print(output)
```
