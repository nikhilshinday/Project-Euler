// #include <iostream>
// using namespace std;

// void print_arr(int array[], int len)
// {
//         for (int i = 0; i < len; i++) {
//                 cout << array[i];
//         }
// }

// void next_permutation(int array[], int len)
// {
//         int k = -1;
//         int l = -1;

//         for (int i = 0; i < len-1; i++) {
//                 if (array[i] < array[i+1]) {
//                         k = i;
//                 }
//         }
        
//         for (int i = k+1; i < len; i++) {
//                 if (array[k] < array[i]) {
//                         l = i;
//                 }
//         }
        
//         array[k] ^= array[l];
//         array[l] ^= array[k];
//         array[k] ^= array[l];

//         for (int i = k+1; i < (k/2)+k+1; i++) {
//                 array[i] ^= array
//         }
// }

// int main()
// {
//         // int array[] = {1,2,3,4}; 
//         // next_permutation(array, sizeof(array)/sizeof(*array));
//         // print_arr(array, sizeof(array)/sizeof(*array));
//         // return 0;
//         cout << 5/2 << endl;
// }

// Program to print all permutations of a string in sorted order.
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string.h>

using namespace std;
 
/* Following function is needed for library function qsort(). Refer
   http://www.cplusplus.com/reference/clibrary/cstdlib/qsort/ */
int compare (const void *a, const void * b)
{  return ( *(char *)a - *(char *)b ); }
 
// A utility function two swap two characters a and b
void swap (char* a, char* b)
{
    char t = *a;
    *a = *b;
    *b = t;
}
 
// This function finds the index of the smallest character
// which is greater than 'first' and is present in str[l..h]
int findCeil (char str[], char first, int l, int h)
{
    // initialize index of ceiling element
    int ceilIndex = l;
 
    // Now iterate through rest of the elements and find
    // the smallest character greater than 'first'
    for (int i = l+1; i <= h; i++)
      if (str[i] > first && str[i] < str[ceilIndex])
            ceilIndex = i;
 
    return ceilIndex;
}
 
// Print all permutations of str in sorted order
void sortedPermutations ( char str[] )
{
    // Get size of string
    int size = strlen(str);
 
    // Sort the string in increasing order
    qsort( str, size, sizeof( str[0] ), compare );
 
    // Print permutations one by one
    bool isFinished = false;
    int counter = 0;
    while ( ! isFinished and counter != 1000000)
    {
        // print this permutation
        printf ("%s \n", str);
 
        // Find the rightmost character which is smaller than its next
        // character. Let us call it 'first char'
        int i;
        for ( i = size - 2; i >= 0; --i )
           if (str[i] < str[i+1])
              break;
 
        // If there is no such chracter, all are sorted in decreasing order,
        // means we just printed the last permutation and we are done.
        if ( i == -1 )
            isFinished = true;
        else
        {
            // Find the ceiling of 'first char' in right of first character.
            // Ceil of a character is the smallest character greater than it
            int ceilIndex = findCeil( str, str[i], i + 1, size - 1 );
 
            // Swap first and second characters
            swap( &str[i], &str[ceilIndex] );
 
            // Sort the string on right of 'first char'
            qsort( str + i + 1, size - i - 1, sizeof(str[0]), compare );
        }
        counter++;
        cout << counter << endl;
    }
}
 
// Driver program to test above function
int main()
{
    char str[] = "0123456789";
    sortedPermutations( str );
    return 0;
}