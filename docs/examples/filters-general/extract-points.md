!!! info
    This example will demonstrate how to extract the points and PointData of any input data set that has valid PointData into a `vtkPolyData` object.

## Overview


## ParaView Example

!!! failure "Description to come!"
    There are a lot of pages in the documentation and we are trying to fill all content as soon as possible. Stay tuned for updates to this page


<!--- TODO --->

## Python Example

!!! info "{lookup:PVGeo.filters.xyz.ExtractPoints}"

```py
import PVGeo
from PVGeo.filters import ExtractPoints

#####################################
# Have some input data source with valid PointData
source = PVGeo.model_build.GlobeSource()
source.Update()
data = source.GetOutput()
#####################################

# Apply the filter:
polyData = ExtractPoints().Apply(data)

# Get and use the result:
print(polyData)
```
