from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules=[
    Extension("mupla_cython",
              include_dirs=["../../../mupdf/include",
                            "../../../mupla"],
              sources=["mupla_cython.pyx"],
              libraries = ["m",
                           ],
              extra_objects=["../../../mupla/libmupla.a"
                             ],
    )
]

setup(
    ext_modules = cythonize(ext_modules)
)
