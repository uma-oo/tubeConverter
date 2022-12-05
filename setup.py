from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Package based on pytube to download videos, audios, playlists of videos and playlists of audios as well'
LONG_DESCRIPTION = 'Package based on pytube to download videos, audios, playlists of videos and playlists of audios as well based on the pytube package'

# Setting up
setup(
    name="tubeConverter",
    version=VERSION,
    author="Oumayma EL-FAHSI",
    author_email="<oumayma.elfahsi@ump.ac.ma>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pytube'],
    keywords=['Python', 'Videos', 'Music', 'Playlist music', 'Playlist videos', 'OOP' ,'YouTube','Converter'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]
)