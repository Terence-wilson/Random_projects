import random

names = ['Acid', 'Phantom', 'Lord', 'Zero', 'Bro', 'Skizo', 'Crash', 'Bit', 'Hex', 'Salt', 
'Hash', 'DOS', 'BIOS', 'Gold', 'Zip', 'Override', 'Phreak', 'Worm', 'Lag', 'dDOS', 'Boss', 'Teddy', 'Optic', 'Flow', 
'Error', 'Box', 'Terminal', 'Rogue', 'Proxy', 'Doc', 'GNU', 'Wiz', 'Angel', 'Chaos', 'Root', 'Toor', 
'Gimp', 'Crypto', 'Black', 'King', 'Gear', 'Metal', 'Sys', 'Dev/', '/Null', 'Retro', 'Default', 'Admin',
'Alt', 'CTRL',  'Net', 'Bot', 'Jack', 'Terminal', 'Giga', 'Byte', 'Kitty', 'Pirate', 'Node', 'Port',
'Virus', 'Flash', 'IP', 'Mac', '0Day', 'Alpha', 'Omega', 'Techno', 'Void', 'Binary', 'Cipher', 'Worm', 
'Payload', 'Data', 'Lag', 'Chungus', 'Donger', 'Script', 'Angle', 'Devil', 'Demon', 'Imp', 
'Hell', 'Bash', 'Code', 'Program', 'Bool', 'Bug', 'Hardcode', 'Loop', 'Package', 'Spoof', '', 'Overflow',
'Gnome', 'Plasma', 'Wolf', 'Hawk', 'Mega', 'Snake', 'Weeb', 'Shadow', '-', 'Death',
'Reaper', 'Shell', 'Power', 'Daemon', 'Joker', 'Boot', 'Bus', 'Cookie', 'LAN', 'WiFi', '.']
alphaDict = {'a':['Acid', 'Phantom', 'Lord', 'Zero'], 
'b':['Bro', 'Skizo', 'Crash', 'Bit'], 
'c':['Hex', 'Salt', 'Hash', 'DOS', 'BIOS'], 
'd':['Gold', 'Zip', 'Override', 'Phreak'], 
'e':['Worm', 'Lag', 'dDOS', 'Optic', 'Teddy'], 
'f':['Boss', 'Flow', 'Error', 'Box', 'Doc'], 
'g':['Rogue', 'Proxy', 'Terminal', 'GNU'], 
'h':['Wiz', 'Angel', 'Chaos', 'Root'], 
'i':['Toor', 'Alpha', 'Crypto', 'Black'], 
'j':['King', 'Gear', 'Metal', 'Sys'], 
'k':['Dev', 'Null', 'Retro', 'Default'], 
'l':['Admin', 'Alt', 'CTRL',  'Net'], 
'm':['Bot', 'Jack', 'Terminal', 'Giga'], 
'n':['Byte', 'Kitty', 'Pirate', 'Node', 'Port'], 
'o':['Virus', 'Flash', 'IP', 'Mac', 'WiFi'], 
'p':['0Day', 'Tux', 'Omega', 'Techno'], 
'r':['Shark', 'Binary', 'Cipher', 'Worm'], 
's':['Payload', 'Data', 'Lag', 'Script'], 
'q':['Chungus', 'Donger', 'Angle', 'Devil'], 
't':['Daemon', 'Imp', 'Hell', 'Bash'], 
'u':['Code', 'Program', 'Bool', 'Bug', 'LAN'], 
'v':['Hardcode', 'Loop', 'Package', 'Spoof'], 
'w':['', 'Overflow', 'Gnome', 'Plasma', 'Cookie'], 
'x':['Wolf', 'Hawk', 'Mega', 'Snake', 'Weeb'], 
'y':['Shadow', '-', 'Death', 'Reaper', 'Bus'], 
'z':['Shell', 'Power', 'Demon', 'Joker', 'Boot']}
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
firstNames = ['Killer', 'Auto', 'Serial', 'Embedded', 'Captain', '/', '.', 'Void']
leetDict = {'e':'3', 'a':'4', 's':'5', 'ate':'8', 'at':'@', 'o':'0', 'l':'1', 'i':'!',
'b':'6', 'z':'2'}

leetLetterPerc = 50
LeetSpeekPerc = 30
i = 10
firstNamePerc = 10


def word(words):
    return words[random.randint(0, len(words)-1)]

def randGen(percent):
    num = random.randint(0, 99)
    if num < percent:
        return True
    return False

def leetSpeeker(words):
    leetWord = ''
    for char in words:
        tempchar = char
        char = char.lower()
        if char in leetDict.keys() and randGen(leetLetterPerc):
            if char == 's' and randGen(50):
                leetWord = leetWord + '$'
            else:
                leetWord = leetWord + leetDict[char]
        else:
            leetWord = leetWord + tempchar
    return leetWord

def calcTot(x):
    tot = 0
    for i in x:
        tot = tot + alpha.index(i)
    return tot

def byName(hacker):
    hackerName = ''
    hackerF = hacker.split()[0].lower()
    hackerS = hacker.split()[1].lower()
    nmlstF = alphaDict[hackerF[0]]
    nmlstS = alphaDict[hackerS[0]]
    fTot = calcTot(hackerF)
    if fTot%10 == 7 or fTot%10 == 3:
        if fTot%10 == len(hackerF):
            hackerName = hackerName + leetSpeeker(firstNames[fTot%(len(firstNames))])
        else:
            hackerName = hackerName + (firstNames[fTot%(len(firstNames))])
    else:
        hackerName = hackerName + nmlstF[fTot%(len(nmlstF))]
    
    sTot = calcTot(hackerS)

    hackerName = hackerName + ' '

    if sTot%10 == len(hackerS):
        hackerName = hackerName + leetSpeeker(nmlstS[sTot%(len(nmlstS))])
    else:
        hackerName = hackerName + nmlstS[sTot%(len(nmlstS))]
    return hackerName


def maker():
    if randGen(firstNamePerc):
        first = word(firstNames)
    else:
        first = word(names)
    second = word(names)
    while first == second:
        second = word(names)
    if first == ' ' or first == '-' or first == '/' or first == '.' or second == ' ' or second == '-' or second == '/' or second == '.':
        name = first + second
    else:
        name = first + " " + second
    if randGen(LeetSpeekPerc):
        return leetSpeeker(name)
    return name

hacker = input("What is you name, H4xor? \n")

if not hacker or hacker == 'no':
    print("\n")
    while i > 0:
        ret = maker()
        if ret:
            print(ret)
            i = i - 1
else:
	print(byName(hacker))




