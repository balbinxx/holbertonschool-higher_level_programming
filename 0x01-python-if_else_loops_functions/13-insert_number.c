#include "lists.h"
/**
 * insert_node - function in C that inserts a number into a sorted singly linked
 * list
 * @head: linked list
 * @number: number for being allocated
 * Return: address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *newnode;
    listint_t *cur; /* cursor used to traverse the list */

    newnode = malloc(sizeof(listint_t));

    if (newnode == NULL)
        return (NULL);

    newnode->n = number;   /* put number into newnode */
    newnode->next = NULL;  /*prevent garbage value errors */

    cur = *head;

    if (cur == NULL) /* check for linked list */
    {
        *head = newnode;
        return (newnode);
    }

    if (cur->n >= number) /* adds at the beginning of the list */
    {
        newnode->next = *head;
        *head = newnode;
        return (newnode);
    }

    while (cur->next != NULL) /* walk on list and insert node*/
    {
        if (cur->next->n >= number)
        {
            break;
        }
        cur = cur->next;
    }

    newnode->next = cur->next;
    cur->next = newnode;
    return (newnode);
}