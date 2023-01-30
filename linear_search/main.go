package main

import "fmt"

func linear(A []int, key int) int {
	index := 0
	for index < len(A) {
		if A[index] == key {
			return index
		}
		index = index + 1

	}
	return -1

}
func main() {
	A := []int{84, 21, 47, 96, 15}
	fmt.Printf("before searching %#v\n", A)
	found := linear(A, 96)
	fmt.Printf("if the element is found at the index is %#v\n", found)

}
