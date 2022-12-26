import bge

cont = bge.logic.getCurrentController()
own  = cont.owner

def zoom_in(cont):
    own = cont.owner
    if own.lens < 36.0:
        own.lens += 1
    
def zoom_out(cont):
    own = cont.owner
    if own.lens > 18.0:
        own.lens -= 1
        
def reset(cont):
    own = cont.owner
    own.lens = 36.0