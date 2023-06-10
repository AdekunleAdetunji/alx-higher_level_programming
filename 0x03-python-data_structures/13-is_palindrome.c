#include <stdlib.h>
#include <stddef.h>
#include "lists.h"

/**
 * count - count the number of nodes in a linked list
 * @head: The head node of the linked list
 * Return: An integer value
 */
int count(listint_t *head)
{
	int count = 0;
	listint_t *temp = head;

	while (temp)
	{
		count++;
		temp = temp->next;
	}

	return (count);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: The address of the linked list head node
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	int i, mid_point, node_count, *node_data;
	listint_t *temp;

	if (!head || !(*head))
		return (0);

	node_count = count(*head);

	node_data = malloc(sizeof(int) * node_count);
	if (!node_data)
		return (0);

	temp = *head;
	for (i = 0; i < node_count; i++)
	{
		node_data[i] = temp->n;
		temp = temp->next;
	}

	mid_point = node_count / 2;
	for (i = 0; i < mid_point; i++)
		if (node_data[i] != node_data[node_count - i - 1])
		{
			free(node_data);
			return (0);
		}
	free(node_data);
	return (1);
}
