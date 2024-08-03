#include "Python.h"

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
    long int str_length;
    const char *str_value;
    PyObject *str_repr;

    fflush(stdout);

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p) && !PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    if (PyUnicode_Check(p))  // Handle Unicode strings
    {
        str_length = PyUnicode_GetLength(p);
        str_repr = PyUnicode_AsEncodedString(p, "utf-8", "strict");
        str_value = PyBytes_AsString(str_repr);

        if (PyUnicode_IS_COMPACT_ASCII(p))
            printf("  type: compact ascii\n");
        else
            printf("  type: compact unicode object\n");

        printf("  length: %ld\n", str_length);
        printf("  value: %s\n", str_value);

        Py_XDECREF(str_repr);  // Decrease reference count and clean up
    }
    else if (PyBytes_Check(p))  // Handle ASCII strings
    {
        str_length = PyBytes_Size(p);
        str_value = PyBytes_AsString(p);

        printf("  type: compact ascii\n");
        printf("  length: %ld\n", str_length);
        printf("  value: %s\n", str_value);
    }
}
