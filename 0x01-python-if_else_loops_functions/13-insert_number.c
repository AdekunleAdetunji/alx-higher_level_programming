#include <stdlib.h>
#include <stddef.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted linked list
 * @head: The address of the head node
 * @number: The number to be inserted in the linked list
 * Return: The address of the node of the new inserted in the list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head, *temp_2 = NULL, *new;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		*head = new;
		new->next = temp;
		return (new);
	}
	while (temp)
	{
		if (temp->n <= number && ((!temp->next) ||
					 (temp->next->n >= number)))
		{
			temp_2 = temp->next;
			temp->next = new;
			new->next = temp_2;
			break;
		}
		temp = temp->next;
	}
	return (new);
}
