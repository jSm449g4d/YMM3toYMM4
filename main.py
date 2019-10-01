#9th

from ARutil import ffzk,mkdiring
import os
import shutil
import resampy
import re

if __name__=="__main__":
    ymm3=input("plz input YMM3_materials folder>>")
    materials=[]
    for fl in ffzk(ymm3):
        materials.append(fl)
        print(fl)

    print("===========================")

    for fl in materials:
        if "." not in fl:continue
        if fl.split(".")[-1] not in ["bmp","jpg","jpeg","png"]:continue
        fln="".join(fl.split(".")[:-1])

        #YMM3 required only "xx.png" as first image
        #YMM4 required both "xx.png" and "xx.0.png" as first image
        if fln+"a."+fl.split(".")[-1] in materials:
            shutil.copy2(fl,fln+".0."+fl.split(".")[-1]);continue

        if re.compile('[a-z]').match(fln[-1]) is None:continue
        os.rename(fl,fln[:-1]+"."+str(1+ord(fln[-1])-ord('a'))+"."+fl.split(".")[-1])
        print(fln[:-1]+"."+str(1+ord(fln[-1])-ord('a'))+"."+fl.split(".")[-1])

    print("Completed!")
