

function selectionSort(arr) {   
    for (let i = 0; i < arr.length - 1; i++) {
        let minIndex = i;
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        if (minIndex !== i) {
            // Swap the found minimum element with the first element
            let temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }
    return arr;
}
// Example usage:
const array = [64, 25, 12, 22, 11];
console.log("Unsorted array:", array);
const sortedArray = selectionSort(array);
console.log("Sorted array:", sortedArray);
// Output:
// Unsorted array: [ 64, 25, 12, 22, 11 ]
// Sorted array: [ 11, 12, 22, 25, 64 ]
module.exports = selectionSort;
// Exporting the selectionSort function for use in other modules
// This implementation of selection sort sorts an array in ascending order.