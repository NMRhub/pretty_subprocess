
import importlib.metadata
import logging
import os
import subprocess
import shlex
pretty_subprocess_logger = logging.getLogger(__name__)

__version__ =  importlib.metadata.version('pretty_subprocess')


def _to_str(a)->str:
    if isinstance(a,(str,bytes,os.PathLike)):
        return os.fsdecode(a)
    return str(a)

def run(*args,**kwargs)->subprocess.CompletedProcess:
    cmd = "Unknown"
    try:
        c = args[0] if args else kwargs.get('args')
        try:
            if isinstance(c,(str,bytes,os.PathLike)):
                cmd = _to_str(c)
            elif c is not None:
                cmd = shlex.join(_to_str(a) for a in c)
        except TypeError:
            pass
        cp = subprocess.run(*args,**kwargs)
        setattr(cp,'command',cmd)
        return cp
    except Exception as e:
        e.add_note(f"Command: {cmd}")
        raise

