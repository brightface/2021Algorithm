#include <iostream>
#include <vector>
#include <climits>
using namespace std;

vector<int> dataSet;

void Merge(vector<int>& data, int start, int end, int middle)
{

	int temp[1000001];
	int tempIndex = 0;
	int i = start;
	int j = middle + 1;
	while (i <= middle && j <= end)
	{
		if (data[i] < data[j])
			temp[tempIndex++] = data[i++];
		else
			temp[tempIndex++] = data[j++];
	}
	while (i <= middle)
		temp[tempIndex++] = data[i++];
	while (j <= end)
		temp[tempIndex++] = data[j++];
	for (int k = start, tempIndex = 0; k <= end; k++)
		data[k] = temp[tempIndex++];
}
void MergeSort(vector<int>& data, int start, int end)
{
	if (start < end)
	{
		int middle = (start + end) / 2;
		//분해후
		MergeSort(data, start, middle);
		MergeSort(data, middle + 1, end);
		//하나까지 분해된걸 합치네
		Merge(data, start, end, middle);
	}
}

int main()
{
	int n = 0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int tmp;
		cin >> tmp;
		dataSet.push_back(tmp);
	}

	
	MergeSort(dataSet, 0, n-1);
	
	//kmp

	for (int i = 0; i < n; i++) {
		cout << dataSet[i] << endl;
	}

	return 0;
}