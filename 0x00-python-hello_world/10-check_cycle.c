#include "lists.h"
#include <stdio.h>
/**
 * check_add- a function that checks if an address is in an array.
 * @ptr: address to check.
 * @arr: array to check if address is present.
 *
 * Return: 0 if address not present and 1 if present.
*/
int check_add(listint *ptr, unsigned int *arr)
{
	int length = sizeof(arr) / sizeof(int);
	int i;

	for (i = 0; i < length; i++)
	{
		if (arr[i] == ptr)
		{
			return (1);
		}
	}
	return (0);
}
/**
 * check_cycle- a function that checks if a singly linked list has
 * a cycle in it.
 * @list: list to check.
 *
 * Return: 0 if there is no cycle, 1 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *temp;
	unsigned int arr[32];
	int i = 0;

	if (list == null)
	{
		return (0);
	}
	temp = list;
	while (temp != NULL)
	{
		if (check_add(temp, arr) == 0)
		{
			arr[i] = temp;
			i++;
			flag = 1;
		}
		else
		{
			flag = 0;
		}
		temp = temp->next;
	}
	if (flag == 1)
	{
		return (0);
	}
	return (1);
}
