#!/usr/bin/env python
# encoding: utf-8
#
# Copyright 2009-2014 Arjen van Bochoven.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
makehtaccess

Based on makecatalogs created by Greg Neagle on 2009-03-30.
Adapted for creating .htaccess files

Install
-------
Put this file in /usr/local/munki and set the permissions executable

What it does
------------
Recursively scans a directory, looking for installer item info files.
Builds a .htaccess file from these files.
This script will add the installer_item_location to .htaccess when the following key is present
and set to true:
<key>restricted</key>
<true/>

Assumes a pkgsinfo directory under repopath.
User calling this needs to be able to write to repo/htaccess.

"""

import sys
import os
import optparse
import re

try:
    from munkilib import FoundationPlist as plistlib
    LOCAL_PREFS_SUPPORT = True
except ImportError:
    try:
        import FoundationPlist as plistlib
        LOCAL_PREFS_SUPPORT = True
    except ImportError:
        # maybe we're not on an OS X machine...
        print >> sys.stderr, ("WARNING: FoundationPlist is not available, "
                             "using plistlib instead.")
        import plistlib
        LOCAL_PREFS_SUPPORT = False

try:
    from munkilib.munkicommon import listdir, get_version
except ImportError:
    # munkilib is not available
    def listdir(path):
        """OSX HFS+ string encoding safe listdir().

        Args:
            path: path to list contents of
        Returns:
            list of contents, items as str or unicode types
        """
        # if os.listdir() is supplied a unicode object for the path,
        # it will return unicode filenames instead of their raw fs-dependent
        # version, which is decomposed utf-8 on OSX.
        #
        # we use this to our advantage here and have Python do the decoding
        # work for us, instead of decoding each item in the output list.
        #
        # references:
        # http://docs.python.org/howto/unicode.html#unicode-filenames
        # http://developer.apple.com/library/mac/#qa/qa2001/qa1235.html
        # http://lists.zerezo.com/git/msg643117.html
        # http://unicode.org/reports/tr15/    section 1.2
        if type(path) is str:
            path = unicode(path, 'utf-8')
        elif type(path) is not unicode:
            path = unicode(path)
        return os.listdir(path)

    def get_version():
        '''Placeholder if munkilib is not available'''
        return 'UNKNOWN'


def print_utf8(text):
    '''Print Unicode text as UTF-8'''
    print text.encode('UTF-8')

def print_err_utf8(text):
    '''Print Unicode text to stderr as UTF-8'''
    print >> sys.stderr, text.encode('UTF-8')


def makehtaccess(repopath, options):
    '''Assembles all pkginfo files into htaccess.
    Assumes a pkgsinfo directory under repopath.
    User calling this needs to be able to write to the repo/htaccess
    directory.'''

    # Make sure the pkgsinfo directory exists
    pkgsinfopath = os.path.join(repopath, 'pkgsinfo')
    # make sure pkgsinfopath is Unicode so that os.walk later gives us
    # Unicode names back.
    if type(pkgsinfopath) is str:
        pkgsinfopath = unicode(pkgsinfopath, 'utf-8')
    elif type(pkgsinfopath) is not unicode:
        pkgsinfopath = unicode(pkgsinfopath)

    if not os.path.exists(pkgsinfopath):
        print_err_utf8("pkgsinfo path %s doesn't exist!" % pkgsinfopath)
        exit(-1)

    # Set a default exit code
    exitCode = 0

    errors = []
    htaccess = []
    
    # Prevent reading the restricted catalog
    htaccess.append("catalogs/restricted")
    
    #Prevent reading pkgsinfo files
    htaccess.append("pkgsinfo/.*")

    # Walk through the pkginfo files
    for dirpath, dirnames, filenames in os.walk(pkgsinfopath):
        for dirname in dirnames:
            # don't recurse into directories that start
            # with a period.
            if dirname.startswith('.'):
                dirnames.remove(dirname)
        for filename in filenames:
            if filename.startswith('.'):
                # skip files that start with a period as well
                continue

            filepath = os.path.join(dirpath, filename)

            # Try to read the pkginfo file
            try:
                pkginfo = plistlib.readPlist(filepath)
            except IOError, inst:
                errors.append("IO error for %s: %s" % (filepath, inst))
                exitCode = -1
                continue
            except Exception, inst:
                errors.append("Unexpected error for %s: %s" % (filepath, inst))
                exitCode = -1
                continue

            # only write restricted items.
            restricted = pkginfo.get('restricted')
            if not restricted:
                continue
            if not restricted == True:
                continue


            if not 'installer_item_location' in pkginfo:
                errors.append(
                    "WARNING: file %s is missing installer_item_location"
                    % filepath[len(pkgsinfopath)+1:])
                # Skip this pkginfo unless we're running with force flag
                if not options.force:
                    exitCode = -1
                    continue

            # Try to form a path and fail if the
            # installer_item_location is not a valid type
            try:
                installeritempath = os.path.join(repopath, "pkgs",
                            pkginfo['installer_item_location'])
            except TypeError:
                errors.append("WARNING: invalid installer_item_location"
                    " in info file %s" % filepath[len(pkgsinfopath)+1:])
                exitCode = -1
                continue

            # Check if the installer item actually exists
            if not os.path.exists(installeritempath):
                errors.append("WARNING: Info file %s refers to "
                              "missing installer item: %s" %
                              (filepath[len(pkgsinfopath)+1:],
                               pkginfo['installer_item_location']))
                # Skip this pkginfo unless we're running with force flag
                if not options.force:
                    exitCode = -1
                    continue
                    
            infofilename = filepath[len(pkgsinfopath)+1:]
            print_utf8("Adding %s to %s..." % (infofilename, 'htaccess'))
            htaccess.append(os.path.join("pkgs", pkginfo['installer_item_location']))
            


    if errors:
        # group all errors at the end for better visibility
        print
        for error in errors:
            print_err_utf8(error)

    htaccesspath = os.path.join(repopath, ".htaccess")
    fileobj = open(htaccesspath, mode='w')
    print_utf8("Writing rules to %s" % htaccesspath)
    
    fileobj.write("Options -Indexes\n")
    fileobj.write("RewriteEngine on\n")
    
    for item in htaccess:
      fileobj.write("RewriteCond %{REMOTE_ADDR} !^145\.108. [NC]\n")
      fileobj.write("RewriteCond %{REMOTE_ADDR} !^130\.37. [NC]\n")
      fileobj.write("RewriteRule ^%s$ - [F,L,NC]\n\n" % re.escape(item))
    fileobj.close()
    # Exit with "exitCode" if we got this far.
    # This will be -1 if there were any errors
    # that prevented the htaccess to be written.
    exit(exitCode)


def pref(prefname):
    """Returns a preference for prefname"""
    if not LOCAL_PREFS_SUPPORT:
        return None
    try:
        _prefs = plistlib.readPlist(PREFSPATH)
    except Exception:
        return None
    if prefname in _prefs:
        return _prefs[prefname]
    else:
        return None


PREFSNAME = 'com.googlecode.munki.munkiimport.plist'
PREFSPATH = os.path.expanduser(os.path.join('~/Library/Preferences',
                                            PREFSNAME))
def main():
    '''Main'''
    usage = "usage: %prog [options] [/path/to/repo_root]"
    p = optparse.OptionParser(usage=usage)
    p.add_option('--version', '-V', action='store_true',
                      help='Print the version of the munki tools and exit.')
    p.add_option('--force', '-f', action='store_true', dest='force',
                      help='Disable sanity checks.')
    p.set_defaults(force=False)
    options, arguments = p.parse_args()

    if options.version:
        print get_version()
        exit(0)

    # Make sure we have a path to work with
    repopath = None
    if len(arguments) == 0:
        repopath = pref('repo_path')
        if not repopath:
            print_err_utf8("Need to specify a path to the repo root!")
            exit(-1)
        else:
            print_utf8("Using repo path: %s" % repopath)
    else:
        repopath = arguments[0].rstrip("/")

    # Make sure the repo path exists
    if not os.path.exists(repopath):
        print_err_utf8("Repo root path %s doesn't exist!" % repopath)
        exit(-1)

    # Make the htaccess
    makehtaccess(repopath, options)

if __name__ == '__main__':
    main()

