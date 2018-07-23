!!! failure "Description to come!"
    There are a lot of pages in the documentation and we are trying to fill all content as soon as possible. Stay tuned for updates to this page


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
