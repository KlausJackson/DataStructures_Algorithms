#include <iostream>
#include <vector>
#include <bitset>
#include <string>
using namespace std;


class Solution {
public:
	vector <string> readBinaryWatch(int turnedOn){
		vector <string> ans;
		for (int h = 0; h < 12; h++){
			for (int m = 0; m < 60; m++){
				if (bitset<10>(h).count() + bitset<6>(m).count() == turnedOn){
					string time = to_string(h) + ":" + (m < 10 ? "0" : "") + to_string(m);
					ans.push_back(time);
				} 
			}
		}
		return ans;
	}

};


int main(){
	vector <string> ans = Solution().readBinaryWatch(1);
	for (vector <string> :: size_type i = 0; i < ans.size(); i++) {
		cout << ans[i] << endl;
	}	
	return 0;
}


// reason why bitset<10>(h) and bitset<6>(m) :

// maximum value of an 4-bit binary number is 15 so the number of bits required 
// to represent the hours is 10 since the maximum hour value is 12 (0 - 11).

// maximum value of an 6-bit binary number is 63 so the number of bits required 
//to represent the minutes is 6 since the maximum minute value is 60 (0 - 59).	
					
