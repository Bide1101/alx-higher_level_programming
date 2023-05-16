#include "lists.h"

/**
* print_python_list_info - a C function that prints some basic
* info about Python lists.
* @p: pointer
* Return: void
*/

void print_python_list_info(PyObject *p)
{
	int size, a, i = 0;
	PyObject *item;
	PyListObject *list_obj = (PyListObject *)p;

	size = Py_SIZE(p);
	a = list_obj->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", a);

	for (; i < size; i++)
	{
		item =  PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
