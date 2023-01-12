import os
import platform
from cmdList import *

def CheckPlatform():
    print("---------------------- Check Platform -----------------")
    print("Platform ============= " + platform.platform())
    print("Version  ============= " + platform.version())
   
def PlatformInstall():
    print("--------------------- Install Depending on Platform ---------------------")
    if substring[0] in platform.version():
        UbuntuInstall()
    elif substring[1] in platform.version():
        FedoraInstall()
    elif substring[2] in platform.version():
        OpenSUSEInstall()
    else:
        print("------------- Can't detect OS --------------")
    
def UbuntuInstall():
    print("--------------- Ubuntu Install -------------------")
    for c in cmdUbuntu:
        os.system(c)
           
def FedoraInstall():
    print("--------------- Fedora Install -------------------")
    for c in cmdFedora:
        os.system(c)
   
def OpenSUSEInstall():
    print("--------------- OpenSUSE Install -------------------")
    for c in cmdOpenSUSE:
        os.system(c)








