"""
reloadall.py: transitively reload nested modules
"""
import types
from imp import reload

def transitive_reload(module, visited):
    if not module in visited:
        print('reloading '+module.__name__)
        reload(module)
        visited[module] = None
        for attrobj in module.__dict__.values():
            if type(attrobj) == types.ModuleType:
                transitive_reload(attrobj, visited)

def reload_all(*args):
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)

if __name__ == '__main__':
    import reloadall
    reload_all(reloadall)
