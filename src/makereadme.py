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
# makereadme.py
# 201901 - Roired
# Script to create a README.txt file skeleton for game dev

import os

filename = 'README.txt'
# TODO: pass the email from the main app
email = 'this@test.com'

# create spacer to separate sections


def FourBlankLines(fName):
    # just creates 4 blank lines and a separator line
    fName.write(
        "---------------------------------------------------------------------------\r\n")
    for cnt in range(5):
        fName.write("\r\n")
        cnt+1


def MakeIndex(fName):
    # creates an index section
    fName.write(
        "---------------------------------------------------------------------------\r\n")
    fName.write("       INDEX\r\n")
    fName.write("   1.  Special Notes for Linux Users\r\n")
    fName.write("   2.  Description\r\n")
    fName.write("   3.  Release Notes\r\n")
    fName.write("   4.  Improvements\r\n")
    fName.write("   5.  Fixes\r\n")
    fName.write("   6.  Known Bugs\r\n")
    fName.write(
        "---------------------------------------------------------------------------\r\n")


def PopulateFile(fName, eMail):
    # populate the README.txt contents according to the previous index, leaving
    # enough space to fill in later
    theFile = open(fName, "w+")
    theFile.write("GAME     :\r\n")
    theFile.write("Version  :\r\n")
    theFile.write("Date     :\r\n")
    theFile.write("Author   :\r\n")
    theFile.write("Resolution:\r\n")
    theFile.write("\r\n")
    MakeIndex(theFile)
    theFile.write(
        "If you encounter any issue, please report at " + eMail + "\r\n")
    FourBlankLines(theFile)
    theFile.write("1>> SPECIAL NOTES FOR LINUX USERS\r\n")
    FourBlankLines(theFile)
    theFile.write("2>> DESCRIPTION\r\n")
    FourBlankLines(theFile)
    theFile.write("3>> RELEASE NOTES\r\n")
    FourBlankLines(theFile)
    theFile.write("4>> IMPROVEMENTS\r\n")
    FourBlankLines(theFile)
    theFile.write("5>> FIXES\r\n")
    FourBlankLines(theFile)
    theFile.write("6>> KNOWN ISSUES\r\n")
    FourBlankLines(theFile)
    theFile.write("7>> TO DO\r\n")
    FourBlankLines(theFile)
    theFile.write("8>> RELEASE RECORD\r\n")
    FourBlankLines(theFile)
    theFile.close()


#def main():
#    PopulateFile(filename, email)


# main()
