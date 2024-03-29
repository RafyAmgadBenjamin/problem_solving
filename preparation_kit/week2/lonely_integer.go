package main

import (
	"bufio"
	"fmt"
	"io"
	"strings"
)

/*
 * Complete the 'lonelyinteger' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY a as parameter.
 */
func lonelyinteger(a []int32) int32 {
	counter := 0
	desiredVal := int32(-1.0)
	for i := 0; i < len(a); i++ {
		counter = 0
		for j := 0; j < len(a); j++ {
			if a[i] == a[j] {
				counter += 1
			}
		}
		if counter == 1 {
			desiredVal = a[i]
		}
	}

	return desiredVal
}

func main() {
	// reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	// stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	// checkError(err)

	// defer stdout.Close()

	// writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	// nTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	// checkError(err)
	// var nTemp int
	// fmt.Scanln(nTemp)
	// n := int32(nTemp)

	// aTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	// var a []int32

	// for i := 0; i < int(n); i++ {
	// 	aItemTemp, err := strconv.ParseInt(aTemp[i], 10, 64)
	// 	checkError(err)
	// 	aItem := int32(aItemTemp)
	// 	a = append(a, aItem)
	// }
	a := []int32{1, 2, 3, 4, 3, 2, 1}

	result := lonelyinteger(a)
	fmt.Print(result)

	// fmt.Fprintf(writer, "%d\n", result)

	// writer.Flush()
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
