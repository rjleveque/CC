

For initial run up to California coast
Files:
    Makefile1  
    setrun1.py
    setplot1.py
Usage:
    make .plots -f Makefile1


For restart run into Crescent City
Files:
    Makefile2  
    setrun2.py
    setplot2.py
Usage:
    mkdir -p _output2   # first create this directory if it doesn't already exist
    cp _output1/fort.chk0081 _output2/restart.data    # if not already there
    cp _output1/fort.amr _output2    # if not already there
    make .plots -f Makefile2
    
NOTE:  Many things cannot be changed between runs, so if you want to change the max. number of levels or refinement ratios, for example, they need to be changed in both Makefiles and 


Things to modify for Tohoku:



Things to modify to change to a different source location:

In the setrun files:
    domain parameters 
    topo and dtopo files
    regions for refinement if it's important to follow the tsunami across the ocean