#include "main.h"
/**
 * _strcat - the2 strings
 *
 * @dest: Input value
 * @src: Input value
 *
 * Return: void
 */
char *_strcat(char *dest, char *src)
{

	int h;
	int K;

	h = 0;
	while (dest[h] != '\0')
	{
		h++;
	}
	K = 0;
	while (src[K] != '\0')
	{
		dest[h] = src[K];
		h++;
		K++;
	}

	dest[h] = '\0';
	return (dest);
}

