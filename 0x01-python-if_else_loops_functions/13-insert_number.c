#include "lists.h"
#include <stdio.h>
/**
 * insert_node- a function that inserts a number into a sorted
 * singly linked list.
 * @head: head of the linked list.
 * @number: number to add.
 *
 * Return: the node.
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *new_node;

	ptr = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;
	if (new_node->n < ptr->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{

		while (ptr != NULL)
		{
			if (ptr->next != NULL)
			{
				if ((ptr->n < number) && ((ptr->next)->n > number))
				{
					new_node->next = ptr->next;
					ptr->next = new_node;
				}
			}
			else if (ptr->next == NULL && ptr->n < new_node->n)
			{
				ptr->next = new_node;
				new_node->next = NULL;
				break;
			}
			ptr = ptr->next;
		}
	}
	return (new_node);
}
