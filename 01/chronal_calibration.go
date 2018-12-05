package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var numbers []int
var sum []int
var sumA int
var result int

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func parseInput(path string) []int {

	file, err := os.Open(path)
	check(err)
	defer file.Close()
	lineCount := 0

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lineCount++
		value, err := strconv.Atoi(scanner.Text())
		check(err)
		numbers = append(numbers, value)
	}
	if err != nil {
		fmt.Fprintln(os.Stderr, "reading standard input:", err)
	}

	return numbers
}

func frequencySteps(something []int) []int {
	for i := 2; i <= len(something); i++ {
		sumA = 0
		for _, num := range something[0:i] {
			sumA += num
		}
		sum = append(sum, sumA)
	}

	return sum
}

func tunedFrequency(elements []int) int {
	// Use map to record duplicates as we find them.
	encountered := map[int]bool{}
	//result := 0
	var result int

	for v := range elements {
		fmt.Println(elements[v])
		if encountered[elements[v]] == true {
			result = elements[v]
		} else {
			// Record this element as an encountered element.
			encountered[elements[v]] = true
		}
	}
	return result
}

func main() {
	inputData := parseInput(os.Args[1])
	var s3 []int
	// increase the counter if not found within this limit :P
	for i := 0; i < 10; i++ {
		s1 := frequencySteps(inputData)
		s2 := tunedFrequency(s1)
		// if s2 != 0 {
		fmt.Println(s2)
		// }
		s3 = []int{s1[len(s1)-1]}
		inputData = append(s3, parseInput(os.Args[1])...)
	}
}
