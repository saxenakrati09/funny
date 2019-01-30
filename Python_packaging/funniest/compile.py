from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("funniest",  ["funniest\\text.py"]),
    Extension("funniest",  ["funniest\\command_line.py"]),

#   ... all your modules that need be compiled ...

]

setup(
    name = 'funniest',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
