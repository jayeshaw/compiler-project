from helper_functions import *
from parser import local_vars

# 32 bit register descriptors
reg_desc = {}
reg_desc["eax"] = set()
reg_desc["ebx"] = set()
reg_desc["ecx"] = set()
reg_desc["edx"] = set()
reg_desc["esi"] = set()
reg_desc["edi"] = set()


def free_all_regs(instr):
    to_free = [instr.src1, instr.src2] # the dest is not to be freed
    for operand in to_free:
        if (operand != None and instr.instr_info['nextuse'][operand] == None \
            and instr.instr_info['live'][operand] == False):
            for reg in symbol_info[operand].address_desc_reg:
                reg_desc[reg].remove(operand)
            symbol_info[operand].address_desc_reg.clear()


def get_register(instr, compulsory = True, exclude_reg = []):
    '''
    function to get the best register for instr.dest, using nextuse 
    liveness of the symbols
    '''
    for reg in symbol_info[instr.src1].address_desc_reg:
        if reg not in exclude_reg:
            if(len(reg_desc[reg]) == 1 and instr.instr_info['nextuse'][instr.src1] == None\
             and not instr.instr_info['live'][instr.src1]):
                symbol_info[instr.src1].address_desc_reg.remove(reg)
                return reg

    for reg in reg_desc.keys():
        if(reg not in exclude_reg):
            if(len(reg_desc[reg]) == 0):
                return reg
    
    if(instr.instr_info['nextuse'][instr.dest] != None or compulsory = True):
        '''
        This part returns the register which contains the value
        of minimum number of symbols
        '''
        R = None
        for reg in reg_desc.keys():
            if(reg not in exclude_reg):
                if(R == None):
                    R = reg   
                elif(len(reg_desc[reg]) < len(reg_desc[R])):
                    R = reg
        save_reg_to_mem(R)
        return R

    else:
        return get_location_in_memory(instr.dest)
    
def save_reg_to_mem(reg):
    '''
    Function to save the contents of a register to memory
    '''
    saved_loc = set()
    for symbol in reg_desc[reg]:
        for(location in symbols[symbol].address_desc_mem):
            if location not in saved_loc:
                print("\tmov " + get_location_in_memory(symbol) + ", " + reg)
                saved_loc.add(location)
        symbols[symbol].address_desc_reg.remove(reg)
    reg_desc[reg].clear()

def get_location_in_memory(symbol):
    '''
    Function to get the location of a symbol in memory
    '''
    for(location in symbols[symbol].address_desc_mem):
        prefix_string = "["
        if(type(location) is int):
            prefix_string = "[ebp"
            if(location >= 0):
                prefix_string = "[ebp+"
        return prefix_string+str(location)+"]"
        
def get_best_location():
    pass




