from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(name='RWMem',
      packages=['RWMem'],
      version='0.0.1',
      license='MIT',
      description='A class to read and write memory.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='duel',
      url='https://github.com/vsantiago113/ReadWriteMemory',
      download_url='https://github.com/vsantiago113/ReadWriteMemory/archive/0.1.5.zip',
      keywords=['ReadWriteMemory', 'Hacking', 'Cheat Engine'],
      python_requires='>=3.6.0',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Topic :: Utilities',
          'License :: OSI Approved :: MIT License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
      ],
      )