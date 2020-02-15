import statistics
import numpy as np
# ******************** AnalysisTypeID = 20 = lostComm *******************

def subSystemBroke(analysis, rsRobotMatches):
    # Initialize the rsCEA record set and define variables specific to this function which lie outside the for loop
    rsCEA = {}
    rsCEA['AnalysisTypeID'] = 22
    numberOfMatchesPlayed = 0

    subSystemBrokeList = []

    # Loop through each match the robot played in.
    for matchResults in rsRobotMatches:
        rsCEA['Team'] = matchResults[analysis.columns.index('Team')]
        rsCEA['EventID'] = matchResults[analysis.columns.index('EventID')]
        autoDidNotShow = matchResults[analysis.columns.index('AutoDidNotShow')]
        scoutingStatus = matchResults[analysis.columns.index('ScoutingStatus')]
        # Skip if DNS or UR
        if autoDidNotShow == 1:
            rsCEA['Match' + str(matchResults[analysis.columns.index('TeamMatchNo')]) + 'Display'] = ''
        elif scoutingStatus == 2:
            rsCEA['Match' + str(matchResults[analysis.columns.index('TeamMatchNo')]) + 'Display'] = ''
        else:
            # Retrieve values from the matchResults and set to appropriate variables
            subSystemBroke = matchResults[analysis.columns.index('SummSubSystemBroke')]
            if subSystemBroke is None:
                subSystemBroke = 0
            if subSystemBroke == 0:
                subSystemBrokeString = 'No'
            else:
                subSystemBrokeString = 'Yes'

            # Perform some calculations
            numberOfMatchesPlayed += 1
            subSystemBrokeList.append(subSystemBroke)

            # Create the rsCEA records for Display, Value, and Format
            rsCEA['Match' + str(matchResults[analysis.columns.index('TeamMatchNo')]) + 'Display'] = subSystemBrokeString
            rsCEA['Match' + str(matchResults[analysis.columns.index('TeamMatchNo')]) + 'Value'] = subSystemBroke
            if subSystemBroke == 0:
                rsCEA['Match' + str(matchResults[analysis.columns.index('TeamMatchNo')]) + 'Format'] = 4
            else:
                rsCEA['Match' + str(matchResults[analysis.columns.index('TeamMatchNo')]) + 'Format'] = 2

    # Create summary data
    if numberOfMatchesPlayed > 0:
        # Summary1 is the % of matches where they lost Comm
        rsCEA['Summary1Display'] = np.sum(subSystemBrokeList) / numberOfMatchesPlayed * 100

    return rsCEA
