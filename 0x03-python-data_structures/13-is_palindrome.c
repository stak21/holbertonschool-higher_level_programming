#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_actual_palin(listint_t **head, listint_t *next);
/**
* is_palindrome - checks if a linked list is a palindrome
* @head: a pointer to a pointer to a linked list
* Return: return 1 if it is a palindrome
*/

int is_palindrome(listint_t **head)
{
	listint_t *next;

	if (head == NULL)
		return (0);
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	next = *head;
	return (is_actual_palin(head, next->next));
}

/**
* is_actual_palin - helper function to check if a linked list is a palin
* @head: a pointer to a pointer to a linked list
* @next: a pointer to a linked list
* Return: true if the values are equal
*/

int is_actual_palin(listint_t **head, listint_t *next)
{
	if (next->next != NULL)
		is_actual_palin(head, next->next);
	if ((*head)->n == next->n)
	{
		*head = (*head)->next;
		return (1);
	}
	else
		return (0);
}
