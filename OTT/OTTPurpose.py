# -*- coding: utf-8 -*-
"""
Created on Fri May 08 12:08:01 2015

@author: Rob
"""

from databaker.constants import *

def per_file(tabs):
    return ["Table 2", "Table 4"]
    
def per_tab(tab):
    
    anchor = tab.excel_ref("A6")
    req_cols = anchor.fill(RIGHT).is_not_blank()
    req_rows = anchor.fill(DOWN) - tab.filter(contains_string("Latest three months")).expand(DOWN)
    
    obs = req_rows.waffle(req_cols).is_not_blank()
    
    tab.excel_ref("B1").dimension("Type", CLOSEST, ABOVE)
    # req_cols.dimension("SA / NSA", DIRECTLY, ABOVE)
    tab.excel_ref("3:4").is_not_blank().children().dimension("Purpose", DIRECTLY, ABOVE)
    req_rows.is_not_blank().dimension("Year", CLOSEST, ABOVE)
    anchor.shift(RIGHT).fill(DOWN).dimension("Month", DIRECTLY, LEFT)
    
    obs = obs - tab.excel_ref('E1').fill(DOWN) 
        
    yield obs
    