#include "main.h"
/**
 * _memset - FILL A BLOCk of MEMORY value
 * @s: INPUT address of memory 
 * @b: INPUT OF the value
 * @n: NUM of BYTES to be CHANG
 *
 * Return: CHANGED ARRay value n bytes
 */
char *_memset(char *s, char b, unsigned int n)
{
	int v = 0;


	for (; n > 0; v++)
	{
		s[v] = b;
		n--;
	}
	return (s);
}
