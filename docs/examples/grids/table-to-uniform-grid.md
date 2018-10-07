!!! warning
    This filter documentation is deprecated. Please use `TableToTimeGrid`

!!! bug
    This filter has some quirks and we are working to completely overhaul it to have correct SEPlib axial conventions (d1=z, d2=x, d3=y) and to be more robust. This documentation is very deprecated.

## Overview

This filter takes a `vtkTable` object with columns that represent data to be translated (reshaped) into a 3D grid (2D also works, just set the third dimensions extent to 1). The grid will be a n1 by n2 by n3 `vtkImageData` structure and an origin (south-west bottom corner) can be set at any xyz point. Each column of the `vtkTable` will represent a data attribute of the `vtkImageData` formed (essentially a uniform mesh). The SEPlib option allows you to unfold data that was packed in the SEPlib format where the most important dimension is z and thus the z data is d1 (d1=z, d2=y, d3=x). When using SEPlib, specify n1 as the number of elements in the Z-direction, n2 as the number of elements in the X-direction, and n3 as the number of elements in the Y-direction (and so on for other parameters).

## ParaView Example

[reader-bin]: ../readers-general/binary-packed-data.md
[reader-gslib]: ../gslib/gslib.md
[reader-sgems]: ../gslib/sgems-grid.md

Say we have some data in 1D format or a series of 1D data sets, like a `vtkTable` where we have columns of data which we know can be restructured into a 2D or 3D volume. One great example is the the table made in the example for using the [Read Binary Packed Data][reader-bin] reader. Follow the instructions to read in that data to a `vtkTable`. Once you have sample data in a `vtkTable`, we can apply a the 'Table to Uniform Grid' Filter and specify the shape of our volumetric data (for 2D data like this example, specify n1 and n2 accordingly and leave n3 as 1). The script provided in the example will output the extent, origin, and spacing parameters for you to use (best to copy/paste from that output into the parameter fields). This example will produce the 2D grid depicted on the [Read Binary Packed Data][reader-bin] page (that image adds the 'Warp by Scalar' filter).

Another example is to use one of the data files from [this website](http://www.trainingimages.org/training-images-library.html) and load it in using the [GSLIB File to Table][reader-gslib] reader. These files are in the SGeMS file format but can also be read by the GSLIB file reader. Through loading this data into a table and then applying a Table to Uniform Grid Filter, we are effectively mimicking what the [SGeMS Grid][reader-grid] reader is doing behind the scenes. These SGeMS files make great example because they outline how we can transfer any data with any number of data arrays to a uniform grid (each data array in the input table will represent a different attribute of the space made up by the vtkImageData grid). The GSLIB reader will print out the dimensions of the grid to the Output Messages console (to see this, select View->Output Messages). Use those dimensions for the n1, n2, and n3 parameters. Play around with the other parameters to get a feel for how this filter behaves.

### Down the Pipeline
- [Translate Origin of Grid](translate-origin-of-grid.md)
- [Reverse Grid Axii](reverse-grid-axii.md)
- [Normalize Array](../filters-general/normalize-array.md)
- [Contour](https://www.paraview.org/Wiki/ParaView/Users_Guide/List_of_filters#Contour)
- [Threshold](https://www.paraview.org/Wiki/ParaView/Users_Guide/List_of_filters#Threshold)



-------------

## Python Example

!!! info "{lookup:PVGeo.grids.transform.TableToGrid}"

```py
import numpy as np
import vtk
import PVGeo
from PVGeo.grids import TableToGrid

###############################
# Create some input tables
table = vtk.vtkTable()
# Populate the tables
arrs = [None, None, None]
n = 400
titles = ('Array 0', 'Array 1', 'Array 2')
arrs[0] = np.random.random(n)
arrs[1] = np.random.random(n)
arrs[2] = np.random.random(n)
table.AddColumn(PVGeo.convertArray(arrs[0], titles[0]))
table.AddColumn(PVGeo.convertArray(arrs[1], titles[1]))
table.AddColumn(PVGeo.convertArray(arrs[2], titles[2]))
###############################

# Use filter
f = TableToGrid()
f.SetExtent(20, 2, 10)
f.SetSpacing(5, 5, 5)
f.SetOrigin(3.3, 6.0, 7)

ido = f.Apply(table)

```
