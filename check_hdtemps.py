#!/usr/bin/python

'''
Nagios script to check HD temps

Requires hdtemps script regularly writing log to /tmp/hdtemps
'''

from optparse import OptionParser
from sys import exit
import os.path

# Version
version = 0.1

# Nagios return methods
def Ok(message):
    Return(0, message)

def Warning(message):
    Return(1, message)

def Critical(message):
    Return(2, message)

def Unknown(message):
    Return(3, message)

def Return(code, message):
    print message
    exit(code)

# Handle arguments
def ProcessArgs():

    parser = OptionParser(usage='',
                          version='%prog {0}'.format(version)
                          )
    
    parser.add_option('-w',
                      '--warning',
                      help='warning temperature threshold (Celsius)',
                      action='store',
                      default=40,
                      type='int',
                      dest='warning'
                      )
    
    parser.add_option('-c',
                      '--critical',
                      help='critical temperature threshold (Celsius)',
                      action='store',
                      default=50,
                      type='int',
                      dest='critical'
                      )
    
    parser.add_option('-f',
                      '--file',
                      help='hdtemps output file (defaults to /tmp/hdtemps)',
                      action='store',
                      default='/tmp/hdtemps',
                      dest='file'
                      )
    
    (options, args) = parser.parse_args()
    
    # Verify output file exists
    if not os.path.isfile(options.file):
        Unknown('Not hdtemps file at {0}'.format(options.file))
    
    # Verify that warning threshold is less than critical threshold
    if options.warning >= options.critical:
        Unknown('Warning threshold ({0}) must be less than Critical threshold ({1})'.format(options.warning,
                                                                                            options.critical))
    
    return options

# Parse hdtemps file
def ParseFile(path):
    
    print "TODO"

# Check temps
def CheckTemps(temps, warning, critical):
    
    print "TODO"

# Main program
if __name__ == "__main__":
    
    # Parse commandline arguments
    options = ProcessArgs()