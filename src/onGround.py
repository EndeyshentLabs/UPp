import bge

cont = bge.logic.getCurrentController()
own  = cont.owner
char = bge.constraints.getCharacter(own)

own["onGround"] = char.onGround