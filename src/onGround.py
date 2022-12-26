import bge
from bge.types import *

cont: SCA_PythonController = bge.logic.getCurrentController()
own: KX_GameObject  = cont.owner
char: KX_CharacterWrapper = bge.constraints.getCharacter(own)

own["onGround"] = char.onGround
