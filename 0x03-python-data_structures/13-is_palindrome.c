#include "lists.h"

/**
* is_palindrome - A function that checks if a singly linked list is
* a palindrome
* @head: head of the list
* Return: 0 or 1
*/

int is_palindrome(listint_t **head)
{
	listint_t *temp, *temp2;
	unsigned int  length = 0, cLen = 0;
	unsigned int i, listLen;

	temp = temp2 = NULL;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	temp = *head;
	length = list_lenght(temp);
	cLen = length * 2;
	listLen = cLen - 2;
	temp2 = *head;

	for (i = 0; i < cLen; i += 2)
	{
		if (temp[i].n != temp2[listLen].n)
			return (0);
		listLen -= 2;
	}
	return (1);
}

/**
* get_node - function to get a node from an index in a linked list
* @head: head of the list
* @index: index to find in the list
* Return: The specific node of the linked list
*/

listint_t *get_node(listint_t *head, unsigned int index)
{
	listint_t *temp = head;
	unsigned int i = 0;

	if (head != NULL)
	{
		while (temp)
		{
			if (i == index)
				return (temp);

			temp = temp->next;
			i += 1;
		}
	}

	return (NULL);
}

/**
* list_lenght - gets the number of elements in a linked list
* @head: head of the list to count
* Return: Number of elements in the list
*/

size_t list_lenght(const listint_t *head)
{
	int len = 0;

	for (len = 0; head != NULL; ++len)
	{
		head = head->next;
	}

	return (len);
}
