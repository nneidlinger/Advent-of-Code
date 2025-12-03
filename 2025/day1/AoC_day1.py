def process_rotations(file_name: str):
    zero_count: int = 0
    curr: int = 50

    try:
        with open(file_name, "r") as file:
            for rotation in file:
                direction: str = rotation[0]
                distance: int = (int)(rotation[1:])
                if distance > 99:
                    zero_count += distance // 100
                    distance = distance % 100

                #print(f"rotating {direction} by {distance}. ", end="")
            
                if direction.lower() == "l":
                    if (curr - distance < 0):
                        curr = 100 - (distance - curr)
                        zero_count += 1
                        if (curr == 0):
                            zero_count += 1
                    else:
                        curr -= distance
                        if (curr == 0):
                            zero_count += 1
                elif direction.lower() == "r":
                    if (curr + distance > 99):
                        curr = (distance + curr) - 100
                        zero_count += 1
                        if (curr == 0):
                            zero_count += 1
                    else:
                        curr += distance
                        if (curr == 0):
                            zero_count += 1
                else:
                    print(f"Error: {direction} is not a valid direction", end="\n")

                #print(f"After rotation, lock is now: {curr}", end="\n")

                
    
    except FileNotFoundError:
        print(f"Error file \"{file_name}\" not found.")
        return 0

    return zero_count

print(f"Num_rotations (Short): {process_rotations("AoC/Day1/short.txt")}")
print(f"Num_rotations (Full): {process_rotations("AoC/Day1/rotations.txt")}")
