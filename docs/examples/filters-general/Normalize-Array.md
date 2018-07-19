!!! info
    This example will demonstrate how to ...

## Overview

This filter allow the user to select an array from the input data set to be normalized. The filter will append another array to that data set for the output. The user can specify how they want to rename the array, can choose a multiplier, and can choose from two types of common normalizations: Feature Scaling and Standard Score.

## ParaView Example

!!! failure "Description to come!"
    There are a lot of pages in the documentation and we are trying to fill all content as soon as possible. Stay tuned for updates to this page


<!--- TODO --->

## Python Example

Take a look at `NormalizeArray`'s code docs [here](http://docs.pvgeo.org/en/latest/suites/General-Filters.html#PVGeo.filters_general.NormalizeArray).

```py
import numpy as np
import vtk
from vtk.numpy_interface import dataset_adapter as dsa
from PVGeo import _helpers
from PVGeo.filters_general import NormalizeArray


# Create some input data
t0 = vtk.vtkTable()

# Populate the data
n = 400
title = 'Array 0'
arr = np.random.random(n) # Table 0
t0.AddColumn(_helpers.numToVTK(arr, title))

# Apply the filter
f = NormalizeArray()
f.SetInputDataObject(t0)
f.SetInputArrayToProcess(0, 0, 0, 6, title) # field 6 is row data
# Set normalization type:
#- See code docs for available options
f.SetNormalization('feature_scale')
#
f.SetNewArrayName('Normalized')
f.Update()

# Now test the result
output = f.GetOutput()
wout = dsa.WrapDataObject(output)
normArr = wout.RowData['Normalized']

```
