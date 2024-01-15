#include "main.h"
/**
 * _strpbrk - Entry point
 *
 * @s: Input
 *
 * @accept: Input
 *
 * Return: Always 0 (Success)
 */
char *_strpbrk(char *s, char *accept)
{
		int c;

		while (*s)
		{
			for (c = 0; accept[c]; c++)
			{
			if (*s == accept[c])
			return (s);
			}
		s++;
		}

	return ('\0');
}
