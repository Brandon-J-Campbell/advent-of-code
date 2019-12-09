import Foundation

class Intcode {
    var input: Dictionary<Int, String>
    var halted = false
    var i = 0
    var relativeBase = 0
    
    init(input: Dictionary<Int, String>) {
        self.input = input
    }
    
    func processInputs(inputValue: Double) -> Double {
        var result: Double?
        while input[i] != "99"/* && result == nil*/ {
            if let instruction = Int(input[i]!) {
                let resultMode = (instruction % 100000) / 10000
                let paramMode2 = (instruction % 10000) / 1000
                let paramMode1 = (instruction % 1000) / 100
                let op = instruction % 100
                
                var value1, value2: Double!
                var resultPos: Int!
                if paramMode1 == 0 {
                    if let pos1 = Int(input[i + 1]!) {
                        if let value = input[pos1] {
                            value1 = Double(value)
                        } else {
                            value1 = Double(0)
                        }
                    }
                } else if paramMode1 == 2 {
                    if let pos1 = Int(input[i + 1]!) {
                        value1 = Double(input[pos1 + relativeBase]!)
                    }
                } else {
                    value1 = Double(input[i + 1]!)!
                }
                
                if (op <= 2 || op >= 5) && op != 9 {
                    if paramMode2 == 0 {
                        if let pos2 = Int(input[i + 2]!) {
                            if let value = input[pos2] {
                                value2 = Double(value)
                            } else {
                                value2 = Double(0)
                            }
                        }
                    } else if paramMode2 == 2 {
                        if let pos2 = Int(input[i + 2]!) {
                            value2 = Double(input[pos2 + relativeBase]!)
                        }
                    } else {
                        value2 = Double(input[i + 2]!)!
                    }
                    
                    if op != 5 && op != 6 {
                        resultPos = Int(input[i + 3]!)!
                        if resultMode == 2 {
                            resultPos += relativeBase
                        }
                    }
                }
//                print("Instruction: \(instruction), Op: \(op), Param1: \(input[i + 1]), Value1: \(value1), Value2: \(value2), Param2: \(input[i + 2]), ResultPos: \(resultPos), RelativeBase: \(relativeBase)")
//
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
                    if let pos1 = Int(input[i + 1]!) {
                        if paramMode1 == 0 {
                            input[pos1] = "\(inputValue)"
                        } else {
                            input[pos1 + relativeBase] = "\(inputValue)"
                        }
                    }
                    i += 2
                case 4:
                    result = value1
                    print(result! as Any)
                    i += 2
                case 5:
                    if value1! != 0 {
                        i = Int(value2!)
                    } else {
                        i += 3
                    }
                case 6:
                    if value1! == 0 {
                        i = Int(value2!)
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
                case 9:
                    relativeBase += Int(value1)
                    i += 2
                default:
                    break
                }
            }
        }
        return result!
    }
}

func getInputStrings(fileUrl: URL) -> Array<String>? {
    guard let inputText = try? String(contentsOf: fileUrl) else { return nil }
    
    return inputText.components(separatedBy: ",")
}

func part1(inputStrings: Array<String>) {
    var dict = Dictionary<Int, String>()
    for i in 0..<inputStrings.count {
        dict[i] = inputStrings[i]
    }
    let intcode = Intcode.init(input: dict)
    let _ = intcode.processInputs(inputValue: 1)
}

func part2(inputStrings: Array<String>) {
    var dict = Dictionary<Int, String>()
    for i in 0..<inputStrings.count {
        dict[i] = inputStrings[i]
    }
    let intcode = Intcode.init(input: dict)
    let _ = intcode.processInputs(inputValue: 2)
}

if let inputStrings = getInputStrings(fileUrl: URL.init(fileURLWithPath: CommandLine.arguments[1], isDirectory: false)) {
    print("Part 1:")
    part1(inputStrings: inputStrings)
    print("Part 2:")
    part2(inputStrings: inputStrings)
}
