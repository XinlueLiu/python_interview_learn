import os, os.path

def dump_state(file,scanin):
    file.writelines(f';0 {scanin} 0 1\n')
    file.writelines(f';1 {scanin} 0 1\n')
    pass

def output_select(file):
    file.writelines(";OUTPUT_SELECT<4:1>\n")
    dump_state(file,1)
    dump_state(file,1)
    dump_state(file,0)
    dump_state(file,0)

def frequency_select(file):
    file.writelines(";FREQSELECT<14:1>\n")
    # if does not care each value in the range, can use _ to represent dontcare
    for _ in range(10):
        dump_state(file,0)
    dump_state(file,1)
    dump_state(file,0)
    dump_state(file,0)
    dump_state(file,0)

def ro_select(file):
    file.writelines(";ROSELECT<4:1>\n")
    dump_state(file,1)
    dump_state(file,0)
    dump_state(file,0)
    dump_state(file,0)

def start_clk(file, clkcycle):
    file.writelines(";START CLK\n")
    for _ in range(clkcycle):
        dump_state(file,0)


def process_header(file):
    # writelines -> write 1 line of content
    file.writelines(";this is the 1GHz test vec\n")
    file.writelines("radix 1 1 1 1\n")
    file.writelines("io i i i i\n")
    file.writelines("vname SCANCLK SCANIN ENABLECOMMON GLOBALENABLEB\n")
    file.writelines("\n\n\ntunit 1p\n")
    file.writelines("period 5000 	;100MHz clock\n")
    file.write('''trise 15	; 15ps rise time\ntfall 15	; 15ps fall time\nvih 0.9\nvil 0\nvoh 0.81\n\nvol 0.09\nchk_window -.98 .99 1	;for 1ns clock\n''')

def readScript(path):
    # move the pointer to the beginning of the file
    path.seek(0)
    print(path.readlines())

def process_script(path, callback):
    # create the directoy if not exist
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # open file with write&read permission
    clkgen = open(path,  "w+")
    process_header(clkgen)
    output_select(clkgen)
    frequency_select(clkgen)
    ro_select(clkgen)
    start_clk(clkgen, 100)
    # call the callback function
    callback(clkgen)
    clkgen.close()

# if _name__ is '__main__' means run the script directly instead of running from another script
if (__name__ == '__main__'):
    path = 'script_folder\clkgen.vec'
    # pass readScript function as a parameter to another function to enforce order
    process_script(path, readScript)