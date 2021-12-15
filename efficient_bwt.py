from suffixTree import *

class efficientBWT(object):
    def __init__(self):
        return

    def encode(self, input):
        #Create S# # : char not in input
        #input을 일반적인 char + integer + $를 제외한 특수문자로 가정

        S = input+'$'
        suffix = SuffixTree(S)


    def decode(self):

        output = ""
        return output
