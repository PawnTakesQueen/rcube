from distutils.core import setup

import rcube

version = rcube.__version__
author = rcube.__author__

setup(name='rcube',
      description='Python module to solve Rubik\'s Cubes',
      license='BSD',
      version=version,
      author=author,
      author_email="vi@pariahvi.com",
      maintainer=author,
      maintainer_email='vi@pariahvi.com',
      url='http://github.com/PariahVi/rcube',
      py_modules=["rcube"],
      platforms='No particular restrictions',
      classifiers=[
           'Development Status :: 5 - Production/Stable',
           'Intended Audience :: Developers',
           'License :: OSI Approved :: BSD License',
           'Programming Language :: Python',
           'Programming Language :: Python :: 2',
           'Programming Language :: Python :: 3',
           'Programming Language :: Python :: 2.4',
           'Programming Language :: Python :: 2.5',
           'Programming Language :: Python :: 2.6',
           'Programming Language :: Python :: 2.7',
           'Programming Language :: Python :: 3.0',
           'Programming Language :: Python :: 3.1',
           'Programming Language :: Python :: 3.2',
           'Programming Language :: Python :: 3.3',
           'Operating System :: OS Independent',
           'Topic :: Software Development :: Libraries :: Python Modules'
          ]
      )
