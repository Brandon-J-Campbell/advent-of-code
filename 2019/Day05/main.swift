import Foundation

func getInputStrings(fileUrl: URL) -> Array<String>? {
    guard let inputText = try? String(contentsOf: fileUrl) else { return nil }
    
    return inputText.components(separatedBy: ",")
}

func processInputs(inputStrings: Array<String>, inputValue: Int) {
    var i = 0
    var input = inputStrings
    while input[i] != "99" {
        if let instruction = Int(input[i]) {
            let paramMode2 = (instruction % 10000) / 1000
            let paramMode1 = (instruction % 1000) / 100
            let op = instruction % 100

            var value1, value2, resultPos: Int!
            if paramMode1 == 0 {
                if let pos1 = Int(input[i + 1]) {
                    value1 = Int(input[pos1])!
                }
            } else {
                value1 = Int(input[i + 1])!
            }
            
            if op <= 2 || op >= 5 {
                if paramMode2 == 0 {
                    if let pos2 = Int(input[i + 2]) {
                        value2 = Int(input[pos2])!
                    }
                } else {
                    value2 = Int(input[i + 2])!
                }
                
                if op != 5 && op != 6 {
                    resultPos = Int(input[i + 3])!
                }
            }
            
            
            switch op {
            case 1:
                let result = value1 + value2
                input[resultPos] = "\(result)"
                i += 4
            case 2:
                let result = value1 * value2
                input[resultPos] = "\(result)"
                i += 4
            case 3:
                let pos1 = Int(input[i + 1])!
                input[pos1] = "\(inputValue)"
                i += 2
            case 4:
                print(value1!)
                i += 2
            case 5:
                if value1! != 0 {
                    i = value2!
                } else {
                    i += 3
                }
            case 6:
                if value1! == 0 {
                    i = value2!
                } else {
                    i += 3
                }
            case 7:
                if value1 < value2 {
                    input[resultPos] = "1"
                } else {
                    input[resultPos] = "0"
                }
                i += 4
            case 8:
                if value1 == value2 {
                    input[resultPos] = "1"
                } else {
                    input[resultPos] = "0"
                }
                i += 4
            default:
                break
            }
        }
    }
}

func part1(inputStrings: Array<String>) {
    processInputs(inputStrings: inputStrings, inputValue: 1)
}

func part2(inputStrings: Array<String>) {
    processInputs(inputStrings: inputStrings, inputValue: 5)
}

if let inputStrings = getInputStrings(fileUrl: URL.init(fileURLWithPath: CommandLine.arguments[1], isDirectory: false)) {
    print("Part 1:")
    part1(inputStrings: inputStrings)
    print("Part 2:")
    part2(inputStrings: inputStrings)
}
