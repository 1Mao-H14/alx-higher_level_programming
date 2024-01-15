#include "main.h"
/**
 * _strcmp - compare string values
 * @s1: input value+
 * @s2: input value+
 *
 * Return: s1[i] - s2[i]
 */
int _strcmp(char *s1, char *s2)
{
	int H;

	H = 0;
	while (s1[H] != '\0' && s2[H] != '\0')
	{
		if (s1[H] != s2[H])
		{
			return (s1[H] - s2[H]);
		}
		H++;
	}
	return (0);
}

