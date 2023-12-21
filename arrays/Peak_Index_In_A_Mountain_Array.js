/**
An array arr is a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.

Beats 83%*/
var peakIndexInMountainArray = function(arr) {
    let start = 0
    let end = arr.length-1
    let mid = Math.floor((start+end)/2)

    while (true){
        if (arr[mid]>arr[mid-1] && arr[mid]>arr[mid+1]){
            return mid
        }

        if (arr[mid]>arr[mid-1]) {
            start = mid;
            mid = Math.floor((start+end)/2);
        }

        else if (arr[mid]<arr[mid-1]) {
            end = mid;
            mid = Math.floor((start+end)/2);
        }
    }
};
