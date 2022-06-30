#include "lists.h"
#include <stdio.h>
/**
 * check_cycle- a function that checks if a singly linked list has
 * a cycle in it.
 * @list: list to check.
 *
 * Return: 0 if there is no cycle, 1 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	fast = list;
	slow = list;
	while (fast && slow && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
