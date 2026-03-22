name = input("Enter the player's name: ")
numOfGamesPly = int(input("Number of games played : "))
totalScore = int(input("Total score achieved : "))
averageScore = totalScore / numOfGamesPly

print(f"\nPlayer: {name}")
print(f"\nGames Played: {numOfGamesPly}")
print(f"\nTotal Score: {totalScore}")
print(f"\nAverage Score: {averageScore}")
#round only two values
print(f"\nAverage Score: {averageScore:.2f}")