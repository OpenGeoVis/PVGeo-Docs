!!! info
    This example will demonstrate how to perform a normalization or any custom mathematical operation on a single data array for an input data set.

## Overview

This filter allow the user to select an array from the input data set to be normalized. The filter will append another array to that data set for the output. The user can specify how they want to rename the array, can choose a multiplier, and can choose from two types of common normalizations: Feature Scaling and Standard Score.

## ParaView Example

!!! failure "Description to come!"
    There are a lot of pages in the documentation and we are trying to fill all content as soon as possible. Stay tuned for updates to this page


<!--- TODO --->

## Python Example

!!! info "{lookup:PVGeo.filters.poly.NormalizeArray}"

```py
import numpy as np
import vtk
from vtk.numpy_interface import dataset_adapter as dsa
import PVGeo
from PVGeo.filters import NormalizeArray

##################
# Create some input data. this can be any `vtkDataObject`
inp = vtk.vtkTable()
# Populate the data
n = 400
title = 'Array 0'
arr = np.random.random(n) # Table 0
inp.AddColumn(PVGeo.convertArray(arr, title))
###################

# Apply the filter
f = NormalizeArray(normalization='feature_scale', newName='foo')
f.SetInputArrayToProcess(0, 0, 0, 6, title) # field 6 is row data
output = f.Apply(inp)

# Check out the result
wout = dsa.WrapDataObject(output)
normArr = wout.RowData['foo']
print(normArr)
```
