import random
import sys

class Player:
    
    def __init__(self, name, player_number):
        self.total_points = 0
        self.name = name
        self.player_number = player_number



def score_checker(bois):
    points = 0
    numbers = bois.keys()
    points += tally_dub_trips(bois)
    points += tally_dub_quad(bois)
    if numbers == [1, 2, 3, 4, 5, 6]:
        points = 1500
        return points
    elif len(numbers) == 3:
        check = True
        for num in numbers:
            if bois[num] != 2:
                check = False
                break
        if check == True:
            points = 1500
            return points
    else:
        points += tally_onesNfives(bois)
        for num in numbers:
            if bois[num] == 3:
                points += 100 * num
            elif bois[num] == 4:
                points += 1000
            elif bois[num] == 5:
                points += 2000
            elif bois[num] == 6:
                points += 3000
        return points

def tally_onesNfives(bois):
    points = 0
    numbers = bois.keys()
    for num in numbers:
        if num == 1 and bois[num] < 4:
            points += 100 * bois[num]
        elif num == 5 and bois[num] < 3:
           points += 50 * bois[num]
    return points

def tally_dub_trips(bois):
    check = True
    points = 0
    numbers = bois.keys()
    if len(bois) == 2:    
        for num in numbers:
            if bois[num] != 3:
                check = False
                break
        if check == True:
            points = 2500
    return points

def tally_dub_quad(bois):
    check = True
    points = 0
    numbers = bois.keys()
    too = 2
    form = 4
    if len(bois) == 2:
        for num in numbers:
            if bois[num] != too:
                if bois[num] != form:
                    check = False
                    break
                else:
                    form = 2
            else: too = 4
        if check == True:
            points = 1500
    return points
    



def roller(dice = 6):
    bigun = []
    for i in range(0, dice):
        roll = random.randint(1, 6)
        bigun.append(roll)
    bigun.sort()
    return bigun


if __name__ == "__main__":
    players = input("Please input a number of players between 1 and 6:\n")
    player_dict = {}
    try:
        players = int(players)
    except ValueError:
        None
    while type(players) is not int or (1 > players or players > 6):
            players = input("Please input a number of players between 1 and 6:\n")
            try:
                players = int(players)
            except ValueError:
                continue    
    for i in range(1, players + 1):
        while len(player_dict) < i:
            player_name = input("What is player {0}'s name?\n".format(str(i)))
            if player_name not in player_dict.keys():
                player_dict[player_name] = Player(player_name, i)
            else: 
                print("Please stop being a dick!")
    
    input("OK, players press enter to begin!")
    check = True
    winner_ind = 9
    while check:
        for person in player_dict:
            end_turn = False
            round_points = 0
            dice_left = 6
            person = player_dict[person]
            print("It is {}'s turn! Here are your point totals: \nTotal points: {}\nRound points: {}\n".format(person.name, person.total_points, round_points))
            while not end_turn:
                input("Press enter to roll")
                roll = roller(dice_left)
                chosen_dict = {}
                choosing = True
                while choosing:
                    remaining_die = roll.copy()
                    numbers = input("Here is what you rolled:\n {}\nPlease select the numbers you want to keep by entering them here, no spaces:\n".format(roll))
                    numbers = str(numbers)
                    on_hold = []
                    chose_num = []
                    while on_hold == []:
                        breaknow = False
                        for i in numbers:
                            try:
                                on_hold.append(int(i))
                                chose_num.append(int(i))
                            except ValueError:
                                pass
                        for num in range(0, len(chose_num)):
                            if chose_num[num] not in remaining_die:
                                print("Please only enter numbers in your roll!")
                                on_hold = []
                                break
                            else:
                                remaining_die.remove(chose_num[num])
                        chose_num = []
                        for d in on_hold:
                            chosen_dict.setdefault(d, 0)
                            chosen_dict[d] += 1
                        curr_score = score_checker(chosen_dict)
                        if curr_score == 0:
                            pip = input("Those are invalid choices! Would you like to end now? y/n: ")
                            if pip == "n" or pip == "N":
                                on_hold = [7]
                            else:
                                end_turn = True
                                choosing = False
                                on_hold = [7]
                                if round_points >= 500:
                                    person.total_points += round_points
                        else:
                            round_points += curr_score
                            dice_left = len(remaining_die)
                            choosing = False
                print("Your total points for this round is {}".format(round_points))
                if end_turn and round_points < 500:
                    print("Sorry, you have FAILED to get ANY points this round due to lack of talent.")
                elif round_points >= 500:
                    pop = input("would you like to roll again? y/n: ")
                    if pop == "y" or pop == "Y":
                        if dice_left == 0:
                            dice_left = 6
                        continue
                    else:
                        person.total_points += round_points
                        end_turn = True
                elif dice_left == 0:
                    dice_left = 6

            input("Your total points are: {} press ENTER for next turn.".format(person.total_points))
                        



