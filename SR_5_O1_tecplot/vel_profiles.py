#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
flow_0vtk = LegacyVTKReader(FileNames=['/home/puja/Code/2sulzer/STAGE/SR_5_O1/flow_0.vtk'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1471, 860]

# get color transfer function/color map for 'Density'
densityLUT = GetColorTransferFunction('Density')
densityLUT.RGBPoints = [1.1367069482803345, 0.231373, 0.298039, 0.752941, 1.9552515149116516, 0.865003, 0.865003, 0.865003, 2.7737960815429688, 0.705882, 0.0156863, 0.14902]
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
renderView1.CameraFocalPoint = [0.15500000026077032, 0.03503672406077385, 0.0]

# show color bar/color legend
flow_0vtkDisplay.SetScalarBarVisibility(renderView1, True)

# get opacity transfer function/opacity map for 'Density'
densityPWF = GetOpacityTransferFunction('Density')
densityPWF.Points = [1.1367069482803345, 0.0, 0.5, 0.0, 2.7737960815429688, 1.0, 0.5, 0.0]
densityPWF.ScalarRangeInitialized = 1

# create a new 'Legacy VTK Reader'
flow_1vtk = LegacyVTKReader(FileNames=['/home/puja/Code/2sulzer/STAGE/SR_5_O1/flow_1.vtk'])

# show data in view
flow_1vtkDisplay = Show(flow_1vtk, renderView1)
# trace defaults for the display properties.
flow_1vtkDisplay.ColorArrayName = ['POINTS', 'Density']
flow_1vtkDisplay.LookupTable = densityLUT
flow_1vtkDisplay.GlyphType = 'Arrow'
flow_1vtkDisplay.ScalarOpacityUnitDistance = 0.007452509560113646

# show color bar/color legend
flow_1vtkDisplay.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(flow_0vtk)

# create a new 'Calculator'
calculator1 = Calculator(Input=flow_0vtk)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.ResultArrayName = 'velocity_s'
calculator1.Function = '(X-Momentum/Density)*iHat+(Y-Momentum/Density)*jHat\n'

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

# set scalar coloring
ColorBy(calculator1Display, ('POINTS', 'velocity_s'))

# rescale color and/or opacity maps used to include current data range
calculator1Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'velocitys'
velocitysLUT = GetColorTransferFunction('velocitys')
velocitysLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 386.76277339067394, 0.865003, 0.865003, 0.865003, 773.5255467813479, 0.705882, 0.0156863, 0.14902]
velocitysLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'velocitys'
velocitysPWF = GetOpacityTransferFunction('velocitys')
velocitysPWF.Points = [0.0, 0.0, 0.5, 0.0, 773.5255467813479, 1.0, 0.5, 0.0]
velocitysPWF.ScalarRangeInitialized = 1

# set active source
SetActiveSource(flow_1vtk)

# create a new 'Calculator'
calculator2 = Calculator(Input=flow_1vtk)
calculator2.Function = ''

# Properties modified on calculator2
calculator2.ResultArrayName = 'velocity_rotor'
calculator2.Function = '(X-Momentum/Density)*iHat+(Y-Momentum/Density)*jHat\n'

# show data in view
calculator2Display = Show(calculator2, renderView1)
# trace defaults for the display properties.
calculator2Display.ColorArrayName = ['POINTS', 'Density']
calculator2Display.LookupTable = densityLUT
calculator2Display.GlyphType = 'Arrow'
calculator2Display.ScalarOpacityUnitDistance = 0.007452509560113646

# hide data in view
Hide(flow_1vtk, renderView1)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(calculator2Display, ('POINTS', 'velocity_rotor'))

# rescale color and/or opacity maps used to include current data range
calculator2Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'velocityrotor'
velocityrotorLUT = GetColorTransferFunction('velocityrotor')
velocityrotorLUT.RGBPoints = [74.90067114421903, 0.231373, 0.298039, 0.752941, 426.22536646541494, 0.865003, 0.865003, 0.865003, 777.5500617866109, 0.705882, 0.0156863, 0.14902]
velocityrotorLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'velocityrotor'
velocityrotorPWF = GetOpacityTransferFunction('velocityrotor')
velocityrotorPWF.Points = [74.90067114421903, 0.0, 0.5, 0.0, 777.5500617866109, 1.0, 0.5, 0.0]
velocityrotorPWF.ScalarRangeInitialized = 1

# set active source
SetActiveSource(calculator2)

# set scalar coloring
ColorBy(calculator2Display, ('POINTS', 'Mach'))

# rescale color and/or opacity maps used to include current data range
calculator2Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Mach'
machLUT = GetColorTransferFunction('Mach')
machLUT.RGBPoints = [0.11025779694318771, 0.231373, 0.298039, 0.752941, 0.6346689127385616, 0.865003, 0.865003, 0.865003, 1.1590800285339355, 0.705882, 0.0156863, 0.14902]
machLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Mach'
machPWF = GetOpacityTransferFunction('Mach')
machPWF.Points = [0.11025779694318771, 0.0, 0.5, 0.0, 1.1590800285339355, 1.0, 0.5, 0.0]
machPWF.ScalarRangeInitialized = 1

# set active source
SetActiveSource(calculator2)

# set active source
SetActiveSource(flow_0vtk)

# hide data in view
Hide(calculator2, renderView1)

# hide data in view
Hide(calculator1, renderView1)

# set active source
SetActiveSource(flow_0vtk)

# show data in view
flow_0vtkDisplay = Show(flow_0vtk, renderView1)

# show color bar/color legend
flow_0vtkDisplay.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# set active source
SetActiveSource(flow_1vtk)

# show data in view
flow_1vtkDisplay = Show(flow_1vtk, renderView1)

# show color bar/color legend
flow_1vtkDisplay.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(flow_0vtk)

# set scalar coloring
ColorBy(flow_0vtkDisplay, ('POINTS', 'Mach'))

# rescale color and/or opacity maps used to include current data range
flow_0vtkDisplay.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
flow_0vtkDisplay.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(flow_1vtk)

# set scalar coloring
ColorBy(flow_1vtkDisplay, ('POINTS', 'Mach'))

# rescale color and/or opacity maps used to include current data range
flow_1vtkDisplay.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
flow_1vtkDisplay.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(calculator1)

# set active source
SetActiveSource(calculator1)

# show data in view
calculator1Display = Show(calculator1, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(Input=calculator1,
    SeedType='Point Source')
streamTracer1.Vectors = ['POINTS', 'velocity_s']
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
streamTracer1.SeedType.Point1 = [0.11387460396621052, -0.0020036074916403926, 0.0]
streamTracer1.SeedType.Point2 = [0.11695804013797854, 0.18333928625378976, -1.5612511283791264e-16]

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

# set active source
SetActiveSource(calculator2)

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
streamTracer2.SeedType.Point1 = [0.29540554081925335, -0.07252406513027485, 0.0]
streamTracer2.SeedType.Point2 = [0.2958998065570745, 0.05286434920663137, -8.153200337090993e-17]

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

# Properties modified on streamTracer2.SeedType
streamTracer2.SeedType.Point1 = [0.32536075676095366, -0.09520444291470595, -1.249000902703301e-16]
streamTracer2.SeedType.Point2 = [0.3540985118152357, 0.05757159742604148, -1.0408340855860843e-16]

# Properties modified on streamTracer2.SeedType
streamTracer2.SeedType.Point2 = [0.31900811599781476, 0.05714366576973146, -1.2663481374630692e-16]

# Properties modified on streamTracer2.SeedType
streamTracer2.SeedType.Point2 = [0.38062599518989226, 0.07992674715167636, -1.2663481374630692e-16]

# Properties modified on streamTracer2.SeedType
streamTracer2.SeedType.Point2 = [0.43137013099513205, 0.10322762583775635, -1.2663481374630692e-16]

# Properties modified on streamTracer2.SeedType
streamTracer2.SeedType.Point1 = [0.31500481067825153, -0.09520444291470595, -9.020562075079397e-17]
streamTracer2.SeedType.Point2 = [0.34230899468389203, 0.08821150401783802, -1.2663481374630692e-16]

# Properties modified on streamTracer2.SeedType
streamTracer2.SeedType.Point1 = [0.2906683373839015, -0.06983237501208539, 6.591949208711867e-17]
streamTracer2.SeedType.Point2 = [0.29104706157451543, 0.07526657141446026, -1.2663481374630692e-16]

# create a new 'Legacy VTK Reader'
surface_flow_0vtk = LegacyVTKReader(FileNames=['/home/puja/Code/2sulzer/STAGE/SR_5_O1/surface_flow_0.vtk'])

# show data in view
surface_flow_0vtkDisplay = Show(surface_flow_0vtk, renderView1)
# trace defaults for the display properties.
surface_flow_0vtkDisplay.ColorArrayName = ['POINTS', 'Density']
surface_flow_0vtkDisplay.LookupTable = densityLUT
surface_flow_0vtkDisplay.GlyphType = 'Arrow'
surface_flow_0vtkDisplay.ScalarOpacityUnitDistance = 0.02609198993524702

# show color bar/color legend
surface_flow_0vtkDisplay.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(streamTracer2, renderView1)

# hide data in view
Hide(flow_1vtk, renderView1)

# hide data in view
Hide(flow_0vtk, renderView1)

# hide data in view
Hide(streamTracer1, renderView1)

# create a new 'Legacy VTK Reader'
surface_flow_1vtk = LegacyVTKReader(FileNames=['/home/puja/Code/2sulzer/STAGE/SR_5_O1/surface_flow_1.vtk'])

# set active source
SetActiveSource(surface_flow_1vtk)

# show data in view
surface_flow_1vtkDisplay = Show(surface_flow_1vtk, renderView1)
# trace defaults for the display properties.
surface_flow_1vtkDisplay.ColorArrayName = ['POINTS', 'Density']
surface_flow_1vtkDisplay.LookupTable = densityLUT
surface_flow_1vtkDisplay.GlyphType = 'Arrow'
surface_flow_1vtkDisplay.ScalarOpacityUnitDistance = 0.01555286428694803

# show color bar/color legend
surface_flow_1vtkDisplay.SetScalarBarVisibility(renderView1, True)

# show data in view
surface_flow_1vtkDisplay = Show(surface_flow_1vtk, renderView1)

# show color bar/color legend
surface_flow_1vtkDisplay.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(streamTracer1)

# show data in view
streamTracer1Display = Show(streamTracer1, renderView1)

# show color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(streamTracer2)

# show data in view
streamTracer2Display = Show(streamTracer2, renderView1)

# show color bar/color legend
streamTracer2Display.SetScalarBarVisibility(renderView1, True)

# Properties modified on streamTracer2.SeedType
streamTracer2.SeedType.Point1 = [0.2974913006807595, -0.1160769040241227, -3.469446951953614e-18]
streamTracer2.SeedType.Point2 = [0.37368072816979425, 0.08588006987623932, -1.2663481374630692e-16]

# Properties modified on streamTracer2.SeedType
streamTracer2.SeedType.Point2 = [0.31463954616404366, 0.07711157749914761, -1.2663481374630692e-16]

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.23723063757668628, 0.0430985751121872, 0.7109624105923719]
renderView1.CameraFocalPoint = [0.23723063757668628, 0.0430985751121872, 0.0]
renderView1.CameraParallelScale = 0.1256817240716507

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).