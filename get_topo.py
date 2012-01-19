"""
Retreive topo and dtopo files needed for Crescent City simulations.

"""

import os,sys

try:
    from pyclaw.geotools import topotools
except:
    print "*** Cannot find geotools module, make sure your PYTHONPATH"
    print "*** includes $CLAW/python directory."
    sys.exit()


# Set environment variable CLAW_TOPO_DOWNLOAD=True to avoid prompts
# before downloading.

force = os.environ.get('CLAW_TOPO_DOWNLOAD', False)
force = (force in [True,'True'])

# Or set force here:
force = True

CCdir = os.getcwd()
remote_top_directory = 'http://www.clawpack.org/geoclaw'

# topo files
# ----------

subdir = 'topo/etopo'
remote_directory = os.path.join(remote_top_directory, subdir)
os.chdir(CCdir)
os.system('mkdir -p %s' % subdir)
os.chdir(subdir)

fname = 'etopo1min139E147E34N41N.asc'
topotools.get_topo(fname, remote_directory, force)

fname = 'etopo4min120E72W40S60N.asc'
topotools.get_topo(fname, remote_directory, force)


subdir = 'topo/CC'
remote_directory = os.path.join(remote_top_directory, subdir)
os.chdir(CCdir)
os.system('mkdir -p %s' % subdir)
os.chdir(subdir)

fname = 'ca_north36secm.asc'
topotools.get_topo(fname, remote_directory, force)

fname = 'cc-1sec-c.asc'
topotools.get_topo(fname, remote_directory, force)

fname = 'cc-1_3sec-c.asc'
topotools.get_topo(fname, remote_directory, force)


# dtopo files
# -----------

subdir = 'dtopo/tohoku'
remote_directory = os.path.join(remote_top_directory, subdir)
os.chdir(CCdir)
os.system('mkdir -p %s' % subdir)
os.chdir(subdir)

fname = 'ucsb3-1min.tt1'
topotools.get_topo(fname, remote_directory, force)

