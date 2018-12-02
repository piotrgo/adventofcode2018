package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func frequency(path string) int {
	var numbers []int
	var sum int
	file, err := os.Open(path)
	check(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		value, err := strconv.Atoi(scanner.Text())
		check(err)
		numbers = append(numbers, value)
	}
	if err != nil {
		fmt.Fprintln(os.Stderr, "reading standard input:", err)
	}
	for _, num := range numbers {
		sum += num
	}
	return sum
}

func main() {
	fmt.Println(frequency(os.Args[1]))
}
