package main

import "fmt"

func shell(A []int) {
	n := len(A)
	gap := n / 2
	for gap > 0 {
		i := gap
		for i < n {
			temp := A[i]
			j := i - gap
			for j >= 0 && A[j] > temp {
				A[j+gap] = A[j]
				j = j - gap
			}
			A[j+gap] = temp
			i = i + 1

		}
		gap = gap / 2
		fmt.Println(A)

	}
}

func main() {

	A := []int{3, 5, 8, 9, 6, 2}
	fmt.Printf("before sorting %#v\n", A)
	shell(A)
	fmt.Printf("After sorting %#v\n ", A)

}
