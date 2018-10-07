!!! info
    This example will demonstrate how to ...

## Overview

This filter will translate the origin of `vtkImageData` to any specified Corner of the data set assuming it is currently in the South West Bottom Corner (will not work if Corner was moved prior).

## ParaView Example

!!! failure "Description to come!"
    There are a lot of pages in the documentation and we are trying to fill all content as soon as possible. Stay tuned for updates to this page


<!--- TODO --->

## Python Example

!!! info "{lookup:PVGeo.grids.transform.TranslateGridOrigin}"

```py
import numpy as np
import vtk
import PVGeo
from PVGeo.grids import TranslateGridOrigin

###############################
# Create some input tables
idi = vtk.vtkImageData()
idi.SetDimensions(20, 2, 10)
idi.SetSpacing(1, 1, 1)
idi.SetOrigin(100, 100, 100)
# Populate the tables
n = 400
title = 'Array 0'
arr = np.random.random(n)
idi.GetPointData().AddArray(PVGeo.convertArray(arr, title))
###############################

# Use the filter
ido = TranslateGridOrigin(corner=1).Apply(idi)

# Checj the result
ox, oy, oz = ido.GetOrigin()
assert(ox == 100-19)
assert(oy == 100)
assert(oz == 100)
```
