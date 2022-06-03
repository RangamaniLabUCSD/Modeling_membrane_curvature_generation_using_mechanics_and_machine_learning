
# Initializing a flat membrane.This needs to be 2D since we're going to use the
# axisymmetric Helfrich model

# Inputs:
#   alpha - dimensionless patch area
#   mesh - meshing for the domain, runs from 0 to 1, i.e. 0:0.01:1
#   lam -- short for lambda - membrane tension at the boundary, in units of pN/nm
#   k0 - bending rigidity of bare membrane, in units of pN*nm
#   R0 - nondimensionalization length

# Output:
#   initSol - initialized solution array

import numpy as np

def endoInit(alpha, mesh, lam, k0, R0):
    ds=0.0001        # small deviation from x=0 (necessary to avoid division by 0)
    t = mesh         # area mesh points; assume we've already multiplied by alpha
    #lam_non_dim = (lam*R0**2)/k0   # dimensionless membrane tension; lam is the dimensional membrane tension -(W + gamma)

    initSol = np.array([ds + np.sqrt(2*t),       # x: dimensionless radial distance
           np.zeros(len(t)),                     # y: dimensionless height
           np.zeros(len(t)),                     # psi: angle between radial basis and tangent to the membrane surface in the radial direction
           np.zeros(len(t)),                     # h: dimensionless mean curvature
           np.zeros(len(t)),                     # l: dimensionless shape equation variable
           lam*np.ones(len(t))])         # lamda tilda: dimensionless membrane tension

    return initSol
