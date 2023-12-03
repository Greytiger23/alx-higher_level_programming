#include <python.h>

/**
 * print_python_list_info - function that prints
 * some basic info about Python lists
 * @p: object
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
Py_ssize_t a, b;
PyObject *x;
if (!PyList_Check(p))
{
printf("Errror: not python list\n");
return;
}
a = PyList_Size(p);
printf("[*] Size of the Python List = %ld\n", a);
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
for (y = 0; y < a; y++)
{
x = PyList_GetItem(p, y);
printf("Element %ld: %s\n", y, Py_TYPE(x)->tp_name);
}
}
