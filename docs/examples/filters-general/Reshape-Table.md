!!! info
    This example will demonstrate how to ...

## Overview

This filter will take a `vtkTable` object and reshape it. This filter essentially treats `vtkTable`s as 2D matrices and reshapes them using `numpy.reshape` in a C contiguous manner. Unfortunately, data fields will be renamed arbitrarily because VTK data arrays require a name.


## ParaView Example

!!! failure "Description to come!"
    There are a lot of pages in the documentation and we are trying to fill all content as soon as possible. Stay tuned for updates to this page


<!--- TODO --->

## Python Example

Take a look at `ReshapeTable`'s code docs [here](http://docs.pvgeo.org/en/latest/suites/General-Filters.html#PVGeo.filters_general.ReshapeTable).

```py
import numpy as np
import vtk
from vtk.numpy_interface import dataset_adapter as dsa
from PVGeo import _helpers
from PVGeo.filters_general import ReshapeTable


```
