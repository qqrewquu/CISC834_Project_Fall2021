#!/usr/bin/python2

# Tell you which object, and what kind, is obtained by an import. This can also
# Will return errorlevel of 2 if object is not found.

from __future__ import print_function

import sys
import imp


_DESC = {
    imp.PY_SOURCE: "python source file",
    imp.PY_COMPILED: "compiled code object file",
    imp.C_EXTENSION: "dynamically loadable shared library",
    imp.PKG_DIRECTORY: "base package",
    imp.C_BUILTIN: "built-in module",
    imp.PY_FROZEN: "frozen module",
}

def pywhich(argv):
    """pywhich <modname>
    Tell you which actual file is being used by an import. The module name
    should be a full module path (e.g. xml.dom.minidom)

    Example:

        pywhich xml.dom.minidom
    """
    if len(argv) < 2:
        print (pywhich.__doc__)
        return 1
    for modname in argv[1:]:
        try:
            fo, path, (suffix, mode, mtype) = imp.find_module(modname) # finds builtins
        except ImportError: # the simpler find_module throws this on namespace packages and subpackages.
            try:
                __import__(modname)
                pkg = sys.modules[modname]
                if hasattr(pkg, "__path__"): # complex package
                    print("{} => {} (package).".format(modname, pkg.__path__[0]))
                else:
                    print("{} => {}".format(modname, pkg.__file__))
            except:
                ex, val, tb = sys.exc_info()
                print("{} => {}: {}!".format(modname, ex.__name__, val))
                return 2
        else:
            if fo is None:
                print("{} => {} ({}).".format(modname, path, _DESC[mtype]))
            else:
                fo.close()
                __import__(modname)
                pkg = sys.modules[modname]
                if hasattr(pkg, "__path__"):
                    print("{} => {} (package).".format(modname, pkg.__file__))
                else:
                    print("{} => {} ({}).".format(modname, pkg.__file__, _DESC[mtype]))

sys.exit(pywhich(sys.argv))
