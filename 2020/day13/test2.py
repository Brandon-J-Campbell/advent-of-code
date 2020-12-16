puzzle = open('input.txt').read().splitlines()
depart = int(puzzle[0])
buses = [(int(bus_interval), bus_time % int(bus_interval))
         for bus_time, bus_interval in enumerate(puzzle[1].split(','))
         if bus_interval != 'x']
print(buses)
print(int.__mul__(*min(((val, val - depart % val) for val, _ in buses),
                  key=lambda x: x[1])))

final_time = buses[0][0] - buses[0][1]
delta = final_time
for bus_interval, bus_time in buses[1:]:
    starting_time = bus_interval - final_time % bus_interval
    current_time = final_time
    cycle = 1
    while True:
        if bus_interval - current_time % bus_interval == bus_time:
            final_time = current_time
        current_time += delta
        if bus_interval - current_time % bus_interval == starting_time:
            break
        cycle += 1
    delta *= cycle
print(final_time)
