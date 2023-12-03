#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - function that checks if a singly
 * linked list is a palindrome
 * @head: array of palindrome
 * Return: void
 */

int is_palindrome(listint_t **head)
{
int a = 1;
listint_t *b = *head, *c = *head;
listint_t *x, *y = *head;
if (*head != NULL && (*head) != NULL)
{
while (b != NULL && b->next != NULL)
{
b = b->next->next;
y = c;
c = c->next;
}
x = rev(c);
while (*head != NULL && x != NULL)
{
if ((*head)->n != x->n)
{
a = 0;
break;
}
*head = (*head)->next;
x = x->next;
}
rev(y->next);
}
return (a);
}
/**
 * rev - function that reveres the list
 * @head: list
 * Return: void
 */
listint_t *rev(listint_t *head)
{
listint_t *a = NULL, *b = NULL;
listint_t *x = head;
while (x != NULL)
{
b = x->next;
x->next = a;
a = x;
x = b;
}
return (a);
}
