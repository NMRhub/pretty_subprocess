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
    try:
        return subprocess.run(*args,**kwargs)
    except Exception as e:
        c = args[0] if args else kwargs.get('args')
        try:
            if isinstance(c,(str,bytes,os.PathLike)):
                e.add_note(f"Command: {_to_str(c)}")
            elif c is not None:
                e.add_note(f"Command: {shlex.join(_to_str(a) for a in c)}")
        except TypeError:
            pass
        raise

