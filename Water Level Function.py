# This function determines the amount of water (~~) collected between steel beams ([]).
# An Array that describes the hight of the steel beams is required as an input.
# Eg. A = [0, 1, 0, 3, 0, 3, 0, 2, 0, 1, 0, 2, 0, 2, 1, 2 ]
# WaterBetweenBeams(A) = 14
#         []~~[]                      3
#         []  []~~[]~~~~~~[]~~[]~~[]  2
#     []~~[]  []  []  []  []  [][][]  1
#   ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^  
def WaterBetweenBeams(InputArray):
    
    #in case of Negative Numbers
    if min(InputArray)<0:
        print("Error: Negative value in input.")
        return "Error: Negative value in input."
        
    #Create a copy of the 'InputArray'
    Array = list(InputArray)

    #Create a backwards copy of the 'InputArray'
    RevArray = list(InputArray)
    RevArray.reverse()

    #Create List 'Levels' from unique Elements in Ascending order
    Levels = list(set(Array))
    Levels.sort()

    #Find increment for each Level and add to List 'Weightings'
    PreviousLevel = 0
    LevelHeights = []
    for Level in Levels:
        LevelHeights.append(Level - PreviousLevel)
        PreviousLevel = Level

    LevelHeights.reverse()
    

    #Sort 'Levels' in decending order
    Levels.sort(reverse=True)


    #Find the first position for each Level
    FirstPostion = []
    MinIndex = len(Array)
    for BeamHeight in Levels:
        BeamIndex = Array.index(BeamHeight)
        MinIndex = min(MinIndex,BeamIndex)
        FirstPostion.append(min(MinIndex, BeamIndex))

    #Find the last position for each Level
    LastPostion = []
    MinIndex = len(Array)
    for BeamHeight in Levels:
        BeamIndex = RevArray.index(BeamHeight)
        MinIndex = min(MinIndex,BeamIndex)
        LastPostion.append(len(Array) - min(MinIndex, BeamIndex))

    #Find the length of each level
    LevelLength = [x - y for x, y in zip(LastPostion, FirstPostion)]

    #Find the area of each level
    LevelArea = [x * y for x, y in zip(LevelLength, LevelHeights)]
    
    #Area Water can only fill where beam is not
    CollectedWater = sum(LevelArea)-sum(Array)
    
    #in Case of decimals
    CollectedWater = round(CollectedWater,10)
    
    print(CollectedWater)
    return(CollectedWater)
