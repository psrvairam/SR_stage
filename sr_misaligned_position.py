#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
flow_0vtk = LegacyVTKReader(FileNames=['SR_Stage/flow_0.vtk'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1471, 860]

# get color transfer function/color map for 'Density'
densityLUT = GetColorTransferFunction('Density')
densityLUT.RGBPoints = [1.0298579931259155, 0.231373, 0.298039, 0.752941, 1.9013529419898987, 0.865003, 0.865003, 0.865003, 2.772847890853882, 0.705882, 0.0156863, 0.14902]
densityLUT.ScalarRangeInitialized = 1.0

# show data in view
flow_0vtkDisplay = Show(flow_0vtk, renderView1)
# trace defaults for the display properties.
flow_0vtkDisplay.ColorArrayName = ['POINTS', 'Density']
flow_0vtkDisplay.LookupTable = densityLUT
flow_0vtkDisplay.GlyphType = 'Arrow'
flow_0vtkDisplay.ScalarOpacityUnitDistance = 0.015087957173809095

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.CameraPosition = [0.15500000026077032, 0.03503672406077385, 10000.0]

# show color bar/color legend
flow_0vtkDisplay.SetScalarBarVisibility(renderView1, True)

# get opacity transfer function/opacity map for 'Density'
densityPWF = GetOpacityTransferFunction('Density')
densityPWF.Points = [1.0298579931259155, 0.0, 0.5, 0.0, 2.772847890853882, 1.0, 0.5, 0.0]
densityPWF.ScalarRangeInitialized = 1

# create a new 'Calculator'
calculator1 = Calculator(Input=flow_0vtk)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.ResultArrayName = 'velocity_stator'
calculator1.Function = '(X-Momentum/Density)*iHat+(Y-Momentum/Density)*jHat'

# show data in view
calculator1Display = Show(calculator1, renderView1)
# trace defaults for the display properties.
calculator1Display.ColorArrayName = ['POINTS', 'Density']
calculator1Display.LookupTable = densityLUT
calculator1Display.GlyphType = 'Arrow'
calculator1Display.ScalarOpacityUnitDistance = 0.015087957173809095

# hide data in view
Hide(flow_0vtk, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(Input=calculator1,
    SeedType='Point Source')
streamTracer1.Vectors = ['POINTS', 'velocity_stator']
streamTracer1.MaximumStreamlineLength = 0.2700733616948128

# init the 'Point Source' selected for 'SeedType'
streamTracer1.SeedType.Center = [0.15500000026077032, 0.03503672406077385, 0.0]
streamTracer1.SeedType.Radius = 0.02700733616948128

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=streamTracer1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=streamTracer1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=streamTracer1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=streamTracer1)

# Properties modified on streamTracer1
streamTracer1.SeedType = 'High Resolution Line Source'

# Properties modified on streamTracer1.SeedType
streamTracer1.SeedType.Point1 = [0.07750041317985935, 0.00612709397824928, -1.6768808563938364e-12]
streamTracer1.SeedType.Point2 = [0.07673246444483825, 0.17948790134700035, -4.689582056016661e-13]

# show data in view
streamTracer1Display = Show(streamTracer1, renderView1)
# trace defaults for the display properties.
streamTracer1Display.ColorArrayName = ['POINTS', 'Density']
streamTracer1Display.LookupTable = densityLUT
streamTracer1Display.GlyphType = 'Arrow'

# hide data in view
Hide(calculator1, renderView1)

# show color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)

# Properties modified on streamTracer1.SeedType
streamTracer1.SeedType.Point1 = [0.24165251453677283, -0.10539608938637139, -1.0942358130705543e-12]
streamTracer1.SeedType.Point2 = [0.25216219108581006, 0.11871403176066231, 7.815970093361102e-13]

# set active source
SetActiveSource(flow_0vtk)

# show data in view
flow_0vtkDisplay = Show(flow_0vtk, renderView1)

# show color bar/color legend
flow_0vtkDisplay.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(calculator1)

# set scalar coloring
ColorBy(calculator1Display, ('POINTS', 'velocity_stator'))

# rescale color and/or opacity maps used to include current data range
calculator1Display.RescaleTransferFunctionToDataRange(True)

# get color transfer function/color map for 'velocitystator'
velocitystatorLUT = GetColorTransferFunction('velocitystator')
velocitystatorLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 416.8586117783825, 0.865003, 0.865003, 0.865003, 833.717223556765, 0.705882, 0.0156863, 0.14902]
velocitystatorLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'velocitystator'
velocitystatorPWF = GetOpacityTransferFunction('velocitystator')
velocitystatorPWF.Points = [0.0, 0.0, 0.5, 0.0, 833.717223556765, 1.0, 0.5, 0.0]
velocitystatorPWF.ScalarRangeInitialized = 1

# set active source
SetActiveSource(calculator1)

# show data in view
calculator1Display = Show(calculator1, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(streamTracer1)

# hide data in view
Hide(flow_0vtk, renderView1)

# set active source
SetActiveSource(flow_0vtk)

# show data in view
flow_0vtkDisplay = Show(flow_0vtk, renderView1)

# show color bar/color legend
flow_0vtkDisplay.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(flow_0vtk, renderView1)

# set active source
SetActiveSource(streamTracer1)

# set active source
SetActiveSource(calculator1)

# set active source
SetActiveSource(streamTracer1)

# hide data in view
Hide(streamTracer1, renderView1)

# set active source
SetActiveSource(streamTracer1)

# show data in view
streamTracer1Display = Show(streamTracer1, renderView1)

# show color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(streamTracer1Display, ('POINTS', 'velocity_stator'))

# rescale color and/or opacity maps used to include current data range
streamTracer1Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Legacy VTK Reader'
flow_1vtk = LegacyVTKReader(FileNames=['SR_Stage/flow_1.vtk'])

# show data in view
flow_1vtkDisplay = Show(flow_1vtk, renderView1)
# trace defaults for the display properties.
flow_1vtkDisplay.ColorArrayName = ['POINTS', 'Density']
flow_1vtkDisplay.LookupTable = densityLUT
flow_1vtkDisplay.GlyphType = 'Arrow'
flow_1vtkDisplay.ScalarOpacityUnitDistance = 0.007452509560113646

# show color bar/color legend
flow_1vtkDisplay.SetScalarBarVisibility(renderView1, True)

# create a new 'Calculator'
calculator2 = Calculator(Input=flow_1vtk)
calculator2.Function = ''

# set active source
SetActiveSource(calculator1)

# set active source
SetActiveSource(calculator2)

# set active source
SetActiveSource(calculator2)

# show data in view
calculator2Display = Show(calculator2, renderView1)
# trace defaults for the display properties.
calculator2Display.ColorArrayName = ['POINTS', 'Density']
calculator2Display.LookupTable = densityLUT
calculator2Display.GlyphType = 'Arrow'
calculator2Display.ScalarOpacityUnitDistance = 0.007452509560113646

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(calculator1, renderView1)

# hide data in view
Hide(streamTracer1, renderView1)

# Properties modified on calculator2
calculator2.ResultArrayName = 'velocity_rotor'
calculator2.Function = '(X-Momentum/Density)*iHat+(Y-Momentum/Density)*jHat'

# show data in view
calculator2Display = Show(calculator2, renderView1)

# hide data in view
Hide(flow_1vtk, renderView1)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(flow_1vtk)

# show data in view
flow_1vtkDisplay = Show(flow_1vtk, renderView1)

# show color bar/color legend
flow_1vtkDisplay.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(calculator2)

# set scalar coloring
ColorBy(calculator2Display, ('POINTS', 'velocity_rotor'))

# rescale color and/or opacity maps used to include current data range
calculator2Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'velocityrotor'
velocityrotorLUT = GetColorTransferFunction('velocityrotor')
velocityrotorLUT.RGBPoints = [8.198624044161495, 0.231373, 0.298039, 0.752941, 671.2540133559373, 0.865003, 0.865003, 0.865003, 1334.3094026677131, 0.705882, 0.0156863, 0.14902]
velocityrotorLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'velocityrotor'
velocityrotorPWF = GetOpacityTransferFunction('velocityrotor')
velocityrotorPWF.Points = [8.198624044161495, 0.0, 0.5, 0.0, 1334.3094026677131, 1.0, 0.5, 0.0]
velocityrotorPWF.ScalarRangeInitialized = 1

# create a new 'Stream Tracer'
streamTracer2 = StreamTracer(Input=calculator2,
    SeedType='Point Source')
streamTracer2.Vectors = ['POINTS', 'velocity_rotor']
streamTracer2.MaximumStreamlineLength = 0.13999998569488525

# init the 'Point Source' selected for 'SeedType'
streamTracer2.SeedType.Center = [0.3499999940395355, 0.017985699698328972, 0.0]
streamTracer2.SeedType.Radius = 0.013999998569488525

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=streamTracer2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=streamTracer2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=streamTracer2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=streamTracer2)

# Properties modified on streamTracer2
streamTracer2.SeedType = 'High Resolution Line Source'

# Properties modified on streamTracer2.SeedType
streamTracer2.SeedType.Point1 = [0.29060987696837154, -0.060955763908869906, -8.668621376273222e-13]
streamTracer2.SeedType.Point2 = [0.3057669910290217, 0.03609720885484857, 0.0]

# show data in view
streamTracer2Display = Show(streamTracer2, renderView1)
# trace defaults for the display properties.
streamTracer2Display.ColorArrayName = ['POINTS', 'Density']
streamTracer2Display.LookupTable = densityLUT
streamTracer2Display.GlyphType = 'Arrow'

# hide data in view
Hide(calculator2, renderView1)

# show color bar/color legend
streamTracer2Display.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(streamTracer2Display, ('POINTS', 'velocity_rotor'))

# rescale color and/or opacity maps used to include current data range
streamTracer2Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
streamTracer2Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(flow_1vtk, renderView1)

# set active source
SetActiveSource(flow_1vtk)

# show data in view
flow_1vtkDisplay = Show(flow_1vtk, renderView1)

# show color bar/color legend
flow_1vtkDisplay.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(calculator2)

# show data in view
calculator2Display = Show(calculator2, renderView1)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(calculator1)

# show data in view
calculator1Display = Show(calculator1, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(streamTracer1)

# show data in view
streamTracer1Display = Show(streamTracer1, renderView1)

# show color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.2590293054804407, -0.0030597945343685965, 10000.0]
renderView1.CameraFocalPoint = [0.2590293054804407, -0.0030597945343685965, 0.0]
renderView1.CameraParallelScale = 0.18401061221330395

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
