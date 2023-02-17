from setuptools import setup


APP = ['run.py']
DATA_FILES = []
OPTION = {'iconfile':'logo192.png'}


setup(
    app = APP,
    data_files=DATA_FILES,
    options={'py2app':OPTION},
    setup_requires = ['py2app']
)