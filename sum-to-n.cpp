#include <iostream>

using namespace std;

int sum_to_n(int n){
    int sum = 0;
    for (int i=0;i<=n;i++){
        sum+=i;
    }
    return sum;
}

int main()
{
    int n;
    scanf("%d",&n);
    int sum = sum_to_n(n);
    printf("%d\n",sum);
    return 0;
}
