import Foundation

func getInputStrings(fileUrl: URL) -> Array<String>? {
    guard let inputText = try? String(contentsOf: fileUrl) else { return nil }
    
    return inputText.components(separatedBy: "\n")
}

func countOrbiters(_ map: Dictionary<String, Array<String>>, start: String, level: Int) -> Int {
    guard let orbiters = map[start] else {
        return level
    }
    var count = 0
    for orbiter in orbiters {
        count += countOrbiters(map, start: orbiter, level: level + 1)
    }
    return count + level
}

func part1(inputStrings: Array<String>) -> Int {
    var map = Dictionary<String, Array<String>>()
    
    for orbit in inputStrings {
        let orbitArray = orbit.components(separatedBy: ")")
        let orbiter = orbitArray[1]
        let orbitee = orbitArray[0]
        if let orbiters = map[orbitee] {
            var mOrbiters = orbiters
            mOrbiters.append(orbiter)
            map[orbitee] = mOrbiters
        } else {
            map[orbitee] = [ orbiter ]
        }
    }
    return countOrbiters(map, start: "COM", level: 0)
}

struct spaceObject {
    var name: String
    var orbits: String?
    var orbiters = Array<String>()
    var neighbors = Array<String>()
}

func findShortestPath(map: Dictionary<String, spaceObject>, source: spaceObject, cameFrom: spaceObject, destination: spaceObject, level: Int) -> Int {
    var shortestPath = -1
    for neighbor in source.neighbors {
        if neighbor != cameFrom.name {
            if let neighborObj = map[neighbor] {
                if neighborObj.name == destination.name {
                    if shortestPath == -1 || level + 1 < shortestPath {
                        shortestPath = level + 1
                    }
                } else {
                    if level + 1 < shortestPath || shortestPath == -1 {
                        let pathValue = findShortestPath(map: map, source: neighborObj, cameFrom: source, destination: destination, level: level + 1)
                        if pathValue != -1 && (shortestPath == -1 || pathValue < shortestPath) {
                            shortestPath = pathValue
                        }
                    }
                }
            }
        }
    }
    return shortestPath
}

func part2(inputStrings: Array<String>) -> Int {
    var map = Dictionary<String, spaceObject>()
    
    for orbit in inputStrings {
        let orbitArray = orbit.components(separatedBy: ")")
        let orbiter = orbitArray[1]
        let orbitee = orbitArray[0]
    
        var orbiterObj: spaceObject
        var orbiteeObj : spaceObject
        
        if map[orbitee] == nil {
            let obj = spaceObject.init(
                name: orbitee
            )
            orbiteeObj = obj
        } else {
            orbiteeObj = map[orbitee]!
        }
        
        if let orb = map[orbiter] {
            orbiterObj = orb
            var m = orbiterObj
            m.orbits = orbitee
        } else {
            let obj = spaceObject.init(
                name: orbiter,
                orbits: orbitee
            )
            orbiterObj = obj
        }
        
        orbiteeObj.orbiters.append(orbiter)
        orbiteeObj.neighbors.append(orbiter)
        orbiterObj.neighbors.append(orbitee)
        
        map[orbiter] = orbiterObj
        map[orbitee] = orbiteeObj
    }
    
    if let you = map["YOU"], let source = map[you.orbits!], let san = map["SAN"], let dest = map[san.orbits!] {
        return findShortestPath(map: map, source: source, cameFrom: you, destination: dest, level: 0)
    } else {
        return -1
    }
}

if let inputStrings = getInputStrings(fileUrl: URL.init(fileURLWithPath: CommandLine.arguments[1], isDirectory: false)) {
    print("Part 1: \(part1(inputStrings: inputStrings))")
    print("Part 2: \(part2(inputStrings: inputStrings))")
}
