# PRG1
PRG1 (Programming 1) is a module in semester 1.1 of the Cybersecurity and Digital Forensics(CSF) course in Ngee Ann Polytechnic. The objective of this assignmnet is to manage a farm, grow crops, and make enough money to pay off a loan within 20 days.

## Game Objective
The player has taken out a loan of $100 to buy a farm in Albatross Town. The goal is to earn enough money by farming crops to pay off the loan within 20 days. The player starts with $20, a 5x5 plot of land, and must strategically manage their resources to succeed.

## Main Features
<ul>
  <li>Main menu: Start a new game, load a saved game, or exit</li>
  <li>Shop: Buy seeds with different prices, grow times, and crop prices from the shop </li>
  <li>Farm Management: Plant seeds and harvest seeds for sale</li>
</ul>

## How to Play
<ol>
  <li>Start a New Game: Begin with $20 and 10 energy on Day 1</li>
  <li>Visit the Shop: Buy seeds from Pierce’s Seed Shop</li>
  <li>Visit the Farm (Move using WASD/ Plant/ Harvest): Plant your seeds on the farm and manage your crops</li>
  <li>End the Day: When you are done with your actions on the farm or have run out of energy, you are prompted to end the day</li>
  <li>Save/Load Game: Save your progress to a .txt file or load a saved game if available</li>
  <li>Win Condition: Have at least $100 after 20 days to win the game</li>
</ol>

### Additional Features Added
<ul>
  <li>Limited Capacity for Seed Bag: Players can carry at most 10 seeds at a time. Therefore, if they attempt to buy more seeds than the bag can carry, the purchase will be rejected.</li>
  <li>Giant Crops: If every crop in a 2x2 square on the farm is of the same type and are all ready to harvest, you can harvest all 4 of the crops using 1 Energy. You must be standing in the top left-hand corner of the 2x2 square.</li>
  <li>High Score Board: If a player wins the game, they will be prompted for their name, which will be stored in a text file along with their final profit amount. There will be an additional option in the main menu “2) Show High Scores” that will display the list of high scores on screen, sorted in descending order of profit. The game will only store the top 5 scores.</li>
</ul>

