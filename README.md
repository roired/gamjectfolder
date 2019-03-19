# Gamjectfolder


> WARNING: cloning this repo and opening it with Gnome Builder causes the project not to build due to wrong file permissions set by GitHub when uploading files. Once the fix is pulled I will remove this warning
---

This is a simple Python app that creates:
 * A folder strutcture suitable for indie game developers,
 * (optional) A default empty README.txt file for a Game Project,
 * (optional) A default database file to manage the project process (needs external app)
 * (optional) An empty "project.godot" file to start a new Godotengine project

Its goal is to automate and standardize the process of starting a new Game Project by providing default folders, subfolders, a README.txt file, a project.godot file with the project name, and a Project Tracking databse as well. All these are based on my personal needs when I face a new game project, based on my extremely short experience with game development.
This app is PART-1. PART-2 will be the Project Tracking app.

The MAIN folder is named with the creation date in ISO format followed by the name the user picks, then the structure follows:

 * YYYYMMDD-Name
    * Name-AuxFiles
      * AuxFONTS
      * AuxIMAGES
      * AuxMODELS
      * AuxPACKAGES
      * AuxSOUNDS
      * AuxTRANSLATIONS
    * Name-BackUPs
    * Name-Builds
      * Alpha
      * Beta
      * ReleaseCandidate
      * README.txt
    * Name-Marketing
      * MktLOGOS
      * MktPRESS_KIT
      * MktSCREENSHOTS
      * MktVIDEOS
    * Name-Planning
      * Name_plan.db
    * Name-PROJECT
      * Proj-FINAL
      * Proj-WIP
        * project.godot
        
It is also distributed as a flatpak file. Using the flatpak file to be installed through the Software Center. It needs to enter the password twice as this flatpak is not signed with any repo (at least just yet).

While being a flatpak sandboxed app, in order to create the folder structure it has access to the filesystem (--filesystem=host).


TODO: 
   - Add Date verification
   - Add "Help" menu to explain how to use
   - Modify titlebar to comply with Gnome standards?
   - ¿Connect with Gnome Calendar and ADD start/end dates? need to study this
