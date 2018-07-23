# Why PVGeo?

!!! failure "More to come!"
    Further information to come!

## About the Project
This code base is full of plugins and macros for the open-source, multi-platform, data analysis, and visualization application [**ParaView**](https://www.paraview.org) by Kitware. These plugins are tailored to the visualization of spatially referenced data in the geosciences, especially geophysics. The overarching  goal of this project is to develop set of codes to visually integrate post-processed data for more *intuitive* visualization. To make more intuitive visualizations, we think it is necessary to reference data in relation to features like topography, well locations, survey points, or other known features that are easier to spatially grasp.

This code base deploys tools to perform post-processing visual analysis and interpretation of geophysical data and models and we hope that geophysicists will gain an ability to represent their 3D spatially referenced data intuitively to interested parties and stakeholders. By integrating the visualization of various data, and creating a sort of visual data fusion, interested parties will gain insight into the value of the information in their models. Through visual integration, we try to mimic the reality of the space in which data was acquired so that it will hold meaning to anyone that immerses into the visualization regardless of background.

??? abstract "SAGEEP 2018 Abstract"
    The results of geophysical imaging techniques often hold high significance to stakeholders in the problems addressed yet the effective perception of those results remains a dynamic challenge for all. To illuminate the value of geophysical imaging techniques, we are developing a framework to visually integrate geophysical data and models in 3D which extends into Virtual Reality (VR) as well as statistically analyzing interpretation advantages in VR. The motivation for this effort comes from a desire to directly engage stakeholders with geophysical data gaining Value of Information (VOI) and de-risking decision making in project planning. This framework is a code base that extends the functionality of the open-source visualization platform ParaView by Kitware. These extensions make it possible to visually integrate geophysical data in a multidimensional rendering space so that the end product is interpretable to non-geoscientists and that all parties can gain insight and VOI from geophysical imaging techniques. To show value in the VR presentation of multi-dimensional visualizations, we aim to develop metrics that will analyze the effectiveness of visual analysis in VR compared to traditional methods. We will evaluate these metrics through statistical gaming type protocol, where we will task subjects with making spatial decisions and finding features of interest in complex geoscientific scenes. We hypothesize that VR will bring the needed perception to most efficiently make spatial decisions and detect features of interest as well as convey information such as uncertainty in a usable manner. We will have preliminary results of the gaming protocol by March 2018 as well as share our visual framework along that journey in the form of a GitHub repository titled “PVGeo.” Our goal in sharing the repository is to deliver a toolset that enables geophysicists to rapidly visualize their data and models as well as effectively communicate their findings to interested stakeholders.


## Outline of Goals

* Develop and document geoscientific plugins for ParaView encompassed in various suites. Each suite of plugins will be tailored to specific data formats and/or processing needs in geoscience. These plugins will take advantage of ParaView and VTK’s Python wrapping and use the Python Programmable Filter in ParaView. The advantage to using Python Programmable filters is that they are easily modified by the end user and can be wrapped in XML to create a GUI for its use in ParaView while having the option to directly edit the source code live in ParaView. The suites of plugins will consist of the following plugin types:

    * **Readers:** A reader puts data from files into proper ParaView data structures on the pipeline. These are plugins that read common geoscientific and geophysical spatial data files (GSLIB, UBC Tensor and OcTree meshes, etc.). Also make readers that read common raw data files (packed binary floats, delimited ASCII, etc.)

    * **Filters:** A filter modifies, transforms, combines, analyses, etc. data on the ParaView pipeline. Plugins that perform post-processing analysis of geoscientific data for visualization. For example, filters that build tubes from a series of points that represent a tunnel or filters that take a 1D array, reshape it to 2D or 3D, and make a volumetric model ready for visualization all while adding spatial reference for visual integration.  

    * **Sources:** Plugins that create simple synthetic data sources that could be used for model generation. We are creating a suite of plugins for generating various types of discretized models/meshes which can be exported. Another example could include a sphere or cube with a specified attribute like a spatially varying density or electrical conductivity. Other sources might include using that synthetic sphere or cube to make a volumetric field of some response. These plugins will tailor to the educational needs in applications of this code base.

* Develop and document the `PVGeo` and `pvmacros` Python modules for use in ParaView's Python Shell. These modules will contain all of the macros, batch processing tasks, and common codes to apply to 3D data scenes.

    * The `PVGeo` module will hold all of the code used in the plugins so that shared features across plugins can be called rather the rewritten and so that we can version control the plugins. This module will be primarily for use in the plugins scripts and not necessary for use in the ParaViewPython shell.

    * The `pvmacros` module with be full of macros and other data-independent scripts that can be used directly in the ParaViewPython shell.

* Make tutorials on the use of the tools provided by this repository as well as share how to use ParaView's native features on open source data (for example):

* Develop customizable scripts for the visualization of common data formats. This will include developing scripts on an individual basis to help others quickly visualize their data and models for quality assessment and unique research needs.
