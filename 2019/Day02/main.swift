import Foundation

func getInputStrings(fileUrl: URL) -> Array<String>? {
    guard let inputText = try? String(contentsOf: fileUrl) else { return nil }
    
    return inputText.components(separatedBy: ",")
}

func processInputs(inputStrings: Array<String>, input1: Int, input2: Int) -> Int {
    var i = 0
    var input = inputStrings
    input[1] = "\(input1)"
    input[2] = "\(input2)"
    while input[i] != "99" {
        if let op = Int(input[i]), let pos1 = Int(input[i + 1]), let pos2 = Int(input[i + 2]), let resultPos = Int(input[i + 3]), let value1 = Int(input[pos1]), let value2 = Int(input[pos2]) {
//            print("op: \(op), pos1: \(pos1), value1: \(value1), pos2: \(pos2), value2: \(value2), resultPos: \(resultPos)")
            switch op {
            case 1:
                let result = value1 + value2
                input[resultPos] = "\(result)"
            case 2:
                let result = value1 * value2
                input[resultPos] = "\(result)"
            default:
                break
            }
        }
        
        i += 4
    }
    
    return Int(input[0])!
}

func part1(inputStrings: Array<String>) -> Int {
    return processInputs(inputStrings: inputStrings, input1: 12, input2: 2)
}

func part2(inputStrings: Array<String>) -> Int {
    var result = 0
    var input1 = 0
    var input2 = 0
    
    repeat {
        result = processInputs(inputStrings: inputStrings, input1: input1, input2: input2)
        
        if result == 19690720 {
            break
        }
        
        if input2 == 99 {
            input2 = 0
            input1 += 1
        } else {
            input2 += 1
        }
    } while true
    
    return input1 * 100 + input2
}

if let inputStrings = getInputStrings(fileUrl: URL.init(fileURLWithPath: CommandLine.arguments[1], isDirectory: false)) {
    print("Part 1: \(part1(inputStrings: inputStrings))")
    print("Part 2: \(part2(inputStrings: inputStrings))")
}
