#setup for reorganising the bvec file
import numpy as np
from dipy.io import read_bvals_bvecs
from dipy.core.geometry  import normalized_vector

#Normalizing bvec file:
bvals, bvecs = read_bvals_bvecs("bvals.bval", "bvecs.bvec")
nvec = normalized_vector(bvecs)

#Changing the b0 bvecs to [0 0 1]:
nvec[np.isnan(nvec)] = 0
nvec[0:4,2] = 1

#Transposing and saving the new normalized bvec file
nvec = np.transpose(bvecs)
np.savetxt("norm_bvec.bvec", nvec, fmt='%.18e', delimiter=' ', newline='\n')
