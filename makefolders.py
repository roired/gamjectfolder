#!/usr/bin/env python
#
# Copyright (c) 2019 ROiRED
# GAMJECTFOLDER is free software distributed under the GNU LGPLv3 license
# and is distributed without any WARRANTY
#
# You should have received a copy of the GNU General Public License along
# with your copy of GAMJECTFOLDER.
#
# MakeFolders.py
# 201901 - Roired
# Script to create a folder structure for a Game Project

import os
import datetime
import makereadme
import pathlib


# projectName = "name"

# Main project Folders:
mainFolders = ["-AuxFiles", "-Marketing", "-Builds", "-PROJECT", "-BackUPs"]
subFolders = [
    ["AuxFONTS", "AuxIMAGES", "AuxMODELS",
        "AuxPACKAGES", "AuxSOUNDS", "AuxTRANSLATIONS"],
    ["MktVIDEOS", "MktLOGOS", "MktSCREENSHOTS", "MktPRESS_KIT"],
    ["Alpha", "Beta", "ReleaseCandidate"],
    ["Proj-WIP", "Proj-FINAL"],
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
    # pData = (pName, sEmail, rEadme, pFolder):
    # method to create the whole folder skeleton
    # Data order: Project Name > Suport Email > Readme > Parent folder
    cnt = 0
    tmpFolder = pData[3]
    parentFolder = os.chdir(tmpFolder)
    folderDate = GetDate()[1]
    folderName = (folderDate + "-" + pData[0])

    #TODO: check if the folder name exists before creating it
    path = pathlib.Path(folderName)
    print(" already have it?? " + str(path.exists()))
    if path.exists():
        print(" the folder is already there ... ")
        return False
    else:
        os.mkdir(folderName)
        os.chdir(folderName)
        baseFolder = os.getcwd()
        for folder in mainFolders:
            os.mkdir(pData[0] + folder)
            os.chdir(pData[0] + folder)
            if cnt == 2 and pData[2] == "True":
                makereadme.PopulateFile("README.txt", pData[1])
            CreateSubFolders(subFolders[cnt])
            cnt += 1
            os.chdir(baseFolder)
        return True


def CreateSubFolders(folderList):
    # method to create subfolders when needed
    if len(folderList) != 0:
        for folder in folderList:
            os.mkdir(folder)


#def main():
#    CreateFolders(projectName)


# main()
