import UIKit

// Day 1

//if let url = Bundle.main.url(forResource: "Day01", withExtension: "txt") {
//    let content = try String(contentsOf: url)
//    let inputArr = content.split(separator: "\n")
//    var increaseCount = 0
//    var lastWindowSum = 999999999
//    var part2count = 0
//    for (idx, input) in inputArr.enumerated() {
//        if idx > 0 {
//            if let cur = Int(input), let prev = Int(inputArr[idx-1]) {
//                if cur > prev {
//                    increaseCount += 1
//                }
//
//                if idx > 1 {
//                    if let prev2 = Int(inputArr[idx-2]) {
//                        let sum = cur + prev + prev2
//                        if sum > lastWindowSum {
//                            part2count += 1
//                        }
//                        lastWindowSum = sum
//                    }
//                }
//            }
//        }
//    }
//    print("Part 1 Increase: \(increaseCount), Part 2 Increase: \(part2count)")
//}

//Day 2
//
//if let url = Bundle.main.url(forResource: "Day02", withExtension: "txt") {
//    let content = try String(contentsOf: url)
//    let commands = content.split(separator: "\n")
//    var depth = 0
//    var depth2 = 0
//    var position = 0
//    var aim = 0
//    for command in commands {
//        let commandArr = command.split(separator: " ")
//        switch commandArr[0] {
//        case "forward":
//            position += Int(commandArr[1])!
//            depth2 += (aim * Int(commandArr[1])!)
//        case "down":
//            depth += Int(commandArr[1])!
//            aim += Int(commandArr[1])!
//        case "up":
//            depth -= Int(commandArr[1])!
//            aim -= Int(commandArr[1])!
//        default:
//            break
//        }
//    }
//
//    print("Part 1: \(depth * position), Part 2: \(depth2 * position)")
//}

//Day 3

if let url = Bundle.main.url(forResource: "Day02", withExtension: "txt") {
    let content = try String(contentsOf: url)
    
}
