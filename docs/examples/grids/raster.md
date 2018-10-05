# Landsat Rasters

!!! failure "Further description to come!"
    There are a lot of pages in the documentation and we are trying to fill all content as soon as possible. Stay tuned for updates to this page

This reader used [`espatools`](https://espatools.readthedocs.io/en/latest/) to read Landsat imagery via an XML metadata file.

## Reader
!!! info "{lookup:PVGeo.grids.fileio.LandsatReader}"


## Example

Download any Landsat data from [USGS' Earth Explorer](https://earthexplorer.usgs.gov) and open the XML file adjacent to the data files using PVGeo's Landsat Reader in ParaView.

<div style="text-align: center;"><img src="docs/examples/grids/images/raster-band3.png" alt="menu"></div>

### Select your bands
Go ahead and load up all the data! If you only want a few bands, then select them from the checklist like the image below:

<div style="text-align: center;"><img src="docs/examples/grids/images/raster-menu.png" alt="menu" width="50%"></div>

### Use RGB

If your raster has enough bands for RGB data, then select the *Create Colors* checkbox, display by the new *Colors* array and turn off *Map Scalars* in the properties to display a true color image.

!!! warning
    *Create Colors* is an experimental feature at the moment. We recommend selecting the bands you need then using PVGeo's `ArraysToRGBA` filter.

<div style="text-align: center;"><img src="docs/examples/grids/images/raster-map-scalars.png" alt="menu" width="50%"></div>

<div style="text-align: center;"><img src="docs/examples/grids/images/raster-RGB.png" alt="menu"></div>
