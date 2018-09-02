# Example Contents
Here is an outline of all the *PVGeo* example pages categorized by suite then by type of functionality.

-----
## General Filters

### Point/Line Sets

- [Add Cell Connectivity to Points](./filters-general/add-cell-connectivity-to-points.md): Generates a line of a series of points
- [Extract Points](./filters-general/extract-points.md): Extract points and attributes form a dataset with valid point data
- [Points to PolyData](./filters-general/points-to-polydata.md): A helper to generate `vtkPolyData` for visualization from a 2D NumPy array of points
- [Points to Tube](./filters-general/points-to-tube.md): Generates a tube/cylinder from a series of points
- [Rotate Points](./filters-general/rotate-points.md): Rotates the point data on an XY plane.
- [Rotation Tool](./filters-general/rotation-tool.md): A set of helpers for coordinate rotations
- [Voxelize Points](./filters-general/voxelize-points.md): Generates a set of voxels / creates a volume of data from a point set

### Mathematical Operations

- [Array Math](./filters-general/array-math.md): Perform a mathematical operation between two arrays in a given data set
- [Normalize Array](./filters-general/normalize-array.md): Perform a mathematical operation on a single array in a given dataset

### Slicing

- [Many Slices Along Axis](./filters-general/many-slices-along-axis.md): Generate *N* slices of a dataset along a specified axis
- [Many Slices Along Points](./filters-general/many-slices-along-points.md): Generate *N* slices of a dataset along a series of points
- [Slice Through Time](./filters-general/slice-through-time.md): Generate a slice of a dataset that translates through time (animated)

### Table Operations

- [Combine Tables](./filters-general/combine-tables.md): Combine two tables with the same number of rows
- [Reshape Table](./filters-general/reshape-table.md): Treat a table as a 2D array and reshape it to a differently sized 2D array
- [Extract Array](./filters-general/extract-array.md): Extract any data array fom a dataset to create a `vtkTable` containing that array.


-----
## General Readers

### Binary/Serialized Data

- [Binary Packed Data](./readers-general/binary-packed-data.md): Reads a 1D data array from a file containing binary numerical data
- [Madagascar SSRSF](./readers-general/madagascar-ssrsf.md): Read the Madagascar Single Stream RSF file format

### ASCII Data

- [Delimited Text](./readers-general/delimited-text.md): A generic reader for ASCII / delimited data files. Frequently inherited.
- [XYZ Files](./readers-general/xyz-reader.md): A makeshift reader for delimited files with varying delimiters for data array titles

-----
## Grid Tools


### Subsetting

- [Extract Topography](./grids/extract-topography.md): Use a topography surface to add an active cells field to an input dataset

### Transformations

- [Flip Grid Axii](./grids/reverse-grid-axii.md): Reverse data along any axis of an input grid
- [Table to Uniform Grid](./grids/table-to-uniform-grid.md): Generate a uniform grid from a table
- [Translate Origin of Grid](./grids/translate-origin-of-grid.md): Translate the corner / origin of an input grid

### Surfer

- [Surfer Grids](./grids/surfer-grid.md): Reader and writer for the Surfer grid format.


-----
## GSLIB & SGeMS

- [GSLIB Table](./gslib/gslib.md): Produce a `vtkTable` from a GSLib file
- [SGeMS Grid](./gslib/sgems-grid.md): Produce a `vtkImageData` (uniform grid) from an SGeMS grid data file

-----
## Model Building

- [Create Earth Source](./model-building/create-earth-source.md): Create `vtkPolyData` with global continents
- [Create Rectilinear Grid](./model-building/create-rectilinear-grid.md): Create a rectilinear grid / tensor mesh (`vtkRectilinearGrid`)
- [Create Uniform Grid](./model-building/create-uniform-grid.md): Create a uniform grid (`vtkImageData`)

-----
## Tunneling

- [Animate TBM](./tunneling/animate-tbm.md): Animate a tunnel boring machine

-----
## UBC Mesh Tools

- [Append Model](./ubc/add-model.md): Add a model attribute to a UBC style grid (supports time series)
- [Read OcTree](./ubc/octree.md): Read an UBC OcTree grid file and a single time series model files
- [Read Tensor Meshes](./ubc/tensor-grids.md): Read an UBC Tensor Mesh grid file and a single time series model files
