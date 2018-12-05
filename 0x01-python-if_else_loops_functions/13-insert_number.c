#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* insert_node - inserts a node into a sorted singly linked list
* @head: a pointer to a pointer to head
* @number: an integer
* Return: the address of the new node or NULL
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nxt_ptr;
	listint_t *prev_ptr;
	listint_t *node;

	if (!head)
		return (NULL);
	nxt_ptr = (*head)->next;
	prev_ptr = *head;

	while (nxt_ptr != NULL && nxt_ptr->n <= number)
	{
		nxt_ptr = nxt_ptr->next;
		prev_ptr = prev_ptr->next;
	}
	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->next = nxt_ptr;
	node->n = number;
	prev_ptr->next = node;

	return (node);
}

