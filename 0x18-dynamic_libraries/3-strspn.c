#include "main.h"
/**
 * _strspn - Entry point
 *
 * @s: input
 *
 * @accept: input
 *
 * Return: Always 0 (Success)
 */
unsigned int _strspn(char *s, char *accept)
{
	unsigned int h = 0;
	int x;

	while (*s)
	{
		for (x = 0; accept[x]; x++)
		{
			if (*s == accept[x])
			{
				h++;
				break;
			}
			else if (accept[x + 1] == '\0')
				return (h);
		}
		s++;
	}
	return (h);
}
