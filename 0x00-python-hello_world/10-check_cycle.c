#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* check_cycle - checks if a linked list has a cycle
* @list: the linked list
* Return: true or false
*/

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (!list || !list->next)
		return (0);


	fast = list->next;
	slow = list;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
			return (1);
	}

	return (0);
}
