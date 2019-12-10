import Foundation
import CoreGraphics

func getAsteroids(input: Array<Character>) -> Array<(x: Int, y: Int)> {
    var x = 0
    var y = 0
    var asteroids = Array<(x: Int, y: Int)>()
    for asteroid in input {
        if asteroid != "\n" {
            if asteroid == "#" {
                asteroids.append((x: x, y: y))
            }
            
            x += 1
        } else {
            x = 0
            y += 1
        }
    }
    return asteroids
}

func part1(input: Array<Character>) -> Int {
    let asteroids = getAsteroids(input: input)
    var max = 0
    for source in asteroids {
        var angles = Array<CGFloat>()
        for destination in asteroids {
            if source != destination {
                let angle = CoreGraphics.atan2(CGFloat(destination.y - source.y), CGFloat(destination.x - source.x))
                if !angles.contains(angle) {
                    angles.append(angle)
                }
            }
        }
        if angles.count > max {
            max = angles.count
        }
    }
    
    return max
}

func part2(input: Array<Character>) -> Int {
    let asteroids = getAsteroids(input: input)
    
    var max = 0
    var base: (x: Int, y: Int)!
    for source in asteroids {
        var angles = Array<CGFloat>()
        for destination in asteroids {
            if source != destination {
                let angle = CoreGraphics.atan2(CGFloat(destination.y - source.y), CGFloat(destination.x - source.x))
                
                if !angles.contains(angle) {
                    angles.append(angle)
                }
            }
        }
        if angles.count > max {
            max = angles.count
            base = source
        }
    }
    
    var angles = Array<(x: Int, y: Int, angle: CGFloat, distance: CGFloat, destroyed: Bool)>()
    for destination in asteroids {
        if base != destination {
            let diffX = abs(destination.x - base.x)
            let diffY = abs(destination.y - base.y)
            let angle = atan2(CGFloat(destination.y - base.y), CGFloat(destination.x - base.x))
            let value = (diffX * diffX) + (diffY * diffY)
            let distance = sqrt(CGFloat(value))
            angles.append((x: destination.x, y: destination.y, angle: angle, distance: distance, destroyed: false))
        }
    }
    var sortedAngles = angles.sorted(by: {
        if $0.angle == $1.angle {
            return $0.distance < $1.distance
        } else {
            return $0.angle < $1.angle
        }
    })
    
    var startI = 0
    for i in 0..<sortedAngles.count-1 {
        if sortedAngles[i].angle >= -1.5707963267948966 {
            startI = i
            break
        }
    }
    
    var i = startI
    var lastDestroyed: CGFloat?
    var destroyedCount = 0
    while destroyedCount < 200 {
        if !sortedAngles[i].destroyed {
            if sortedAngles[i].angle != lastDestroyed {
                sortedAngles[i].destroyed = true
                lastDestroyed = sortedAngles[i].angle
                destroyedCount += 1
                if destroyedCount == 200 {
                    return sortedAngles[i].x * 100 + sortedAngles[i].y
                }
            }
        }
        
        if i + 1 == sortedAngles.count {
            i = 0
            lastDestroyed = nil
        } else {
            i += 1
        }
    }
    
    return -1
}



if let inputText = try? String(contentsOf: URL.init(fileURLWithPath: CommandLine.arguments[1], isDirectory: false)) {
    let input = Array(inputText)

    print("Part 1: \(part1(input: input))")
    print("Part 2: \(part2(input: input))")
}
