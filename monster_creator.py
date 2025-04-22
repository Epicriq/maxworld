import sys
from system.living.monster import Monster

name = sys.argv[1]
print("=== LOAD ===")
monster = Monster(name)
print(f"Monster name: \"{monster.name}\"")
print(f"Monster info:\n{monster.info._storage}")
print(f"Monster state:\n{monster.state._storage}")
print("=== SAVE ===")
monster.save()