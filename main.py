from bwt import *
from efficient_bwt import *

if __name__=="__main__":
    b=BWT()
    eb=efficientBWT()
    bret,index=b.encode("appellee")
    ebret=eb.encode("appellee")
    print(bret)
    print(index)
    print(ebret)
