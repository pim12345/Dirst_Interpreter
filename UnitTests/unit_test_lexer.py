import os
import sys
import unittest

from Lexer.lexer import *
from Lexer.tokens import *
from Parser.parser import *
from Runner.runner import *
from Tools.tools import *

class TestLexerDirectorySubset(unittest.TestCase):
    def test_fnc(self):
        dirstCode = ["\tfnc_function_n"]

        consoleInput = ""#max recursion depth is default 1000,can be changed to an higher value, to support bigger functions
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].functionInput, 'n')
        self.assertEqual(lex_output[0].parameter1, 'function')
        self.assertEqual(lex_output[0].isInALoop, 1)
        self.assertIsInstance(lex_output[0], fnc)
        #print(lex_output)
    #todo add test for forgetting tab before function	
    def test_dif(self): 
        dirstCode = ["\tdif_n"]
        consoleInput = ""#max recursion depth is default 1000,can be changed to an higher value, to support bigger functions
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, 'n')
        self.assertEqual(lex_output[0].isInALoop, 1)
        self.assertIsInstance(lex_output[0], dif_directory)
    
    def test_nif(self): 
        dirstCode = ["\tnif_n"]
        consoleInput = ""#max recursion depth is default 1000,can be changed to an higher value, to support bigger functions
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, 'n')
        self.assertEqual(lex_output[0].isInALoop, 1)
        self.assertIsInstance(lex_output[0], nif)
        
    def test_lpc(self): 
        dirstCode = ["\tlpc_n"]
        consoleInput = ""#max recursion depth is default 1000,can be changed to an higher value, to support bigger functions
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, 'n')
        self.assertEqual(lex_output[0].isInALoop, 1)
        self.assertIsInstance(lex_output[0], lpc)
        
    def test_lpn(self): 
        dirstCode = ["\tlpn_n"]
        consoleInput = ""#max recursion depth is default 1000,can be changed to an higher value, to support bigger functions
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, 'n')
        self.assertEqual(lex_output[0].isInALoop, 1)
        self.assertIsInstance(lex_output[0], lpn)
        
    def test_dlw(self): 
        dirstCode = ["\tdlw_n"]
        consoleInput = ""#max recursion depth is default 1000,can be changed to an higher value, to support bigger functions
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, 'n')
        self.assertEqual(lex_output[0].isInALoop, 1)
        self.assertIsInstance(lex_output[0], dlw)
        
    def test_dlu(self): 
        dirstCode = ["\tdlu_n"]
        consoleInput = ""#max recursion depth is default 1000,can be changed to an higher value, to support bigger functions
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, 'n')
        self.assertEqual(lex_output[0].isInALoop, 1)
        self.assertIsInstance(lex_output[0], dlu)
        
class TestLexerDATSubset(unittest.TestCase):
    def test_abs(self):
        dirstCode = ["abs_val1_val2.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, 'val1')
        self.assertEqual(lex_output[0].parameter2, 'val2')
        self.assertIsInstance(lex_output[0], abs)
        
    def test_neg(self):
        dirstCode = ["neg_val1_val2.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, 'val1')
        self.assertEqual(lex_output[0].parameter2, 'val2')
        self.assertIsInstance(lex_output[0], neg)
        
    def test_add(self):
        dirstCode = ["add_val1_val2_val3.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, 'val1')
        self.assertEqual(lex_output[0].parameter2, 'val2')
        self.assertEqual(lex_output[0].parameter3, 'val3')
        self.assertIsInstance(lex_output[0], add)
        
    def test_sub(self):
        dirstCode = ["sub_val1_val2_val3.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, 'val1')
        self.assertEqual(lex_output[0].parameter2, 'val2')
        self.assertEqual(lex_output[0].parameter3, 'val3')
        self.assertIsInstance(lex_output[0], sub_dat)
        
    def test_mul(self):
        dirstCode = ["mul_val1_val2_val3.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, 'val1')
        self.assertEqual(lex_output[0].parameter2, 'val2')
        self.assertEqual(lex_output[0].parameter3, 'val3')
        self.assertIsInstance(lex_output[0], mul)
        
    def test_div(self):
        dirstCode = ["div_val1_val2_val3.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, 'val1')
        self.assertEqual(lex_output[0].parameter2, 'val2')
        self.assertEqual(lex_output[0].parameter3, 'val3')
        self.assertIsInstance(lex_output[0], div_dat)
        
    def test_mod(self):
        dirstCode = ["mod_val1_val2_val3.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, 'val1')
        self.assertEqual(lex_output[0].parameter2, 'val2')
        self.assertEqual(lex_output[0].parameter3, 'val3')
        self.assertIsInstance(lex_output[0], mod)
        
    def test_and(self):
        dirstCode = ["and_val1_val2_val3.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, 'val1')
        self.assertEqual(lex_output[0].parameter2, 'val2')
        self.assertEqual(lex_output[0].parameter3, 'val3')
        self.assertIsInstance(lex_output[0], and_)
        
    def test_orb(self):
        dirstCode = ["orb_val1_val2_val3.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, 'val1')
        self.assertEqual(lex_output[0].parameter2, 'val2')
        self.assertEqual(lex_output[0].parameter3, 'val3')
        self.assertIsInstance(lex_output[0], orb)
        
    def test_xor(self):
        dirstCode = ["xor_val1_val2_val3.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, 'val1')
        self.assertEqual(lex_output[0].parameter2, 'val2')
        self.assertEqual(lex_output[0].parameter3, 'val3')
        self.assertIsInstance(lex_output[0], xor)
        
    def test_xad(self):
        dirstCode = ["xad_val1_val2_val3.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, 'val1')
        self.assertEqual(lex_output[0].parameter2, 'val2')
        self.assertEqual(lex_output[0].parameter3, 'val3')
        self.assertIsInstance(lex_output[0], xad)
        
    def test_nad(self):
        dirstCode = ["nad_val1_val2_val3.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertIsInstance(lex_output[0], nad)
        
    def test_nor(self):
        dirstCode = ["nor_val1_val2.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertIsInstance(lex_output[0], nor)
        
    def test_not_(self):
        dirstCode = ["not_val1_val2.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertIsInstance(lex_output[0], not_)
        
    def test_mor(self):
        dirstCode = ["mor_val1_val2_val3.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertEqual(lex_output[0].parameter3,"val3")
        self.assertIsInstance(lex_output[0], mor)
        
    def test_les(self):
        dirstCode = ["les_val1_val2_val3.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertEqual(lex_output[0].parameter3,"val3")
        self.assertIsInstance(lex_output[0], les)
        
    def test_equ(self):
        dirstCode = ["equ_val1_val2_val3.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertEqual(lex_output[0].parameter3,"val3")
        self.assertIsInstance(lex_output[0], equ)
        
    def test_neq(self):
        dirstCode = ["neq_val1_val2_val3.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertEqual(lex_output[0].parameter3,"val3")
        self.assertIsInstance(lex_output[0], neq)
        
    def test_get(self):
        dirstCode = ["get_val1_val2_val3.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertEqual(lex_output[0].parameter3,"val3")
        self.assertIsInstance(lex_output[0], get)
        
    def test_let(self):
        dirstCode = ["let_val1_val2_val3.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertEqual(lex_output[0].parameter3,"val3")
        self.assertIsInstance(lex_output[0], let)
        
    def test_rdi(self):
        dirstCode = ["rdi_val1.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertIsInstance(lex_output[0], rdi)
        
    def test_ric(self):
        dirstCode = ["ric_val1.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertIsInstance(lex_output[0], ric)
        
    def test_dsi(self):
        dirstCode = ["dsi_val1.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertIsInstance(lex_output[0], dsi)
        
    def test_dic(self):
        dirstCode = ["dic_val1.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertIsInstance(lex_output[0], dic)
        
    def test_set(self):
        dirstCode = ["set_val1_val2.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertIsInstance(lex_output[0], set)
        
    def test_max(self):
        dirstCode = ["max_val1_val2_val3.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertIsInstance(lex_output[0], max_)
        
    def test_min(self):
        dirstCode = ["min_val1_val2_val3.dat"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertIsInstance(lex_output[0], min_)
        
class TestLexerTXTSubset(unittest.TestCase):
    def test_rdc(self):
        dirstCode = ["rdc_val1.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertIsInstance(lex_output[0], rdc)
        
    def test_rds(self):
        dirstCode = ["rds_val1.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertIsInstance(lex_output[0], rds)
        
    def test_eof(self):
       dirstCode = ["eof_val1.txt"]
       consoleInput = ""
       lex_output = lex(dirstCode, consoleInput)
       self.assertEqual(lex_output[0].parameter1, "val1")
       self.assertIsInstance(lex_output[0], eof)
    
    def test_dsc(self):
        dirstCode = ["dsc_val1_val2.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertIsInstance(lex_output[0], dsc)
        
    def test_dss(self):
        dirstCode = ["dss_val1.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertIsInstance(lex_output[0], dss)
        
    def test_dsl(self):
        dirstCode = ["dsl_val1.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertIsInstance(lex_output[0], dsl)
        
    def test_dec(self):
        dirstCode = ["dec_val1_val2.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertIsInstance(lex_output[0], dec)
        
    def test_des(self):
        dirstCode = ["des_val1.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertIsInstance(lex_output[0], des)
        
    def test_del(self):
        dirstCode = ["del_val1.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertIsInstance(lex_output[0], del_)
        
    def test_clr(self):
        dirstCode = ["clr_val1.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertIsInstance(lex_output[0], clr)
        
    def test_cat(self):
        dirstCode = ["cat_val1_val2_val3.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertEqual(lex_output[0].parameter3,"val3")
        self.assertIsInstance(lex_output[0], cat)
        
    def test_idx(self):
        dirstCode = ["idx_val1_val2_val3.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertIsInstance(lex_output[0], idx)
        
    def test_ids(self):
        dirstCode = ["ids_val1_val2_val3_val4.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertEqual(lex_output[0].parameter4, "val4")
        self.assertIsInstance(lex_output[0], ids)
        
    def test_lid(self):
        dirstCode = ["lid_val1_val2_val3.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertIsInstance(lex_output[0], lid)
        
    def test_rep(self):
        dirstCode = ["rep_val1_val2_val3_val4.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertEqual(lex_output[0].parameter4, "val4")
        self.assertIsInstance(lex_output[0], rep)
        
    def test_sub_txt(self):
        dirstCode = ["sub_val1_val2_val3_val4.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertEqual(lex_output[0].parameter3,"val3")
        self.assertEqual(lex_output[0].parameter4,"val4")
        self.assertIsInstance(lex_output[0], sub_txt)
        
    def test_rmv(self):
        dirstCode = ["rmv_val1_val2_val3_val4.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertEqual(lex_output[0].parameter3,"val3")
        self.assertEqual(lex_output[0].parameter4,"val4")
        self.assertIsInstance(lex_output[0], rmv)
        
    def test_ins(self):
        dirstCode = ["ins_val1_val2_val3_val4.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertEqual(lex_output[0].parameter4, "val4")
        self.assertIsInstance(lex_output[0], ins)
        
    def test_tou(self):
        dirstCode = ["tou_val1_val2.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertIsInstance(lex_output[0], tou)
        
    def test_tol(self):
        dirstCode = ["tol_val1_val2.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertIsInstance(lex_output[0], tol)
        
    def test_pdl(self):
        dirstCode = ["pdl_val1_val2_val3.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertIsInstance(lex_output[0], pdl)
        
    def test_cpl(self):
        dirstCode = ["cpl_val1_val2_val3_val4.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertEqual(lex_output[0].parameter4, "val4")
        self.assertIsInstance(lex_output[0], cpl)
        
    def test_pdr(self):
        dirstCode = ["pdr_val1_val2_val3.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertIsInstance(lex_output[0], pdr)
        
    def test_cpr(self):
        dirstCode = ["cpr_val1_val2_val3_val4.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertEqual(lex_output[0].parameter3,"val3")
        self.assertEqual(lex_output[0].parameter4,"val4")
        self.assertIsInstance(lex_output[0], cpr)
        
    def test_sam(self):
        dirstCode = ["sam_val1_val2_val3.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertEqual(lex_output[0].parameter3,"val3")
        self.assertIsInstance(lex_output[0], sam)
        
    def test_dif_txt(self):
        dirstCode = ["dif_val1_val2_val3.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertIsInstance(lex_output[0], dif_txt)
        
    def test_hiv_txt(self):
        dirstCode = ["hiv_val1_val2_val3.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertIsInstance(lex_output[0], hiv)
        
    def test_lov_txt(self):
        dirstCode = ["lov_val1_val2_val3.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1") 
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertEqual(lex_output[0].parameter3,"val3")
        self.assertIsInstance(lex_output[0], lov)
        
    def test_hev_txt(self):
        dirstCode = ["hev_val1_val2_val3.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1") 
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertEqual(lex_output[0].parameter3,"val3")
        self.assertIsInstance(lex_output[0], hev)
        
    def test_lev_txt(self):
        dirstCode = ["lev_val1_val2_val3.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1") 
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertEqual(lex_output[0].parameter3,"val3")
        self.assertIsInstance(lex_output[0], lev)
        
    def test_ssw_txt(self):
        dirstCode = ["ssw_val1_val2_val3.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1") 
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertEqual(lex_output[0].parameter3,"val3")
        self.assertIsInstance(lex_output[0], ssw)
        
    def test_sew_txt(self):
        dirstCode = ["sew_val1_val2_val3.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1") 
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertEqual(lex_output[0].parameter3,"val3")
        self.assertIsInstance(lex_output[0], sew)
        
    def test_trm_txt(self):
        dirstCode = ["trm_val1_val2_val3.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertIsInstance(lex_output[0], trm)
        
    def test_tms_txt(self):
        dirstCode = ["tms_val1_val2_val3.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertIsInstance(lex_output[0], tms)
        
    def test_tme_txt(self):
        dirstCode = ["tme_val1_val2_val3.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertIsInstance(lex_output[0], tme)
        
    def test_ses_txt(self):
        dirstCode = ["ses_val1_val2.txt"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertIsInstance(lex_output[0], ses)
        
class TestLexerBINSubset(unittest.TestCase):
    def test_pls_bin(self):
        dirstCode = ["pls_val1_val2_val3.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertIsInstance(lex_output[0], pls)
        
    def test_mns_bin(self):
        dirstCode = ["mns_val1_val2_val3.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1") 
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertEqual(lex_output[0].parameter3,"val3")
        self.assertIsInstance(lex_output[0], mns)
        
    def test_tms_bin(self):
        dirstCode = ["tms_val1_val2_val3.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertIsInstance(lex_output[0], tms)
        
    def test_dvb_bin(self):
        dirstCode = ["dvb_val1_val2_val3.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertIsInstance(lex_output[0], dvb)
        
    def test_pwr_bin(self):
        dirstCode = ["pwr_val1_val2_val3.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertIsInstance(lex_output[0], pwr)
        
    def test_sgn_bin(self):
        dirstCode = ["sgn_val1_val2.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertIsInstance(lex_output[0], sgn)
        
    def test_sqr_bin(self):
        dirstCode = ["sqr_val1_val2.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertIsInstance(lex_output[0], sqr)
        
    def test_sin_bin(self):
        dirstCode = ["sin_val1_val2.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertIsInstance(lex_output[0], sin)
        
    def test_cos_bin(self):
        dirstCode = ["cos_val1_val2.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1") 
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertIsInstance(lex_output[0], cos)
        
    def test_tan_bin(self):
        dirstCode = ["tan_val1_val2.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertIsInstance(lex_output[0], tan)
        
    def test_snh_bin(self):
        dirstCode = ["snh_val1_val2.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertIsInstance(lex_output[0], snh)
        
    def test_csh_bin(self):
        dirstCode = ["csh_val1_val2.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1") 
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertIsInstance(lex_output[0], csh)
        
    def test_tnh_bin(self):
        dirstCode = ["tnh_val1_val2.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertIsInstance(lex_output[0], tnh)
        
    def test_cil_bin(self):
        dirstCode = ["cil_val1_val2.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertIsInstance(lex_output[0], cil)
        
    def test_flr_bin(self):
        dirstCode = ["flr_val1_val2.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertIsInstance(lex_output[0], flr)
        
    def test_log_bin(self):
        dirstCode = ["log_val1_val2.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertIsInstance(lex_output[0], log)
        
    def test_lge_bin(self):
        dirstCode = ["lge_val1_val2.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertIsInstance(lex_output[0], lge)
        
    def test_lbq_bin(self):
        dirstCode = ["lbq_val1_val2_val3.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertIsInstance(lex_output[0], lbq)
        
    def test_epw_bin(self):
        dirstCode = ["epw_val1_val2.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertIsInstance(lex_output[0], epw)
        
    def test_avl_bin(self):
        dirstCode = ["avl_val1_val2.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertIsInstance(lex_output[0], avl)
        
    def test_rnd_bin(self):
        dirstCode = ["rnd_val1.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertIsInstance(lex_output[0], rnd)
    
    def test_rou_bin(self):
        dirstCode = ["rou_val1_val2.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertIsInstance(lex_output[0], rou)
        
    def test_asn_bin(self):
        dirstCode = ["asn_val1_val2.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertIsInstance(lex_output[0], asn)
        
    def test_acs_bin(self):
        dirstCode = ["acs_val1_val2.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertIsInstance(lex_output[0], acs)
        
    def test_atn_bin(self):
        dirstCode = ["atn_val1_val2.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertIsInstance(lex_output[0], atn)
        
    def test_mks_bin(self):
        dirstCode = ["mks_val1_val2.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertIsInstance(lex_output[0], mks)
        
    def test_fmx_bin(self):
        dirstCode = ["fmx_val1_val2_val3.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertEqual(lex_output[0].parameter2, "val2") 
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertIsInstance(lex_output[0], fmx)
        
    def test_fmn_bin(self):
        dirstCode = ["fmn_val1_val2_val3.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")  
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertIsInstance(lex_output[0], fmn)
        
    def test_grt_bin(self):
        dirstCode = ["grt_val1_val2_val3.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")  
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertIsInstance(lex_output[0], grt)
        
    def test_lst_bin(self):
        dirstCode = ["lst_val1_val2_val3.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")  
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertEqual(lex_output[0].parameter3,"val3")
        self.assertIsInstance(lex_output[0], lst)
        
    def test_eqt_bin(self):
        dirstCode = ["eqt_val1_val2_val3.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")  
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertEqual(lex_output[0].parameter3,"val3")
        self.assertIsInstance(lex_output[0], eqt)
        
    def test_net_bin(self):
        dirstCode = ["net_val1_val2_val3.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")  
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertEqual(lex_output[0].parameter3,"val3")
        self.assertIsInstance(lex_output[0], net)
        
    def test_gte_bin(self):
        dirstCode = ["gte_val1_val2_val3.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")  
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertEqual(lex_output[0].parameter3,"val3")
        self.assertIsInstance(lex_output[0], gte)
        
    def test_lte_bin(self):
        dirstCode = ["lte_val1_val2_val3.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")  
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertEqual(lex_output[0].parameter3,"val3")
        self.assertIsInstance(lex_output[0], lte)
        
    def test_rfv_bin(self):
        dirstCode = ["rfv_val1.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")  
        self.assertIsInstance(lex_output[0], rfv)
        
    def test_dfv_bin(self):
        dirstCode = ["dfv_val1.bin"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")  
        self.assertIsInstance(lex_output[0], dfv_bin)

    
class TestLexerZIPSubset(unittest.TestCase):
    def test_giv_zip(self):
        dirstCode = ["giv_val1_val2_val3.zip"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")  
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertEqual(lex_output[0].parameter3,"val3")
        self.assertIsInstance(lex_output[0], giv)
        
    def test_siv_zip(self):
        dirstCode = ["siv_val1_val2_val3.zip"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")  
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertIsInstance(lex_output[0], siv)
        
    def test_gsv_zip(self):
        dirstCode = ["gsv_val1_val2_val3.zip"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")  
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertIsInstance(lex_output[0], gsv)
        
    #in documentation duplicate siv token, same token here so it it the same test as above
    
    def test_gfv_zip(self):
        dirstCode = ["gfv_val1_val2_val3.zip"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")  
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertIsInstance(lex_output[0], gfv)
        
    def test_sfv_zip(self):
        dirstCode = ["sfv_val1_val2_val3.zip"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")  
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertEqual(lex_output[0].parameter3,"val3")
        self.assertIsInstance(lex_output[0], sfv)
        
    def test_fia_zip(self):
        dirstCode = ["fia_val1_val2.zip"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertIsInstance(lex_output[0], fia)
        
    def test_zia_zip(self):
        dirstCode = ["zia_val1_val2.zip"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertIsInstance(lex_output[0], zia)
        
    def test_fsa_zip(self):
        dirstCode = ["fsa_val1_val2.zip"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertIsInstance(lex_output[0], fsa)
        
    def test_zsa_zip(self):
        dirstCode = ["zsa_val1_val2.zip"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertIsInstance(lex_output[0], zsa)
        
    def test_ffa_zip(self):
        dirstCode = ["ffa_val1_val2.zip"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2")
        self.assertIsInstance(lex_output[0], ffa)
        
    def test_zfa_zip(self):
        dirstCode = ["zfa_val1_val2.zip"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertEqual(lex_output[0].parameter2,"val2")
        self.assertIsInstance(lex_output[0], zfa)
        
class TestLexerEXESubset(unittest.TestCase):
    def test_sia_exe(self):
        dirstCode = ["sia_val1_val2.exe"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertEqual(lex_output[0].parameter2, "val2") 
        self.assertIsInstance(lex_output[0], sia)
        
    def test_ssa_exe(self):
        dirstCode = ["ssa_val1_val2_val3.exe"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertEqual(lex_output[0].parameter2,"val2") 
        self.assertEqual(lex_output[0].parameter3,"val3") 
        self.assertIsInstance(lex_output[0], ssa)
        
    def test_sti_exe(self):
        dirstCode = ["sti_val1_val2.exe"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertEqual(lex_output[0].parameter2, "val2") 
        self.assertIsInstance(lex_output[0], sti)
        
    def test_stf_exe(self):
        dirstCode = ["stf_val1_val2.exe"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1") 
        self.assertEqual(lex_output[0].parameter2,"val2") 
        self.assertIsInstance(lex_output[0], stf)
        
    def test_stc_exe(self):
        dirstCode = ["stc_val1_val2_val3.exe"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertEqual(lex_output[0].parameter2, "val2") 
        self.assertEqual(lex_output[0].parameter3, "val3")
        self.assertIsInstance(lex_output[0], stc)
        
    def test_its_exe(self):
        dirstCode = ["its_val1_val2.exe"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")  
        self.assertEqual(lex_output[0].parameter2, "val2") 
        self.assertIsInstance(lex_output[0], its)
        
    def test_itf_exe(self):
        dirstCode = ["itf_val1_val2.exe"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")  
        self.assertEqual(lex_output[0].parameter2,"val2") 
        self.assertIsInstance(lex_output[0], itf)
        
    def test_ias_exe(self):
        dirstCode = ["ias_val1_val2.exe"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")  
        self.assertEqual(lex_output[0].parameter2, "val2") 
        self.assertIsInstance(lex_output[0], ias)
        
    def test_aif_exe(self):
        dirstCode = ["aif_val1_val2.exe"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")  
        self.assertEqual(lex_output[0].parameter2,"val2") 
        self.assertIsInstance(lex_output[0], aif)
        
    def test_fts_exe(self):
        dirstCode = ["fts_val1_val2.exe"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")  
        self.assertEqual(lex_output[0].parameter2, "val2") 
        self.assertIsInstance(lex_output[0], fts)
        
    def test_fti_exe(self):
        dirstCode = ["fti_val1_val2.exe"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")  
        self.assertEqual(lex_output[0].parameter2,"val2") 
        self.assertIsInstance(lex_output[0], fti)
        
    def test_afi_exe(self):
        dirstCode = ["afi_val1_val2.exe"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")  
        self.assertEqual(lex_output[0].parameter2,"val2") 
        self.assertIsInstance(lex_output[0], afi)

class TestLexerDLLSubset(unittest.TestCase):
    def test_psh_dll(self):
        dirstCode = ["psh_val1.dll"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertIsInstance(lex_output[0], psh)
        
    def test_pop_dll(self):
        dirstCode = ["pop_val1.dll"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertIsInstance(lex_output[0], pop)
        
    def test_spk_dll(self):
        dirstCode = ["spk_val1.dll"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertIsInstance(lex_output[0], spk)
        
    def test_ssz_dll(self):
        dirstCode = ["ssz_val1.dll"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertIsInstance(lex_output[0], ssz)
        
    def test_enq_dll(self):
        dirstCode = ["enq_val1.dll"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertIsInstance(lex_output[0], enq)
        
    def test_deq_dll(self):
        dirstCode = ["deq_val1.dll"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertIsInstance(lex_output[0], deq)
        
    def test_qpk_dll(self):
        dirstCode = ["qpk_val1.dll"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertIsInstance(lex_output[0], qpk)
        
    def test_qsz_dll(self):
        dirstCode = ["qsz_val1.dll"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertIsInstance(lex_output[0], qsz)
        
    def test_tpl_dll(self):
        dirstCode = ["tpl.dll"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertIsInstance(lex_output[0], tpl)
        
    def test_tpr_dll(self):
        dirstCode = ["tpr.dll"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertIsInstance(lex_output[0], tpr)
        
    def test_tsv_dll(self):
        dirstCode = ["tsv_val1.dll"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertIsInstance(lex_output[0], tsv)
        
    def test_tgv_dll(self):
        dirstCode = ["tgv_val1.dll"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1") 
        self.assertIsInstance(lex_output[0], tgv)
        
    def test_gbe_dll(self):
        dirstCode = ["gbe.dll"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertIsInstance(lex_output[0], gbe)
        
    def test_gen_dll(self):
        dirstCode = ["gen.dll"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertIsInstance(lex_output[0], gen)
        
    def test_gef_dll(self):
        dirstCode = ["gef.dll"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertIsInstance(lex_output[0], gef)
        
    def test_lce_dll(self):
        dirstCode = ["lce.dll"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertIsInstance(lex_output[0], lce)
        
    def test_lcn_dll(self):
        dirstCode = ["lcn.dll"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertIsInstance(lex_output[0], lcn)
        
    def test_lcf_dll(self):
        dirstCode = ["lcf.dll"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertIsInstance(lex_output[0], lcf)
        
    def test_ges_dll(self):
        dirstCode = ["ges_val1.dll"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertIsInstance(lex_output[0], ges)
        
    def test_ces_dll(self):
        dirstCode = ["ces.dll"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertIsInstance(lex_output[0], ces)
        
class TestLexerCSVSubset(unittest.TestCase):
    def test_cia_csv(self):
        dirstCode = ["cia_val1.csv"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertIsInstance(lex_output[0], cia)
        
    def test_civ_csv(self):
        dirstCode = ["civ_val1.csv"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1") 
        self.assertIsInstance(lex_output[0], civ)
        
    def test_csa_csv(self):
        dirstCode = ["csa_val1.csv"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertIsInstance(lex_output[0], csa)
        
    def test_csv_csv(self):
        dirstCode = ["csv_val1.csv"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertIsInstance(lex_output[0], csv)
        
    def test_cfa_csv(self):
        dirstCode = ["cfa_val1.csv"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1") 
        self.assertIsInstance(lex_output[0], cfa)
        
    def test_cfv_csv(self):
        dirstCode = ["cfv_val1.csv"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertIsInstance(lex_output[0], cfv)
        
    def test_dia_csv(self):
        dirstCode = ["dia_val1.csv"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertIsInstance(lex_output[0], dia)
        
    def test_div_csv(self):
        dirstCode = ["div_val1.csv"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertIsInstance(lex_output[0], div_csv)
        
    def test_dsa_csv(self):
        dirstCode = ["dsa_val1.csv"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertIsInstance(lex_output[0], dsa)
        
    def test_dsv_csv(self):
        dirstCode = ["dsv_val1.csv"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1") 
        self.assertIsInstance(lex_output[0], dsv)
        
    def test_dfa_csv(self):
        dirstCode = ["dfa_val1.csv"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "val1")
        self.assertIsInstance(lex_output[0], dfa)
        
    def test_dfv_csv(self):
        dirstCode = ["dfv_val1.csv"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1,"val1")
        self.assertIsInstance(lex_output[0], dfv_csv)
        
class TestLexerLNKSubset(unittest.TestCase):#LNK class is added for the atp course
    def test_run_lnk(self):
        dirstCode = ["run_FunctionName_input_output.lnk"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].functionName, "FunctionName")
        self.assertEqual(lex_output[0].parameterVar, "input")
        self.assertEqual(lex_output[0].returnVar, "output")
        self.assertIsInstance(lex_output[0], run)
        
    def test_rtn_lnk(self):
        dirstCode = ["rtn_n.lnk"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        self.assertEqual(lex_output[0].parameter1, "n")
        self.assertIsInstance(lex_output[0], rtn)