#include "main.h"

/**
 * char *_strcpy - a function that copies the string pointed to by src
 *
 * @dst: copy-to
 *
 * @surc: copy-from
 *
 * Return: string
 */
char *_strcpy(char *dst, char *surc)
{
	int h = 0;
	int n = 0;

	while (*(surc + h) != '\0')
	{
		h++;
	}
	for ( ; n < h ; n++)
	{
		dst[n] = surc[n];
	}
	dst[h] = '\0';
	return (dst);
}

