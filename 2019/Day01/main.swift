import Foundation


func fuelRequirement(_ mass: Double) -> Int {
/*
     Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
*/
    let step1 : Double = mass / 3.0
    let step2 = floor(step1)
    let step3 = step2 - 2
    
    return Int(step3)
}

func getInputStrings(fileUrl: URL) -> Array<String>? {
    guard let inputText = try? String(contentsOf: fileUrl) else { return nil }
    
    return inputText.components(separatedBy: "\n")
}

func part1(inputStrings: Array<String>) -> Int {
    var total = 0
    for input in inputStrings {
        if let inputNumber = Double(input) {
            total += fuelRequirement(inputNumber)
        }
    }
    return total
}

func calculateFuelRequirement(_ inputNumber: Double) -> Int {
    let total = fuelRequirement(inputNumber)
    if total <= 0 {
        return 0
    } else {
        return total + calculateFuelRequirement(Double(total))
    }
}

func part2(inputStrings: Array<String>) -> Int {
    var total = 0
    for input in inputStrings {
        if let inputNumber = Double(input) {
            total += calculateFuelRequirement(inputNumber)
        }
    }
    return total
}

if let inputStrings = getInputStrings(fileUrl: URL.init(fileURLWithPath: CommandLine.arguments[1], isDirectory: false)) {
    print("Part 1: \(part1(inputStrings: inputStrings))")
    print("Part 2: \(part2(inputStrings: inputStrings))")
}
