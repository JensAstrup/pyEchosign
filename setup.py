import os

from setuptools import setup
from setuptools.command.build_py import build_py

version = os.environ.get('CI_COMMIT_TAG', None)


class BuildPyCommand(build_py):
    def run(self):
        if version is None:
            raise RuntimeError('CI_COMMIT_TAG must defined as an environment variable to build.')
        build_py.run(self)


setup(
    cmdclass={
        'build_py': BuildPyCommand,
    },
    name='pyEchosign',
    version=version,
    packages=['pyEchosign', 'pyEchosign.classes', 'pyEchosign.exceptions', 'pyEchosign.utils'],
    url='https://gitlab.com/jensastrup/pyEchosign',
    license='MIT',
    author='Jens Astrup',
    author_email='jensaiden@gmail.com',
    description='Connect to the Echosign API without constructing HTTP requests',
    long_description=open('README.rst').read(),
    install_requires=['requests>=2.12.4, <3.0.0', 'arrow>=0.10.0, <1.0.0'],
    tests_require=['coverage', 'nose'],
    keywords='adobe echosign',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Office/Business',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
        'Natural Language :: English'
    ]
)
