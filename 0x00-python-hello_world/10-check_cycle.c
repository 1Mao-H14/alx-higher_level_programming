#include "lists.h"

/**
 * check_cycle - a function in C that checks if a singly linked list has a cycle in it
 * @list: input the argument of linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *xxx = list;
	listint_t *www = list;

	if (!list)
		return (0);

	while (xxx && www && www->next)
	{
		xxx = xxx->next;
		www = www->next->next;
		if (xxx == www)
			return (1);
	}

	return (0);
}

