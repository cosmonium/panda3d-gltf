from setuptools import setup

__version__ = ''
#pylint: disable=exec-used
exec(open('gltf/version.py').read())

setup(
    version=__version__,
    keywords='panda3d gltf',
    packages=['gltf'],
    install_requires=[
        'panda3d',
    ],
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest',
        'pylint',
        'pytest-pylint',
    ],
    entry_points={
        'console_scripts': [
            'gltf2bam=gltf.cli:main'
        ],
        'gui_scripts': [
            'gltf-viewer=gltf.viewer:main'
        ],
        'panda3d.loaders': [
            'gltf=gltf.loader:GltfLoader'
        ],
    },
)
