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
# makedbplan.py
# 201901 - Roired
# Script to create a Database structure for project management

import os
import sqlite3

def CreatePlanDatabase(projName, datesList):
    # creates the Project management Database table
    # can be opened with a DB Browser, or managed with Gajeplan
    # TODO: need to define clearly each table later Right now
    # only creates the database for testing purpose
    # TODO: depending on setup, might need a single .py file for this
    dbName = projName + "_plan.db"
    dbConnect = sqlite3.connect(dbName)

    # Create TABLES and add the project start/end dates
    CreateProjectTimeTable(dbConnect)
    CreateKanbanTable(dbConnect)
    CreateTaskTable(dbConnect)
    AddProjectDates(dbConnect, datesList)

    dbConnect.commit()
    dbConnect.close()

def CreateProjectTimeTable(connection):
    # creates the project timer, start-date, estimated-end, and real-end
    c = connection.cursor()
    myCommand = "CREATE TABLE global (id INT, date DATE, name CHAR)"
    # creates a table for the start date, the estimated end, and the real end
    c.execute(myCommand)


def CreateKanbanTable(connection):
    # creates the kanban table with todo-doing-done
    c = connection.cursor()
    myCommand = "CREATE TABLE kanban (id INT, taskName CHAR, taskDescription CHAR, status INT, dateIn DATE, dateOut DATE)"
    c.execute(myCommand)


def CreateTaskTable(connection):
    # creates the table for tracking task times grouped in "code/art/sound"
    c = connection.cursor()
    myCommand = "CREATE TABLE tracker (id INT, taskName CHAR, taskDescription CHAR, taskGroup CHAR, date DATE, time TIME)"
    c.execute(myCommand)

def AddProjectDates(connection, datesList):
    # adds project start date and project end date, project estimated end
    # project end and estimated end are equal at the beginning, they will
    # differ if the project end date becomes different when finished
    c = connection.cursor()
    startDate = datesList[0]
    endDate = datesList[1]
    commandStart = "INSERT INTO global VALUES (0,'{}' ,'Project Start Date')".format(startDate)
    commandEstEnd = "INSERT INTO global VALUES (1,'{}' ,'Project Estimated End Date')".format(endDate)
    commandRealEnd = "INSERT INTO global VALUES (2,'{}' ,'Project Real End Date')".format(endDate)
    c.execute(commandStart)
    c.execute(commandEstEnd)
    c.execute(commandRealEnd)


