# Lowest note: 21
# Highest note: 108
from itertools import cycle
import string
import os
LETTERS = string.ascii_lowercase
KEYS = cycle(string.ascii_uppercase[0:7])
SKIPS = cycle([2,1,2,2,1,2,2])
HERE = os.path.abspath(os.path.dirname(__file__))
OUTPUT = os.path.join(HERE, "output_files")
BOMEFILES = os.path.join(HERE, "OldBomeFiles")
GENERAL = os.path.join(OUTPUT, "general_output_file.txt")
BOILERPLATE = os.path.join(BOMEFILES, "boilerplate.xdl")

def write_to_generic(write_my_string):

    with open(GENERAL, 'a') as the_file:
        the_file.write(write_my_string)
        # for number in range(26):
            # writestring = "Name" + str(number + 1) + "=" + LETTERS[number] + "\n"
            # writestring = "Options" + str(number + 1) + "=Actv01Stop00OutO00StMa00000001label0006__cmt>\n"
        #    writestring = 'Outgoing'+ str(number + 1) +'=KAM3<Outgoing Action="KeyStrokes"><Type>Text</Type><Keys><Key Char="' + LETTERS[number] + '"/></Keys></Outgoing>\n'
        #    the_file.write(writestring)
        # key = 57 # starting with A
        # counter = 0

        # while key < 101:
        #     writestring = 'Incoming' + str(counter + 1) +'=MID3<Incoming Action="MIDI"><Simple Type="NoteOn"><Channel num="0" Type="New Version Required"/><Value1 num="' + str(key) + '" setvar="oo" Type="New Version Required"/></Simple></Incoming>\n'
        #     key +=  next(SKIPS)
        #     counter += 1
        #     the_file.write(writestring)


def file_to_bome_text(filepath:str)-> str:
    file1 = open(filepath, 'r')
    output_string = ""
    Lines = file1.readlines()
    for line in Lines:
        linelength = len(line)
        for symbol_index in range(linelength - 1):
            output_string += '<Key Char="'
            symbol = line[symbol_index]
            if symbol == "<":
                symbol = "&lt;"
            if symbol == ">":
                symbol = "&gt;"
            if symbol == '"':
                symbol = "&quot;"
            output_string += symbol
            output_string += '"/>'
        output_string += '<Key VK="13"/><Key Release="Y" VK="13"/>'   # Return at end of line
        output_string += '<Key Ext="Y" VK="36"/><Key Release="Y" Ext="Y" VK="36"/>' # Home key

    return output_string


test_string = file_to_bome_text(os.path.join(BOMEFILES, "reactor.xml"))
write_to_generic(test_string)