double findMean(int a[], int n) 
{ 
    int sum = 0; 
    for (int i = 0; i < n; i++)  
        sum += a[i]; 
      
    return (double)sum/(double)n; 
} 
