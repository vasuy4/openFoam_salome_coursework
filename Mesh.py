#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.13.0 with dump python functionality
###

import sys
import salome
import json
import os

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'/home/artem/Downloads/artem')

###
### SHAPER component
###

from SketchAPI import *

from salome.shaper import model

model.begin()
partSet = model.moduleDocument()

### Create Part
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
minSize: float = 0.5
maxSize: float = 3
with open(os.path.expanduser("~/Downloads/artem/data.json"), "r") as file:
    data = json.load(file)
    model.addParameter(Part_1_doc, "heightS", data["heightS"])
    model.addParameter(Part_1_doc, "heightB", data["heightB"])
    model.addParameter(Part_1_doc, "widthL", data["widthL"])
    model.addParameter(Part_1_doc, "widthR", data["widthR"])
    model.addParameter(Part_1_doc, "angle", data["angle"])
    model.addParameter(Part_1_doc, "triangle", data["triangle"])
    model.addParameter(Part_1_doc, "gap", data["gap"])
    model.addParameter(Part_1_doc, "distanceToTriangle", data["distanceToTriangle"])
    minSize = data["minSize"]
    maxSize = data["maxSize"]

# model.addParameter(Part_1_doc, "heightS", '33')
# model.addParameter(Part_1_doc, "heightB", '55')
# model.addParameter(Part_1_doc, "widthL", '66')
# model.addParameter(Part_1_doc, "widthR", '22')
# model.addParameter(Part_1_doc, "angle", '11')
# model.addParameter(Part_1_doc, "triangle", '6')
# model.addParameter(Part_1_doc, "gap", '3')
# model.addParameter(Part_1_doc, "distanceToTriangle", '15')
### Create Sketch
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))

### Create SketchLine
SketchLine_1 = Sketch_1.addLine(0, 0, 0, 33)
Sketch_1.setVertical(SketchLine_1.result())

### Create SketchLine
SketchLine_2 = Sketch_1.addLine(0, 33, 66, 39.35507718103754)
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_2.startPoint())

### Create SketchLine
SketchLine_3 = Sketch_1.addLine(66, 39.35507718103754, 66, 43.99999999999999)
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchLine_3.startPoint())
Sketch_1.setVertical(SketchLine_3.result())

### Create SketchLine
SketchLine_4 = Sketch_1.addLine(66, 43.99999999999999, 88, 43.99999999999999)
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_4.startPoint())
Sketch_1.setHorizontal(SketchLine_4.result())

### Create SketchLine
SketchLine_5 = Sketch_1.addLine(0, 0, 66, -6.355077181037557)
Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchLine_5.startPoint())

### Create SketchLine
SketchLine_6 = Sketch_1.addLine(66, -11.00000000000001, 66, -6.355077181037557)
Sketch_1.setCoincident(SketchLine_5.endPoint(), SketchLine_6.endPoint())
Sketch_1.setVertical(SketchLine_6.result())

### Create SketchLine
SketchLine_7 = Sketch_1.addLine(66, -11.00000000000001, 88, -11.00000000000001)
Sketch_1.setHorizontal(SketchLine_7.result())

### Create SketchLine
SketchLine_8 = Sketch_1.addLine(88, -11.00000000000001, 88, 43.99999999999999)
Sketch_1.setCoincident(SketchLine_7.endPoint(), SketchLine_8.startPoint())
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_8.endPoint())
Sketch_1.setVertical(SketchLine_8.result())

### Create SketchLine
SketchLine_9 = Sketch_1.addLine(48.02762280979693, 34.61065880359235, 54.00000000000001, 35.18573331871369)

### Create SketchLine
SketchLine_10 = Sketch_1.addLine(51.51184054406257, 29.72596569345443, 48.02762280979693, 34.61065880359235)
Sketch_1.setCoincident(SketchLine_9.startPoint(), SketchLine_10.endPoint())

### Create SketchLine
SketchLine_11 = Sketch_1.addLine(51.51184054406257, 29.72596569345443, 54.00000000000001, 35.18573331871369)
Sketch_1.setCoincident(SketchLine_10.startPoint(), SketchLine_11.startPoint())
Sketch_1.setCoincident(SketchLine_9.endPoint(), SketchLine_11.endPoint())

### Create SketchLine
SketchLine_12 = Sketch_1.addLine(48.02762280979692, -1.610658803592363, 53.99999999999999, -2.185733318713708)

### Create SketchLine
SketchLine_13 = Sketch_1.addLine(53.99999999999999, -2.185733318713708, 51.51184054406193, 3.274034306546194)
Sketch_1.setCoincident(SketchLine_12.endPoint(), SketchLine_13.startPoint())

### Create SketchLine
SketchLine_14 = Sketch_1.addLine(48.02762280979692, -1.610658803592363, 51.51184054406193, 3.274034306546194)
Sketch_1.setCoincident(SketchLine_12.startPoint(), SketchLine_14.startPoint())
Sketch_1.setCoincident(SketchLine_13.endPoint(), SketchLine_14.endPoint())
Sketch_1.setLength(SketchLine_1.result(), "heightS")
Sketch_1.setLength(SketchLine_7.result(), "widthR")
Sketch_1.setCoincident(SketchLine_7.startPoint(), SketchLine_6.startPoint())
Sketch_1.setEqual(SketchLine_4.result(), SketchLine_7.result())
Sketch_1.setParallel(SketchLine_12.result(), SketchLine_5.result())
Sketch_1.setParallel(SketchLine_9.result(), SketchLine_2.result())
Sketch_1.setLength(SketchLine_9.result(), "triangle")
Sketch_1.setEqual(SketchLine_9.result(), SketchLine_11.result())
Sketch_1.setEqual(SketchLine_9.result(), SketchLine_10.result())
Sketch_1.setEqual(SketchLine_9.result(), SketchLine_12.result())
Sketch_1.setEqual(SketchLine_12.result(), SketchLine_14.result())
Sketch_1.setEqual(SketchLine_12.result(), SketchLine_13.result())

### Create SketchConstraintAngle
Sketch_1.setAngle(SketchLine_2.result(), SketchLine_5.result(), "angle", type = "Direct")
Sketch_1.setEqual(SketchLine_3.result(), SketchLine_6.result())
Sketch_1.setLength(SketchLine_8.result(), "heightB")
Sketch_1.setDistance(SketchLine_10.endPoint(), SketchLine_2.result(), "gap", True)
Sketch_1.setDistance(SketchLine_12.startPoint(), SketchLine_5.result(), "gap", True)
Sketch_1.setDistance(SketchLine_3.result(), SketchLine_11.endPoint(), "distanceToTriangle - triangle/2", True)
Sketch_1.setDistance(SketchLine_6.result(), SketchLine_12.endPoint(), "distanceToTriangle-triangle/2", True)
Sketch_1.setDistance(SketchLine_1.result(), SketchLine_6.startPoint(), "widthL", True)
Sketch_1.setDistance(SketchLine_4.result(), SketchLine_1.endPoint(), "heightB/2-heightS/2", True)

### Create SketchProjection
SketchProjection_1 = Sketch_1.addProjection(model.selection("VERTEX", "PartSet/Origin"), False)
SketchPoint_1 = SketchProjection_1.createdFeature()
Sketch_1.setCoincident(SketchAPI_Point(SketchPoint_1).coordinates(), SketchLine_1.startPoint())
model.do()
Sketch_1.changeFacesOrder([[SketchLine_5.result(), SketchLine_6.result(), SketchLine_7.result(), SketchLine_8.result(), SketchLine_4.result(), SketchLine_3.result(), SketchLine_2.result(), SketchLine_1.result(), SketchLine_9.result(), SketchLine_11.result(), SketchLine_10.result(), SketchLine_14.result(), SketchLine_13.result(), SketchLine_12.result()],
                           [SketchLine_12.result(), SketchLine_13.result(), SketchLine_14.result()],
                           [SketchLine_10.result(), SketchLine_11.result(), SketchLine_9.result()]
                          ])
model.do()

### Create Face
Face_1 = model.addFace(Part_1_doc, [model.selection("FACE", "Sketch_1/Face-SketchLine_5f-SketchLine_6r-SketchLine_7f-SketchLine_8f-SketchLine_4r-SketchLine_3r-SketchLine_2r-SketchLine_1r-SketchLine_9f-SketchLine_11r-SketchLine_10f-SketchLine_14f-SketchLine_13r-SketchLine_12r")])

### Create Extrusion
Extrusion_1 = model.addExtrusion(Part_1_doc, [model.selection("FACE", "Sketch_1/Face-SketchLine_5f-SketchLine_6r-SketchLine_7f-SketchLine_8f-SketchLine_4r-SketchLine_3r-SketchLine_2r-SketchLine_1r-SketchLine_9f-SketchLine_11r-SketchLine_10f-SketchLine_14f-SketchLine_13r-SketchLine_12r")], model.selection(), 5, 5, "Faces|Wires")

### Create Group
Group_1 = model.addGroup(Part_1_doc, "Faces", [model.selection("FACE", "Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_1")])
Group_1.setName("inlet")
Group_1.result().setName("inlet")

### Create Group
Group_2 = model.addGroup(Part_1_doc, "Faces", [model.selection("FACE", "Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_8")])
Group_2.setName("outlet")
Group_2.result().setName("outlet")

### Create Group
Group_3 = model.addGroup(Part_1_doc, "Faces", [model.selection("FACE", "Extrusion_1_1/To_Face"), model.selection("FACE", "Extrusion_1_1/From_Face")])
Group_3.setName("frontAndBack")
Group_3.result().setName("frontAndBack")

### Create Group
Group_4_objects = [model.selection("FACE", "Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_2"),
                   model.selection("FACE", "Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_3"),
                   model.selection("FACE", "Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_4"),
                   model.selection("FACE", "Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_5"),
                   model.selection("FACE", "Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_6"),
                   model.selection("FACE", "Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_7"),
                   model.selection("FACE", "Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_9"),
                   model.selection("FACE", "Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_11"),
                   model.selection("FACE", "Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_10"),
                   model.selection("FACE", "Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_12"),
                   model.selection("FACE", "Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_14"),
                   model.selection("FACE", "Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_13")]
Group_4 = model.addGroup(Part_1_doc, "Faces", Group_4_objects)
Group_4.setName("walls")
Group_4.result().setName("walls")

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
Face_1_1, = SHAPERSTUDY.shape(model.featureStringId(Face_1))
Extrusion_1_1, inlet, outlet, frontAndBack, walls, = SHAPERSTUDY.shape(model.featureStringId(Extrusion_1))
###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

Mesh_1 = smesh.Mesh(Extrusion_1_1,'Mesh_1')
NETGEN_1D_2D_3D = Mesh_1.Tetrahedron(algo=smeshBuilder.NETGEN_1D2D3D)
NETGEN_3D_Parameters_1 = NETGEN_1D_2D_3D.Parameters()
NETGEN_3D_Parameters_1.SetMaxSize( maxSize )
NETGEN_3D_Parameters_1.SetMinSize( minSize )
NETGEN_3D_Parameters_1.SetSecondOrder( 0 )
NETGEN_3D_Parameters_1.SetOptimize( 1 )
NETGEN_3D_Parameters_1.SetFineness( 2 )
NETGEN_3D_Parameters_1.SetChordalError( -1 )
NETGEN_3D_Parameters_1.SetChordalErrorEnabled( 0 )
NETGEN_3D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_3D_Parameters_1.SetFuseEdges( 1 )
NETGEN_3D_Parameters_1.SetQuadAllowed( 0 )
NETGEN_3D_Parameters_1.SetCheckChartBoundary( 0 )
inlet_1 = Mesh_1.GroupOnGeom(inlet,'inlet',SMESH.FACE)
[ inlet_1 ] = Mesh_1.GetGroups()
outlet_1 = Mesh_1.GroupOnGeom(outlet,'outlet',SMESH.FACE)
[ inlet_1, outlet_1 ] = Mesh_1.GetGroups()
frontAndBack_1 = Mesh_1.GroupOnGeom(frontAndBack,'frontAndBack',SMESH.FACE)
[ inlet_1, outlet_1, frontAndBack_1 ] = Mesh_1.GetGroups()
walls_1 = Mesh_1.GroupOnGeom(walls,'walls',SMESH.FACE)
[ inlet_1, outlet_1, frontAndBack_1, walls_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.Compute()
Mesh_1.CheckCompute()
[ inlet_1, outlet_1, frontAndBack_1, walls_1 ] = Mesh_1.GetGroups()
try:
  Mesh_1.ExportUNV( r'/home/artem/Downloads/artem/Mesh.unv', 0 )
  pass
except:
  print('ExportUNV() failed. Invalid file name?')


## Set names of Mesh objects
smesh.SetName(inlet_1, 'inlet')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')
smesh.SetName(walls_1, 'walls')
smesh.SetName(outlet_1, 'outlet')
smesh.SetName(NETGEN_1D_2D_3D.GetAlgorithm(), 'NETGEN 1D-2D-3D')
smesh.SetName(frontAndBack_1, 'frontAndBack')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
