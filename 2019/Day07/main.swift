import Foundation

class intcode {
    var input: Array<String>
    var amplifier: Int
    var amplifierUsed = false
    var halted = false
    var i = 0
    
    init(input: Array<String>, amplifier: Int) {
        self.input = input
        self.amplifier = amplifier
    }
    
    func processInputs(inputValue: Int) -> Int {
        var result: Int?
        while input[i] != "99" && result == nil {
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
                    if amplifierUsed {
                        input[pos1] = "\(inputValue)"
                    } else {
                        input[pos1] = "\(amplifier)"
                        amplifierUsed = true
                    }
                    i += 2
                case 4:
                    result = value1
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
        if result != nil {
            return result!
        } else {
            self.halted = true
            return inputValue
        }
    }
}

func getInputStrings(fileUrl: URL) -> Array<String>? {
    guard let inputText = try? String(contentsOf: fileUrl) else { return nil }
    
    return inputText.components(separatedBy: ",")
}

func processInputs(inputStrings: Array<String>, inputValues: Array<Int>) -> Int {
    var i = 0
    var inputIndex = 0
    var result: Int!
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
                input[pos1] = "\(inputValues[inputIndex])"
                inputIndex += 1
                i += 2
            case 4:
                result = value1
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
    return result
}

func getPermutations(digits: Array<Int>) -> Array<Array<Int>> {
    var permutations = Array<Array<Int>>()
    
    if digits.count == 1 {
        permutations.append(digits)
        return permutations
    }
    
    for i in 0..<digits.count {
        let firstDigit = digits[i]
        var otherDigits = digits
        otherDigits.remove(at: i)
        let subPermutations = getPermutations(digits: otherDigits)
        
        for p in subPermutations {
            var permutation = p
            permutation.insert(firstDigit, at: 0)
            permutations.append(permutation)
        }
    }
    
    return permutations
}

func part1(inputStrings: Array<String>) {
    let amplifiers = [4, 3, 2, 1, 0]
    var thrusterValue = 0
    
    let permutations = getPermutations(digits: amplifiers)
    for p in permutations {
        var inputValue = 0
        for amp in p {
            inputValue = processInputs(inputStrings: inputStrings, inputValues: [ amp, inputValue ])
        }
        if inputValue > thrusterValue {
            thrusterValue = inputValue
        }
    }
    print(thrusterValue)
}

func part2(inputStrings: Array<String>) {
    let amplifierValues = [9, 8, 7, 6, 5]
    let permutations = getPermutations(digits: amplifierValues)
    var thrusterValue = 0
    
    
    for p in permutations {
        var amplifiers = Array<intcode>()
        var inputValue = 0
        
        for amp in p {
            amplifiers.append(intcode.init(input: inputStrings, amplifier: amp))
        }
        
        var i = 0
        while true {
            inputValue = amplifiers[i].processInputs(inputValue: inputValue)
            if amplifiers[i].halted {
                break
            }
            
            if i == amplifiers.count - 1 {
                i = 0
            } else {
                i += 1
            }
        }
        if inputValue > thrusterValue {
            thrusterValue = inputValue
        }
    }
    print(thrusterValue)
}

if let inputStrings = getInputStrings(fileUrl: URL.init(fileURLWithPath: CommandLine.arguments[1], isDirectory: false)) {
    print("Part 1:")
    part1(inputStrings: inputStrings)
    print("Part 2:")
    part2(inputStrings: inputStrings)
}

