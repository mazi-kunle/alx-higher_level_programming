#include "lists.h"
#include <stddef.h>

/**
 * reverse_list- a function that reverses a linked list.
 * @head: head of the linked list.
 *
*/

void reverse_list(listint_t **head)
{
	listint_t *prev, *curr, *next;

	if (*head != NULL)
	{
		prev = NULL;
		next = NULL;
		curr = *head;
		while (curr != NULL)
		{
			next = curr->next;
			curr->next = prev;
			prev = curr;
			curr = next;
		}
		*head = prev;
	}
}

/**
 * is_palindrome- a function that checks if a singly linked list is a
 * palindrome.
 * @head: head of the linked list.
 *
 * Return: int.
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev;
	listint_t *second_half;

	slow = *head;
	fast = *head;
	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev = slow;
			slow = slow->next;
		}
		if (fast != NULL)
		{
			slow = slow->next;
		}
		second_half = slow;
		prev->next = NULL;
		reverse_list(&second_half);
		while (*head != NULL && second_half != NULL)
		{
			if ((*head)->n != second_half->n)
			{
				return (0);
			}
			*head = (*head)->next;
			second_half = second_half->next;
		}
	}
	return (1);
}
