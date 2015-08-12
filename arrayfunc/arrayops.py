"""
Python Equivalent Operators and Functions
-----------------------------------------

================= ======================
Name               Equivalent to        
================= ======================
af_add             x + y                
af_div             x / y                
af_div_r           y / x                
af_floordiv        x // y               
af_floordiv_r      y // x               
af_mod             x % y                
af_mod_r           y % x                
af_mult            x * y                
af_neg             -x                   
af_pow             x**y                 
af_pow_r           y**x                 
af_sub             x - y                
af_sub_r           y - x                
af_and             x & y                
af_or              x | y                
af_xor             x ^ y                
af_invert          ~x                   
af_eq              x == y               
af_gt              x > y                
af_gte             x >= y               
af_lt              x < y                
af_lte             x <= y               
af_ne              x != y               
af_lshift          x << y               
af_lshift_r        y << x               
af_rshift          x >> y               
af_rshift_r        y >> x               
af_abs             abs(x)               
math_acos          math.acos(x)         
math_acosh         math.acosh(x)        
math_asin          math.asin(x)         
math_asinh         math.asinh(x)        
math_atan          math.atan(x)         
math_atan2         math.atan2(x, y)     
math_atan2_r       math.atan2(y, x)     
math_atanh         math.atanh(x)        
math_ceil          math.ceil(x)         
math_copysign      math.copysign(x, y)  
math_cos           math.cos(x)          
math_cosh          math.cosh(x)         
math_degrees       math.degrees(x)      
math_erf           math.erf(x)          
math_erfc          math.erfc(x)         
math_exp           math.exp(x)          
math_expm1         math.expm1(x)        
math_fabs          math.fabs(x)         
math_factorial     math.factorial(x)    
math_floor         math.floor(x)        
math_fmod          math.fmod(x, y)      
math_fmod_r        math.fmod(y, x)      
math_gamma         math.gamma(x)        
math_hypot         math.hypot(x, y)     
math_hypot_r       math.hypot(y, x)     
math_isinf         math.isinf(x)        
math_isnan         math.isnan(x)        
math_ldexp         math.ldexp(x, y)     
math_lgamma        math.lgamma(x)       
math_log           math.log(x)          
math_log10         math.log10(x)        
math_log1p         math.log1p(x)        
math_pow           math.pow(x, y)       
math_pow_r         math.pow(y, x)       
math_radians       math.radians(x)      
math_sin           math.sin(x)          
math_sinh          math.sinh(x)         
math_sqrt          math.sqrt(x)         
math_tan           math.tan(x)          
math_tanh          math.tanh(x)         
math_trunc         math.truc(x)         
================= ======================

Additional Operators
--------------------

================= ======================
Name               Equivalent to        
================= ======================
aops_subst_gt      x > y                
aops_subst_gte     x >= y               
aops_subst_lt      x < y                
aops_subst_lte     x <= y               
================= ======================
"""

import collections

##############################################################################

aops = collections.namedtuple('aops', [
'af_add', 'af_div', 'af_div_r', 'af_floordiv', 'af_floordiv_r', 
'af_mod', 'af_mod_r', 'af_mult', 'af_neg', 'af_pow', 
'af_pow_r', 'af_sub', 'af_sub_r', 'af_and', 'af_or', 
'af_xor', 'af_invert', 'af_eq', 'af_gt', 'af_gte', 
'af_lt', 'af_lte', 'af_ne', 'af_lshift', 'af_lshift_r', 
'af_rshift', 'af_rshift_r', 'af_abs', 'math_acos', 'math_acosh', 
'math_asin', 'math_asinh', 'math_atan', 'math_atan2', 'math_atan2_r', 
'math_atanh', 'math_ceil', 'math_copysign', 'math_cos', 'math_cosh', 
'math_degrees', 'math_erf', 'math_erfc', 'math_exp', 'math_expm1', 
'math_fabs', 'math_factorial', 'math_floor', 'math_fmod', 'math_fmod_r', 
'math_gamma', 'math_hypot', 'math_hypot_r', 'math_isinf', 'math_isnan', 
'math_ldexp', 'math_lgamma', 'math_log', 'math_log10', 'math_log1p', 
'math_pow', 'math_pow_r', 'math_radians', 'math_sin', 'math_sinh', 
'math_sqrt', 'math_tan', 'math_tanh', 'math_trunc', 'aops_subst_gt', 
'aops_subst_gte', 'aops_subst_lt', 'aops_subst_lte', ])._make([
1, 2, 3, 4, 5, 
6, 7, 8, 9, 10, 
11, 12, 13, 14, 15, 
16, 17, 18, 19, 20, 
21, 22, 23, 24, 25, 
26, 27, 28, 29, 30, 
31, 32, 33, 34, 35, 
36, 37, 38, 39, 40, 
41, 42, 43, 44, 45, 
46, 47, 48, 49, 50, 
51, 52, 53, 54, 55, 
56, 57, 58, 59, 60, 
61, 62, 63, 64, 65, 
66, 67, 68, 69, 70, 
71, 72, 73, ])
