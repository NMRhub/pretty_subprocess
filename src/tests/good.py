import pretty_subprocess
import logging
logging.basicConfig()

try:
    cp = pretty_subprocess.run(('/bin/ls','/tmp'),capture_output=True)
    print(cp.command)
except:
    logging.exception('false')


#pretty_subprocess.run("/bin/junk")


