import bge
from bge.types import *

def zoom_in(cont: SCA_PythonController) -> None:
    own: KX_Camera = cont.owner
    if own.lens < 36.0:
        own.lens += 1
    
def zoom_out(cont: SCA_PythonController) -> None:
    own: KX_Camera = cont.owner
    if own.lens > 18.0:
        own.lens -= 1
        
def reset(cont: SCA_PythonController) -> None:
    own: KX_Camera = cont.owner
    own.lens = 36.0
