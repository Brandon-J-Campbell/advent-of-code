import Foundation

func getInputStrings(fileUrl: URL) -> String? {
    guard let inputText = try? String(contentsOf: fileUrl) else { return nil }
    
    return inputText
}

struct Layer {
    var zeroes: Int
    var ones: Int
    var twos: Int
    var values: Array<String>
}

func getLayers(inputString: String) -> Array<Layer> {
    let inputStrings = Array(inputString)
    var layers = Array<Layer>()
    
    var zeroes = 0
    var ones = 0
    var twos = 0
    var values = Array<String>()
    
    for i in 0..<inputStrings.count {
        values.append("\(inputStrings[i])")
        switch inputStrings[i] {
        case "0":
            zeroes += 1
        case "1":
            ones += 1
        case "2":
            twos += 1
        default:
            break
        }
        
        if (i + 1) % (25 * 6) == 0 {
            layers.append(Layer.init(zeroes: zeroes, ones: ones, twos: twos, values: values))
            zeroes = 0
            ones = 0
            twos = 0
            values = Array<String>()
        }
    }
    
    return layers
}

func part1(inputString: String) -> Int {
    let layers = getLayers(inputString: inputString)
    
    var leastLayer = layers[0]
    for layer in layers {
        if layer.zeroes < leastLayer.zeroes {
            leastLayer = layer
        }
    }
    return leastLayer.ones * leastLayer.twos
}

func part2(inputString: String) {
    let layers = getLayers(inputString: inputString)
    var finalValues = Array<String>()
    
    for i in 0..<(25 * 6) {
        var value = "2"
        for j in 1...layers.count {
            let currentlayer = layers[layers.count - j]
            switch currentlayer.values[i] {
            case "0":
                value = " "
            case "1":
                value = currentlayer.values[i]
            default:
                break
            }
        }
        finalValues.append(value)
    }
    print(finalValues)
}

if let inputString = getInputStrings(fileUrl: URL.init(fileURLWithPath: CommandLine.arguments[1], isDirectory: false)) {
    print("Part 1: \(part1(inputString: inputString))")
    print("Part 2:")
    part2(inputString: inputString)
}
