from cx_Freeze import setup,Executable

setup(
    name = "test",
	version="0.1",
	description="test",
	executables=[Executable("test1.py")],
	options = {
	}
)