import os.path
from pathlib import Path
import shutil
filepath = 'subjects.txt'
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
#        print("{}".format(licd ne.strip()))
        os.chdir("{}".format(line.strip()))
        dirpath = os.getcwd()
        print("current directory is : " + dirpath)
        foldername = os.path.basename(dirpath)
        print("Directory name is : " + foldername)
        my_file = Path("ande_merged\merged\AMICO\NODDI\FIT_ICVF.nii.gz")
        if my_file.is_file():
            print("NODDI Processing is Done")
        else:
            print("Must run AMICO")
            os.chdir("{}".format(line.strip()))
            os.chdir("ande_merged\merged") #organizing bval/bvec into norm bval file           
            execfile(os.path.abspath("C:\\Users\\bagdasarian\\Documents\\Python Scripts\\bvec_organize.py"))
            os.chdir("{}".format(line.strip())) 
            
            ex_vivo = Path("ande_merged\merged\ex_vivo.txt") #setup if ex vivo sample
            if ex_vivo.is_file():
                print("ex vivo Processing")
                execfile(os.path.abspath("C:\\Users\\bagdasarian\\Documents\\Python Scripts\\AMICO_run_ex_vivo.py"))
            else:
                print("in vivo Processing")
                execfile(os.path.abspath("C:\\Users\\bagdasarian\\Documents\\Python Scripts\\AMICO_run.py"))
             os.chdir("{}".format(line.strip()))
             os.chdir("ande_merged")
             shutil.rmtree('kernels')    #the kernel datasets are huge, recommend deleting after processing

#DKI Processing if able
        my_DKI_file = Path("ande_merged\merged\DKI")
        if my_DKI_file.is_file():   
           print("DKI Processing is Done")
        else:
            print("Must run DiPy")
            os.chdir("{}".format(line.strip()))
            os.chdir("ande_merged\merged") 
            os.makedirs("DKI")#Creating DKI directory 
            os.chdir("{}".format(line.strip()))         
            execfile(os.path.abspath("C:\\Users\\bagdasarian\\Documents\\Python Scripts\\myDKI.py"))
            
            
        line = fp.readline()
        cnt += 1
    
    
