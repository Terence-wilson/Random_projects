import random
import sys

class Player:
    
    def __init__(self, name, player_number, AI = False):
        self.total_points = 0
        self.name = name
        self.player_number = player_number
        self.AI = AI



def score_checker(bois):
    points = 0
    tot_die = sum(bois.values())
    numbers = list(bois.keys())
    if tally_dub_trips(bois):
        return 2500, 0
    if tally_dub_quad(bois):
        return 1500, 0
    if tally_trip_dubs(bois):
        return 1500, 0
    if numbers == [1, 2, 3, 4, 5, 6]:
        return 1500, 0   
    else:
        OF_points, count = tally_onesNfives(bois)
        points += OF_points
        tot_die -= count
        for num in numbers:
            if bois[num] == 3 and num != 1:
                tot_die -= 3
                points += 100 * num
            elif bois[num] == 4:
                tot_die -= 4
                points += 1000
            elif bois[num] == 5:
                tot_die -= 5
                points += 2000
            elif bois[num] == 6:
                tot_die = 0
                points += 3000
        return points, tot_die
    

def tally_onesNfives(bois):
    points = 0
    numbers = bois.keys()
    count = 0
    for num in numbers:
        if num == 1 and bois[num] != 4:
            count += 1 * bois[num]
            points += 100 * bois[num]
        elif num == 5 and bois[num] < 3:
            count += 1 * bois[num]
            points += 50 * bois[num]
    return points, count

def tally_dub_trips(bois):
    check = True
    numbers = bois.keys()
    if len(bois) == 2:    
        for num in numbers:
            if bois[num] != 3:
                check = False
                break
    else:
        check = False
    return check

def tally_trip_dubs(bois):
    check = True
    numbers = bois.keys()
    if len(bois) == 3:
        for num in numbers:
            if bois[num] != 2:
                check = False
                break
    else: 
        check = False
    return check

def tally_dub_quad(bois):
    check = True
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
    else:
        check = False
    return check

def check_funkle(bois):
    score, num = score_checker(bois)
    if score > 0:
        return False
    else: 
        return True
def construct_dict(dice):
    dice_dict = {}
    for d in dice:
        dice_dict.setdefault(d, 0)
        dice_dict[d] += 1
    return dice_dict

def al_rolls(rollnum = 100000):
    rolls = []
    dice = 1
    while dice <= 6:
            freqs = {}
            count = 0
            while count < rollnum:
                roll = construct_dict(roller(dice))
                score, num = score_checker(roll)
                freqs.setdefault((score, num), 0)
                freqs[(score, num)] += 1
                count += 1
            tot = sum(freqs.values())
            keys = list(freqs.keys())
            for key in keys:
                freqs[key] = freqs[key]/tot
            for key in range(0, len(keys)):
                if key == 0:
                    continue
                freqs[keys[key]] = round(freqs[keys[key]] + freqs[keys[key - 1]], 5)
            rolls.append(freqs)
            dice += 1
    return rolls

def calc_roll_prob(round, dice, points):
    if dice == 0:
        return 1
    return (dice/6) * (500/points)



def roller(dice = 6):
    bigun = []
    for i in range(0, dice):
        roll = random.randint(1, 6)
        bigun.append(roll)
    bigun.sort()
    return bigun

def game(player_dict_keys, final_round = False):
    input("OK, players press enter to begin!\n")
    check = True
    while check:
        if final_round == True:
            check = False
        for person in player_dict_keys:
            end_turn = False
            round_num = 1
            round_points = 0
            dice_left = 6
            person = player_dict[person]
            print("It is {}'s turn! Here are your point totals: \nTotal points: {}\nRound points: {}\n\n".format(person.name, person.total_points, round_points))
            while not end_turn:
                if person.AI:
                    if dice_left == 0:
                        dice_left = 6
                    else:
                        roll_dict = roll_AI[dice_left-1]
                        roll_prob = random.random()
                        for roll in roll_dict.keys():
                            if roll_dict[roll] > roll_prob:
                                round_points += roll[0]
                                dice_left = roll[1]
                                if roll[0] > 0:
                                    print("{} got {} Points this roll!\n".format(person.name, roll[0]))
                                else:
                                    print("{} Funkled...\n".format(person.name))
                                    end_turn = True
                                break
                        if round_points >= 500 and not end_turn:
                            probbo = calc_roll_prob(round_num, dice_left, round_points)
                            if probbo < random.random():
                                person.total_points += round_points
                                end_turn = True
                                print("{} ends with {} points\n".format(person.name, person.total_points) )
                else:
                    input("Press enter to roll")
                    print(" \n")
                    roll = roller(dice_left)
                    #roll = [7]
                    roll_dict = construct_dict(roll)
                    if check_funkle(roll_dict):
                        round_points = 0
                        print("FUNKLE!!!\n")
                        break
                    chosen_dict = {}
                    choosing = True
                    while choosing:
                        remaining_die = roll.copy()
                        numbers = input("Here is what you rolled:\n {}\nPlease select the numbers you want to keep by entering them here, no spaces:\n".format(roll))
                        print(" \n")
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
                                    on_hold = []
                                    break
                                else:
                                    remaining_die.remove(chose_num[num])
                            chose_num = []
                            chosen_dict = construct_dict(on_hold)
                            curr_score, num = score_checker(chosen_dict)
                            if curr_score == 0 or num > 0:
                                pip = input("Those are invalid choices! Would you like to end now? y/n:\n ")
                                print("\n")
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
                    print("Your total points for this round is {}\n".format(round_points))
                    if end_turn and round_points < 500:
                        print("Sorry, you have FAILED to get ANY points this round due to lack of talent.\n")
                    elif round_points >= 500:
                        pop = input("would you like to roll again? y/n: ")
                        print("\n")
                        if pop == "y" or pop == "Y":
                            if dice_left == 0:
                                dice_left = 6
                            continue
                        else:
                            person.total_points += round_points
                            print("Your total points are: {}\n".format(person.total_points))
                            end_turn = True
                    elif dice_left == 0:
                        dice_left = 6
            if not final_round:        
                if person.total_points >= 10000:
                    print("It's the final turn! Everyone gets one more round to beat {}!\n\n".format(person.name))
                    curr_winners.append(player_dict.pop(person.name))
                    player_dict_keys = list(player_dict.keys())
                    return game(player_dict_keys, final_round=True)
            else:
                if person.total_points >= 10000:
                    curr_winners.append(player_dict.pop(person.name))
                input("Your total points are: {} press ENTER.\n".format(person.total_points))
    if len(curr_winners) > 1:
        print("The winners are: {}".format([i.name for i in curr_winners]))
    else:
        print("The winner is {}!".format(curr_winners[0].name))
                        

if __name__ == "__main__":
    args = sys.argv
    dice = 6
    if len(args) > 1:
        while dice >= 1:
            freqs = {}
            count = 0
            while count < int(args[1]):
                roll = construct_dict(roller(dice))
                score, num = score_checker(roll)
                freqs.setdefault((score, num), 0)
                freqs[(score, num)] += 1
                count += 1
            tot = sum(freqs.values())
            keys = list(freqs.keys())
            for key in keys:
                freqs[key] = freqs[key]/tot
            print("point frequencies for rolls with {} dice:".format(dice))
            for key in range(0, len(keys)):
                if key == 0:
                    continue
                freqs[keys[key]] = round(freqs[keys[key]] + freqs[keys[key - 1]], 5)
            for key in keys:
                print("{}: {}".format(key, freqs[key]))
            dice -= 1
    else:       
        rule1 = "Scoring:\n   1's are worth 100pts\n   5's are worth 50pts\n   3 of a kind is worth that number times 100 with the exception of 1's\n   "
        rule1_2 = "4 of a kind is worth 1000pts alone, and 1500pts if you get it with a pair\n   5 of a kind is worth 2000pts\n   6 of a kind is worth 3000pts\n   "
        rule1_3 = "1-6 straight is worth 1500pts\n   Three pairs are worth 1500pts\n   Two triplets are worth 2500pts\n\n"
        rule2 = "Gameplay:\n   Each player rolls, and then can set aside a number of scoreable die which are totaled each round. The remaining die are rolled\n   "
        rule2_2 = "until the player reaches at least 500pts. If the player reaches 500pts they may end their turn. If the player runs out of dice, and they have \n   "
        rule2_3 = "not \"Funkled\" then they will have the choice to continue rolling starting with six die again. The goal is to reach 10000pts. \n   "
        rule3 = "Once a player reaches 10000pts the rest of the players have one more turn to catch up. whoever ends the game with 10000+ pts wins the game.\n"
        bonus = "\n\nTO PLAY AGAINST AN AI: set player number to 1. To see 2 AI duke it out, set player number to 1 and name yourself ALY\n"
        print("\nHere are the rules to this game:\n\n" + rule1 + rule1_2 + rule1_3 + rule2 + rule2_2 + rule2_3 + rule3 + bonus)
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
                    if player_name == "ALY":
                        player_dict["ALY"].AI = True
                else: 
                    print("Please stop being a dick!\n\n")
        if players < 2:
            print("You will be playing against AL! He is the resident AI, though intelligence isn't really his thing...")
            roll_AI = al_rolls()
            player_dict["AL"] = Player("AL", 2, True)
        curr_winners = []
        player_dict_keys = list(player_dict.keys())
        game(player_dict_keys)
