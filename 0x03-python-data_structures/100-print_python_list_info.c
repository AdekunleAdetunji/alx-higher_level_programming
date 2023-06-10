#include <Python.h>

void print_python_list_info(PyObject *p);
/**
 * print_python_list_info - prints formated information about python list
 * object
 * @p: The address of the python list
 * Return: Null
 */
void print_python_list_info(PyObject *p)
{
	const char *name;
	PyObject *list_item;
	Py_ssize_t i, mem_size = ((PyListObject *)p)->allocated;
	Py_ssize_t list_size = PyList_Size(p);

	printf("[*] Size of the Python List = %zd\n", list_size);
	printf("[*] Allocated = %zd\n", mem_size);

	for (i = 0; i < list_size; i++)
	{
		list_item = PyList_GetItem(p, i);
		name = Py_TYPE(list_item)->tp_name;
		printf("Element %zd: %s\n", i, name);
	}
}
