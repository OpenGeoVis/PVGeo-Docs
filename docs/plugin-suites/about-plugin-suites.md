# About Plugin Suites
We are deploying *PVGeo* in various sub-packages we call suites. These suites consists of a series of reader or filter plugins (or both) for a general area of geoscientific processing or visualization. For example, we have created a suite called *UBC Mesh Tools* which contains file readers for the UBC Mesh types and filters for processes related to the UBC mesh formats. Another example of a suite is *Model Building*; this is a suite of various plugins that allow a user to create various types of models interactively within ParaView. Take a look at the navigation pane to the left to explore the different plugin suites.


## The Plugin Framework

In developing the *PVGeo* repository, we decided to follow a framework of development that generates various sets of tools that can be used within ParaView or outside in other Python environments with the VTK Python library. This would allow for users of *PVGeo* to be able to use all of the functionality as plugins in ParaView with interactive user menus or outside of ParaView be able to integrate with there existing data processing suites using Python and VTK. This development framework also focuses heavily on the open source paradigm in that *PVGeo* contains many base classes for developers to inherit functionality to aid in the development of new features. Unfortunately, the development of plugins for the ParaView software platform may imply an ambitious programming endeavor, including creating CMakeLists, developing in lower level programming languages like C++, learning new libraries to create interactive GUI components, and building the plugins into the ParaView source code. However, the *PVGeo* module takes advantage of functionality by Kitware that facilitates the rapid development of readers, sources, filters, and writers: instantiations of the `VTKPythonAlgorithmBase` class in Python. Python is an accessible language, easy to learn, and popular among geoscientists using packages like: SimPEG, ObsPy, EarthPy, pyFLOWGO, GeoNotebook, and more. We choose to develop the *PVGeo* library to work well with other Python libraries by following the following framework:

- **Extendable:** This software will harness the established and robust visualization platforms ParaView and VTK, extend their functionality, and remain open-source for contributions and integration into other Python powered geoscientific processing suites.
- **Safe:** The software must preserve data integrity and precision.
- **Dynamic:** The software must enable a dynamic link between external processing software and visualization libraries.
- **Modular:** The software will be modular so that various visualization suites can be implemented separately but also work together. This software should be usable both within and outside of ParaView.
- **Rapid development:** Through further subclasses of the `VTKPythonAlgorithmBase` class and the templates in *PVGeo*, it is easy to prototype and develop a plugin in a matter of minutes without the need to rebuild the software.
- **Computational power:** VTK has NumPy wrapping to allow for the use of Python's complex numerical analysis libraries like SciPy and NumPy.
- **Easy customization by end user:** since most geoscientists know and use Python, they can easily dive into the source code delivered in this repo to tailor it to their needs.
- **Easy GUI component creation:** Graphical User Interface elements can be easily produced to pair with plugins.


### Readers
A reader takes data from files and puts them into the proper VTK and ParaView data structures so that we can visualize that data on the VTK or ParaView pipeline. ParaView comes with a plethora of native data format readers but there are still many more formats in the geosciences that have not been implemented. By creating formats for common geoscientific formats, we hope to make the process of getting data into the ParaView pipeline as simple as possible.


### Filters
A filter modifies, transforms, combines, analyses, processes, etc. data in VTK data structures on either a VTK or ParaView pipeline. Filters provide a means for changing how we visualize data or create a means of generating topology for an input data source to better represent that data in a 3D rendering environment.
For example, we have developed a filter called [***Voxelize Points***](filters-general/voxelize-points.md) which takes a set of scattered points sampled on a rectilinear reference frame and generates voxels for every point such that the volume of data made by the points is filled with topologically connected cells.
Or for another filter, maybe we might have a series of scattered points that we know represent the center of a tunnel or tube that represents a well. We can use a filter to transform those points into a connected line that we then construct a cylinder around. This allows us to save out minimal data (just XYZ points as opposed to complex geometries that make up the tunnel) to our hard drive while still having complex visualizations from that data.


### Sources
A source takes input parameters from a user and generates a data object for visualization or export. In *PVGeo*, we have implemented the *Model Building* suite with many sources that allow for a user to specify attributes of a data set such as a model discretization and have a data source appear in the rendering environment alongside their other data for that scene.



### About `PVGeo`
`PVGeo` is a python module we are developing to modulize all functionality common throughout the plugins. This module will contain the bulk of our code for file readers and visual filters. We are publishing the plugins code base in this manner so that we can easily update/change the code with minor deprecation issues.
