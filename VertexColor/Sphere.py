import maya.cmds as cmds
import maya.OpenMaya
import maya.OpenMayaMPx

stockPath = #please write your data directory
f = open(stockPath)

IM = 64
JM = 32
Rp = 1
N = 51

cmds.polySphere(sx=IM, sy=JM+1, r=Rp)

cmds.select('pSphere1.vtx[:]')
selectedVertex_list = cmds.ls(sl=True)
selectedVertex_num =cmds.filterExpand(selectedVertex_list , sm=31)
v_cnt = cmds.polyEvaluate(v=1)
data = f.read()
data3 = data.split()
data2=list(map(float,data3))
for iii in range(N):
    b = 23*(data2[iii*(IM+1)*(JM+2)]-1) + 0.4
    cmds.polyColorPerVertex(selectedVertex_num[2048], rgb=(0.0 ,0.0 ,b) ,a=1 ,cdo=True)
    for i in range(JM):
        for ii in range(IM):
            b = 23*(data2[iii*(IM+1)*(JM+2) + IM+1+ii+(IM+1)*i]-1) + 0.4
            cmds.polyColorPerVertex(selectedVertex_num[ii+IM*i], rgb=(0.0 ,0.0 ,b) ,a=1 ,cdo=True)
    b = 23*(data2[iii*(IM+1)*(JM+2)+2210]-1) + 0.4
    cmds.polyColorPerVertex(selectedVertex_num[2049], rgb=(0.0 ,0.0 ,b) ,a=1 ,cdo=True)
    cmds.select('pSphere1.vtxFace[:][:]')
    cmds.setKeyframe(time=4*iii+1)
