import pretty_subprocess
import logging
logging.basicConfig()

try:
    pretty_subprocess.run("/bin/false",check=True)
except:
    logging.exception('false')

try:
    pretty_subprocess.run("/bin/junk")
except:
    logging.exception('junk')

try:
    cp = pretty_subprocess.run(('/bin/false','fails','today'),check=True)
except:
    logging.exception('false')

try:
    cp = pretty_subprocess.run(5)
except:
    logging.exception('false')

#pretty_subprocess.run("/bin/junk")


