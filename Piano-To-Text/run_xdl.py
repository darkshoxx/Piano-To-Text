from xdl import XDL
# This obviously only works in the ChemPU Stack
from chemputerxdl import ChemputerPlatform
import os

HERE = os.path.abspath(os.path.dirname(__file__))
xdl_file = os.path.join(HERE, "my_file.xdl")

x = XDL(xdl_file, platform=ChemputerPlatform)
print(x.human_readable())