#include <stdlib.h>
#include <stdio.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    *returnSize = 2;
    int* ret = (int*) malloc(sizeof(int) * 2);
    for (int i = 0; i < numsSize; i++) {
        for (int j = i+1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                ret[0] = i;
                ret[1] = j;
                return ret;
            }
        }
    }
    return NULL;
}

int main() {
	int* returnSize;
	int nums[4] = {2, 7, 11, 15};
	int numsSize = 4;
	int target = 9;
	int* output = twoSum(nums, numsSize, target, returnSize);
	printf("[%d, %d]", output[0], output[1]);
}
