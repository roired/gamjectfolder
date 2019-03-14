# Gamjectfolder


> WARNING: cloning this repo and opening it with Gnome Builder causes the project not to build due to wrong file permissions set by GitHub when uploading files. Once the fix is pulled I will remove this warning
---

This is a simple Python app that creates a folder strutcture as well as a default empty README.txt file for a Game Project.

Its goal is to standarize the process of starting a new Game Project by providing default folders and subfolders as well.

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
    * Name-PROJECT
      * Proj-FINAL
      * Proj-WIP
        
It is also distributed as a flatpak file. Using the flatpak file to be installed through the Software Center. It needs to enter the password twice as this flatpak is not signed with any repo (at least just yet).

While being a flatpak sandboxed app, in order to create the folder structure it has access to the filesystem (--filesystem=host).


TODO: 
   - Add a "estimated end date"
   - Add a checkbox to "create project tracker" (needs Gamplan project finished)
   - Improve Icon to match "papirus" icon theme
   - Remove all "print" debugs
   - ¿Connect with Gnome Calendar and ADD start/end dates? need to study this
