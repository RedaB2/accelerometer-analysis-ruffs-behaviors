##################################################
# Helper functions (os-related)
##################################################
# Author: Reda Boutayeb
# Email: boutayeb@usc.edu
# Author: Srujan Gowda Sathiganahally Jagadeesha
# Email: sathigan@usc.edu
# Author: Rohit Milind Sonawane
# Email: rsonawan@usc.edu
##################################################

from __future__ import absolute_import
import os
import errno


def mkdir_if_missing(dir_path):
    """
    Function that creates directory path if missing

    :param dir_path: string
        Path to be created
    """
    try:
        os.makedirs(dir_path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
