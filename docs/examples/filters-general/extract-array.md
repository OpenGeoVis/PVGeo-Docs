!!! info
    This example will demonstrate how to extract an array from any input data set to make a `vtkTable` of that single data array

## Overview


## ParaView Example

!!! failure "Description to come!"
    There are a lot of pages in the documentation and we are trying to fill all content as soon as possible. Stay tuned for updates to this page


<!--- TODO --->

## Python Example

{lookup:PVGeo.filters.tables.ExtractArray}


```py
import PVGeo
from PVGeo.filters import ExtractArray

# Create input data
grd = PVGeo.model_build.CreateTensorMesh().Apply()

# Construct the filter
filt = ExtractArray()
# Define the array to extract
filt.SetInputArrayToProcess(0, 0, 0, 1, 'Random Data')

# Apply the filter on the input
table = filt.Apply(grd)
print(table)
```
