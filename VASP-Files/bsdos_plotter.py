# Call with your python executable to generate combined DOS/bandstructure figure 
#   from your two vasprun files
# Relies upon pymatgen version 4.5.6 or greater, matplotlib, and glob

from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.electronic_structure.plotter import BSDOSPlotter
import glob
import matplotlib as plt

bs_name = sorted(glob.glob('*.xml'))[0] # Takes the xml files in alphabetical order  
dos_name = sorted(glob.glob('*.xml'))[1] # e.g. bs.xml, dos.xml


bs_vrun = Vasprun(bs_name, parse_projected_eigen=True)
dos_vrun = Vasprun(dos_name)

bs = bs_vrun.get_band_structure(kpoints_filename = 'KPOINTS.bands')
dos = dos_vrun.complete_dos

bsdosplot = BSDOSPlotter()
figuro = bsdosplot.get_plot(bs, dos)
figuro.savefig('bsdos.png')