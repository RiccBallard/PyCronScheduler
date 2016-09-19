#!/usr/bin/env python
# encoding: utf-8
'''
tools.buildFromUI -- use pyuic4 to convert UI files from QT to python files

tools.buildFromUI is a description

It defines classes_and_methods

@author:     Ricc

@copyright:  2016 RBE All rights reserved.

@license:    GPL license

@contact:    user_email
@deffield    updated: Updated
'''

import sys
import os
import glob

# import argparse
import subprocess
import yaml

__all__ = []
__version__ = '0.2a'
__date__ = '2016-08-13'
__updated__ = '2016-08-14'

DEBUG = 1
TESTRUN = 0
PROFILE = 0

def main(argv=None):

    program_name = os.path.basename(sys.argv[0])
    display_info(program_name)
                 
    try:

        # MAIN BODY #
        options = load_config();
        process_ui_files(options)
        
    except Exception, e:
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2

def load_config():
    
    with open(".buildFromUI.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
    
    cfg = cfg['PyCronScheduler']
    option = {}
    option['indir'] = cfg['src'] + cfg['in']
    option['outdir'] = cfg['src'] + cfg['out']
    option['srcdir'] = cfg['src']
    option['exe'] = False
    if ( cfg.has_key('exe') ):
        if ( cfg['exe'] ):
            option['exe'] = True
            
        
    return option
    
def process_ui_files(config):       
    process_files = glob.glob(config['indir'] + "/*.ui")
    
    print "Source:      " + config['indir']
    print "Destination: " + config['outdir'] + "\n"
    
    for myFile in process_files:
        path_fname = list(os.path.split(os.path.abspath(myFile)))
        print "Converting\n\tfile: " + path_fname[1]
        
        outfname = os.path.splitext(path_fname[1])[0]
        print "\t  to: " + outfname 
        
        outfname = config['outdir'] + outfname + ".py"
        cmd = build_cmd(myFile, outfname, config['exe'])
        return_code = subprocess.call(cmd, shell=True)
        
        if (return_code == 0):        
            print "pyuic4 conversion: success"
        else:
            print "pyuic4 conversion: failed code " + return_code 
     
        print ""
     
     
def build_cmd(in_file, out_file, exe):
    cmd = "pyuic4 "
    if (exe):
        cmd = cmd + "-x "
    
    cmd = cmd + in_file + " -o " +  out_file
     
    return cmd
         
def display_info(program_name):
         
    print program_name + " written by Ricc Ballard"
    print "version: " + __version__ + " created on: " + __date__
    print "Last updated on: " + __updated__ + "\n" 
     
     
     
     
if __name__ == "__main__":
    if DEBUG:
        sys.argv.append("-h")
    if TESTRUN:
        import doctest
        doctest.testmod()
    if PROFILE:
        import cProfile
        import pstats
        profile_filename = 'tools.buildFromUI_profile.txt'
        cProfile.run('main()', profile_filename)
        statsfile = open("profile_stats.txt", "wb")
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
    sys.exit(main())
    
       
    
    
    