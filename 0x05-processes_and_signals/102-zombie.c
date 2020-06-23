#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>


/**
 * infinite_while - infinite Loop
 * Return: 0 Success or 1 Error
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - function main
 * Return: 0 Success or 1 Error
 *
 */

int main(void)
{
	int p = 5;
	pid_t child_pid;

	while (p--)
	{
		child_pid = fork();
		if (child_pid > 0)
			printf("Zombie process created, PID: %i\n", child_pid);
		else
			exit(0);
	}
	infinite_while();

	return (0);
}
