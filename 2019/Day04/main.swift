import Foundation

func evaluate(input: Int, part2: Bool) -> Bool {
    var inputArray = Array<Int>()
    let inputString = "\(input)"
    let inputStringArray = Array(inputString)
    
    for i in 0..<inputStringArray.count {
        inputArray.append(Int(String(inputStringArray[i]))!)
    }
    
    if inputArray.sorted() != inputArray {
        return false
    }

    for i in 0..<inputArray.count-1 {
        if inputArray[i] == inputArray[i+1] {
            if !part2 {
                return true
            }
            
            var stillTrue = true
            if i + 1 < inputArray.count - 1 {
                if inputArray[i+2] == inputArray[i] {
                    stillTrue = false
                }
            }
            
            if i - 1 >= 0 {
                if inputArray[i-1] == inputArray[i] {
                    stillTrue = false
                }
            }
            
            if stillTrue {
                return true
            }
        }
    }
    return false
}

func part1() -> Int {
    var rv = 0
    for number in 240298...784956 {
        if evaluate(input: number, part2: false) {
            rv += 1
        }
    }
    return rv
}

func part2() -> Int {
    var rv = 0
    for number in 240298...784956 {
        if evaluate(input: number, part2: true) {
            rv += 1
        }
    }
    return rv
}

print(part1())
print(part2())
