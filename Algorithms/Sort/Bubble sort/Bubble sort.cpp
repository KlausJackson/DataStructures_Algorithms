#include <iostream>

using namespace std;

void bubble_sort(float list[], int n){
	for (int i = 0; i < n - 1; i++){
		for (int j = 0; j < n - i - 1; j++){
			if (list[j] < list[j + 1]){
				float temp = list[j];
				list[j] = list[j + 1];
				list[j + 1] = temp;
			}
		}
	}
}

int main(){
	
	int n;
	cout << "n = "; cin >> n;
	float list[n];
	
	cout << "List to sort: ";
	for (int i = 0; i < n; i++){
		cin >> list[i];
	}	
	
	bubble_sort(list, n);
	cout << "List after sorting:";
	for (int i = 0; i < n; i++){
		cout << " " << list[i];
	}		
	
}

