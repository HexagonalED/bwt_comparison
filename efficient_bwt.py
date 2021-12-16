from suffixTree import *

class efficientBWT(object):
    def __init__(self):
        return

    def encode(self, input):
        #Create S# # : char not in input
        #input을 일반적인 char + integer + $를 제외한 특수문자로 가정

        S = input+'$'
        suffix = SuffixTree(S)
        sufArr=suffix.traverse(0,0)
        ret=""
        origin=sufArr.index(len(input))
        for x in sufArr:
            if x==0:
                ret+='$'
            else:
                ret+=S[x-1]

        #return ret.replace('$',''),origin
        return ret,origin

    def decode(self):

        output = ""
        return output



if __name__=="__main__":
    x=efficientBWT()
    ret=x.encode("appellee")
    print(ret)




