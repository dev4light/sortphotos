import pytest
import sys
from . import sortphotos

def test_sortphotos():
    # sortPhotos('./src', './dst', '%Y/%m', '%Y/%m',  verbose=True)
    sys.argv = ['/mnt/nas/dev/sortphotos/src/test/src', '/mnt/nas/dev/sortphotos/src/test/dst', 
    '--sort %Y/%m',
    '-x exif.model =~ "sony" => cam=sony']
    sortphotos.main()