//binary search algorithm

//binary search function
function binarySearch(arr, target) {
    let left = 0;
    let right = arr.length - 1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);

        if (arr[mid] === target) {
            return mid; // Target found, return index
        }else if (arr[mid] < target) {
            left = mid + 1; // Target is in the right half
        } else {
            right = mid - 1; // Target is in the left half
        }

    }
    return -1; // Target not found
}

// Example usage:
const sortedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const targetValue = 5;  
const result = binarySearch(sortedArray, targetValue);
console.log(`Target found at index: ${result}`); // Output: Target found at index: 4
module.exports = binarySearch; // Exporting the function for use in other files
// Exporting the function for use in other files
// This allows the function to be imported in other modules or test files.      
