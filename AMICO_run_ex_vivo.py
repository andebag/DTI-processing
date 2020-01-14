#NODDI Pocessing

#starting up AMICO processing program
import amico
amico.core.setup()

#setting data location
ae = amico.Evaluation("ande_merged", "merged")

#bringing in bval/bvec files
amico.util.fsl2scheme("ande_merged/merged/bvals.bval", "ande_merged/merged/norm_bvec.bvec")

#activating rician debiasing
#ae.set_config('doDebiasSignal',True)

#setting SNR level
#ae.set_config('DWI-SNR',75.)
#for ex vivo
ae.set_config('DWI-SNR',750.)
#loading in raw data and masking
ae.load_data(dwi_filename = "rawDTI.nii", scheme_filename = "bvals.scheme", mask_filename = "DTImask.nii", b0_thr = 0)

#setting up model and running
ae.set_model("NODDI")
ae.model.isExVivo = True   #ex vivo settings
ae.model.dPar = 0.9E-3 #sets diffusivity of the model, activate for ex vivo
ae.model.dIso = 2.0E-3 #sets isotropic diffusivity
ae.generate_kernels()
ae.load_kernels()
ae.fit()

#saving results
ae.save_results()