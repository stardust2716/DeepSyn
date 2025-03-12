from rdkit import RDConfig
import unittest
import random
from rdkit import Chem
from rdkit.Chem import Draw, AllChem
from rdkit.Chem.Draw import rdMolDraw2D
from rdkit import Geometry
#%matplotlib inline
from numpy.polynomial.polynomial import polyfit
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib
# from IPython.display import SVG, display
# import seaborn as sns; sns.set(color_codes=True)

reaction='CC#CCN.c1ccc2c(c1)sc1ccccc12>>C(=CC(=C1CC2)S(=N2)(C)=NC(=O)C#CC)C=C1'#'[CH3:1][C:2](=[O:3])[OH:4].[CH3:5][NH2:6]>CC(O)C.[Pt]>[CH3:1][C:2](=[O:3])[NH:6][CH3:5].[OH2:4]'
rxn = AllChem.ReactionFromSmarts(reaction,useSmiles=True)
#d = Draw.MolDraw2DSVG(900, 300)
d = Draw.MolDraw2DCairo(600, 250)
d.DrawReaction(rxn)
d.FinishDrawing()


png_data = d.GetDrawingText()

# save png to file
with open('mol2.png', 'wb') as png_file:
    png_file.write(png_data)
#d.show()


# rxn = AllChem.ReactionFromSmarts('[CH3:1][C:2](=[O:3])[OH:4].[CH3:5][NH2:6]>CC(O)C.[Pt]>[CH3:1][C:2](=[O:3])[NH:6][CH3:5].[OH2:4]',useSmiles=True)
# colors=[(0.3,0.7,0.9),(0.9,0.7,0.9),(0.6,0.9,0.3),(0.9,0.9,0.1)]
# d = Draw.MolDraw2DSVG(900, 300)
# d.DrawReaction(rxn,highlightByReactant=True,highlightColorsReactants=colors)
# d.FinishDrawing()

# txt = d.GetDrawingText()
# self.assertTrue(txt.find("<svg") != -1)
# self.assertTrue(txt.find("</svg>") != -1)

# svg = d.GetDrawingText()
# svg2 = svg.replace('svg:','')
# with open('mol_image.svg', 'wb') as png_file:
#     png_file.write(svg2)
# svg3 = SVG(svg2)
# display(svg3)