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
    listint_t *nwn;
    listint_t *x;

    nwn = malloc(sizeof(listint_t));

    if (nwn == NULL)
        return (NULL);

    nwn->n = number;   
    nwn->next = NULL;  

    x = *head;

    if (x == NULL) 
    {
        *head = nwn;
        return (nwn);
    }

    if (x->n >= number) 
    {
        nwn->next = *head;
        *head = nwn;
        return (nwn);
    }

    while (x->next != NULL) 
    {
        if (x->next->n >= number)
        {
            break;
        }
        x = x->next;
    }

    nwn->next = x->next;
    x->next = nwn;
    return (nwn);
 
}