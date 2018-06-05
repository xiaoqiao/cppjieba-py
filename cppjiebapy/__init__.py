from cppjieba_py import cut_for_search_internal,cut_internal as cut_i
from cppjieba_py import Tokenizer
from cppjieba_py import lcut,lcut_for_search
def cut(*args,**kvargs):
    it = cut_i(*args,**kvargs)
    for word in it:
        yield word.word

def cut_for_search(*args,**kvargs):
    it = cut_for_search_internal(*args,**kvargs)
    for word in it:
        yield word.word

def c_cut(ins,*args,**kvargs):
    it = ins.cut_internal(*args,**kvargs)
    for word in it:
        yield word.word

def c_cut_for_search(ins,*args,**kvargs):
    it = ins.cut_for_search_internal(*args,**kvargs)
    for word in it:
        yield word.word

setattr(Tokenizer,"cut",c_cut)
setattr(Tokenizer,"cut_for_search",c_cut_for_search)
