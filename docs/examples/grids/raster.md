# Landsat Rasters


This reader uses [**espatools**](https://espatools.readthedocs.io/en/latest/) to read Landsat imagery via an XML metadata file. [**Espatools**](https://espatools.readthedocs.io/en/latest/) is an open-source Python package for simple loading of Landsat imagery as NumPy arrays and we have built an easy to use interface to load any Landsat imagery directly into ParaView with an ability to choose predefined color schemes!


<div style="text-align: center;"><img src="docs/examples/grids/images/raster-collage.png" alt="collage" width="97%"></div>


Overall, the ``LandsatReader`` in PVGeo is meant for direct use in ParaView and we would not recommend using ``LandsatReader`` in a standalone Python environment as ``espatools`` has a much simpler API. If you'd like to see the code docs for this reader, then:  {lookup:PVGeo.grids.fileio.LandsatReader}.


## Example

Download any Landsat data from [**USGS' Earth Explorer**](https://earthexplorer.usgs.gov) and open the XML file adjacent to the data files using PVGeo's Landsat Reader in ParaView.

For this example, we downloaded Landsat 8 imagery over Golden & Boulder, Colorado. This raster set is from Path 34 Row 32 during June 27, 2018. The demonstrated dataset comes as a `.tar.gz` compressed dataset which contains 10 bands (`.tif` files) and a few metadata files (`.txt` and `.xml` files). `espatools` is built to parse the `.xml` metadata file to read all of the bands for that dataset and provide a convenient and intuitive means of accessing that metadata along side the raw data in a Python environment. Using PVGeo in ParaView, you can select *File->Open...* and select the `.xml` metadata file and PVGeo will know to use the `LandsatReader` to read all of the bands.


### Select your bands
Go ahead and load up all the data! If you only want a few bands, then select them from the checklist like the image below:

Select your bands using the checkboxes. We usually load all of the bands but if you want to conserve memory and have faster file reads, definitely only select the bands you desire.

<div style="text-align: center;"><img src="docs/examples/grids/images/raster-menu.png" alt="menu" width="50%"></div>

After loading you can select any of the bands as data arrays to display in the Render View. Here is an example of Band 3 from our sample dataset:

<div style="text-align: center;"><img src="docs/examples/grids/images/raster-band3.png" alt="band3"></div>


### Use RGB Color Schemes

If your raster has enough bands for RGB data, then select the a *Color Scheme* from the drop down menu.
This will add a new RGB data array for your raster set. To see the RGB values in the Render View, turn off *Map Scalars* in the properties to display a true color image.

!!! warning
    *Color Scheme* uses predefined color schemes for the raster set's satellite which ``espatools`` manages on the backend. You may need to load all data arrays/bands for this to work. We recommend selecting the bands you need then using PVGeo's `ArraysToRGBA` filter.

Select a *Color Scheme*:

<div style="text-align: center;"><img src="docs/examples/grids/images/raster-color-scheme.png" alt="menu" width="50%"></div>

Be sure to turn off *Map Scalars* to see the RGB values:

<div style="text-align: center;"><img src="docs/examples/grids/images/raster-map-scalars.png" alt="menu" width="50%"></div>

<div style="text-align: center;"><img src="docs/examples/grids/images/raster-RGB.png" alt="menu"></div>
