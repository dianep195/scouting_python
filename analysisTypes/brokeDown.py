import statistics
import numpy as np
# ******************** AnalysisTypeID = 21 = brokeDown *******************

def brokeDown(analysis, rsRobotMatches, brokeDownList=None):
    # Initialize the rsCEA record set and define variables specific to this function which lie outside the for loop
    rsCEA = {}
    rsCEA['AnalysisTypeID'] = 21
    numberOfMatchesPlayed = 0

    lostCommList = []

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
            lostComm = matchResults[analysis.columns.index('SummBrokeDown')]
            if brokeDown is None:
                brokeDown = 0
            if brokeDown == 0:
                brokeDownString = 'No'
            else:
                brokeDownString = 'Yes'

            # Perform some calculations
            numberOfMatchesPlayed += 1

            brokeDownList.append(brokeDown)

            # Create the rsCEA records for Display, Value, and Format
            rsCEA['Match' + str(matchResults[analysis.columns.index('TeamMatchNo')]) + 'Display'] = brokeDownString
            rsCEA['Match' + str(matchResults[analysis.columns.index('TeamMatchNo')]) + 'Value'] = brokeDown
            if brokeDown == 0:
                rsCEA['Match' + str(matchResults[analysis.columns.index('TeamMatchNo')]) + 'Format'] = 4
            else:
                rsCEA['Match' + str(matchResults[analysis.columns.index('TeamMatchNo')]) + 'Format'] = 2

    # Create summary data
    if numberOfMatchesPlayed > 0:
        # Summary1 is the % of matches where they broke down
        rsCEA['Summary1Display'] = np.sum(brokeDownList) / numberOfMatchesPlayed * 100

    return rsCEA