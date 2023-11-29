#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - function that inserts a
 * number into a sorted singly linked list
 * @head: array of numbers
 * @number: integer
 * Return: void
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *a, *b = *head;
if (head == NULL)
{
return (NULL);
}
a = malloc(sizeof(listint_t));
if (a == NULL)
{
return (NULL);
}
a->n = number;
if (*head == NULL || number < (*head)->n)
{
a->next = *head;
*head = a;
return (a);
}
while (b != NULL && b->next->n < number)
{
b = b->next;
}
a->next = b->next;
b->next = a;
return (a);
}
