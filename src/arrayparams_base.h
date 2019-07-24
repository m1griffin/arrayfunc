//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayparams_base.c
// Purpose:  Common functions for arrayfunc.
// Language: C
// Date:     28-Nov-2017
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2017    Michael Griffin    <m12.griffin@gmail.com>
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

#include "Python.h"

/*--------------------------------------------------------------------------- */

// The maximum length of dynamically created format strings.
#define FMTSTRLEN 25

/*--------------------------------------------------------------------------- */


// The data arrays. Each element represents a different data type.
union dataarrays {
	uint8_t *buf;
	signed char *b;
	unsigned char *B;
	signed short *h;
	unsigned short *H;
	signed int *i;
	unsigned int *I;
	signed long *l;
	unsigned long *L;
	signed long long *q;
	unsigned long long *Q;
	float *f;
	double *d;
};

// This is used to hold the additional non-array parameters.
struct paramsvals {
	signed char b;
	unsigned char B;
	signed short h;
	unsigned short H;
	signed int i;
	unsigned int I;
	signed long l;
	unsigned long L;
	signed long long q;
	unsigned long long Q;
	float f;
	double d;
};


// The categories that a parameter can fall into.
enum paramtypes
{ 
	paramobj_error,
	paramobj_array,
	paramobj_int,
	paramobj_uint,
	paramobj_float,
};


// This holds both array and numeric (integer or floating point) data values.
// This is used to parse the parameters.
struct paramsdata {
	char arraycode;
	long long llintparam;
	unsigned long long ullintparam;
	double dparam;
	Py_buffer pybuffer;
	union dataarrays array;
	enum paramtypes paramtype;
};

/*--------------------------------------------------------------------------- */

char isfloatarraycode(char arraycode);
char isdoublearraycode(char arraycode);


char lookuparraycode(PyObject *dataobj);
	
char isarrayobjtype(PyObject *dataobj);


Py_ssize_t calcarraylength(char itemcode, Py_ssize_t bufferlength);
Py_ssize_t adjustarraymaxlen(Py_ssize_t arraylength, Py_ssize_t arraymaxlen);
	
void makefmtstr(char *basestr, char *funcname, char *formatstr);


/*--------------------------------------------------------------------------- */

char issignedcharrange(signed long long x);
char issignedshortrange(signed long long x);
char issignedintrange(signed long long x);
char issignedlongrange(signed long long x);

char isunsignedcharrange(unsigned long long x);
char isunsignedshortrange(unsigned long long x);
char isunsignedintrange(unsigned long long x);
char isunsignedlongrange(unsigned long long x);

char isfloatrange(double x);


/*--------------------------------------------------------------------------- */

int get_paramdata(PyObject *dataobj, struct paramsdata *paramobjdata, char *hasbuffer, char *paramoverflow);

char get_numericparams(char arraycode, struct paramsdata *paramobjdata,
			struct paramsvals *checkedvalue, char *paramoverflow);

/*--------------------------------------------------------------------------- */

int get_paramdata_simple(PyObject *dataobj, struct paramsdata *paramobjdata, char *hasbuffer);

char get_numericparams_simple(char arraycode, struct paramsdata *paramobjdata,
			struct paramsvals *checkedvalue);

/*--------------------------------------------------------------------------- */
