#! pvpython

# import the simple module from the paraview
from os import listdir
from os.path import isfile, join
from pvmacros import *

import sys
from paraview.simple import LoadPlugin
sys.path.append('/Users/bane/anaconda3/envs/paraview/lib/python2.7/site-packages/')
LoadPlugin('/Users/bane/Documents/OpenGeoVis/Software/PVGeo/PVPlugins/PVGeo_All.py')
from paraview.simple import *

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new GlobeSource from PVGeo
cone1 = GlobeSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
cone1Display = Show(cone1, renderView1)
# trace defaults for the display properties.
cone1Display.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

#### uncomment the following to render all views and export
RenderAllViews()
export.exportVTKjs(FileName='test-pvpython')
# alternatively, if you want to write images, you can use SaveScreenshot(...).
