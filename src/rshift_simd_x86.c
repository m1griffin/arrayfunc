//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   rshift_simd_x86.c
// Purpose:  Calculate the rshift of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     12-Mar-2019
// Ver:      06-Sep-2021.
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2021    Michael Griffin    <m12.griffin@gmail.com>
//
//   Licensed under the Apache License, Version 2.0 (the "License");
//   you may not use this file except in compliance with the License.
//   You may obtain a copy of the License at
//
//       http://www.apache.org/licenses/LICENSE-2.0
//
//   Unless required by applicable law or agreed to in writing, software
//   distributed under the License is distributed on an "AS IS" BASIS,
//   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//   See the License for the specific language governing permissions and
//   limitations under the License.
//
//------------------------------------------------------------------------------

/*--------------------------------------------------------------------------- */
// This must be defined before "Python.h" in order for the pointers in the
// argument parsing functions to work properly. 
#define PY_SSIZE_T_CLEAN

#include "Python.h"

#include "simddefs.h"

#include "arrayerrs.h"

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

// Auto generated code goes below.

// Function specific macros and other definitions.
#include "rshift_defs.h"

/*--------------------------------------------------------------------------- */
/* Initialise an SIMD vector with a specified value.
   initval = The value to initialise the vector to.
   Returns the initalised SIMD vector. 
*/
#if defined(AF_HASSIMD_X86)
v16qi initvec_signed_char(signed char initval) {

	unsigned int y;
	signed char initvals[CHARSIMDSIZE];
	v16qi simdvec;

	for (y = 0; y < CHARSIMDSIZE; y++) {
		initvals[y] = initval;
	}
	simdvec = (v16qi) __builtin_ia32_lddqu((char *) (initvals));

	return simdvec;
}
#endif



/*--------------------------------------------------------------------------- */
/* Initialise an SIMD vector with a specified value.
   initval = The value to initialise the vector to.
   Returns the initalised SIMD vector. 
*/
#if defined(AF_HASSIMD_X86)
v16qi initvec_unsigned_char(unsigned char initval) {

	unsigned int y;
	unsigned char initvals[CHARSIMDSIZE];
	v16qi simdvec;

	for (y = 0; y < CHARSIMDSIZE; y++) {
		initvals[y] = initval;
	}
	simdvec = (v16qi) __builtin_ia32_lddqu((char *) (initvals));

	return simdvec;
}
#endif



/*--------------------------------------------------------------------------- */
/* Initialise an SIMD vector with a specified value.
   initval = The value to initialise the vector to.
   Returns the initalised SIMD vector. 
*/
#if defined(AF_HASSIMD_X86)
v8hi initvec_unsigned_short(unsigned short initval) {

	unsigned int y;
	unsigned short initvals[SHORTSIMDSIZE];
	v8hi simdvec;

	for (y = 0; y < SHORTSIMDSIZE; y++) {
		initvals[y] = initval;
	}
	simdvec = (v8hi) __builtin_ia32_lddqu((char *) (initvals));

	return simdvec;
}
#endif



/*--------------------------------------------------------------------------- */
/* Initialise an SIMD vector with a specified value.
   initval = The value to initialise the vector to.
   Returns the initalised SIMD vector. 
*/
#if defined(AF_HASSIMD_X86)
v4si initvec_signed_int(signed int initval) {

	unsigned int y;
	signed int initvals[INTSIMDSIZE];
	v4si simdvec;

	for (y = 0; y < INTSIMDSIZE; y++) {
		initvals[y] = initval;
	}
	simdvec = (v4si) __builtin_ia32_lddqu((char *) (initvals));

	return simdvec;
}
#endif



/*--------------------------------------------------------------------------- */
/* Initialise an SIMD vector with a specified value.
   initval = The value to initialise the vector to.
   Returns the initalised SIMD vector. 
*/
#if defined(AF_HASSIMD_X86)
v4si initvec_unsigned_int(unsigned int initval) {

	unsigned int y;
	unsigned int initvals[INTSIMDSIZE];
	v4si simdvec;

	for (y = 0; y < INTSIMDSIZE; y++) {
		initvals[y] = initval;
	}
	simdvec = (v4si) __builtin_ia32_lddqu((char *) (initvals));

	return simdvec;
}
#endif



/*--------------------------------------------------------------------------- */
// Right shifts in Python are arithmetic shifts, not logical shifts. An 
// arithmetic right shift will shift in either '0' or '1' bits for the new high
// bits depending on whether the existing sign bit was a 0 or 1. Because x86 
// SIMD doesn't offer arithmetic shifts for all array types, we must simulate
// it using logical shifts of a larger size and then use and operations to 
// insert the appropriate bits at the right places.
//
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_X86)
void rshift_signed_char_1_simd(Py_ssize_t arraylen, signed char *data1, signed char param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	// The mask and shift operations are done using a different data
	// type than the parameters passed to the function. We always use
	// the largest x86 shift operation available, which is unsigned int
	v4si datasliceleft, vmaskslice;
	v16qi vbinmaskslice, vcheckslice, varithmask;


	// Used to initialise the masks to sort out which bytes have their high bits set.
	v16qi vhighbitmask = {0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 
							0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80};
	v16qi vbinmaskzero = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	

	// This mask gets rid of the bits which would otherwise get shifted
	// into the adjoining vector element.
	unsigned int maskvals[] = {0xffffffff, 0xfefefefe, 0xfcfcfcfc, 0xf8f8f8f8, 0xf0f0f0f0, 0xe0e0e0e0, 0xc0c0c0c0, 0x80808080};
	unsigned int selectedmask;
	int shiftlimit, shiftlimit2;

	// For the turning the logical shift into an arithmetic shift.
	unsigned char binmasks[] = {0x00, 0x80, 0xc0, 0xe0, 0xf0, 0xf8, 0xfc, 0xfe, 0xff};
	unsigned char selectedbinmask;


	// Select the mask value based on how many positions we are required
	// to shift. This is limited to the number of masks defined.
	shiftlimit = (sizeof(param) * 8) - 1;
	if ((param > shiftlimit) || (param < 0)) {
		selectedmask = 0;
	} else {
		selectedmask = maskvals[param];
	}

	// Initialise the mask values. This mask is  used to slice off the bits
	// that would otherwise overflow into adjacent bytes, as we are using an
	// SIMD instruction meant for a larger word size.
	// We are doing this using an unsigned int because we do unsigned int SIMD.
	vmaskslice = initvec_unsigned_int(selectedmask);


	// Binmask for sign bits.
	if (param <= 0) {
		selectedbinmask = 0;
	} else {
		shiftlimit2 = (sizeof(param) * 8);
		if (param > shiftlimit2) {
			selectedbinmask = binmasks[shiftlimit2];
		} else {
			selectedbinmask = binmasks[param];
		}
	}

	// Initialise the binmask values. This mask is used to emulate the effect of
	// arithmetic right shift when the sign bit is set. When the high bit is
	// set we need to add in more '1' bits where they would have been shift in. 
	vbinmaskslice = initvec_unsigned_char(selectedbinmask);



	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *) &data1[index]);

		// This one is used to see if the high bit is set in each byte.
		vcheckslice = (v16qi) __builtin_ia32_pand128( (v2di) datasliceleft, (v2di) vhighbitmask);
		// Now pick either the mask or zero for each byte.
		varithmask = (v16qi) __builtin_ia32_pblendvb128(vbinmaskzero, vbinmaskslice, vcheckslice);

		
		// Mask off the bits that would otherwise overflow into the adjacent byte.
		datasliceleft = (v4si) __builtin_ia32_pand128( (v2di) datasliceleft,  (v2di) vmaskslice);

		// The actual SIMD operation. This should always be the lshift or rshift
		// operation for unsigned integer.
		datasliceleft = __builtin_ia32_psrldi128(datasliceleft, (int) param);

		// Now OR the result with the arithmetic mask to put the shift sign bits
		// back in.
		datasliceleft = (v4si)  __builtin_ia32_por128( (v2di) datasliceleft,  (v2di) varithmask);

		// Store the result.
		__builtin_ia32_storedqu((char *) &data1[index], (v16qi) datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] >> param;
	}

}



// param_arr_num_arr
void rshift_signed_char_2_simd(Py_ssize_t arraylen, signed char *data1, signed char param, signed char *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	// The mask and shift operations are done using a different data
	// type than the parameters passed to the function. We always use
	// the largest x86 shift operation available, which is unsigned int
	v4si datasliceleft, vmaskslice;
	v16qi vbinmaskslice, vcheckslice, varithmask;


	// Used to initialise the masks to sort out which bytes have their high bits set.
	v16qi vhighbitmask = {0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 
							0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80};
	v16qi vbinmaskzero = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	

	// This mask gets rid of the bits which would otherwise get shifted
	// into the adjoining vector element.
	unsigned int maskvals[] = {0xffffffff, 0xfefefefe, 0xfcfcfcfc, 0xf8f8f8f8, 0xf0f0f0f0, 0xe0e0e0e0, 0xc0c0c0c0, 0x80808080};
	unsigned int selectedmask;
	int shiftlimit, shiftlimit2;

	// For the turning the logical shift into an arithmetic shift.
	unsigned char binmasks[] = {0x00, 0x80, 0xc0, 0xe0, 0xf0, 0xf8, 0xfc, 0xfe, 0xff};
	unsigned char selectedbinmask;


	// Select the mask value based on how many positions we are required
	// to shift. This is limited to the number of masks defined.
	shiftlimit = (sizeof(param) * 8) - 1;
	if ((param > shiftlimit) || (param < 0)) {
		selectedmask = 0;
	} else {
		selectedmask = maskvals[param];
	}

	// Initialise the mask values. This mask is  used to slice off the bits
	// that would otherwise overflow into adjacent bytes, as we are using an
	// SIMD instruction meant for a larger word size.
	// We are doing this using an unsigned int because we do unsigned int SIMD.
	vmaskslice = initvec_unsigned_int(selectedmask);


	// Binmask for sign bits.
	if (param <= 0) {
		selectedbinmask = 0;
	} else {
		shiftlimit2 = (sizeof(param) * 8);
		if (param > shiftlimit2) {
			selectedbinmask = binmasks[shiftlimit2];
		} else {
			selectedbinmask = binmasks[param];
		}
	}

	// Initialise the binmask values. This mask is used to emulate the effect of
	// arithmetic right shift when the sign bit is set. When the high bit is
	// set we need to add in more '1' bits where they would have been shift in. 
	vbinmaskslice = initvec_unsigned_char(selectedbinmask);



	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *) &data1[index]);

		// This one is used to see if the high bit is set in each byte.
		vcheckslice = (v16qi) __builtin_ia32_pand128( (v2di) datasliceleft, (v2di) vhighbitmask);
		// Now pick either the mask or zero for each byte.
		varithmask = (v16qi) __builtin_ia32_pblendvb128(vbinmaskzero, vbinmaskslice, vcheckslice);

		
		// Mask off the bits that would otherwise overflow into the adjacent byte.
		datasliceleft = (v4si) __builtin_ia32_pand128( (v2di) datasliceleft,  (v2di) vmaskslice);

		// The actual SIMD operation. This should always be the lshift or rshift
		// operation for unsigned integer.
		datasliceleft = __builtin_ia32_psrldi128(datasliceleft, (int) param);

		// Now OR the result with the arithmetic mask to put the shift sign bits
		// back in.
		datasliceleft = (v4si)  __builtin_ia32_por128( (v2di) datasliceleft,  (v2di) varithmask);

		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[index], (v16qi) datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] >> param;
	}

}
#endif


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_X86)
void rshift_unsigned_char_1_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	// The mask and shift operations are done using a different data
	// type than the parameters passed to the function. We always use
	// the largest x86 shift operation available, which is unsigned int
	v4si datasliceleft, vmaskslice;

	// This mask gets rid of the bits which would otherwise get shifted
	// into the adjoining vector element.
	unsigned int maskvals[] = {0xffffffff, 0xfefefefe, 0xfcfcfcfc, 0xf8f8f8f8, 0xf0f0f0f0, 0xe0e0e0e0, 0xc0c0c0c0, 0x80808080};
	unsigned int compvals[INTSIMDSIZE];
	unsigned int selectedmask;
	unsigned int y;
	unsigned char shiftlimit;

	// Select the mask value based on how many positions we are required
	// to shift. This is limited to the number of masks defined.
	shiftlimit = (sizeof(param) * 8) - 1;
	if ((param > shiftlimit) || (param < 0)) {
		selectedmask = 0;
	} else {
		selectedmask = maskvals[param];
	}
	
	// Initialise the mask values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = selectedmask;
	}
	vmaskslice = (v4si) __builtin_ia32_lddqu((char *) compvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *) &data1[index]);

		// Mask off the bits that would otherwise overflow into the adjacent byte.
		datasliceleft = (v4si) __builtin_ia32_pand128( (v2di) datasliceleft,  (v2di) vmaskslice);

		// The actual SIMD operation. This should always be the lshift or rshift
		// operation for unsigned integer.
		datasliceleft = __builtin_ia32_psrldi128(datasliceleft, (int) param);

		// Store the result.
		__builtin_ia32_storedqu((char *) &data1[index], (v16qi) datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] >> param;
	}

}



// param_arr_num_arr
void rshift_unsigned_char_2_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char param, unsigned char *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	// The mask and shift operations are done using a different data
	// type than the parameters passed to the function. We always use
	// the largest x86 shift operation available, which is unsigned int
	v4si datasliceleft, vmaskslice;

	// This mask gets rid of the bits which would otherwise get shifted
	// into the adjoining vector element.
	unsigned int maskvals[] = {0xffffffff, 0xfefefefe, 0xfcfcfcfc, 0xf8f8f8f8, 0xf0f0f0f0, 0xe0e0e0e0, 0xc0c0c0c0, 0x80808080};
	unsigned int compvals[INTSIMDSIZE];
	unsigned int selectedmask, y;
	int shiftlimit;

	// Select the mask value based on how many positions we are required
	// to shift. This is limited to the number of masks defined.
	shiftlimit = (sizeof(param) * 8) - 1;
	if ((param > shiftlimit) || (param < 0)) {
		selectedmask = 0;
	} else {
		selectedmask = maskvals[param];
	}
	
	// Initialise the mask values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = selectedmask;
	}
	vmaskslice = (v4si) __builtin_ia32_lddqu((char *) compvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *) &data1[index]);

		// Mask off the bits that would otherwise overflow into the adjacent byte.
		datasliceleft = (v4si) __builtin_ia32_pand128( (v2di) datasliceleft,  (v2di) vmaskslice);

		// The actual SIMD operation. This should always be the lshift or rshift
		// operation for unsigned integer.
		datasliceleft = __builtin_ia32_psrldi128(datasliceleft, (int) param);

		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[index], (v16qi) datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] >> param;
	}

}
#endif



/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_X86)
void rshift_unsigned_short_1_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v8hi datasliceleft;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *) &data1[index]);
		// The actual SIMD operation. 
		datasliceleft = __builtin_ia32_psrlwi128(datasliceleft, (int) param);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data1[index], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] >> param;
	}

}



// param_arr_num_arr
void rshift_unsigned_short_2_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short param, unsigned short *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v8hi datasliceleft;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *) &data1[index]);
		// The actual SIMD operation. 
		datasliceleft = __builtin_ia32_psrlwi128(datasliceleft, (int) param);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[index], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] >> param;
	}

}
#endif



/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_X86)
void rshift_signed_int_1_simd(Py_ssize_t arraylen, signed int *data1, signed int param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4si datasliceleft;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *) &data1[index]);
		// The actual SIMD operation. 
		datasliceleft = __builtin_ia32_psradi128(datasliceleft, (int) param);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data1[index], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] >> param;
	}

}



// param_arr_num_arr
void rshift_signed_int_2_simd(Py_ssize_t arraylen, signed int *data1, signed int param, signed int *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4si datasliceleft;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *) &data1[index]);
		// The actual SIMD operation. 
		datasliceleft = __builtin_ia32_psradi128(datasliceleft, (int) param);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[index], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] >> param;
	}

}
#endif



/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_X86)
void rshift_unsigned_int_1_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4si datasliceleft;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *) &data1[index]);
		// The actual SIMD operation. 
		datasliceleft = __builtin_ia32_psrldi128(datasliceleft, (int) param);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data1[index], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] >> param;
	}

}



// param_arr_num_arr
void rshift_unsigned_int_2_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int param, unsigned int *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4si datasliceleft;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *) &data1[index]);
		// The actual SIMD operation. 
		datasliceleft = __builtin_ia32_psrldi128(datasliceleft, (int) param);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[index], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] >> param;
	}

}
#endif


