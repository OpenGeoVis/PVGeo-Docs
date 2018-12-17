Here is a list of features that are shortly coming to this repo.We will try to regularly update this page; for a more update view of our activity, please check out the different projects on the GitHub page [**here**](https://github.com/OpenGeoVis/PVGeo/projects).

More documentation is soon to come. We want to do it right: with tutorials, example data, and detailed justification for need and use of each reader, filter, and macro.

!!! info "Suggestions?"
    We need **your** suggestions for what kinds of file format readers to make as well as ideas for filters to meet your data needs. Post on the [**issues page**](https://github.com/OpenGeoVis/PVGeo/issues) on GitHub as a feature request.

    Don't have a GitHub account but still have ideas or questions? Post a comment at the [bottom of this page](#comments) or join the *PVGeo* community discussions on [**Slack**](http://slack.pvgeo.org/).

### Readers
- [ ] **Open Mining Format:** Project files containg all data types. More info found [**here**](https://github.com/GMSGDataExchange/omf). *NOTE: We opened a [**pull request for omf**](https://github.com/GMSGDataExchange/omf/pull/27) that needs to be addressed and finished before further progress on this.*
- [ ] **Well logs:** Readers for common formats (LAS) and easy ways to project well logs in XYZ space. [Details here](http://www.cwls.org/las/)
- [ ] **ESRI shape files:** Details [**here**](https://www.esri.com/library/whitepapers/pdfs/shapefile.pdf) and [**here**](https://en.wikipedia.org/wiki/Shapefile)
- [x] [**ESRI Grid**](../examples/grids/esri-grid.md): 2D ESRI ASCII and binary grid data files
- [x] [**UBC Tensor Meshes**](../examples/ubc/tensor-grids.md): both 2D and 3D implemented with time series capabilities
- [x] [**UBC OcTree Mesh**](../examples/ubc/octree.md): fully implemented but we need test mesh-model file pairs with time series capabilities

<!---
- [ ] **ESRI Grid:** Details [**here**](https://en.wikipedia.org/wiki/Esri_grid) and [**here**](http://desktop.arcgis.com/en/arcmap/10.3/manage-data/raster-and-images/esri-grid-format.htm)
-->

### Filters

- [ ] **Transpose Grid:** Transpose or swap axes of grid data sets (vtkImageData and vtkRectilinearGrid)
- [x] **Extract Array:** This will allow you to extract any array from any data structure as a `vtkTable`.
- [x] **Reshape Table:** Adding ability to reshape using Fortran ordering on the currently available filter.
- [x] **[Voxelize Points](../examples/filters-general/voxelize-points.md):** This will take a point set and generate voxels of some specified size at every point or estimate an appropriate voxel size if the points are uniformly spaced.
- [x] **[Many Slices Along Points](../examples/filters-general/many-slices-along-points.md):** Generate many slices of dataset along a line at every point on that line (normal is the vector from that point to the next).
- [x] **[Append Model to UBC Mesh](../examples/ubc/add-model.md):** This will load a model file and tag it on to vtkStructuredGrid loaded from a UBC Mesh reader. Think of it as appending models as attributes to the 3D mesh.

<!---
**Structure Point Set:** This will take scattered point data and create connectivity/structure either in the form of hexahedrons or quads. More info to come.
-->
### Macros in `pvmacros`
- [x] Save screenshots in isometric views, side, top, etc. in an automated fashion
- [x] [Export a scene](../pvmacros/export/exportvtkjs.md) to a shareable 3D format

### Scripts
- [ ] How to start making your own scripts (tips, tricks, and general advice)
- [ ] A few sample scripts to set up tutorial environments.

### Examples and Other Docs
- Tutorials for each filter/reader/macro will be in their respective documentation.
- [ ] How to send data scenes made using the Readers, Filters, and Macros in this repository over to the Virtual Reality build of ParaView
- [ ] How to build your own plugins using this project's framework and build scripts
- [ ] Importing DEM topography (with/without satellite imagery)
- [ ] Slicing/cropping a data scene through all components/datasets (managing links)
