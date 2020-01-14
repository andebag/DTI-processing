import os.path
from pathlib import Path
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
            print("file in folder do not alter")
        else:
            print("Must run AMICO")
            os.chdir("{}".format(line.strip()))
            os.chdir("ande_merged\merged") #organizing bval/bvec into norm bval file           
            execfile(os.path.abspath("C:\\Users\\bagdasarian\\Documents\\AMICO-master\\execute_files\\bvec_organize.py"))
            os.chdir("{}".format(line.strip()))            
            execfile(os.path.abspath("C:\\Users\\bagdasarian\\Documents\\AMICO-master\\execute_files\\AMICO_run.py"))
    #        C:\Users\bagdasarian\Desktop\Jens_DTI\AMICO_run.py")
        line = fp.readline()
        cnt += 1
    
    
