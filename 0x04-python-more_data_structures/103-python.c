#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints information about byte objects
 *
 * @byte_obj: Python byte object
 * Return: No return value
 */
void print_python_bytes(PyObject *byte_obj)
{
    char *byte_string;
    long int byte_size, limit;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(byte_obj))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    byte_size = ((PyVarObject *)(byte_obj))->ob_size;
    byte_string = ((PyBytesObject *)byte_obj)->ob_sval;

    printf("  size: %ld\n", byte_size);
    printf("  trying string: %s\n", byte_string);

    limit = (byte_size >= 10) ? 10 : byte_size + 1;
    printf("  first %ld bytes:", limit);

    for (char *c = byte_string; c < byte_string + limit; c++)
    {
        if (*c >= 0)
            printf(" %02x", *c);
        else
            printf(" %02x", 256 + *c);
    }

    printf("\n");
}

/**
 * print_python_list - Prints information about list objects
 *
 * @list_obj: Python list object
 * Return: No return value
 */
void print_python_list(PyObject *list_obj)
{
    long int list_size;
    PyListObject *list;
    PyObject *list_item;

    list_size = ((PyVarObject *)(list_obj))->ob_size;
    list = (PyListObject *)list_obj;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", list_size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (long int i = 0; i < list_size; i++)
    {
        list_item = ((PyListObject *)list_obj)->ob_item[i];
        printf("Element %ld: %s\n", i, ((list_item)->ob_type)->tp_name);
        if (PyBytes_Check(list_item))
            print_python_bytes(list_item);
    }
}
