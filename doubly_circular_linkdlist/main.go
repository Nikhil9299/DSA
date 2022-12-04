package main

import (
	"fmt"
	"os"
	"strconv"
)

type Node struct {
	prev  *Node
	value int
	next  *Node
}
type DoubleCircular struct {
	head *Node
	tail *Node
	size int
}

func (dc *DoubleCircular) addLast(val int) {
	newNode := &Node{value: val}
	if dc.size == 0 {
		newNode.next = newNode
		dc.head = newNode
		dc.head.prev = newNode
	} else {
		newNode.next = dc.tail.next
		dc.tail.next = newNode
		newNode.prev = dc.tail
	}
	dc.tail = newNode
	dc.size++
}

func (dc *DoubleCircular) display() {
	ptr := dc.head
	for i := 0; i < dc.size; i++ {
		fmt.Printf("%v--->", ptr.value)
		ptr = ptr.next
	}
	fmt.Println()
}

func (dc *DoubleCircular) addFirst(val int) {
	newNode := &Node{value: val}
	if dc.size == 0 {
		newNode.next = dc.head
		dc.head = newNode
		dc.head.prev = newNode
	} else {
		dc.tail.next = newNode
		newNode.next = dc.head
		newNode.prev = dc.tail
		dc.head = newNode

	}
	dc.size++
}

func (dc *DoubleCircular) addBetween(val, pos int) {
	newest := &Node{value: val}
	ptr := dc.head
	for i := 1; i < pos-1; i++ {
		ptr = ptr.next
	}
	newest.next = ptr.next
	newest.prev = ptr
	ptr.next = newest

	dc.size++
}

func main() {
	dc := DoubleCircular{}

	var choice string

	for true {
		fmt.Println("\nEnter your choice")
		fmt.Println("1. Insert value in linked last")
		fmt.Println("2. Display linkedList")
		fmt.Println("3. Deleting from begining ")
		fmt.Println("4. Deleting from last")
		fmt.Println("5. Deleting from specific position")
		fmt.Println("6. Insert at specific position")
		fmt.Println("7. insert at starting")
		fmt.Println("0. Exit")

		fmt.Scanln(&choice)

		switch choice {
		case "1":
			var data string
			fmt.Println("Enter your value for linked list")
			fmt.Scanln(&data)
			num, _ := strconv.Atoi(data)
			dc.addLast(num)

		case "2":
			dc.display()
		default:
			os.Exit(0)
		}
	}

}

//dc.addLast(1)
//dc.display()
//dc.addLast(2)
//dc.display()
//dc.addLast(3)
//dc.display()
//dc.addLast(4)
//dc.display()
//dc.addFirst(0)
// dc.display()
// dc.addBetween(33, 3)
// dc.display()
