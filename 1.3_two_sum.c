#include <stdio.h>

// function that checks if sum of user inputs matches any number in the list of integers
void twoSumChecker(int list[], int length, int x) {
    int found_sum = 0; // found_sum will be "1" once there is a match in numbers
    // int sum_num = x + y; // finds the sum of user's two inputs

    for (int i = 0; i < length-1; i++) {
        if (found_sum == 1)
        {
            break;
        }
        for (int j = 1; j < length; j++) {
        int sum = list[i] + list[j];
            if (x == sum)
            {
                // prints that the numbers were matched and sets found_sum = 1 and exits the loop
                printf("There are two numbers in the list summing to the keyed-in number %d",x);
                found_sum = 1;
                break;
            }
        }
    }
    
    // if found_sum == 0, it means that no numbers were matched
    if (!found_sum)
    {
        printf("There are not two numbers in the list summing to the keyed-in number %d", x);
    }

}

int main() 
{
    int list[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};  // A list of integer numbers

    // calculates the length of given list and assigns to list_length
    int list_length = sizeof(list) / sizeof(list[0]);
    int num1, num2;
    
    // prompt user to input first and second numbers
    printf("Enter a number: ");
    scanf("%d", &num1);

    // calls the twoSumChecker function
    twoSumChecker(list, list_length, num1);
    return 0;
}