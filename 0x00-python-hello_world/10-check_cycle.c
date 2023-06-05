#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle in it
 * @list: The head node of the linked list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *step_1, *step_2;

	if (!list)
		return (0);

	step_1 = list;
	step_2 = list;

	while(step_2 && step_2->next)
	{
		step_1 = step_1->next;
		step_2 = step_2->next->next;
		if (step_1 == step_2)
			return (1);
	}
	return (0);
}
