import Foundation

func getInputStrings(fileUrl: URL) -> Array<String>? {
    guard let inputText = try? String(contentsOf: fileUrl) else { return nil }
    
    return inputText.components(separatedBy: "\n")
}

// Function to determine whether 2 lines cross -- https://www.hackingwithswift.com/example-code/core-graphics/how-to-calculate-the-point-where-two-lines-intersect
func linesCross(start1: CGPoint, end1: CGPoint, start2: CGPoint, end2: CGPoint) -> (x: CGFloat, y: CGFloat)? {
    // calculate the differences between the start and end X/Y positions for each of our points
    let delta1x = end1.x - start1.x
    let delta1y = end1.y - start1.y
    let delta2x = end2.x - start2.x
    let delta2y = end2.y - start2.y

    // create a 2D matrix from our vectors and calculate the determinant
    let determinant = delta1x * delta2y - delta2x * delta1y

    if abs(determinant) < 0.0001 {
        // if the determinant is effectively zero then the lines are parallel/colinear
        return nil
    }

    // if the coefficients both lie between 0 and 1 then we have an intersection
    let ab = ((start1.y - start2.y) * delta2x - (start1.x - start2.x) * delta2y) / determinant

    if ab > 0 && ab < 1 {
        let cd = ((start1.y - start2.y) * delta1x - (start1.x - start2.x) * delta1y) / determinant

        if cd > 0 && cd < 1 {
            // lines cross – figure out exactly where and return it
            let intersectX = start1.x + ab * delta1x
            let intersectY = start1.y + ab * delta1y
            return (intersectX, intersectY)
        }
    }

    // lines don't cross
    return nil
}

func getPoints(_ instructions : String) -> Array<(point: CGPoint, distance: CGFloat)> {
    var point = CGPoint.init(x: 0, y: 0)
    var points = Array<(point: CGPoint, distance: CGFloat)>()
    var count = CGFloat(0.0)
    
    for instr in instructions.components(separatedBy: ",") {
        points.append((point, count))
        
        let direction = instr.prefix(1)
        count = CGFloat(Double(instr.suffix(instr.count - 1))!)
        
        switch direction {
        case "R":
            point = CGPoint(x: point.x + count, y: point.y)
        case "L":
            point = CGPoint(x: point.x - count, y: point.y)
        case "U":
            point = CGPoint(x: point.x, y: point.y + count)
        case "D":
            point = CGPoint(x: point.x, y: point.y - count)
        default:
            break
        }
    }
    
    return points
}

func part1(inputStrings: Array<String>) -> Int {
    let instructions1 = inputStrings[0]
    let points1 = getPoints(instructions1)
    let instructions2 = inputStrings[1]
    let points2 = getPoints(instructions2)
    
    var intersections = Array<CGPoint>()
    
    for i in 1..<points1.count {
        for j in 1..<points2.count {
            if let intersectingPoint = linesCross(start1: points1[i-1].point, end1: points1[i].point, start2: points2[j-1].point, end2: points2[j].point) {
                intersections.append(CGPoint(x: intersectingPoint.x, y: intersectingPoint.y))
            }
        }
    }
    
    var smallestDistance = CGFloat(-1.0)
    for point in intersections {
        let distance = abs(point.x) + abs(point.y)
        if smallestDistance == -1.0 || distance < smallestDistance {
            smallestDistance = distance
        }
    }
    return Int(smallestDistance)
}

func part2(inputStrings: Array<String>) -> Int {
    let instructions1 = inputStrings[0]
    let points1 = getPoints(instructions1)
    let instructions2 = inputStrings[1]
    let points2 = getPoints(instructions2)
    var steps = Array<CGFloat>()

    var iSteps = CGFloat(0.0)
    for i in 1..<points1.count {
        var jSteps = CGFloat(0.0)
        for j in 1..<points2.count {
            if let intersectingPoint = linesCross(start1: points1[i-1].point, end1: points1[i].point, start2: points2[j-1].point, end2: points2[j].point) {
                let distance1 = abs(points1[i-1].point.x - intersectingPoint.x) + abs(points1[i-1].point.y - intersectingPoint.y)
                let distance2 = abs(points2[j-1].point.x - intersectingPoint.x) + abs(points2[j-1].point.y - intersectingPoint.y)
                steps.append(iSteps + jSteps + distance1 + distance2)
            }
            jSteps += points2[j].distance
        }
        iSteps += points1[i].distance
    }
    
    let sortedSteps = steps.sorted()
    return Int(sortedSteps[0])
}


if let inputStrings = getInputStrings(fileUrl: URL.init(fileURLWithPath: CommandLine.arguments[1], isDirectory: false)) {
    print("Part 1: \(part1(inputStrings: inputStrings))")
    print("Part 2: \(part2(inputStrings: inputStrings))")
}
