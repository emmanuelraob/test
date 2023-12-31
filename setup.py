from setuptools import setup, Extension
from Cython.Build import cythonize

# Define una extensión con opciones de compilación adicionales para ball.pyx
extensions = [
    Extension(
        "ball",  # Nombre del módulo
        ["ball.pyx"],
        extra_compile_args=["-O3"],  # Opciones de compilación adicionales
        extra_link_args=["-O3"]
    )
]

setup(
    name="Nombre",
    ext_modules=cythonize(extensions)
)
