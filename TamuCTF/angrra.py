import angr
import claripy
import sys
import monkeyhex
proj=angr.Project('/home/madhav/Downloads/angrmanagement')
state=proj.factory.entry_state()
sim=proj.factory.simgr(state)
sim.explore(find=lambda k: b'Correct' in k.posix.dumps(1))
k=sim.found[0]
ans=k.posix.dumps(0)
print(ans)
