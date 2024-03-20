#include <iostream>
using namespace std;

int n, count = 0, k[10];
bool check[10];

void output(){
	count++;
	cout << count << ". ";
	for (int j = 1; j <= n; j++){
		cout << k[j] << " ";
	}
	cout << "\n";
}

void try_c(int i){
	for (int j = 1; j <= n; j++){
		if (check[j] == false){
			k[i] = j;
			check[j] = true;
			
			if (i == n) output();
			else try_c(i + 1);
			check[j] = false;
		}
	}
}

void try_binary(int i){
	for (int j = 0; j <= 1; j++){
		k[i] = j;
		if (i == n) output();
		else try_binary(i + 1);
	}
}

int main(){

	cout << "n = "; cin >> n;
	for (int i = 1; i <= n; i++){
		check[i] = false;
	}
	
	try_c(1);
	count = 0;
	cout << "\n";
	try_binary(1);
	
	return 0;
}
