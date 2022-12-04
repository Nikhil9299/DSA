package main

import "fmt"

func binary(A []int, key int) int {
	l := 0
	r := len(A) - 1
	for l <= r {
		mid := (l + r) / 2
		if key == A[mid] {
			return mid
		} else if key < A[mid] {
			r = mid - 1
		} else if key > A[mid] {
			l = mid + 1
		}
	}
	return -1

}

func main() {
	A := []int{15, 21, 47, 84, 96}
	fmt.Printf("before searching %#v\n", A)
	found := binary(A, 16)
	fmt.Println("the element is found at index: ", found)

}
