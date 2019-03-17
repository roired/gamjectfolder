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
# application.py
# 201902 - Roired
# Script to hold the app logic
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from typing import List

from . import makefolders # import the core tasks

# Data order: Project Name > Suport Email > Readme > Parent folder > Mgmt File > Godot File > End-Year > End-Month > End-Day
projectData = ["", "", "", "", "", "", "", "", ""]

# sentences for the message dialog:
# - Warning - gtk-dialog-error
# - Project name already exists - gtk-dialog-error
warningLabelTexts = [
    "You should provide a Project NAME in order to create the folder skeleton.\n\r\n\rPlease add a name and try again.",
    "The project name you have chosen already exists.\n\r\n\rCan't create the folder skeleton.\n\r\n\rPlease, pick a different name and try again.",
    "You should provide a Parent Folder in order to create the folder skeleton.\n\r\n\rPlease provide a Parent Folder and try again."
]

finishedLabelTexts = [
    "The project Skeleton has been completed.\n\r\n\rYou can check the result by clicking the \"Open Folder\" button.\n\r\n\r",
    "\n\r\n\rIf you want to open the GODOT project in Godotengine now, you can click the \"Open Project\" button."
]

def clearFields():
    # print("Should reset all fields")
    app.object("dataPName").set_text("")
    app.object("dataSEmail").set_text("")
    # resets the parent folder to NONE
    app.object("dataPFolder").unselect_all()
    app.object("dataRFile").set_active(False)
    app.object("dataPMFile").set_active(False)
    app.object("dataGodotFile").set_active(False)
    app.object("dataEndYear").set_text("")
    app.object("dataEndMonth").set_text("")
    app.object("dataEndDay").set_text("")

class Handler:
    # class to manage all Glade file signals

    # AppWindow signals
    def on_AppWindow_destroy(self, *args):
        Gtk.main_quit()

    def on_create_project_clicked(self, widget):
        # creates the folder structure if needed data is provided
        global projectData
        global warningLabelTexts
        global finishedLabelTexts
        # print("create project with params : " + projectData[0]+ projectData[1] + projectData[2]+projectData[3])
        if projectData[0] == "":
            app.object("warningLabel").set_text(warningLabelTexts[0])
            app.object("WarningDialog").run()

            # print("should provide project name")
        elif projectData[3] == "":
            app.object("warningLabel").set_text(warningLabelTexts[2])
            app.object("WarningDialog").run()

            # print("should provide parent folder")
        else:
            if makefolders.CreateFolders(projectData):
                app.object("GeneralDialog").run()
            else:
                app.object("warningLabel").set_text(warningLabelTexts[1])
                app.object("WarningDialog").run()

        # makereadme.PopulateFile("README.txt", "emailio")

    def on_new_project_clicked(self, widget):
        # clears the fields set to placeholders
        clearFields()

    def on_quit_activate(self, *args):
        # just quits the app
        Gtk.main_quit()

    def on_about_activate(self, widget):
        # shows the About app dialog
        app.object("AboutDialog").run()

    def on_new_activate(self, widget):
        # clears the fields set to placeholders
        clearFields()

    def on_dataRFile_toggled(self, widget):
        # checks wether to make a README.txt file from input
        global projectData
        if widget.get_active():
            projectData[2] = "True"
            # print("make README -" + projectData[3] + " - value : " + str(widget.get_active()))
        else:
            projectData[2] = "False"
            # print("NO readme -" + projectData[3] + " - value : " + str(widget.get_active()))

    def on_dataPMFile_toggled(self, widget):
        # checks wether to create a Project Management database file
        global projectData
        if widget.get_active():
            projectData[4] = "True"
        else:
            projectData[4] = "False"

    def on_dataGodotFile_toggled(self, widget):
        # checks wether to create a Godot project file to be opened later
        global projectData
        if widget.get_active():
            projectData[5] = "True"
        else:
            projectData[5] = "False"


    def on_dataPFolder_file_set(self, widget):
        # gets parent folder where to create the skeleton
        global projectData
        separent = widget.get_filename()
        projectData[3] = separent
        # print("i have a parent folder :::: " + separent)

    def on_dataSEmail_changed(self, widget):
        # gets the support email from input
        global projectData
        semail = widget.get_text()
        projectData[1] = semail
        # print("i have EMAIL > " + semail)

    def on_dataPName_changed(self, widget):
        # gets the project name from input
        global projectData
        sename = widget.get_text()
        projectData[0] = sename
        # print("I have a NAMEEE -> -> " + sename)

    def on_dataEndYear_changed(self, widget):
        # gets the project estimated end year
        global projectData
        sendyear = widget.get_text()
        projectData[6] = sendyear

    def on_dataEndMonth_changed(self, widget):
        # gets the project estimated end month
        global projectData
        sendmonth = widget.get_text()
        projectData[7] = sendmonth

    def on_dataEndDay_changed(self, widget):
        # gets the project estimated end day
        global projectData
        sendday = widget.get_text()
        projectData[8] = sendday


    # AboutDialog signals
    def on_aboutClose_clicked(self, widget):
        # hides the About Dialog when closed
        app.object("AboutDialog").hide_on_delete()

    # DoneDialog signals
    def on_openFolder_clicked(self, widget):
        # opens the destination folder where the skeleton has been created
        global projectData
        # print("should open new project folder")
        os.system("xdg-open "+ projectData[3])
        app.object("GeneralDialog").hide_on_delete()

    def on_dialogClose_clicked(self, widget):
        # hides the completed dialog when closed
        app.object("GeneralDialog").hide_on_delete()

    # WarningDialog signals (common to done dialog)
    def on_warningClose_clicked(self, widget):
        # hides the warning dialog when closed
        app.object("WarningDialog").hide_on_delete()



class MyApplication:
    # application class
    def __init__(self):
        # initialize the app class. Gets the builder and Glade file to parse it along with the signals
        builder = Gtk.Builder()
        # builder.add_from_file("gjfGUI.glade")
        # commented as Gnome Builder does not like this
        # need to do as in the following lines in order to get the
        # right path to the Glade file
        filename = "/org/gnome/Gamjectfolder/gjfGUI.glade"


        # finally looks like this one is the right one
        builder.add_from_resource(filename)
        builder.connect_signals(Handler())

        # self.about = self.builder.get_object("AboutDialog")

        dataDate = makefolders.GetDate()[0]

        builder.get_object("dataDate").set_text(dataDate)

        self.object = builder.get_object
        self.object("AppWindow").show_all()
        # window = self.builder.get_object("AppWindow")
        # window.show_all()

    def main(self):
        Gtk.main()

# def main():
    # main, as to be called by gamjectfolder.in
#    app = MyApplication()
#    return app.main()

app = MyApplication()
app.main()    
