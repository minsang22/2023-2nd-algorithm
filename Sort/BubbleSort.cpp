#include <stdio.h>
#include <iostream>
using namespace std;
#define MAX_SIZE 1000

void swap(int *a, int *b){
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void bubbleSort(int a[], int n){
    int comp_cnt = 0; 
    int swap_cnt = 0;  
    for (int pass = 1; pass < n; pass++){
        for (int i = 1; i <= n - pass; i++){
            comp_cnt++;
            if (a[i - 1] > a[i]){
                swap(&a[i - 1], &a[i]);
                swap_cnt++;
            }
        }
    }
    cout << comp_cnt << " " << swap_cnt << " " ;
}

void bubbleSortImproved1(int a[], int n){
    int comp_cnt = 0; 
    int swap_cnt = 0;  

    for (int pass = 1; pass < n; pass++){
        bool swapped = false;
        for (int i = 1; i <= n - pass; i++){
            comp_cnt++;
            if (a[i - 1] > a[i]){
                swap(&a[i - 1], &a[i]);
                swap_cnt++;
                swapped = true;
            }
        }
        if (swapped == false){
            break;
        }
    }

    cout << comp_cnt << " " << swap_cnt << " " ;
}

void bubbleSortImproved2(int a[], int n){
    int comp_cnt = 0;
    int swap_cnt = 0;  
    int lastSwaapedPos = n;

    while (lastSwaapedPos > 0){
        int swappedPost = 0;
        for (int i = 1; i < lastSwaapedPos; i++){
            comp_cnt++;
            if (a[i - 1] > a[i]){
                swap(&a[i - 1], &a[i]);
                swap_cnt++;
                swappedPost = i;
            }
        }
        lastSwaapedPos = swappedPost;
    }
    cout << comp_cnt << " " << swap_cnt << endl ;
}

void copyArray(int a[], int b[], int n){
    for (int i = 0; i < n; i++)
        a[i] = b[i];
}

int main(){
    int numTestCases;
    int a[MAX_SIZE], b[MAX_SIZE];
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i)
    {
        int num;
        scanf("%d", &num);
        for (int j = 0; j < num; j++)
            scanf("%d", &b[j]);
        copyArray(a, b, num);
        bubbleSort(a, num);
        copyArray(a, b, num);
        bubbleSortImproved1(a, num);
        copyArray(a, b, num);
        bubbleSortImproved2(a, num);
    }
    return 0;
}