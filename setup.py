from cx_Freeze import setup, Executable
setup(
    name = "hola",
    version = "1.0.0",
    options = {"build_exe": {
        'include_msvcr': True
    }},
    executables = [Executable("login_window.py",base="Win32GUI")]
    )