#include <iostream>
#include <vector>
using namespace std;

void Merge(vector<int>& data, int* sortedTemp, int start, int end, int middle)
{
	int tempIndex = 0;
	int i = start;
	int j = middle + 1;
	while (i <= middle && j <= end)
	{
		if (data[i] < data[j])
			sortedTemp[tempIndex++] = data[i++];
		else
			sortedTemp[tempIndex++] = data[j++];
	}
	while (i <= middle)
		sortedTemp[tempIndex++] = data[i++];
	while (j <= end)
		sortedTemp[tempIndex++] = data[j++];
	for (int k = start, tempIndex = 0; k <= end; k++)
		data[k] = sortedTemp[tempIndex++];
}
void MergeSort(vector<int>& data, int* sortedTemp, int start, int end)
{
	if (start < end)
	{
		int middle = (start + end) / 2;
		//분해후
		MergeSort(data, sortedTemp, start, middle);
		MergeSort(data, sortedTemp, middle + 1, end);
		//하나까지 분해된걸 합치네
		Merge(data, sortedTemp, start, end, middle);
	}
}

int main()
{
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	int n = 0;
	cin >> n;
	vector<int> arr;
	for (int i = 0; i < n; i++) {
		int tmp;
		cin >> tmp;
		arr.push_back(tmp);
	}
	
	int* sortedTemp = new int[n];
	MergeSort(arr, sortedTemp, 0, n - 1);

	for (int i = 0; i < n; i++) {
		cout << arr[i] << endl;
	}

	return 0;
}