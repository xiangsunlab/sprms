"""
SPRMS
The NYU Shanghai Summer Undergraduate Research Experience Program in Molecular Science (SRPMS)
"""

# Add imports here
from .sprms import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
