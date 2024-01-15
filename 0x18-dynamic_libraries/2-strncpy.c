#include "main.h"
/**
 * _strncpy - copy a string
 *
 * @dest: Input value
 *
 * @src: Input value
 *
 * @m: Input value
 *
 * Return: dest
 */
char *_strncpy(char *dest, char *src, int m)
{
	int h;

	h = 0;
	while (h < m && src[h] != '\0')
	{
		dest[h] = src[h];
		h++;
	}
	while (h < m)
	{
		dest[h] = '\0';
		h++;
	}

	return (dest);
}
