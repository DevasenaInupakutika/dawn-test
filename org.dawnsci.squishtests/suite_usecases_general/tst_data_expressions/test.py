source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))

import os

# This test makes sure we can start and stop DAWN
def main():
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()
    
    # On a test you may add test code here 
    #Open data browsing perspective
    openPerspective("Data Browsing (default)")

    # Exit (or disconnect) DAWN
    openExternalFile("315029.dat")
    mouseDrag(waitForObject(":_Sash"), 2, 313, 0, -16, Modifier.None, Button.Button1)
    mouseClick(waitForObject(":Data_Table"), 70, 293, 0, Button.Button3)
    activateItem(waitForObjectItem(":_Menu_3", "Add expression"))
    type(waitForObject(":Data_Text"), "dat:mean(Pilatus,0)")
    type(waitForObject(":Data_Text"), "<Return>")
    
    system = getPlottingSystem("315029.dat")
    test.verify(system.getTraces().size()==1)
    test.verify(system.getTraces().iterator().next().getData().getRank()==2)
    
    closeOrDetachFromDAWN()
