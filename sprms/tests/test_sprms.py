"""
Unit and regression test for the sprms package.
"""

# Import package, test suite, and other packages as needed
import sprms
import pytest
import sys

def test_sprms_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "sprms" in sys.modules
