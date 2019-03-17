#!/usr/bin/env python3
#
# Copyright 2019 ROIRED
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# makefolders.py
# 201901 - Roired
# Script to create a folder structure for the project

import os
import datetime
import pathlib
import sys
import subprocess

from subprocess import Popen, PIPE
from pathlib import Path
from datetime import date

from . import makereadme
from . import makedbplan

# import makereadme
# import makedbplan



# Main project Folders:
mainFolders = ["-AuxFiles", "-Marketing", "-Builds", "-PROJECT", "-BackUPs", "-Planning"]
subFolders = [
    ["AuxFONTS", "AuxIMAGES", "AuxMODELS",
        "AuxPACKAGES", "AuxSOUNDS", "AuxTRANSLATIONS"],
    ["MktVIDEOS", "MktLOGOS", "MktSCREENSHOTS", "MktPRESS_KIT"],
    ["Alpha", "Beta", "ReleaseCandidate"],
    [],
    [],
    ["Trns-DEFAULT"]
]

def GetDate():
    # gets the today date in the preferred format
    dateNow = datetime.datetime.now()
    dateSet = dateNow.strftime("%Y.%m.%d")
    dateName = dateNow.strftime("%Y%m%d")
    datesFormated = [dateSet, dateName]
    return datesFormated


def CreateFolders(pData):
    # pData = (pName, sEmail, rEadme, pFolder, mAnagment, gOdot):
    # method to create the whole folder skeleton
    # Data order: Project Name > Suport Email > Readme > Parent folder > Mgmt File > Godot File > End-Year > End-Month > End-Day
    cnt = 0
    tmpFolder = pData[3]
    parentFolder = os.chdir(tmpFolder)
    folderDate = GetDate()[1]
    folderName = (folderDate + "-" + pData[0])

    #TODO: check if the folder name exists before creating it add warning
    path = pathlib.Path(folderName)
    # print(" already have it?? " + str(path.exists()))
    if path.exists():
        # print(" the folder is already there ... ")
        return False
    else:
        os.mkdir(folderName)
        os.chdir(folderName)
        baseFolder = os.getcwd()
        for folder in mainFolders:
            os.mkdir(pData[0] + folder)
            os.chdir(pData[0] + folder)

            if cnt == 2 and pData[2] == "True":
                # Create the readme file if selected
                makereadme.PopulateFile("README.txt", pData[1])


            if cnt == 3:
                # Create the work folders
                CreateWorkFolders(pData[0], pData[5])

            if cnt == 5 and pData[4] == "True":
                # Create the project planning database file
                datesList = CreateDatesList(pData)
                makedbplan.CreatePlanDatabase(pData[0], datesList)

            CreateSubFolders(subFolders[cnt])
            cnt += 1
            os.chdir(baseFolder)

        return True

def CreateWorkFolders(projName, projFile):
    # creates the WIP folder and the final folder, and
    # creates a GODOT project file in the WIP folder if passed
    wipFolder = projName + "WIP"
    finalFolder = projName + "FINAL"
    os.mkdir(wipFolder)
    os.mkdir(finalFolder)
    if projFile == "True":
        # projectFile = "project.godot"
        os.chdir(wipFolder)
        CreateGodotPFile(wipFolder)
        # theFile = open(projectFile, "w+")
        # theFile.close()
        os.chdir("..")


def CreateSubFolders(folderList):
    # method to create subfolders when needed
    if len(folderList) != 0:
        for folder in folderList:
            os.mkdir(folder)


def CreateGodotPFile(projName):
    # creates a default, empty godot project file with the project name in it
    fileName = "project.godot"
    theFile = open(fileName, "w+")
    theFile.write("[application]\r\n")
    theFile.write("\r\nconfig/name=\"{}\"".format(projName))
    theFile.close()

def CreateDatesList(projData):
    # returns the list of data already formated, to pass to the database
    sYear = date.today().isoformat()
    # print("today is " + sYear)
    eYear = date(int(projData[6]),int(projData[7]), int(projData[8])).isoformat()
    # print("end date is " + eYear)
    datesList = (sYear, eYear)
    return datesList

# comment next after testing until EOF
'''
def main():
    projectData = ["nametest", "email@mail.emi", "True", "", "True", "True"]
    thisFolder = os.getcwd()
    projectData[3] = thisFolder
    CreateFolders(projectData)


main()
'''

