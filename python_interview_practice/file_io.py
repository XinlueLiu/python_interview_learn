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
    file.writelines(";this is the 1GHz test vec\n")
    file.writelines("radix 1 1 1 1\n")
    file.writelines("io i i i i\n")
    file.writelines("vname SCANCLK SCANIN ENABLECOMMON GLOBALENABLEB\n")
    file.writelines("\n\n\ntunit 1p\n")
    file.writelines("period 5000 	;100MHz clock\n")
    file.write('''trise 15	; 15ps rise time\ntfall 15	; 15ps fall time\nvih 0.9\nvil 0\nvoh 0.81\n\nvol 0.09\nchk_window -.98 .99 1	;for 1ns clock\n''')

def process_script(path, callback):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    clkgen = open(path,  "w+")
    process_header(clkgen)
    output_select(clkgen)
    frequency_select(clkgen)
    ro_select(clkgen)
    start_clk(clkgen, 100)
    callback(clkgen)
    clkgen.close()

def readScript(path):
    path.seek(0)
    print(path.readlines())

if (__name__ == '__main__'):
    path = '/Volumes/Macintosh HD/Users/xinlueliu/saved_files/python/python_interview_practice/script_folder/clkgen.vec'
    process_script(path, readScript)