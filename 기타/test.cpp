#include <iostream>

using namespace std;

int main(){
    int N, K, W, V, sumW, sumV;
    sumV = 0;
    sumW = 0;
    int preV = 0;
    int preW = 0;
    cin >> N >> K;
    for(int i = 0; i < N; i++){
        cin >> W >> V;
        if(sumW < W) {
            sumW += W;
            if(preW < sumW){
                preW = sumW;
                sumV += V;
                if(preV < sumV) preV = sumV;
                else sumV = preV;
            }
            else sumW = preW;
        }
    }
    cout << sumV;
    return 0;
}