#include "main.h"

/**
 * _atoi - converts a string to an integer
 * @C: string to be converted
 *
 * Return: the int converted from the string
 */
int _atoi(char *C)
{
	int H, k, n, x, f, digit;

	H = 0;
	k = 0;
	n = 0;
	x = 0;
	f = 0;
	digit = 0;

	while (C[x] != '\0')
		x++;

	while (f == 0 && H < x)
	{
		if (C[H] == '-')
			++k;

		if (C[H] >= '0' && C[H] <= '9')
		{
			digit = C[H] - '0';
			if (k % 2)
				digit = -digit;
			n = n * 10 + digit;
			f = 1;
			if (C[H + 1] < '0' || C[H + 1] > '9')
				break;
			f = 0;
		}
		H++;
	}

	if (f == 0)
		return (0);

	return (n);
}
