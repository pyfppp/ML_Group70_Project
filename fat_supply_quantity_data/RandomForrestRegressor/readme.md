# pictures' meanings
1. forrest_poly.png  
Using default K in KFold as metrics to find the best poly degree.  
conclusion: when poly =2 then error is the smallest and the score is the biggest,  
so we choose 2 as the best polynomial features' degree
2. forrest_k.png
Now using default poly degree to search the best K in KFold  
conclusion: When k=6 the error reached the lowest, but when k=10, the score comes to near 0.9,  
which is a significant improvement, so we choose 10 as the best K