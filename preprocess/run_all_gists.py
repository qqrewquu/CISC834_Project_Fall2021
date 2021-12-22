
import os 
from os import walk
from os import listdir
from os.path import isfile, join
import subprocess
import commands
import signal
import logging
import csv 
import sys


# Seconds for timeout
TIMEOUT_SECONDS = 60

# Configure logging
logging.basicConfig(format='%(asctime)-15s %(message)s')
logger = logging.getLogger('test_gist')
logger.setLevel(logging.INFO)


class timeout:
    """Timeout class.
    Taken from StackOverflow: https://stackoverflow.com/a/22348885
    """

    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message

    def handle_timeout(self, signum, frame):
        logger.info('Timeout encountered')
        # print('Timeout encountered')
        raise TimeoutError(self.error_message)

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)

    def __exit__(self, type, value, traceback):
        signal.alarm(0)


class TimeoutError(Exception):
    def __init__(self,mess): 
        super(TimeoutError, self).__init__()
        pass




if __name__ == '__main__':
    # Init results list
    data_path = '../datasets/gistable-evaluated-gists'
    results = []
    # a variable control number of files being read
    '''Loop through working directory to get all the dir path/name, and file names'''
    for (dirpath, dirnames, filenames) in walk(data_path):
        #Loop through all the directories 
        for dir in dirnames[:]: 
            # Loop through all the files in the current directory 
            for f in listdir(data_path +'/'+ dir):
                # keep only python file
                if f.endswith(".py"):
                    pyfile = join(dir, f)
                    '''author's method'''
                    # run file see if there is any error 
                    try:
                        try:
                            with timeout(seconds=TIMEOUT_SECONDS):
                                execfile(pyfile, {}, {})
                        except TimeoutError:
                            pass
                        import_error = False
                        logger.info('No Error')
                        # _log(gist_id + '/initial-eval/result', 'Success', consul_addr)
                        
                        results.append({
                        'id': dir,
                        'initial-eval':'Success'
                        })
                    except BaseException as e:                        
                        print('str(e) = {}'.format(str(e)))
                        import_error = (type(e).__name__ == 'ImportError')
                        logger.info('Error')
                
                        results.append({
                        'id': dir,
                        'initial-eval':type(e).__name__
                        })      
        # break for os.walk     
        break    
   
   
    '''write results to csv'''
    

    logger.info('Wring results to gists.csv')
    print(len(results))


    with open('all-gists-results_2500.csv', 'w') as results_file:
        fieldnames = ['id', 'initial-eval']
        # Create dict writer
        writer = csv.DictWriter(results_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)        
        print('file has been saved')

                