import cx_Freeze

executables = [cx_Freeze.Executable("battlecalculator.py")]

cx_Freeze.setup(
    name="Corona Game",
    options={"build_exe":{"packages":["pygame"]}},
    executables=executables
    )
