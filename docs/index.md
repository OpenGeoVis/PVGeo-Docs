# *PVGeo*

[![Vimeo](https://img.shields.io/badge/demos-grey.svg?logo=vimeo)](https://vimeo.com/user82050125)
[![Documentation Status](https://readthedocs.org/projects/pvgeo/badge/?version=latest)](http://docs.pvgeo.org/en/latest/?badge=latest)
[![PyPI](https://img.shields.io/pypi/v/PVGeo.svg?logo=python)](https://pypi.org/project/PVGeo/)
[![Build Status](https://img.shields.io/travis/OpenGeoVis/PVGeo/master.svg?label=build&logo=travis)](https://travis-ci.org/OpenGeoVis/PVGeo)
[![AppVeyor](https://ci.appveyor.com/api/projects/status/it085qovtnb0mcgr/branch/master?svg=true)](https://ci.appveyor.com/project/banesullivan/pvgeo/branch/master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4b9e8d0ef37a4f70a2d02c0d53ed096f)](https://www.codacy.com/app/banesullivan/PVGeo?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=OpenGeoVis/PVGeo&amp;utm_campaign=Badge_Grade)
[![codecov](https://codecov.io/gh/OpenGeoVis/PVGeo/branch/master/graph/badge.svg)](https://codecov.io/gh/OpenGeoVis/PVGeo/branch/master)

*PVGeo* is a Python package that contains VTK powered tools for data visualization in geophysics which are wrapped for direct use within the application [**ParaView by Kitware**](https://www.paraview.org). These tools are tailored to data visualization in the geosciences with a heavy focus on structured data sets like 2D or 3D time-varying grids.

On this website, we provide several examples and tutorials of how to use *PVGeo* in a python environment as well as how to use the ParaView plugins delivered along side the python package for common tasks in the visualization of geoscientific data.

Feel free to join the *PVGeo* community on Slack to keep up with new features and for any help using the code library and follow us on Twitter to keep up:

<script async defer src="http://slack.pvgeo.org/slackin.js?large"></script> <a href="https://twitter.com/OpenGeoVis?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-size="large" data-show-count="false">Follow @OpenGeoVis</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


??? question "Suggestions?"
    If you have an idea for a file reader, data filter, ParaView plugin, or would like to see how we would address a geoscientific visualization problem with ParaView, please post your thoughts on the [**issues page**](https://github.com/OpenGeoVis/PVGeo/issues) or become involved with the *PVGeo* community discussions on [**Slack**](http://slack.pvgeo.org/).

??? tip "How to use *PVGeo*"
    To download and use the *PVGeo* code library, follow the installation instructions on the [**Getting Started Page**](overview/getting-started#install-pvgeo). If you are interested in development, all code is published on the GitHub repository *PVGeo* linked to this page. Click the 'PVGeo on GitHub' link on the right side of the menu bar at the top to find all of the code or you can follow [**this link**](https://github.com/OpenGeoVis/PVGeo). Also take a look at the [**Development Guide**](dev-guide/contributing/)

??? tip "How to explore this documentation"
    *On a Desktop:* There are six main sections to this website shown in the navigation tab at the top of the page. Use these tabs to explore the different aspects of the project! Use the sidebar to the right to explore the contents of the current page and use the sidebar to the left to find all the different pages for this active section/tab. Here is a list of the available sections:

    - **Overview:** An introduction to the project with installation details on how to get started.
    - **Examples:** A guide to all of the plugins we have implemented for use directly in ParaView. This section has all the information you will need to understand how to use our plugins and how we group them together into what we call *suites*. This section has high level explanations and examples while the [docs website](http://docs.pvgeo.org) has the code documentation.
    - **Docs:** This tab will forward you to the [code docs website](http://docs.pvgeo.org)
    - **PV Macros:** A guide on how to use all of the macros developed in the `pvmacros` module.
    - **Resources:** A conglomerate of additional resources that are helpful when using ParaView and VTK for geoscientific applications.
    - **Development Guide:** This is an all encompassing guid on how to start making your own plugins as well as how to contribute to the *PVGeo* repository.


??? failure "Web renderings not working?"
    If the web renderings like the one below in the [demo section](#demo) of this page are not working, then please make sure to enable javascript in your web browser.


## Demo
Check out the [**Demo Page**](http://demo.pvgeo.org) to see video demos and interactive demos like the scene below. This is an example of three data sets visually integrated using our framework within ParaView then exported to a shareable format. Go ahead, click it and move it around!

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="http://viewer.pvgeo.org/?fileURL=https://dl.dropbox.com/s/ypdmmwb3qmax3r6/homepage.vtkjs?dl=0" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>


-------

## About the Authors [![GitHub contributors](https://img.shields.io/github/contributors/OpenGeoVis/PVGeo.svg?logo=github&logoColor=white)](https://GitHub.com/OpenGeoVis/PVGeo/graphs/contributors/) [![Open Source](https://img.shields.io/badge/open--source-yes-brightgreen.svg)](https://opensource.com/resources/what-open-source)

The *PVGeo* code library is managed by [**Bane Sullivan**](http://banesullivan.com), graduate student in the Hydrological Science and Engineering interdisciplinary program at the Colorado School of Mines under Whitney Trainor-Guitton. If you have questions please inquire with [**info@pvgeo.org**](mailto:info@pvgeo.org) or join the *PVGeo* community on Slack: <script async defer src="http://slack.pvgeo.org/slackin.js"></script>


!!! info "Thank you to our contributors!"
    It is important to note the project is open source and that many features in this repository were made possible by contributors volunteering their time. Please take a look at the [**Contributors Page**](https://github.com/OpenGeoVis/PVGeo/graphs/contributors) to learn more about the developers of *PVGeo*.

------

<!--

## Documentation

All documentation for the code produced from this project is included on the [**docs website**](http://docs.pvgeo.org). This website contains a high level explanation of all of the produced plugins (filters, readers, sources, and sinks) and macros with detailed use examples with other overarching project documentation. Use the menu bar at the top to explore this website and to find all the examples for plugins, macros, and more as you need. There are also details on how to [**build your own plugins**](./dev-guide/build-your-own-plugins.md), how to [**export data scenes**](./pvmacros/export/exportvtkjs.md), and transferring your complex data scenes into [**virtual reality**](./virtual-reality/entering-virtual-reality.md).

The purpose of including all this extra documentation is to provide a convenient location for geoscientists to learn how to tailor ParaView to their needs because data representation and communication are an integral part of success in science. To efficiently represent our spatial data is the first step to becoming successful and productive geoscientists. This is the principle behind why we are publishing this documentation along with the code in the repository. Not only do we want to communicate the effort and motivation for this project efficiently, but we want to empower others to communicate their scientific endeavors through spatial visualizations effectively.

### Plugin Documentation
There is a page dedicated to every plugin and on these pages, you will find implementation details, parameters, code quirks, and general usage information. We are working to have an example for every reader and filter so that users can get a feel for what is going on and how they might apply these plugins to address their needs. Since almost all geoscientific data is proprietary, these tutorials will likely come late so that we can find good open data sets and models that users can find outside of this repo for free.

### Macro documentation
Each macro produced in `pvmacros` will have a distinct purpose, be it to export isometric screenshots of any data scene or create various types of slices through a data volume. The macros will have broad applications and be formatted to work with generally any data scene or data of specific formats so that they can be easily expanded upon to complete specific tasks. For the macros, we will try to immediately have sample data and a tutorial upon publishing with documentation of what we are doing and why.

-->


<a class="twitter-timeline" data-height="750" data-theme="light" href="https://twitter.com/OpenGeoVis?ref_src=twsrc%5Etfw">Tweets by OpenGeoVis</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
