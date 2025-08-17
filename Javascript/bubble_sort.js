//bubble sort algoithm 

//bubble sort function 
function bubble_sort(arr) { 
    const n = arr.length;
    let swapped;
    do {
        swapped = false;
        for (let i = 0; i < n - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                // Swap elements if they are in the wrong order     
                [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
                swapped = true; // Set swapped to true if a swap occurred
            }   
        }
        n--; // Reduce the range for the next pass
    }   
    while (swapped);   // Continue until no swaps are made
    return arr; // Return the sorted array
}
// Example usage:
const unsortedArray = [64, 34, 25, 12, 22, 11, 90];
const sortedArray = bubble_sort(unsortedArray);
console.log(`Sorted array: ${sortedArray}`);    
// Output: Sorted array: [11, 12, 22, 25, 34, 64, 90]
module.exports = bubble_sort; // Exporting the function for use in other files
// This allows the function to be imported in other modules or test files.

// Exporting the function for use in other files

module.exports = bubble_sort; // Exporting the function for use in other files
// This allows the function to be imported in other modules or test files.
// This allows the function to be imported in other modules or test files.
// This allows the function to be imported in other modules or test files.
