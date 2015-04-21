#creates Custom Menu item.
#this script should be put in the following folder:
# C:/users/<user name>/AppData/Local/AgiSoft/PhotoScan Pro/scripts

import PhotoScan 
import math


def squareToMax():

	doc = PhotoScan.app.document

	chunk = doc.chunk
	reg = chunk.region
	S = reg.size
	A = max([S.x, S.y, S.z])
	reg.size = PhotoScan.Vector( [A,A,A] )
	chunk.region = reg

	print("Script finished. Region is now square\n")

def squareToMin():

	doc = PhotoScan.app.document

	chunk = doc.chunk
	reg = chunk.region
	S = reg.size
	A = min([S.x, S.y, S.z])
	reg.size = PhotoScan.Vector( [A,A,A] )
	chunk.region = reg

	print("Script finished. Region is now square\n")

def scootRegionPosX():
	doc = PhotoScan.app.document

	chunk = doc.chunk
	reg = chunk.region

	T = chunk.transform.rotation.inv() * PhotoScan.Vector([.1,0.0,0.0])
	reg.center += T
	chunk.region = reg

def scootRegionNegX():
	doc = PhotoScan.app.document

	chunk = doc.chunk
	reg = chunk.region

	T = chunk.transform.rotation.inv() * PhotoScan.Vector([-.1,0.0,0.0])
	reg.center += T
	chunk.region = reg

def scootRegionPosY():
	doc = PhotoScan.app.document

	chunk = doc.chunk
	reg = chunk.region

	T = chunk.transform.rotation.inv() * PhotoScan.Vector([0.0,0.1,0.0])
	reg.center += T
	chunk.region = reg


def scootRegionNegY():
	doc = PhotoScan.app.document

	chunk = doc.chunk
	reg = chunk.region

	T = chunk.transform.rotation.inv() * PhotoScan.Vector([0.0,-.1,0.0])
	reg.center += T
	chunk.region = reg


def scootRegionPosZ():
	doc = PhotoScan.app.document

	chunk = doc.chunk
	reg = chunk.region

	T = chunk.transform.rotation.inv() * PhotoScan.Vector([0.0,0.0,0.1])
	reg.center += T
	chunk.region = reg

def scootRegionNegZ():
	doc = PhotoScan.app.document

	chunk = doc.chunk
	reg = chunk.region

	T = chunk.transform.rotation.inv() * PhotoScan.Vector([0.0,0.0,-.1])
	reg.center += T
	chunk.region = reg



PhotoScan.app.addMenuItem("Custom menu/Square Region To Max", squareToMax)	
PhotoScan.app.addMenuItem("Custom menu/Square Region To Min", squareToMin)	

PhotoScan.app.addMenuItem("Custom menu/Scoot Region +X", scootRegionPosX, "]")	
PhotoScan.app.addMenuItem("Custom menu/Scoot Region -X", scootRegionNegX, "[")	
PhotoScan.app.addMenuItem("Custom menu/Scoot Region +Y", scootRegionPosY, "}")	
PhotoScan.app.addMenuItem("Custom menu/Scoot Region -Y", scootRegionNegY, "{")	
PhotoScan.app.addMenuItem("Custom menu/Scoot Region +Z", scootRegionPosZ, ">")	
PhotoScan.app.addMenuItem("Custom menu/Scoot Region -Z", scootRegionNegZ, "<")	




