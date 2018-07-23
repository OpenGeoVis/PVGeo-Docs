# About Examples
`PVGeo` is a python module we are developing to contain the bulk of our code for file readers and filters. *PVGeo* is deployed in various sub-packages called *suites*. These *suites* consist of a series of reader, filter, source, or writer plugins (or any combination of those) for a general area of geoscientific processing and visualization.

Take a look at the navigation pane to the left to explore the different suites in their drop down menu. Each feature (reader, filter, etc.) has its own page where you can find an overview of that feature, an example of how to use it directly in ParaView, and an example on how to use it in a standard Python environment.

For example specific questions, concerns, or insights, please leave a comment at the bottom of that example's page for other users to find. If you think there may be a serious problem with an example, please open an issue on the [**Issues Page**](https://github.com/OpenGeoVis/PVGeo/issues) so that we can promptly fix it.


------
## Types of Features

### Readers
A reader takes data from files and puts them into the proper VTK and ParaView data structures so that we can visualize that data on the VTK or ParaView pipeline. ParaView comes with a plethora of native data format readers but there are still many more formats in the geosciences that have not been implemented. By creating formats for common geoscientific formats, we hope to make the process of getting data into the ParaView pipeline as simple as possible.


### Filters
A filter modifies, transforms, combines, analyses, processes, etc. data in VTK data structures on either a VTK or ParaView pipeline. Filters provide a means for changing how we visualize data or create a means of generating topology for an input data source to better represent that data in a 3D rendering environment.
For example, we have developed a filter called [***Voxelize Points***](filters-general/voxelize-points.md) which takes a set of scattered points sampled on a rectilinear reference frame and generates voxels for every point such that the volume of data made by the points is filled with topologically connected cells.
Or for another filter, maybe we might have a series of scattered points that we know represent the center of a tunnel or tube that represents a well. We can use a filter to transform those points into a connected line that we then construct a cylinder around. This allows us to save out minimal data (just XYZ points as opposed to complex geometries that make up the tunnel) to our hard drive while still having complex visualizations from that data.


### Sources
A source takes input parameters from a user and generates a data object for visualization or export. In *PVGeo*, we have implemented the *Model Building* suite with many sources that allow for a user to specify attributes of a data set such as a model discretization and have a data source appear in the rendering environment alongside their other data for that scene.


### Writers
These features have not yet been deployed but they will enable users to save data from VTK data structures in ParaView to common geoscientific data formats.
