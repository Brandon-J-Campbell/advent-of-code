//: Playground - noun: a place where people can play

import UIKit
import XCPlayground
import Foundation

XCPlaygroundPage.currentPage.needsIndefiniteExecution = true

let urlSession : URLSession = URLSession.shared
var inputUrlString : String

func quicksort<T: Comparable>(_ a: [T]) -> [T] {
    guard a.count > 1 else { return a }
    
    let pivot = a[a.count/2]
    let less = a.filter { $0 < pivot }
    let equal = a.filter { $0 == pivot }
    let greater = a.filter { $0 > pivot }
    
    return quicksort(less) + equal + quicksort(greater)
}

// Day 1 - Problem

/*
enum direction {
    case north
    case south
    case east
    case west
}

inputUrlString = "https://dl.dropboxusercontent.com/u/47309/AdventOfCode2016/day01-1-input.txt"
let task = urlSession.dataTask(with: URL.init(string: inputUrlString)!, completionHandler: { (data: Data?, response: URLResponse?, error: Error?) -> Void in
    if error == nil {
        var x = 0, y = 0
        let result = NSString(data: data!, encoding:String.Encoding.ascii.rawValue)!
        //let result = "R8, R4, R4, R8"
        let resultArray = result.components(separatedBy: ", ")
        var dict : Dictionary<String, String> = Dictionary<String, String>.init()
        
        var currentDirection : direction = direction.north
        
        for command in resultArray {
            
            
            let nextDirection = command.substring(to: command.index(after: command.startIndex))
            switch (currentDirection) {
                case .north:
                    if nextDirection == "L" {
                        currentDirection = direction.west
                    } else {
                        currentDirection = direction.east
                    }
                    break
                
                case direction.south:
                    if nextDirection == "L" {
                        currentDirection = direction.east
                    } else {
                        currentDirection = direction.west
                    }
                    break
                
                case direction.east:
                    if nextDirection == "L" {
                        currentDirection = direction.north
                    } else {
                        currentDirection = direction.south
                    }
                    break
                
                case direction.west:
                    if nextDirection == "L" {
                        currentDirection = direction.south
                    } else {
                        currentDirection = direction.north
                    }
                    break
            }
            
            var commandString = command.substring(from: command.index(after: command.startIndex))
            if let nextMoveCount : Int = Int(commandString) {
                var i = 0
                switch (currentDirection) {
                    case direction.north:
                        repeat {
                            y += 1
                            i += 1
                            
                            let coordString = "\(x),\(y)"
                            if let dup = dict.index(forKey: coordString) {
                                print(coordString)
                            } else {
                                dict[coordString] = "HIT"
                            }
                        } while i < nextMoveCount
                        break
                    
                    case direction.south:
                        repeat {
                            y -= 1
                            i += 1
                            
                            let coordString = "\(x),\(y)"
                            if let dup = dict.index(forKey: coordString) {
                                print(coordString)
                            } else {
                                dict[coordString] = "HIT"
                            }
                        } while i < nextMoveCount
                        break
                    
                    case direction.east:
                        repeat {
                            x += 1
                            i += 1
                            
                            let coordString = "\(x),\(y)"
                            if let dup = dict.index(forKey: coordString) {
                                print(coordString)
                            } else {
                                dict[coordString] = "HIT"
                            }
                        } while i < nextMoveCount
                        break
                    
                    case direction.west:
                        repeat {
                            x -= 1
                            i += 1
                            
                            let coordString = "\(x),\(y)"
                            if let dup = dict.index(forKey: coordString) {
                                print(coordString)
                            } else {
                                dict[coordString] = "HIT"
                            }
                        } while i < nextMoveCount
                        break
                }
            }
        }
        
        print("Endpoint - x: \(x) y: \(y)")
    }
})

task.resume()
 
*/

// Day 2 - Problem 1
/*
inputUrlString = "https://dl.dropboxusercontent.com/u/47309/AdventOfCode2016/day02-1-input.txt"
let task = urlSession.dataTask(with: URL.init(string: inputUrlString)!, completionHandler: { (data: Data?, response: URLResponse?, error: Error?) -> Void in
    if error == nil {
        let result = NSString(data: data!, encoding:String.Encoding.ascii.rawValue)!
        //let result = "ULL\nRRDDD\nLURDL\nUUUUD"
        let resultArray = result.components(separatedBy: "\n")
        var code = ""
        
        var currentNumber = 5
        for input in resultArray {
            for char in input.characters {
                switch (char) {
                    case "U":
                        if currentNumber > 3 {
                            currentNumber -= 3
                        }
                        break
                    case "D":
                        if currentNumber < 7 {
                            currentNumber += 3
                        }
                        break
                    case "L":
                        if currentNumber != 1 && currentNumber != 4 && currentNumber != 7 {
                            currentNumber -= 1
                        }
                        break
                    case "R":
                        if currentNumber != 3 && currentNumber != 6 && currentNumber != 9 {
                            currentNumber += 1
                        }
                        break
                    default:
                        break
                }
            }
            code = code.appending("\(currentNumber)")
        }
        print(code)
    }
})
task.resume()
*/

// Day 2 - Problem 2

/*

inputUrlString = "https://dl.dropboxusercontent.com/u/47309/AdventOfCode2016/day02-1-input.txt"
let task = urlSession.dataTask(with: URL.init(string: inputUrlString)!, completionHandler: { (data: Data?, response: URLResponse?, error: Error?) -> Void in
    if error == nil {
        let result = NSString(data: data!, encoding:String.Encoding.ascii.rawValue)!
        let resultArray = result.components(separatedBy: "\n")
        var code = ""
        
        var currentNumber = 5
        for input in resultArray {
            for char in input.characters {
                switch (char) {
                case "U":
                    if currentNumber != 5 && currentNumber != 2 && currentNumber != 1 && currentNumber != 4 && currentNumber != 9 {
                        if currentNumber == 3 || currentNumber == 13 {
                            currentNumber -= 2
                        } else {
                            currentNumber -= 4
                        }
                    }
                    break
                case "D":
                    if currentNumber != 5 && currentNumber != 10 && currentNumber != 13 && currentNumber != 12 && currentNumber != 9 {
                        if currentNumber == 1 || currentNumber == 11 {
                            currentNumber += 2
                        } else {
                            currentNumber += 4
                        }
                    }
                    break
                case "L":
                    if currentNumber != 1 && currentNumber != 2 && currentNumber != 5 && currentNumber != 10 && currentNumber != 13 {
                        currentNumber -= 1
                    }
                    break
                case "R":
                    if currentNumber != 1 && currentNumber != 4 && currentNumber != 9 && currentNumber != 12 && currentNumber != 13 {
                        currentNumber += 1
                    }
                    break
                default:
                    break
                }
            }
            code = code.appending("\(currentNumber) ")
        }
        print(code)
    }
})
task.resume()
 
*/

// Day 3 - Problem 1

/*
 
inputUrlString = "https://dl.dropboxusercontent.com/u/47309/AdventOfCode2016/day03-1-input.txt"
let task = urlSession.dataTask(with: URL.init(string: inputUrlString)!, completionHandler: { (data: Data?, response: URLResponse?, error: Error?) -> Void in
    if error == nil {
        let result = NSString(data: data!, encoding:String.Encoding.ascii.rawValue)!
        let resultArray = result.components(separatedBy: "\n")
        var validTriangles = 0
        
        for input in resultArray {
            let lengthsStringsArray = input.trimmingCharacters(in: NSCharacterSet.whitespacesAndNewlines).components(separatedBy: " ")
            var lengthsArray = Array<Int>()
            
            for lengthString in lengthsStringsArray {
                if lengthString != "" {
                    lengthsArray.append(Int(lengthString)!)
                }
            }
            
            let sortedArray = quicksort(lengthsArray)
            print("\(sortedArray)")
            
            if sortedArray[0] + sortedArray[1] > sortedArray[2] {
                validTriangles += 1
            }
        }
        print("\(validTriangles)")
    }
})
task.resume()
 
 */

// Day 3 - Problem 2

/*

inputUrlString = "https://dl.dropboxusercontent.com/u/47309/AdventOfCode2016/day03-1-input.txt"
let task = urlSession.dataTask(with: URL.init(string: inputUrlString)!, completionHandler: { (data: Data?, response: URLResponse?, error: Error?) -> Void in
    if error == nil {
        let result = NSString(data: data!, encoding:String.Encoding.ascii.rawValue)!
        let resultArray = result.components(separatedBy: "\n")
        var validTriangles = 0
        var rowNumber = 0
        var columnNumber = 0
        var arrangedArrays = Array<Array<Int>>()
        
        for input in resultArray {
            let lengthsStringsArray = input.trimmingCharacters(in: NSCharacterSet.whitespacesAndNewlines).components(separatedBy: " ")
            var lengthsArray = Array<Int>()
            
            for lengthString in lengthsStringsArray {
                if lengthString != "" {
                    lengthsArray.append(Int(lengthString)!)
                }
            }
            
            if (columnNumber == 0) {
                arrangedArrays.append(Array<Int>())
                arrangedArrays.append(Array<Int>())
                arrangedArrays.append(Array<Int>())
            }
            arrangedArrays[rowNumber].append(lengthsArray[0])
            arrangedArrays[rowNumber + 1].append(lengthsArray[1])
            arrangedArrays[rowNumber + 2].append(lengthsArray[2])
            
            if (columnNumber == 2) {
                columnNumber = 0
                rowNumber += 3
            } else {
                columnNumber += 1
            }
        }
        
        for lengthsArray in arrangedArrays {
            let sortedArray = quicksort(lengthsArray)
            print("\(sortedArray)")
            
            if sortedArray[0] + sortedArray[1] > sortedArray[2] {
                validTriangles += 1
            }
        }
        print("\(validTriangles)")
    }
})
task.resume()
 
 */