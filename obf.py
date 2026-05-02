import os
def spt(s):
    r=s.split(" ")
    rr=[]
    for a in range(len(r)):
        
        if r[a].strip()!= "":
            rr.append(r[a])
    return rr
print("give me the .o object file name ? ")
a=input().strip()
os.system("objdump -x "+a+" > out.txt")
f1=open(a,"rb")
btxt=f1.read()
f1.close()
ta=0
tb=0
f1=open("out.txt","r")
txt=f1.read()
f1.close()
txts=txt.split("\n")
t=False
print("\033c")
t=False
tta=0
for a in txts:
    aa=spt(a)
    if len(aa)>0:
        if t:
            if len(aa)>1:
                
                if aa[1].strip()==".text":
                    if len(aa)>5:
                           
                        ta=int(aa[5],16)
                        tta=ta   
                        tb=int(aa[2],16)
                        tb=tb+ta
                        
        if a.strip()=="SYMBOL TABLE:":
             t=False
        if a.strip()=="Sections:":
             t=True
t=False
for a in txts:
    aa=spt(a)
    if len(aa)>0:
        if t:
            if len(aa)==4:
               
            
                
                print(aa[3].strip()+" = ",end=" ")
                if 0==0:
                    td=int(aa[0],16)
                
                    tc=tta+td
                    counter=0

                    while 1:
                        if counter==0:
                            if btxt[tc]<32 or btxt[tc]>127:
                                break
                        if btxt[tc]==0:
                            break
                        if tc>tb:
                            break
                        print(chr(btxt[tc]),end="")

                        tc=tc+1
                    print("")
        if a.strip()=="SYMBOL TABLE:":
             t=True
