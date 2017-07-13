# -*- coding: utf-8 -*-
"""
Well I'm gonna try to put all of the py files in the same thing for the executable
"""

'''
These functions are used for the Motivation and Reaction in the GUI

Initially I was also going to have a rumor generator, and I kind of do but
I thought it was more information than necessary because they could be pretty
long and weren't something useable while actually running the session

The way that these work is that it chooses from the toggles on, let's say you
have Information checked in the Reaction menu, it selects the string:
    'Indifferent but helpful. The NPC localinformation(b).'
    
When ReactionGen gets to the line 
    String = BCheck(String)
    
BCheck finds that the string 'localinformation(b)' corresponds to the table found in
    'Tables/Rumors/B-LocalInformation.txt'
    
and chooses a random line from that table, for example
    'tells of majorboon(h) concerning the area'
    
When BCheck gets to the line
    String = HCheck(String)

it then finds a random line from the table found in
    'Tables/Rumors/H-MajorBoon.txt'

and so on.
    
'''


import random
import os
import os.path
import csv
import Tkinter as tk
import xlsxwriter
import datetime
ScriptDir = os.path.dirname(__file__)

####################################
# These functions use the NPC motivation, area, and reaction
# tables found on R/BehindTheTables as well as various
# rumor generators found there as well
####################################

def RandomTable(Table):
    '''
    This function is used to get a random string from a file in the 
    rumors folder.  Put the table's name in as a string without .txt
    Note: I SHOULD HAVE FIGURED THIS OUT LIKE 3 FUCKING WEEKS AGO
    '''
    Path = 'Tables/Rumors/' + Table + '.txt'
    Path = os.path.join(ScriptDir, Path)
    String = random.choice(open(Path).readlines())
    return String.strip('\n')
    
def ReactionGen(Toggles):
    '''
    This generates a random reaction from the the choices given in the GUI:
        Hostile
        Unhappy
        Disgruntled
        Indifferent
        Pleased
        Happy
        Friendly
    It uses the following secondary tables
        A
        B
        E
        F
        G
        H
    '''
    
    Active = []
    Hostile = Toggles[0]
    Unhappy = Toggles[1]
    Disgruntled = Toggles[2]
    Indifferent = Toggles[3]
    Pleased = Toggles[4]
    Happy = Toggles[5]
    Friendly = Toggles[6]
    
    Total = Hostile + Unhappy + Disgruntled + Indifferent + Pleased + Happy + Friendly
    if (Total == 0):
        return 'No options selected, right click on the button.'
    
    if (Hostile == 1):
        Active.append(1)
    if (Unhappy == 1):
        Active.append(2)
    if (Disgruntled == 1):
        Active.append(3)
    if (Indifferent == 1):
        Active.append(4)
    if (Pleased == 1):
        Active.append(5)
    if (Happy == 1):
        Active.append(6)
    if (Friendly == 1):
        Active.append(7)
        
    ReactionNum = random.choice(Active)
    if (ReactionNum == 1):
        String = 'Hostile. Now the NPC is a nemesis. He/she causes majorbane(f) and will pursue the PC until one them is dead.'
    elif (ReactionNum == 2):
        String = 'Unhappy. The NPC causes minorbane(e). There is an 80% chance his/her attitude will shift to hostile on next encounter.'
    elif (ReactionNum == 3):
        String = 'Disgruntled. The NPC gives a false rumor. There is a 40% chance his/her attitude will shift to unhappy on next encounter.'
    elif (ReactionNum == 4):
        infoNum = random.randint(1,3)
        if (infoNum == 1):
            String = 'Indifferent but helpful. The NPC personalinformation(a) or localinformation(b), as requested.'
        elif (infoNum == 2):
            String = 'Indifferent but helpful. The NPC localinformation(b).'
        elif (infoNum == 3):
            String = 'Indifferent but helpful. The NPC personalinformation(a).'
    elif (ReactionNum == 5):
        String = 'Pleased. The NPC shares a specific rumor. There is a 40% chance his/her attitude will shift to happy on next encounter.'
    elif (ReactionNum == 6):
        String = 'Happy. The NPC gives minorboon(g). There is an 80% chance his/her attitude will shift to friendly on next encounter.'
    elif (ReactionNum == 7):
        String = 'Friendly. The NPC is now an ally. He/she gives majorboon(h) and will protect the PC with his/her life.'
    
    String = FCheck(String)
    String = ECheck(String)
    String = ACheck(String)
    String = BCheck(String)
    String = HCheck(String)
    String = GCheck(String)
    return String

def MotivationGen(Toggles):
    '''
    This generates a random motivation from the the choices given in the GUI:
        OnTheRun
        Vendetta
        Information
        BuyingOrSelling
        LocalQuest
        QuestEnemy
        QuestTreasure
    It uses the following secondary tables
        A
        B
        C
        I
        J
        K
        L
        M
        N
        O
        P
        Q
        R
        U
    '''
    
    Active = []
    OnTheRunMotivation = Toggles[0]
    VendettaMotivation = Toggles[1]
    InformationMotivation = Toggles[2]
    BuyingOrSellingMotivation = Toggles[3]
    LocalQuestMotivation = Toggles[4]
    QuestEnemyMotivation = Toggles[5]
    QuestTreasureMotivation = Toggles[6]
    
    Total = OnTheRunMotivation + VendettaMotivation + InformationMotivation\
    + BuyingOrSellingMotivation + LocalQuestMotivation + QuestEnemyMotivation\
    + QuestTreasureMotivation
    if (Total == 0):
        return 'No options selected, right click on the button.'
    
    if (OnTheRunMotivation == 1):
        Active.append(1)
    if (VendettaMotivation == 1):
        Active.append(2)
    if (InformationMotivation == 1):
        Active.append(3)
    if (BuyingOrSellingMotivation == 1):
        Active.append(4)
    if (LocalQuestMotivation == 1):
        Active.append(5)
    if (QuestEnemyMotivation == 1):
        Active.append(6)
    if (QuestTreasureMotivation == 1):
        Active.append(7)
        
    MotivationNum = random.choice(Active)
    if (MotivationNum == 1):
        infoNum = random.randint(1,3)
        if (infoNum == 1):
            String = 'The NPC is on the run after ontherun(j) minorenemy(q) for evildeeds(p).'
        elif (infoNum == 2):
            String = 'The NPC is on the run after ontherun(j) majorenemy(r) for evildeeds(p).'
        elif (infoNum == 3):
            String = 'The NPC is on the run after ontherun(j) minorenemy(q) for gooddeeds(o).'
            
    elif (MotivationNum == 2):
        infoNum = random.randint(1,4)
        if (infoNum == 1):
            String = 'vendetta(i) majorenemy(r).'
        elif (infoNum == 2):
            String = 'vendetta(i) majorenemy(r).'
        elif (infoNum == 3):
            String = 'vendetta(i) minorenemy(q).'
        elif (infoNum == 4):
            String = 'vendetta(i) minorenemy(q).'
            
    elif (MotivationNum == 3):
        infoNum = random.randint(1,3)
        if (infoNum == 1):
            String = 'The NPC personalinformation(a).'
        elif (infoNum == 2):
            String = 'The NPC localinformation(b).'
        elif (infoNum == 3):
            String = 'The NPC is searching for iteminformation(c).'
            
    elif (MotivationNum == 4):
        infoNum = random.randint(1,3)
        if (infoNum == 1):
            String = 'The NPC is selling buyingorselling(k) at a nearby location, then returning to his/her home in home(l).'
        elif (infoNum == 2):
            String = 'The NPC is buying buyingorselling(k) at a nearby location, then returning to his/her home in home(l).'
        elif (infoNum == 3):
            String = 'The NPC is buying and selling buyingorselling(k) at a nearby location, then returning to his/her home in home(l).'
            
    elif (MotivationNum == 5):
        String = 'The NPC is on a local quest to minorquest(m) for a treasure(u).'
        
    elif (MotivationNum == 6):
        infoNum = random.randint(1,4)
        if (infoNum == 1):
            String = 'The NPC is on a quest to majorquest(n) for minorenemy(q).'
        elif (infoNum == 2):
            String = 'The NPC is on a quest to minorquest(m) for minorenemy(q).'
        elif (infoNum == 3):
            String = 'The NPC is on a quest to minorquest(m) for majorenemy(r).'
        elif (infoNum == 4):
            String = 'The NPC is on a quest to majorquest(n) for majorenemy(r).'
        
    elif (MotivationNum == 7):
        infoNum = random.randint(1,2)
        if (infoNum == 1):
            String = 'The NPC is on a quest to minorquest(m) for a treasure(u).'
        elif (infoNum == 2):
            String = 'The NPC is on a quest to majorquest(n) for a treasure(u).'
            
    String = JCheck(String)
    String = QCheck(String)
    String = RCheck(String)
    String = OCheck(String)
    String = PCheck(String)
    String = ICheck(String)
    String = ACheck(String)
    String = BCheck(String)
    String = CCheck(String)
    String = KCheck(String)
    String = LCheck(String)
    String = MCheck(String)
    String = UCheck(String)
    String = NCheck(String)
    return String

def Area():
    String = RandomTable('Area')
    String = AACheck(String)
    String = BBCheck(String)
    String = DCheck(String)
    String = UCheck(String)
    String = SCheck(String)
    String = TCheck(String)
    return String

def ACheck(String):
    if ('personalinformation(a)' in String):
        PersonalInformation = RandomTable('A-PersonalInformation')
        String = String.replace('personalinformation(a)',PersonalInformation)
    String = GCheck(String)
    String = VCheck(String)
    String = QCheck(String)
    String = RCheck(String)
    String = WCheck(String)
    return String

def BCheck(String):
    if ('localinformation(b)' in String):
        PersonalInformation = RandomTable('B-LocalInformation')
        String = String.replace('localinformation(b)',PersonalInformation)
    String = GCheck(String)
    String = LCheck(String)
    String = HCheck(String)
    String = VCheck(String)
    String = RCheck(String)
    String = QCheck(String)
    String = YCheck(String)
    String = ZCheck(String)
    String = FCheck(String)
    String = XCheck(String)
    return String

def CCheck(String):
    if ('iteminformation(c)' in String):
        NewString = RandomTable('C-ItemInformation')
        String = String.replace('iteminformation(c)',NewString)
    String = C1Check(String)
    String = C2Check(String)
    String = C3Check(String)
    String = C4Check(String)
    String = C5Check(String)
    String = C6Check(String)
    String = C7Check(String)
    String = C8Check(String)
    return String

def C1Check(String):
    if ('artifact(c1)' in String):
        NewString = RandomTable('C1-Artifact')
        String = String.replace('artifact(c1)',NewString)
    return String

def C2Check(String):
    if ('object(c2)' in String):
        NewString = RandomTable('C2-Object')
        String = String.replace('object(c2)',NewString)
    return String

def C3Check(String):
    if ('book(c3)' in String):
        NewString = RandomTable('C3-Book')
        String = String.replace('book(c3)',NewString)
    return String

def C4Check(String):
    if ('armor(c4)' in String):
        NewString = RandomTable('C4-Armor')
        String = String.replace('armor(c4)',NewString)
    return String

def C5Check(String):
    if ('weapon(c5)' in String):
        NewString = RandomTable('C5-Weapon')
        String = String.replace('weapon(c5)',NewString)
    return String

def C6Check(String):
    if ('implement(c6)' in String):
        NewString = RandomTable('C6-Implement')
        String = String.replace('implement(c6)',NewString)
    return String

def C7Check(String):
    if ('art(c7)' in String):
        NewString = RandomTable('C7-Art')
        String = String.replace('art(c7)',NewString)
    return String

def C8Check(String):
    if ('prosthesis(c8)' in String):
        NewString = RandomTable('C8-Prosthesis')
        String = String.replace('prosthesis(c8)',NewString)
    return String

def DCheck(String):
    if ('faction(d)' in String):
        NewString = RandomTable('D-Faction')
        String = String.replace('faction(d)',NewString)
    String = CCCheck(String)
    return String

def ECheck(String):
    if ('minorbane(e)' in String):
        NewString = RandomTable('E-MinorBane')
        String = String.replace('minorbane(e)',NewString)
    String = QCheck(String)
    String = RCheck(String)
    String = TCheck(String)
    String = SCheck(String)
    return String

def FCheck(String):
    if ('majorbane(f)' in String):
        NewString = RandomTable('F-MajorBane')
        String = String.replace('majorbane(f)',NewString)
    String = RCheck(String)
    return String

def GCheck(String):
    if ('minorboon(g)' in String):
        NewString = RandomTable('G-MinorBoon')
        String = String.replace('minorboon(g)',NewString)
    String = QCheck(String)
    String = RCheck(String)
    return String

def HCheck(String):
    if ('majorboon(h)' in String):
        NewString = RandomTable('H-MajorBoon')
        String = String.replace('majorboon(h)',NewString)
    String = UCheck(String)
    String = C1Check(String)
    return String

def ICheck(String):
    if ('vendetta(i)' in String):
        NewString = RandomTable('I-Vendetta')
        String = String.replace('vendetta(i)',NewString)      
    return String

def JCheck(String):
    if ('ontherun(j)' in String):
        NewString = RandomTable('J-OnTheRun')
        String = String.replace('ontherun(j)',NewString)
    String = CCCheck(String)
    return String

def KCheck(String):
    if ('buyingorselling(k)' in String):
        NewString = RandomTable('K-BuyingOrSelling')
        String = String.replace('buyingorselling(k)',NewString)      
    return String

def LCheck(String):
    if ('home(l)' in String):
        NewString = RandomTable('L-Homeland')
        String = String.replace('home(l)',NewString)      
    return String

def MCheck(String):
    if ('minorquest(m)' in String):
        NewString = RandomTable('M-MinorQuest')
        String = String.replace('minorquest(m)',NewString)
    String = UCheck(String)
    return String

def NCheck(String):
    if ('majorquest(n)' in String):
        NewString = RandomTable('N-MajorQuest')
        String = String.replace('majorquest(n)',NewString)
    String = C1Check(String)
    return String

def OCheck(String):
    if ('gooddeeds(o)' in String):
        NewString = RandomTable('O-GoodDeeds')
        String = String.replace('gooddeeds(o)',NewString)
    String = C1Check(String)
    return String

def PCheck(String):
    if ('evildeeds(p)' in String):
        NewString = RandomTable('P-EvilDeeds')
        String = String.replace('evildeeds(p)',NewString)
    return String

def QCheck(String):
    if ('minorenemy(q)' in String):
        NewString = RandomTable('Q-MinorEnemy')
        String = String.replace('minorenemy(q)',NewString)
    return String

def RCheck(String):
    if ('majorenemy(r)' in String):
        NewString = RandomTable('R-MajorEnemy')
        String = String.replace('majorenemy(r)',NewString)
    return String

def SCheck(String):
    if ('haunted(s)' in String):
        NewString = RandomTable('S-Haunted')
        String = String.replace('haunted(s)',NewString)
    return String

def TCheck(String):
    if ('curse(t)' in String):
        NewString = RandomTable('T-Cursed')
        String = String.replace('curse(t)',NewString)
    return String

def UCheck(String):
    if ('treasure(u)' in String):
        NewString = RandomTable('U-Treasure')
        String = String.replace('treasure(u)',NewString)  
    String = C1Check(String)
    return String

def VCheck(String):
    if ('emergency(v)' in String):
        NewString = RandomTable('V-Emergency')
        String = String.replace('emergency(v)',NewString)
    return String

def WCheck(String):
    if ('warning(w)' in String):
        NewString = RandomTable('W-Warning')
        String = String.replace('warning(w)',NewString)
    return String

def XCheck(String):
    if ('socialevent(x)' in String):
        NewString = RandomTable('X-SocialEvents')
        String = String.replace('socialevent(x)',NewString)
    String = X1Check(String)
    return String

def X1Check(String):
    if ('familyevent(x1)' in String):
        NewString = RandomTable('X1-FamilyEvents')
        String = String.replace('familyevent(x1)',NewString)
    return String

def YCheck(String):
    if ('politicalevent(y)' in String):
        NewString = RandomTable('Y-PoliticalEvents')
        String = String.replace('politicalevent(y)',NewString)
    return String

def ZCheck(String):
    if ('religiousevent(z)' in String):
        NewString = RandomTable('Z-ReligiousEvents')
        String = String.replace('religiousevent(z)',NewString)
    return String

def AACheck(String):
    if ('faithtouched(aa)' in String):
        NewString = RandomTable('AA-Faithtouched')
        String = String.replace('faithtouched(aa)',NewString)
    return String

def BBCheck(String):
    if ('weavetouched(bb)' in String):
        NewString = RandomTable('BB-Weavetouched')
        String = String.replace('weavetouched(bb)',NewString)
    return String

def CCCheck(String):
    if ('mysterycult(cc)' in String):
        NewString = RandomTable('CC-MysteryCult')
        String = String.replace('mysterycult(cc)',NewString)
    String = CC1Check(String)
    String = CC2Check(String)
    return String

def CC1Check(String):
    if ('(cc1)' in String):
        NewString = RandomTable('CC1-Diety')
        String = String.replace('(cc1)',NewString)      
    return String

def CC2Check(String):
    if ('(cc2)' in String):
        NewString = RandomTable('CC2-Locals')
        String = String.replace('(cc2)',NewString)      
    return String

def RumorGen():
    '''
    This was going to be used but I didn't think it was very useful since
    the NPC's reaction and motivation are already more than I typically use
    '''
    RumorNum = random.randint(1,3)
    if (RumorNum == 1):
        String = BasicRumor()
    elif (RumorNum == 2):
        String = PoliticalRumor()
    else:
        String = StrangeCrimeRumor()
    return String

def BasicRumor():
    String = 'I heard that, ' + RandomTable('Rumor-When') + ', ' + RandomTable('Rumor-Who') \
    + ' was seen with ' + RandomTable('Rumor-WhoOrWhat') + ' down near ' + RandomTable('Rumor-Where') \
    + ' and nearby there was ' + RandomTable('Rumor-WhoOrWhat2') + '. I heard it from ' \
    + RandomTable('Rumor-Who2') + ', so it ' + RandomTable('Rumor-Veracity') + '.'
    return String

def PoliticalRumor():
    String = RandomTable('Political-Center') + ' ' + RandomTable('Political-Relation')\
    + ' is trying to ' + RandomTable('Political-Plot') + '. They '\
    + RandomTable('Political-WillDo') + ' and it\'s all because '\
    + RandomTable('Political-Motivation') + '. I ' + RandomTable('Political-Heard')
    if ('motivation1()' in String):
        Motivation = RandomTable('Political-Motivation1')
        String = String.replace('motivation1()',Motivation)
    if ('relation()' in String):
        Relation = RandomTable('Political-Relation')
        String = String.replace('relation()',Relation)
    return String

def StrangeCrimeRumor():
    String = RandomTable('StrangeCrime-VictimType') + ' ' + RandomTable('StrangeCrime-Origin')\
    + ' ' + RandomTable('StrangeCrime-Victim') + ' is believed to have been ' + RandomTable('StrangeCrime-Crime')\
    + ' ' + RandomTable('StrangeCrime-Location') + ' ' + RandomTable('StrangeCrime-Circumstances')\
    + ' The case is being handled by ' + RandomTable('StrangeCrime-Investigators')\
    + ' who are ' + RandomTable('StrangeCrime-Interest') + ' solving it and ' + RandomTable('StrangeCrime-Willingness')\
    + ' share details. ' + RandomTable('StrangeCrime-Source') + ' a connection to '\
    + RandomTable('StrangeCrime-Clue') + '.'
    return String

'''
These functions are the meat of the random generation.

Table of Contents:
    1. Excel functions
    2. Functions that take in the toggles from the GUI and then randomly choose
       from between them, they call other functions
    3. Face Description functions
    4. Physical Description functions
    5. Accessory Description functions
    6. Voice functions
    7. Calm and Stressed Trait functions
    8. Mood functions
    9. Profession functions
    10. Human specific functions
    11. Elf specific functions
    12. Dwarf specific functions
    13. Halfling specific functions
    14. Dragonborn specific functions
    15. Gnome specific functions
    16. Half-Elf specific functions
    17. Half-Orc specific functions
    18. Tiefling specific functions
    
'''

###############################################################################  
#   SECTION 1:                                                                #
#   Function definitions                                                      #
###############################################################################



#####################################
#        Begin excel functions      #
#####################################
    
def ExcelWrite(NameList,n1,wb,Name,Age,Gender,Race,FaceDescription,\
                PhysicalDescription,AccessoriesDescription,VoiceSpeed,\
                VoiceQuality,Profession,CalmTrait,StressedTrait,Mood,Reaction,\
                Motivation,Notes,Color1,Color2):  
    if (n1 > 0):
        #This loop is so that if the same name is generated it doesn't crash and they are distinguishable
        i=2
        j=1
        while Name in NameList:
            if (i == 2):
                Name = Name + ' ' + str(i)
            elif (i > 2):
                j = j + 1
                jlen=len(str(j))
                cutoff=1+jlen
                Name = Name[:-cutoff] + ' ' + str(i)
            i = i + 1   
    
    ws = wb.add_worksheet(Name)
    
    style0 = wb.add_format() # Create the style for odd rows
    style0.set_font_name('Calibri')
    style0.set_font_size(11)
    style0.set_fg_color(Color1)
    style0.set_align('top')
    
    style1 = wb.add_format() # Create the style for the name box
    style1.set_font_name('Calibri')
    style1.set_font_size(12)
    style1.set_bold()
    style1.set_fg_color(Color1)
    style1.set_align('top')
    
    style2 = wb.add_format() # Create the style for even rows
    style2.set_font_name('Calibri')
    style2.set_font_size(11)
    style2.set_fg_color(Color2)
    style2.set_align('top')
    
    
    # This section writes out the table to be what I want it
    # Rows 1:3      Demographics
    # Rows 4:6      Description
    # Rows 7:8      Voice
    # Row 9         Profession
    # Row 10        Calm Trait
    # Row 11        Stressed Trait
    # Row 12        Mood
    # Row 13        Reaction
    # Row 14        Motivation
    # Row 15        Session notes
    
    Display = GetDisplay()
    # This is a stub until I add the height and weight
    
    ws.merge_range('A1:A3', Name, style1)
    ws.write(0, 1, str(Age), style0)
    ws.write(1, 1, Gender, style0)
    ws.write(2, 1, Race, style0)
    
    ws.merge_range('A4:A6', 'Description', style2)
    ws.write(3, 1,FaceDescription, style2)
    ws.write(4, 1,PhysicalDescription, style2)
    ws.write(5, 1,AccessoriesDescription, style2)
    
    ws.merge_range('A7:A8', 'Voice', style0)
    ws.write(6, 1, VoiceSpeed, style0)
    ws.write(7, 1, VoiceQuality, style0)
    ws.write(8, 0,'Profession', style2)
    
    ws.write(8, 1,Profession, style2)
    ws.write(9, 0,'Calm Trait', style0)
    ws.write(9, 1,CalmTrait, style0)
    ws.write(10, 0,'Stressed Trait', style0)
    ws.write(10, 1,StressedTrait, style0)
    
    ws.write(11, 0,'Mood', style2)
    ws.write(11, 1,Mood, style2)
    ws.write(12, 0,'Reaction', style2)
    ws.write(12, 1,Reaction, style2)
    
    ws.write(13, 0,'Motivation', style0)
    ws.write(13, 1,Motivation, style0)
    
    ws.write(14, 0,'Session Notes', style2)
    ws.write(14, 1,Notes, style2)
    
    ws.set_column('A:A', 12.86)
    ws.set_column('B:B', 33)
    
    return Name

#def DemographicsGen():
#    DemoPath = 'Tables/Demographics.xlsx'
#    DemoPath = os.path.join(ScriptDir, DemoPath)
#    from openpyxl import load_workbook
#    DemoWB = load_workbook(DemoPath)
#    DemoWS = DemoWB.active
#    HumanPer = DemoWS['A1'].value
#    DwarfPer = HumanPer + DemoWS['A2'].value
#    ElfPer = DwarfPer + DemoWS['A3'].value
#    HalflingPer = ElfPer + DemoWS['A4'].value
#    HalfElfPer = HalflingPer + DemoWS['A5'].value
#    GnomePer = HalfElfPer + DemoWS['A6'].value
#    HalfOrcPer = GnomePer + DemoWS['A7'].value
#    DragonbornPer = HalfOrcPer + DemoWS['A8'].value
#    TieflingPer = DragonbornPer + DemoWS['A9'].value
##    GoliathPer = TieflingPer + DemoWS['A10'].value

#####################################
#         End excel functions       #
#####################################





#####################################
#      Begin preset functions       #
#####################################

#def PresetRead():
#    Preset1Path = 'Tables/Presets/Preset1.txt'
#    Preset1Path = os.path.join(ScriptDir, Preset1Path)
#    Preset2Path = 'Tables/Presets/Preset2.txt'
#    Preset2Path = os.path.join(ScriptDir, Preset2Path)
#    Preset3Path = 'Tables/Presets/Preset3.txt'
#    Preset3Path = os.path.join(ScriptDir, Preset3Path)
#    Preset4Path = 'Tables/Presets/Preset4.txt'
#    Preset4Path = os.path.join(ScriptDir, Preset4Path)
#    
#    def PresetReduction():
#        n = 0
#        while (n < 71):
#            n = n + 1
#    
#    Preset1 = open(Preset1Path).read().splitlines()
#    
#    
#    print(Preset1[1])


#####################################
#        End preset functions       #
#####################################





#####################################
#Begin Random demographic functions #
#####################################

def RaceGen(Races):
    HumanPer = Races[0]
    DwarfPer = HumanPer + Races[1]
    ElfPer = DwarfPer + Races[2]
    HalflingPer = ElfPer + Races[3]
    HalfElfPer = HalflingPer + Races[4]
    GnomePer = HalfElfPer + Races[5]
    HalfOrcPer = GnomePer + Races[6]
    DragonbornPer = HalfOrcPer + Races[7]
    TieflingPer = DragonbornPer + Races[8]
    
    
    RaceNum = random.randint(1,100)
    if (RaceNum <= HumanPer):
        Race = 'Human'
    elif (RaceNum <= DwarfPer):
        Race = DwarfRaceGen()
    elif (RaceNum < ElfPer):
        Race = ElfRaceGen()
    elif (RaceNum <= HalflingPer):
        Race = 'Halfling'
    elif (RaceNum <= HalfElfPer):
        Race = 'Half-Elf'
    elif (RaceNum <= GnomePer):
        Race = 'Gnome'
    elif (RaceNum <= HalfOrcPer):
        Race = 'Half-Orc'
    elif (RaceNum <= DragonbornPer):
        Race = 'Dragonborn'
    elif (RaceNum <= TieflingPer):
        Race = 'Tiefling'
    return Race

def GenderGen(Toggles):
    
    Active = [] 
    Male = Toggles[0]
    Female = Toggles[1]
    Total = Male + Female
    if (Total == 0):
        return 'No options selected, right click on the button.'
    
    if (Male == 1):
        Active.append(1)
    if (Female == 1):
        Active.append(2)

    GenderNum = random.choice(Active)
    if (GenderNum == 1):
        Gender = 'Male'
    elif (GenderNum == 2):
        Gender = 'Female'
    return Gender.strip('\n')

def NameGen(Race,Gender,Toggles):
    Active = [] 
    HumanGen1 = Toggles[0]
    HumanGen2 = Toggles[1]
    HumanGen3 = Toggles[2]
    AncientGen = Toggles[3]
    
    if (Race == 'Human'):
        Total = HumanGen1 + HumanGen2 + HumanGen3 + AncientGen
        if (Total == 0 and Race == 'Human'):
            return 'No options selected, right click on the button.'
    
        if (HumanGen1 == 1):
            Active.append(1)
        if (HumanGen2 == 1):
            Active.append(2)
        if (HumanGen3 == 1):
            Active.append(3)
        if (AncientGen == 1):
            Active.append(4)
        GenNum = random.choice(Active)
        if (GenNum == 1):
             Name = HumanNameGen1(Gender)
        elif (GenNum == 2):
            Name = HumanNameGen2(Gender)
        elif (GenNum == 3):
            Name = HumanNameGen3(Gender)
        elif (GenNum == 4):
            Name = AncientNameGen(Gender)
        
    elif (Race == 'Wood Elf' or Race == 'High Elf' or Race == 'Drow Elf'):
        Name = ElfNameGen()
    elif (Race == 'Hill Dwarf' or Race == 'Mountain Dwarf' or Race == 'Duregar Dwarf'):
        Name = DwarfNameGen(Gender)
    elif (Race == 'Halfling'):
        Name = HalflingNameGen()
    elif (Race == 'Gnome'):
        Name = GnomeNameGen()
    elif (Race == 'Half-Orc'):
        Name = HalfOrcNameGen(Gender)
    elif (Race == 'Half-Elf'):
        Name = HalfElfNameGen(Gender)
    elif (Race == 'Dragonborn'):
        Name = DragonbornNameGen()
    elif (Race == 'Tiefling'):
        Name = TieflingNameGen(Gender)
    else:
        Name = HumanNameGen1(Gender)
    return Name

def AgeGen(Race,MinAge,MaxAge):
    if (Race == 'Human'):
        Age = HumanAgeGen(MinAge,MaxAge)
    elif (Race == 'Wood Elf' or Race == 'High Elf' or Race == 'Drow Elf'):
        Age = ElfAgeGen(MinAge,MaxAge)
    elif (Race == 'Hill Dwarf' or Race == 'Mountain Dwarf' or Race == 'Duregar Dwarf'):
        Age = DwarfAgeGen(MinAge,MaxAge)
    elif (Race == 'Halfling'):
        Age = HalflingAgeGen(MinAge,MaxAge)
    elif (Race == 'Gnome'):
        Age = GnomeAgeGen(MinAge,MaxAge)
    elif (Race == 'Half-Orc'):
        Age = HalfOrcAgeGen(MinAge,MaxAge)
    elif (Race == 'Half-Elf'):
        Age = HalfElfAgeGen(MinAge,MaxAge)
    elif (Race == 'Dragonborn'):
        Age = DragonbornAgeGen(MinAge,MaxAge)
    elif (Race == 'Tiefling'):
        Age = TieflingAgeGen(MinAge,MaxAge)
    else:
        Age = HumanAgeGen(MinAge,MaxAge)
    return Age
#####################################
# End Random demographic functions  #
#####################################





####################################################
#Begin functions for NPCs that aren't race specific#
####################################################
  
#Generates a random eye description, considered a face description
def StdEyeGen():
    EyesPath = 'Tables/Physical Description/NPCEyes.txt'
    EyesPath = os.path.join(ScriptDir, EyesPath)
    EyeDescription = random.choice(open(EyesPath).readlines())
    return EyeDescription.strip('\n')

#Generates a random ear description, considered a face description
def StdEarsGen():
    EarsPath = 'Tables/Physical Description/NPCEars.txt'
    EarsPath = os.path.join(ScriptDir, EarsPath)
    EarsDescription = random.choice(open(EarsPath).readlines())
    return EarsDescription.strip('\n')

#Generates a random mouth description, considered a face description
def StdMouthGen():
    MouthPath = 'Tables/Physical Description/NPCMouth.txt'
    MouthPath = os.path.join(ScriptDir, MouthPath)
    MouthDescription = random.choice(open(MouthPath).readlines())
    return MouthDescription.strip('\n')

#Generates a random nose description, considered a face description
def StdNoseGen():
    NosePath = 'Tables/Physical Description/NPCNose.txt'
    NosePath = os.path.join(ScriptDir, NosePath)
    NoseDescription = random.choice(open(NosePath).readlines())
    return NoseDescription.strip('\n')

#Generates a random chin or jaw description, considered a face description
def StdChinorJawGen():
    ChinorJawPath = 'Tables/Physical Description/NPCChinorJaw.txt'
    ChinorJawPath = os.path.join(ScriptDir, ChinorJawPath)
    ChinorJawDescription = random.choice(open(ChinorJawPath).readlines())
    return ChinorJawDescription.strip('\n')

#Generates a random hair description, considered a face description
def StdHairGen():
    HairPath = 'Tables/Physical Description/NPCHair.txt'
    HairPath = os.path.join(ScriptDir, HairPath)
    HairDescription = random.choice(open(HairPath).readlines())
    return HairDescription.strip('\n')

#Generates a random description not in the previous face description tables, considered a face description
def StdOtherGen():
    OtherPath = 'Tables/Physical Description/NPCFaceOther.txt'
    OtherPath = os.path.join(ScriptDir, OtherPath)
    OtherDescription = random.choice(open(OtherPath).readlines())
    return OtherDescription.strip('\n')

#Generates a random scar description, considered a physical description
def FaceDescriptionGen(Toggles):
    # This function makes use of the previously defined functions and the
    # toggles given to it from the GUI.  It starts by defining the corresponding
    # variables in the right click menu and then creates a list of the ones that
    # are active

    Eye = Toggles[0]
    Ears = Toggles[1]
    Mouth = Toggles[2]
    Nose = Toggles[3]
    ChinOrJaw = Toggles[4]
    Hair = Toggles[5]
    Other = Toggles[6]
    
    # Checks to make sure at least one of the toggles is on
    Total = Eye + Ears + Mouth + Nose + ChinOrJaw + Hair + Other
    if (Total == 0):
        return 'No options selected, right click on the button.'
    
    # See which toggles are active, then add them to a list called Active
    # the values added correspond to the number they appear in the toggle menu
    Active = []
    if (Eye == 1):
        Active.append(1)
    if (Ears == 1):
        Active.append(2)
    if (Mouth == 1):
        Active.append(3)
    if (Nose == 1):
        Active.append(4)
    if (ChinOrJaw == 1):
        Active.append(5)
    if (Hair == 1):
        Active.append(6)
    if (Other == 1):
        Active.append(7)
    
    # Chooses a random number from the Active list and then compares the value
    # to see which generator it should use
    FaceNum = random.choice(Active)
    if (FaceNum == 1):
        FaceDescription = StdEyeGen()
    elif (FaceNum == 2):
        FaceDescription = StdEarsGen()
    elif (FaceNum == 3):
        FaceDescription = StdMouthGen()
    elif (FaceNum == 4):
        FaceDescription = StdNoseGen()
    elif (FaceNum == 5):
        FaceDescription = StdChinorJawGen()
    elif (FaceNum == 6):
        FaceDescription = StdHairGen()
    elif (FaceNum == 7):
        FaceDescription = StdOtherGen()
    return FaceDescription.strip('\n')




#Generates a random height, considered a physical description
def StdHeightGen():
    HeightPath = 'Tables/Physical Description/NPCHeight.txt'
    HeightPath = os.path.join(ScriptDir, HeightPath)
    HeightDescription = random.choice(open(HeightPath).readlines())
    return HeightDescription

#Generates a random general body description, considered a physical description
def StdBodyGen():
    BodyPath = 'Tables/Physical Description/NPCBody.txt'
    BodyPath = os.path.join(ScriptDir, BodyPath)
    Body = random.choice(open(BodyPath).readlines())
    Body = Body.lower()
    BodyDescription = "Their body is " + Body
    return BodyDescription.strip('\n')

#Generates a random hands description, considered a physical description
def StdHandsGen():
    HandsPath = 'Tables/Physical Description/NPCHands.txt'
    HandsPath = os.path.join(ScriptDir, HandsPath)
    HandDescription = random.choice(open(HandsPath).readlines())
    return HandDescription

#Generates a random scar description, considered a physical description
def StdScarGen():
    ScarPath = 'Tables/Physical Description/NPCScar.txt'
    ScarPath = os.path.join(ScriptDir, ScarPath)
    BodyLocationPath = 'Tables/Physical Description/NPCBodyLocation.txt'
    BodyLocationPath = os.path.join(ScriptDir, BodyLocationPath)
    ScarDescription = random.choice(open(ScarPath).readlines()).strip('\n') + ' on their ' + random.choice(open(BodyLocationPath).readlines()).lower()
    return ScarDescription.strip('\n')

def PhyscialDescriptionGen(Toggles):
    # See FaceDescriptionGen (line 286) for a walkthrough of this kind of function
    Active = []
    Height = Toggles[0]
    Body = Toggles[1]
    Hands = Toggles[2]
    Scars = Toggles[3]
    Total = Height + Body + Hands + Scars
    if (Total == 0):
        return 'No options selected, right click on the button.'
    
    if (Height == 1):
        Active.append(1)
    if (Body == 1):
        Active.append(2)
    if (Hands == 1):
        Active.append(3)
    if (Scars == 1):
        Active.append(4)
    
    PhysicalNum = random.choice(Active)
    if (PhysicalNum == 1):
        PhysicalDescription = StdHeightGen()
    elif (PhysicalNum == 2):
        PhysicalDescription = StdBodyGen()
    elif (PhysicalNum == 3):
        PhysicalDescription = StdHandsGen()
    elif (PhysicalNum == 4):
        PhysicalDescription = StdScarGen()
    return PhysicalDescription.strip('\n')


#Generates a random tattoo description, considered an accessory
def StdTattooGen():
    TattooPath = 'Tables/Physical Description/NPCTattoo.txt'
    TattooPath = os.path.join(ScriptDir, TattooPath)
    BodyLocationPath = 'Tables/Physical Description/NPCBodyLocation.txt'
    BodyLocationPath = os.path.join(ScriptDir, BodyLocationPath)
    TattooDescription = random.choice(open(TattooPath).readlines()).strip('\n') + ' on their ' + random.choice(open(BodyLocationPath).readlines()).lower()
    return TattooDescription.strip('\n')

#Generates a random jewelery description, considered an accessory
def StdJeweleryGen():
    JeweleryPath = 'Tables/Physical Description/NPCJewelery.txt'
    JeweleryPath = os.path.join(ScriptDir, JeweleryPath)
    Jewelery = random.choice(open(JeweleryPath).readlines()).strip('\n')
    JeweleryMaterialPath = 'Tables/Physical Description/NPCJeweleryMaterial.txt'
    JeweleryMaterialPath = os.path.join(ScriptDir, JeweleryMaterialPath)
    JeweleryMaterial = random.choice(open(JeweleryMaterialPath).readlines())
    JeweleryMaterial = JeweleryMaterial.lower()
    JeweleryJewelsPath = 'Tables/Physical Description/NPCJeweleryJewels.txt'
    JeweleryJewelsPath = os.path.join(ScriptDir, JeweleryJewelsPath)
    JeweleryJewels = random.choice(open(JeweleryJewelsPath).readlines())
    if (JeweleryMaterial != 'gemstones\n'): #Adds the jewelery encrusted with different jewels
        JeweleryDescription = Jewelery + " made of " + JeweleryMaterial
    elif (JeweleryMaterial == 'gemstones\n'):
        JeweleryDescription = Jewelery + ' set with ' + JeweleryJewels.lower()
    return JeweleryDescription.strip('\n')

#Generates a random clothing description, considered an accessory
def StdClothesGen():
    ClothesPath = 'Tables/Physical Description/NPCClothes.txt'
    ClothesPath = os.path.join(ScriptDir, ClothesPath)
    Clothes = random.choice(open(ClothesPath).readlines())
    Clothes = Clothes.lower()
    ClothesDescription = "Their clothing is " + Clothes
    return ClothesDescription.strip('\n')

#Chooses which of the previous accessory descriptions to choose from
def AccessoryDescriptionGen(Toggles):
    ###
    # We pass in the list of current toggles
    # from that list figure out which are active
    # and then choose randomly choose from the active
    # toggles to get the proper description
    ###
    Active = [] 
    Tattoos = Toggles[0]
    Jewelery = Toggles[1]
    Clothes = Toggles[2]
    Total = Tattoos + Jewelery + Clothes
    if (Total == 0):
        return 'No options selected, right click on the button.'
    
    if (Tattoos == 1):
        Active.append(1)
    if (Jewelery == 1):
        Active.append(2)
    if (Clothes == 1):
        Active.append(3)

    AccessoryNum = random.choice(Active)
    if (AccessoryNum == 1):
        AccessoryDescription = StdTattooGen()
    elif (AccessoryNum == 2):
        AccessoryDescription = StdJeweleryGen()
    elif (AccessoryNum == 3):
        AccessoryDescription = StdClothesGen()
    return AccessoryDescription.strip('\n')



#Generates a random voice speed
def VoiceSpeedGen():
    VoiceSpeedPath = 'Tables/Voice/VoiceSpeed.txt'
    VoiceSpeedPath = os.path.join(ScriptDir, VoiceSpeedPath)
    VoiceSpeed = random.choice(open(VoiceSpeedPath).readlines())
    return VoiceSpeed.strip('\n')

#Generates a random voice quality
def VoiceQualityGen():
    VoiceQualityPath = 'Tables/Voice/VoiceQuality.txt'
    VoiceQualityPath = os.path.join(ScriptDir, VoiceQualityPath)
    VoiceQuality = random.choice(open(VoiceQualityPath).readlines())
    return VoiceQuality.strip('\n')


# These functions are used to get a specific personality trait
def PositiveTraitGen():
    PositiveTraitsPath = 'Tables/Personality Traits/PositiveTraits.txt'
    PositiveTraitsPath = os.path.join(ScriptDir, PositiveTraitsPath)
    PositiveTrait = random.choice(open(PositiveTraitsPath).readlines())
    return PositiveTrait.strip('\n')

def NeutralTraitGen():
    NeutralTraitsPath = 'Tables/Personality Traits/NeutralTraits.txt'
    NeutralTraitsPath = os.path.join(ScriptDir, NeutralTraitsPath)
    NeutralTrait = random.choice(open(NeutralTraitsPath).readlines())
    return NeutralTrait.strip('\n')

def NegativeTraitGen():
    NegativeTraitsPath = 'Tables/Personality Traits/NegativeTraits.txt'
    NegativeTraitsPath = os.path.join(ScriptDir, NegativeTraitsPath)
    NegativeTrait = random.choice(open(NegativeTraitsPath).readlines())
    return NegativeTrait.strip('\n')

#Generates a random trait for the NPC when they are calm
def CalmTraitGen(Toggles):
    # See FaceDescriptionGen (line 286) for a walkthrough of this kind of function
    Active = []
    Positive = Toggles[0]
    Neutral = Toggles[1]
    Negative = Toggles[2]
    Total = Positive + Neutral + Negative
    if (Total == 0):
        return 'No options selected, right click on the button.'
    
    if (Positive == 1):
        Active.append(1)
    if (Neutral == 1):
        Active.append(2)
    if (Negative == 1):
        Active.append(3)
        
    TraitNum = random.choice(Active)
    if (TraitNum == 1):
        CalmTrait = PositiveTraitGen()
    elif (TraitNum == 2):
        CalmTrait = NeutralTraitGen()
    elif (TraitNum == 3):
        CalmTrait = NegativeTraitGen()
    return CalmTrait.strip('\n')

#Generates a random trait for the NPC when they are stressed
def StressedTraitGen(Toggles):
    # See FaceDescriptionGen (line 379) for a walkthrough of this kind of function
    Active = []
    Positive = Toggles[0]
    Neutral = Toggles[1]
    Negative = Toggles[2]
    Total = Positive + Neutral + Negative
    if (Total == 0):
        return 'No options selected, right click on the button.'
    
    if (Positive == 1):
        Active.append(1)
    if (Neutral == 1):
        Active.append(2)
    if (Negative == 1):
        Active.append(3)
        
    TraitNum = random.choice(Active)
    if (TraitNum == 1):
        StressedTrait = PositiveTraitGen()
    elif (TraitNum == 2):
        StressedTrait = NeutralTraitGen()
    elif (TraitNum == 3):
        StressedTrait = NegativeTraitGen()
    return StressedTrait.strip('\n')

    
#Generates a random mood
def HappyGen():
    HappysPath = 'Tables/Personality Traits/MoodHappy.txt'
    HappysPath = os.path.join(ScriptDir, HappysPath)
    Happy = 'Happy: ' + random.choice(open(HappysPath).readlines())
    return Happy.strip('\n')

def SadGen():
    SadsPath = 'Tables/Personality Traits/MoodSad.txt'
    SadsPath = os.path.join(ScriptDir, SadsPath)
    Sad = 'Sad: ' + random.choice(open(SadsPath).readlines())
    return Sad.strip('\n')

def DisgustedGen():
    DisgustedsPath = 'Tables/Personality Traits/MoodDisgusted.txt'
    DisgustedsPath = os.path.join(ScriptDir, DisgustedsPath)
    Disgusted = 'Disgusted: ' + random.choice(open(DisgustedsPath).readlines())
    return Disgusted.strip('\n')

def AngryGen():
    AngrysPath = 'Tables/Personality Traits/MoodAngry.txt'
    AngrysPath = os.path.join(ScriptDir, AngrysPath)
    Angry = 'Angry: ' + random.choice(open(AngrysPath).readlines())
    return Angry.strip('\n')

def FearfulGen():
    FearfulsPath = 'Tables/Personality Traits/MoodFearful.txt'
    FearfulsPath = os.path.join(ScriptDir, FearfulsPath)
    Fearful = 'Fearful: ' + random.choice(open(FearfulsPath).readlines())
    return Fearful.strip('\n')

def BadGen():
    BadsPath = 'Tables/Personality Traits/MoodBad.txt'
    BadsPath = os.path.join(ScriptDir, BadsPath)
    Bad = 'Bad: ' + random.choice(open(BadsPath).readlines())
    return Bad.strip('\n')

def SurprisedGen():
    SurprisedsPath = 'Tables/Personality Traits/MoodSurprised.txt'
    SurprisedsPath = os.path.join(ScriptDir, SurprisedsPath)
    Surprised = 'Surprised: ' + random.choice(open(SurprisedsPath).readlines())
    return Surprised.strip('\n')

def MoodGen(Toggles):
    # See FaceDescriptionGen (line 286) for a walkthrough of this kind of function
    Active = []
    Happy = Toggles[0]
    Sad = Toggles[1]
    Disgusted = Toggles[2]
    Angry = Toggles[3]
    Fearful = Toggles[4]
    Bad = Toggles[5]
    Surprised = Toggles[6]
    
    Total = Happy + Sad + Disgusted + Angry + Fearful + Bad + Surprised
    if (Total == 0):
        return 'No options selected, right click on the button.'
    
    if (Happy == 1):
        Active.append(1)
    if (Sad == 1):
        Active.append(2)
    if (Disgusted == 1):
        Active.append(3)
    if (Angry == 1):
        Active.append(4)
    if (Fearful == 1):
        Active.append(5)
    if (Bad == 1):
        Active.append(6)
    if (Surprised == 1):
        Active.append(7)
        
    MoodNum = random.choice(Active)
    if (MoodNum == 1):
        Mood = HappyGen()
    elif (MoodNum == 2):
        Mood = SadGen()
    elif (MoodNum == 3):
        Mood = DisgustedGen()
    elif (MoodNum == 4):
        Mood = AngryGen()
    elif (MoodNum == 5):
        Mood = FearfulGen()
    elif (MoodNum == 6):
        Mood = BadGen()
    elif (MoodNum == 7):
        Mood = SurprisedGen()
    
    return Mood.strip('\n')

##
# Generates a random profession
# from the choices given in the toggle menu
##
def CommonerCraftsmenGen():
    CommonerCraftsmensPath = 'Tables/Professions/CommonerCraftsmen.txt'
    CommonerCraftsmensPath = os.path.join(ScriptDir, CommonerCraftsmensPath)
    CommonerCraftsmen = random.choice(open(CommonerCraftsmensPath).readlines())
    return CommonerCraftsmen.strip('\n')

def CommonerLaborerGen():
    CommonerLaborersPath = 'Tables/Professions/CommonerLaborers.txt'
    CommonerLaborersPath = os.path.join(ScriptDir, CommonerLaborersPath)
    CommonerLaborer = random.choice(open(CommonerLaborersPath).readlines())
    return CommonerLaborer.strip('\n')

def CommonerProfessionsGen():
    CommonerProfessionsPath = 'Tables/Professions/CommonerProfessions.txt'
    CommonerProfessionsPath = os.path.join(ScriptDir, CommonerProfessionsPath)
    CommonerProfessions = random.choice(open(CommonerProfessionsPath).readlines())
    return CommonerProfessions.strip('\n')

def FarmersGen():
    FarmersPath = 'Tables/Professions/Farmers.txt'
    FarmersPath = os.path.join(ScriptDir, FarmersPath)
    Farmers = random.choice(open(FarmersPath).readlines())
    return Farmers.strip('\n')

def MilitaryAndWarriorsGen():
    MilitaryAndWarriorsPath = 'Tables/Professions/MilitaryAndWarriors.txt'
    MilitaryAndWarriorsPath = os.path.join(ScriptDir, MilitaryAndWarriorsPath)
    MilitaryAndWarriors = random.choice(open(MilitaryAndWarriorsPath).readlines())
    return MilitaryAndWarriors.strip('\n')

def BureaucratsGen():
    BureaucratsPath = 'Tables/Professions/Bureaucrats.txt'
    BureaucratsPath = os.path.join(ScriptDir, BureaucratsPath)
    Bureaucrats = random.choice(open(BureaucratsPath).readlines())
    return Bureaucrats.strip('\n')

def ClergymenGen():
    ClergymenPath = 'Tables/Professions/Clergymen.txt'
    ClergymenPath = os.path.join(ScriptDir, ClergymenPath)
    Clergymen = random.choice(open(ClergymenPath).readlines())
    return Clergymen.strip('\n')

def CriminalsGen():
    CriminalsPath = 'Tables/Professions/Criminals.txt'
    CriminalsPath = os.path.join(ScriptDir, CriminalsPath)
    Criminals = random.choice(open(CriminalsPath).readlines())
    return Criminals.strip('\n')

def AcademicsGen():
    AcademicsPath = 'Tables/Professions/Academics.txt'
    AcademicsPath = os.path.join(ScriptDir, AcademicsPath)
    Academics = random.choice(open(AcademicsPath).readlines())
    return Academics.strip('\n')

def MagiciansGen():
    MagiciansPath = 'Tables/Professions/Magicians.txt'
    MagiciansPath = os.path.join(ScriptDir, MagiciansPath)
    Magicians = random.choice(open(MagiciansPath).readlines())
    return Magicians.strip('\n')

def ProfessionGen(Toggles):
    # See FaceDescriptionGen (line 286) for a walkthrough of this kind of function
    Active = []
    CommonerCraftsmen = Toggles[0]
    CommonerLaborer = Toggles[1]
    CommonerProfessions = Toggles[2]
    Farmers = Toggles[3]
    MilitaryAndWarriors = Toggles[4]
    Bureaucrats = Toggles[5]
    Clergymen = Toggles[6]
    Criminals = Toggles[7]
    Academics = Toggles[8]
    Magicians = Toggles[9]
    
    Total = CommonerCraftsmen + CommonerLaborer + CommonerProfessions + Farmers + MilitaryAndWarriors + Bureaucrats + Clergymen + Criminals + Academics + Magicians
    if (Total == 0):
        return 'No options selected, right click on the button.'
    
    if (CommonerCraftsmen == 1):
        Active.append(1)
    if (CommonerLaborer == 1):
        Active.append(2)
    if (CommonerProfessions == 1):
        Active.append(3)
    if (Farmers == 1):
        Active.append(4)
    if (MilitaryAndWarriors == 1):
        Active.append(5)
    if (Bureaucrats == 1):
        Active.append(6)
    if (Clergymen == 1):
        Active.append(7)
    if (Criminals == 1):
        Active.append(8)
    if (Academics == 1):
        Active.append(9)
    if (Magicians == 1):
        Active.append(10)
    
    ProfessionNum = random.choice(Active)
    if (ProfessionNum == 1):
        Profession = CommonerCraftsmenGen()
    elif (ProfessionNum == 2):
        Profession = CommonerLaborerGen()
    elif (ProfessionNum == 3):
        Profession = CommonerProfessionsGen()
    elif (ProfessionNum == 4):
        Profession = FarmersGen()
    elif (ProfessionNum == 5):
        Profession = MilitaryAndWarriorsGen()
    elif (ProfessionNum == 6):
        Profession = BureaucratsGen()
    elif (ProfessionNum == 7):
        Profession = ClergymenGen()
    elif (ProfessionNum == 8):
        Profession = CriminalsGen()
    elif (ProfessionNum == 9):
        Profession = AcademicsGen()
    elif (ProfessionNum == 10):
        Profession = MagiciansGen()            
    return Profession.strip('\n')

##################################################
#End functions for NPCs that aren't race specific#
##################################################











#####################################
#       Begin Human functions       #
#####################################
def HumanNameGen1(Gender):
    # This name generator makes a name by taking letters until it gets to a vowel
    # then it adds a male or female suffix
    HumanNamesPath = 'Tables/Name/HumanNames.txt'
    HNPath = os.path.join(ScriptDir, HumanNamesPath)
    FirstName=random.choice(open(HNPath).readlines()).strip('\n')
    LastName=random.choice(open(HNPath).readlines()).strip('\n')
    #Removes the suffix from the first name to later make them sound male or female
    n=0
    vowels = ["a","e","i","o","u"]
    while (n == 0):
        if (len(FirstName) == 1):
            FirstName=random.choice(open(HNPath).readlines()).strip('\n')
     
        if (FirstName[-1].lower() in vowels):
           FirstName = FirstName[:-1]
           n = 1
        else:
            FirstName = FirstName[:-1]
            
    if (Gender == 'Male'):
        HumanMaleSufPath = 'Tables/Name/HumanMaleSuffix.txt'
        HMSPath = os.path.join(ScriptDir, HumanMaleSufPath)
        FirstName = FirstName.title() + random.choice(open(HMSPath).readlines())
    else:
        HumanFemaleSufPath = 'Tables/Name/HumanFemaleSuffix.txt'
        HFSPath = os.path.join(ScriptDir, HumanFemaleSufPath)
        FirstName = FirstName + random.choice(open(HFSPath).readlines())
    Name = FirstName.strip().title() + ' ' + LastName
    return Name

def HumanNameGen2(Gender):
    # This one just makes name off of 20 different prefixes and suffixes
    # for first and last names
    HumanFNFSPath = 'Tables/Name/HumanFNFS.txt'
    HumanFNFSPath = os.path.join(ScriptDir, HumanFNFSPath)
    HumanFNSSPath = 'Tables/Name/HumanFNSS.txt'
    HumanFNSSPath = os.path.join(ScriptDir, HumanFNSSPath)
    HumanLNFSPath = 'Tables/Name/HumanLNFS.txt'
    HumanLNFSPath = os.path.join(ScriptDir, HumanFNFSPath)
    HumanLNSSPath = 'Tables/Name/HumanLNSS.txt'
    HumanLNSSPath = os.path.join(ScriptDir, HumanFNSSPath)        
    FNFS = random.choice(open(HumanFNFSPath).readlines()).strip('\n')
    FNSS = random.choice(open(HumanFNSSPath).readlines()).strip('\n')
    LNFS = random.choice(open(HumanLNFSPath).readlines()).strip('\n')
    LNSS = random.choice(open(HumanLNSSPath).readlines()).strip('\n')
    Name = FNFS + FNSS + ' ' + LNFS + LNSS
    return Name

def HumanNameGen3(Gender):
    # This one uses 3 different lists for the syllables and makes a first and last name
    #
    HumanFSPath = 'Tables/Name/HumanFirstSyllable.txt'
    HumanFSPath = os.path.join(ScriptDir, HumanFSPath)
    HumanSSPath = 'Tables/Name/HumanSecondSyllable.txt'
    HumanSSPath = os.path.join(ScriptDir, HumanSSPath)
    HumanTSPath = 'Tables/Name/HumanThirdSyllable.txt'
    HumanTSPath = os.path.join(ScriptDir, HumanTSPath)
    FirstNameInt = random.randint(0,10)
    LastNameInt = random.randint(0,10)
    if (FirstNameInt < 7):
        FS = random.choice(open(HumanFSPath).readlines()).strip('\n')
        SS = random.choice(open(HumanSSPath).readlines()).strip('\n')
        TS = random.choice(open(HumanTSPath).readlines()).strip('\n')
        FirstName = FS + SS + TS
    else:
        FS = random.choice(open(HumanFSPath).readlines()).strip('\n')
        SS = random.choice(open(HumanSSPath).readlines()).strip('\n')
        FirstName = FS + SS
    if (LastNameInt < 7):
        FS = random.choice(open(HumanFSPath).readlines()).strip('\n')
        SS = random.choice(open(HumanSSPath).readlines()).strip('\n')
        LastName = FS + SS
    else:
        FS = random.choice(open(HumanFSPath).readlines()).strip('\n')
        SS = random.choice(open(HumanSSPath).readlines()).strip('\n')
        TS = random.choice(open(HumanTSPath).readlines()).strip('\n')
        LastName = FS + SS + TS
    Name = FirstName + ' ' + LastName
    return Name

def AncientNameGen(Gender):
    AncientMalePath = 'Tables/Name/AncientMaleNames.txt'
    AncientMalePath = os.path.join(ScriptDir, AncientMalePath)
    AncientFemalePath = 'Tables/Name/AncientFemaleNames.txt'
    AncientFemalePath = os.path.join(ScriptDir, AncientFemalePath)
    if (Gender == 'Male'):
        Name = random.choice(open(AncientMalePath,encoding="utf-8").readlines()).strip('\n').title()
    else:
        Name = random.choice(open(AncientFemalePath,encoding="utf-8").readlines()).strip('\n').title()       
    return Name


def HumanAgeGen(MinAge,MaxAge):
    # These are the default human age range
    DefaultMin = 8
    DefaultMax = 100
    # This is the range and it's used for scaling
    DefaultRange = DefaultMax - DefaultMin
    
    # Get an integer value for the minimum and maximum based on the values
    # from the GUI's popup menu
    CalcMin = int(MinAge * DefaultRange / 100 + DefaultMin)
    CalcMax = int(MaxAge * DefaultRange / 100 + DefaultMin)
    
    # Get a random age from inbetween the minimum and maximum
    Age = random.randint(CalcMin,CalcMax)
    return Age
#####################################
#       End Human functions         #
#####################################





#####################################
#        Begin Elf functions        #
#####################################    
def ElfNameGen():
    ElfPrePath = 'Tables/Name/ElfPrefix.txt'
    EPPath = os.path.join(ScriptDir, ElfPrePath)
    ElfSufPath = 'Tables/Name/ElfSuffix.txt'
    ESPath = os.path.join(ScriptDir, ElfSufPath)
    temp = random.randint(1,10)
    if (temp < 5):
        Prefix = random.choice(open(EPPath).readlines()).strip('\n')
        Suffix = random.choice(open(ESPath).readlines()).strip('\n')
        Name = Prefix.strip() + Suffix
    elif (temp < 8):
        Prefix = random.choice(open(EPPath).readlines()).strip('\n')
        Suffix1 = random.choice(open(ESPath).readlines()).strip('\n')
        Suffix2 = random.choice(open(ESPath).readlines()).strip('\n')
        Name = Prefix + Suffix1 + Suffix2
    elif (temp < 10):
        Prefix1 = random.choice(open(EPPath).readlines()).strip('\n')
        Suffix1 = random.choice(open(ESPath).readlines()).strip('\n')
        Prefix2 = random.choice(open(EPPath).readlines()).strip('\n')
        Suffix2 = random.choice(open(ESPath).readlines()).strip('\n')
        Name = Prefix1 + Suffix1 + ' ' + Prefix2 + Suffix2
    elif (temp == 10):
        Prefix1 = random.choice(open(EPPath).readlines()).strip('\n')
        Suffix1 = random.choice(open(ESPath).readlines()).strip('\n')
        Suffix2 = random.choice(open(ESPath).readlines()).strip('\n')
        Suffix3 = random.choice(open(ESPath).readlines()).strip('\n')
        Name = Suffix1.title() + '\'' + Prefix1 + Suffix2 + Suffix3
    return Name


def ElfAgeGen(MinAge,MaxAge):
    # These are the default elf age range
    DefaultMin = 8
    DefaultMax = 750
    # This is the range and it's used for scaling
    DefaultRange = DefaultMax - DefaultMin
    
    # Get an integer value for the minimum and maximum based on the values
    # from the GUI's popup menu
    CalcMin = int(MinAge * DefaultRange / 100 + DefaultMin)
    CalcMax = int(MaxAge * DefaultRange / 100 + DefaultMin)
    
    # Get a random age from inbetween the minimum and maximum
    Age = random.randint(CalcMin,CalcMax)
    return Age

def ElfHeightGen(MinHeight, MaxHeight):
    # These are the default min and max elf heights
    DefaultMin = 48
    DefaultMax = 60
    # This is the range and it's used for scaling
    DefaultRange = DefaultMax - DefaultMin
    
    # Get an integer value for the minimum and maximum based on the values
    # from the GUI's popup menu
    CalcMin = int(MinHeight * DefaultRange / 100 + DefaultMin)
    CalcMax = int(MaxHeight * DefaultRange / 100 + DefaultMin)
    
    # Get a random age from inbetween the minimum and maximum
    Height = random.randint(CalcMin,CalcMax)
    return Height

def ElfRaceGen():
    ElfRaceInt = random.randint(1,100)
    if (ElfRaceInt < 45):
        Race = 'Wood Elf'
    elif (ElfRaceInt < 100):
        Race = 'High Elf'
    else:
        Race = 'Drow Elf'
    return Race

#####################################
#         End Elf functions         #
#####################################





#####################################
#       Begin Dwarf functions       #
#####################################

def DwarfNameGen(Gender):
    DwarfPrePath = 'Tables/Name/DwarfPrefix.txt'
    DPPath = os.path.join(ScriptDir, DwarfPrePath)
    Prefix = random.choice(open(DPPath).readlines())
    Prefix = Prefix.strip('\n')
    if (Gender == 'Male'): ###CLEAN THIS UP MOVE TO LOWER PART WITH GENDERS
        DwarfMaleSufPath = 'Tables/Name/DwarfMaleSuffix.txt'
        DMSPath = os.path.join(ScriptDir, DwarfMaleSufPath)
        Suffix = random.choice(open(DMSPath).readlines())
        Suffix = Suffix.strip('\n')
        Name = Prefix + Suffix
    else:
        DwarfFemaleSufPath = 'Tables/Name/DwarfFemaleSuffix.txt'
        DFSPath = os.path.join(ScriptDir, DwarfFemaleSufPath)
        Suffix = random.choice(open(DFSPath).readlines()).strip('\n')
        Name = Prefix + Suffix
    return Name
    

def DwarfAgeGen(MinAge,MaxAge):
    # These are the default dwarf age range
    DefaultMin = 8
    DefaultMax = 350
    # This is the range and it's used for scaling
    DefaultRange = DefaultMax - DefaultMin
    
    # Get an integer value for the minimum and maximum based on the values
    # from the GUI's popup menu
    CalcMin = int(MinAge * DefaultRange / 100 + DefaultMin)
    CalcMax = int(MaxAge * DefaultRange / 100 + DefaultMin)
    
    # Get a random age from inbetween the minimum and maximum
    Age = random.randint(CalcMin,CalcMax)
    return Age

def DwarfHeightGen(MinHeight, MaxHeight):
    # These are the default min and max dwarf heights
    DefaultMin = 48
    DefaultMax = 60
    # This is the range and it's used for scaling
    DefaultRange = DefaultMax - DefaultMin
    
    # Get an integer value for the minimum and maximum based on the values
    # from the GUI's popup menu
    CalcMin = int(MinHeight * DefaultRange / 100 + DefaultMin)
    CalcMax = int(MaxHeight * DefaultRange / 100 + DefaultMin)
    
    # Get a random height from inbetween the minimum and maximum
    Height = random.randint(CalcMin,CalcMax)
    return Height

def DwarfRaceGen():
    DwarfRaceInt = random.randint(1,100)
    if (DwarfRaceInt < 45):
        Race = 'Mountain Dwarf'
    elif (DwarfRaceInt < 100):
        Race = 'Hill Dwarf'
    else:
        Race = 'Duergar Dwarf' 
    return Race

#####################################
#        End Dwarf functions        #
#####################################




#####################################
#      Begin Halfling functions     #
#####################################     

def HalflingNameGen():
        NameInt = random.randint(1,20)    
        HalflingPath = 'Tables/Name/HalflingNames.txt'
        HalflingPath = os.path.join(ScriptDir, HalflingPath)
        if (NameInt < 4):
            Name = random.choice(open(HalflingPath).readlines()).strip('\n')
        elif (NameInt < 10):
            Prefix = random.choice(open(HalflingPath).readlines()).strip('\n')
            Suffix = random.choice(open(HalflingPath).readlines()).strip('\n')
            Name = Prefix + Suffix.lower()
        elif (NameInt < 14):
            Prefix1 = random.choice(open(HalflingPath).readlines()).strip('\n')
            Prefix2 = random.choice(open(HalflingPath).readlines()).strip('\n')
            Suffix2 = random.choice(open(HalflingPath).readlines()).strip('\n')
            Name = Prefix1 + ' ' + Prefix2 + Suffix2.lower()
        elif (NameInt < 20):
            Prefix1 = random.choice(open(HalflingPath).readlines()).strip('\n')
            Suffix1 = random.choice(open(HalflingPath).readlines()).strip('\n')
            Prefix2 = random.choice(open(HalflingPath).readlines()).strip('\n')
            Suffix2 = random.choice(open(HalflingPath).readlines()).strip('\n')
            Name = Prefix1 + Suffix1.lower() + ' ' + Prefix2 + Suffix2.lower()
        else:
            Prefix = random.choice(open(HalflingPath).readlines()).strip('\n')
            Suffix = random.choice(open(HalflingPath).readlines()).strip('\n')
            HalflingEarnedPath = 'Tables/Name/HalflingEarnedNames.txt'
            HalflingPath = os.path.join(ScriptDir, HalflingEarnedPath)
            EarnedName = random.choice(open(HalflingEarnedPath).readlines()).strip('\n')
            Name = Prefix + Suffix.lower() + ' ' + EarnedName
        return Name


def HalflingAgeGen(MinAge,MaxAge):
    # These are the default Halfling age range
    DefaultMin = 8
    DefaultMax = 250
    # This is the range and it's used for scaling
    DefaultRange = DefaultMax - DefaultMin
    
    # Get an integer value for the minimum and maximum based on the values
    # from the GUI's popup menu
    CalcMin = int(MinAge * DefaultRange / 100 + DefaultMin)
    CalcMax = int(MaxAge * DefaultRange / 100 + DefaultMin)
    
    # Get a random age from inbetween the minimum and maximum
    Age = random.randint(CalcMin,CalcMax)
    return Age

#####################################
#       End Halfling functions      #
#####################################





#####################################
#     Begin Dragonborn functions    #
#####################################
def DragonbornNameGen():
    NameInt = random.randint(1,20)    
    DragonbornNamePath = 'Tables/Name/DragonNames.txt'
    DragonbornNamePath = os.path.join(ScriptDir, DragonbornNamePath)
    if (NameInt < 2):
        Name = random.choice(open(DragonbornNamePath).readlines()).strip('\n')
    elif (NameInt < 15):
        Prefix = random.choice(open(DragonbornNamePath).readlines()).strip('\n')
        Suffix = random.choice(open(DragonbornNamePath).readlines()).strip('\n')
        Name = Prefix + Suffix.lower()
    elif (NameInt < 19):
        Prefix1 = random.choice(open(DragonbornNamePath).readlines()).strip('\n')
        Prefix2 = random.choice(open(DragonbornNamePath).readlines()).strip('\n')
        Suffix = random.choice(open(DragonbornNamePath).readlines()).strip('\n')
        Name = Prefix1 + Prefix2.lower() + Suffix.lower()
    else:
        Prefix1 = random.choice(open(DragonbornNamePath).readlines()).strip('\n')
        Suffix1 = random.choice(open(DragonbornNamePath).readlines()).strip('\n')
        Prefix2 = random.choice(open(DragonbornNamePath).readlines()).strip('\n')
        Suffix2 = random.choice(open(DragonbornNamePath).readlines()).strip('\n')
        Name = Prefix1 + Suffix1.lower() + ' ' + Prefix2 + Suffix2.lower()
    return Name

def DragonbornAgeGen(MinAge,MaxAge):
    # These are the default Dragonborn age range
    DefaultMin = 3
    DefaultMax = 80
    # This is the range and it's used for scaling
    DefaultRange = DefaultMax - DefaultMin
    
    # Get an integer value for the minimum and maximum based on the values
    # from the GUI's popup menu
    CalcMin = int(MinAge * DefaultRange / 100 + DefaultMin)
    CalcMax = int(MaxAge * DefaultRange / 100 + DefaultMin)
    
    # Get a random age from inbetween the minimum and maximum
    Age = random.randint(CalcMin,CalcMax)
    return Age

def DragonbornRaceGen():
    DragonbornAncestryPath = 'Tables/Name/DragonAncestry.txt'
    DragonbornAncestryPath = os.path.join(ScriptDir, DragonbornAncestryPath)
    Ancestry = random.choice(open(DragonbornAncestryPath).readlines()).strip('\n')
    Race =  Ancestry + 'Dragonborn'     
    return Race

#####################################
#     End Dragonborn functions      #
#####################################





#####################################
#       Begin Gnome functions       #
#####################################
def GnomeNameGen():
    NameInt = random.randint(1,10)    
    GnomePath = 'Tables/Name/GnomeNames.txt'
    GnomePath = os.path.join(ScriptDir, GnomePath)
    if (NameInt < 5):
        Name = random.choice(open(GnomePath).readlines()).strip('\n')
    elif (NameInt < 8):
        Prefix = random.choice(open(GnomePath).readlines()).strip('\n')
        Suffix = random.choice(open(GnomePath).readlines()).strip('\n')
        Name = Prefix + Suffix.lower()
    elif (NameInt < 10):
        Prefix = random.choice(open(GnomePath).readlines()).strip('\n')
        Suffix = random.choice(open(GnomePath).readlines()).strip('\n')
        GnomeEarnedPath = 'Tables/Name/GnomeEarnedNames.txt'
        GnomePath = os.path.join(ScriptDir, GnomeEarnedPath)
        EarnedName = random.choice(open(GnomeEarnedPath).readlines()).strip('\n')
        Name = EarnedName + ' ' + Prefix + Suffix.lower()
    else:
        Prefix1 = random.choice(open(GnomePath).readlines()).strip('\n')
        Suffix = random.choice(open(GnomePath).readlines()).strip('\n')
        Prefix2 = random.choice(open(GnomePath).readlines()).strip('\n')
        Name = Prefix1 + Prefix2.lower() + Suffix.lower()
    return Name.strip('\n')


def GnomeAgeGen(MinAge,MaxAge):
    # These are the default Gnome age range
    DefaultMin = 10
    DefaultMax = 500
    # This is the range and it's used for scaling
    DefaultRange = DefaultMax - DefaultMin
    
    # Get an integer value for the minimum and maximum based on the values
    # from the GUI's popup menu
    CalcMin = int(MinAge * DefaultRange / 100 + DefaultMin)
    CalcMax = int(MaxAge * DefaultRange / 100 + DefaultMin)
    
    # Get a random age from inbetween the minimum and maximum
    Age = random.randint(CalcMin,CalcMax)
    return Age

#####################################
#        End Gnome functions        #
#####################################




#####################################
#     Begin Half-Elf functions      #
#####################################
def HalfElfNameGen(Gender):
    #Half-elves are typically named as the opposite of whatever race they're raised by
    #So we calculate the percentage of each based on the demographics and then we
    #Give the opposite percentages
    
    RacePath = 'Tables/Toggles/Race.csv'
    RacePath = os.path.join(ScriptDir, RacePath)
    InitialRace = []
    with open(RacePath) as f:
        reader = csv.reader(f)
        InitialRace = next(reader)
    
    
    HumanPer = int(InitialRace[0])
    ElfPer = int(InitialRace[2])
    
    TotalPer = HumanPer + ElfPer
    if (HumanPer == 0 and ElfPer == 0):
        HumanPer = 50
        ElfPer = 50
        TotalPer = 100
    HumanPer = HumanPer*100/TotalPer
    ElfPer = ElfPer*100/TotalPer
    NameInt = random.randint(1,100)
    if (HumanPer > NameInt):
        Name = ElfNameGen()      
    else:
        Name = HumanNameGen1(Gender)
    return Name

def HalfElfAgeGen(MinAge,MaxAge):
    # These are the default Half-Elf age range
    DefaultMin = 10
    DefaultMax = 180
    # This is the range and it's used for scaling
    DefaultRange = DefaultMax - DefaultMin
    
    # Get an integer value for the minimum and maximum based on the values
    # from the GUI's popup menu
    CalcMin = int(MinAge * DefaultRange / 100 + DefaultMin)
    CalcMax = int(MaxAge * DefaultRange / 100 + DefaultMin)
    
    # Get a random age from inbetween the minimum and maximum
    Age = random.randint(CalcMin,CalcMax)
    return Age

#####################################
#      End Half-Elf functions       #
#####################################




#####################################
#      Begin Half-Orc functions     # 
#####################################
def HalfOrcNameGen(Gender):
    # Creates the name for the Half-Orcs, they can have human names but I
    # think they're less interesting so there aren't many of them
    NameInt = random.randint(1,20)    
    HalfOrcPrePath = 'Tables/Name/HalfOrcPrefix.txt'
    HalfOrcPrePath = os.path.join(ScriptDir, HalfOrcPrePath)
    HalfOrcSufPath = 'Tables/Name/HalfOrcSuffix.txt'
    HalfOrcSufPath = os.path.join(ScriptDir, HalfOrcSufPath)
    if (NameInt < 10):
        Prefix = random.choice(open(HalfOrcPrePath).readlines()).strip('\n')
        Suffix = random.choice(open(HalfOrcSufPath).readlines()).strip('\n')
        Name = Prefix + Suffix
    elif (NameInt < 13):
        #This elif creates the human names
        Name = HumanNameGen1(Gender)
    elif (NameInt < 15):
        Prefix = random.choice(open(HalfOrcPrePath).readlines()).strip('\n')
        Suffix1 = random.choice(open(HalfOrcSufPath).readlines()).strip('\n')
        Suffix2 = random.choice(open(HalfOrcSufPath).readlines()).strip('\n')
        Name = Prefix + Suffix1 + Suffix2
    else:
        Prefix1 = random.choice(open(HalfOrcPrePath).readlines()).strip('\n')
        Prefix2 = random.choice(open(HalfOrcPrePath).readlines()).strip('\n')
        Suffix = random.choice(open(HalfOrcSufPath).readlines()).strip('\n')
        Name = Prefix1 + ' ' + Prefix2 + Suffix
    return Name


def HalfOrcAgeGen(MinAge,MaxAge):
    # These are the default Half-Orc age range
    DefaultMin = 5
    DefaultMax = 75
    # This is the range and it's used for scaling
    DefaultRange = DefaultMax - DefaultMin
    
    # Get an integer value for the minimum and maximum based on the values
    # from the GUI's popup menu
    CalcMin = int(MinAge * DefaultRange / 100 + DefaultMin)
    CalcMax = int(MaxAge * DefaultRange / 100 + DefaultMin)
    
    # Get a random age from inbetween the minimum and maximum
    Age = random.randint(CalcMin,CalcMax)
    return Age

#####################################
#       End Half-Orc functions      #
#####################################





#####################################
#     Begin Tiefling functions      #
#####################################

def TieflingNameGen(Gender):
    NameInt = random.randint(1,10)
    if (NameInt < 2): #Virtue names
        TieflingVirtuePath = 'Tables/Name/TieflingVirtue.txt'
        TieflingVirtuePath = os.path.join(ScriptDir, TieflingVirtuePath)
        Name = random.choice(open(TieflingVirtuePath).readlines()).strip('\n')
    else: #'Typical' names
        TieflingPrePath = 'Tables/Name/TieflingPrefix.txt'
        TPPath = os.path.join(ScriptDir, TieflingPrePath)
        Prefix = random.choice(open(TPPath).readlines()).strip('\n')
        if (Gender == 'Male'):
            TieflingMaleSufPath = 'Tables/Name/TieflingMaleSuffix.txt'
            TMSPath = os.path.join(ScriptDir, TieflingMaleSufPath)
            Suffix = random.choice(open(TMSPath).readlines()).strip('\n')
            Name = Prefix + Suffix
        else:
            TieflingFemaleSufPath = 'Tables/Name/TieflingFemaleSuffix.txt'
            TFSPath = os.path.join(ScriptDir, TieflingFemaleSufPath)
            Suffix = random.choice(open(TFSPath).readlines()).strip('\n')
            Name = Prefix + Suffix
        
    return Name

def TieflingAgeGen(MinAge,MaxAge):
    # These are the default Tiefling age range
    DefaultMin = 8
    DefaultMax = 115
    # This is the range and it's used for scaling
    DefaultRange = DefaultMax - DefaultMin
    
    # Get an integer value for the minimum and maximum based on the values
    # from the GUI's popup menu
    CalcMin = int(MinAge * DefaultRange / 100 + DefaultMin)
    CalcMax = int(MaxAge * DefaultRange / 100 + DefaultMin)
    
    # Get a random age from inbetween the minimum and maximum
    Age = random.randint(CalcMin,CalcMax)
    return Age
#####################################
#       End Tiefling functions      #
#####################################



'''
Coded by: OmnipotentSpoon (some random fucking dude)

This is the GUI!

Table of contents:
    1. Checks to see if the excel sheet needs to be moved
    2. Declare all of the variables used in the Tkinter program
    3. Define functions that get variables in a list based on the menu
    4. Open files that were saved from last time the program was run
       and creates lists of the values (so that you can pick up where
       you left off, it was more useful before I added presets)
    5. Set the saved values to the proper variables initally
    6. Open the excel sheet
    7. Define functions that create popups when you right click on buttons
    8. Function that saves the toggles when the program is closed
    9. Functions for the color menu
    10. GUI functions are what run when the button is left clicked, most
        of them just call a function from one of the other .py files,
        either GeneratorFunctions.py or RumorGenerator.py
    11. Functions used to save the excel sheet and run when the program is closed
    12. Then the buttons and labels are created
    13. They are placed in the proper grid
    
'''


##########################################
#    Check to see if a move is needed    #
##########################################

#
# Basically check to see if there already exists a file named
# New NPCs.xlsx in the current directory, if there is then create
# a new path to a file in the Old NPCs that goes like
# 'Old NPCs from *Date* + *num*' where *Date* is todays date
# and *num* is the number of sheets created on that day
#

ScriptDir = os.path.dirname(__file__)
MoveNeeded = os.path.isfile('New NPCs.xlsx')
if (MoveNeeded == True):
    MoveComplete = False
    Date = str(datetime.datetime.now())[0:10]
    #NewPath =  'Old NPCs/Excel/' + 'NPCs from ' + Date + ' 1.xlsx'
    #Uncomment if you ever want to store it there because of text files
    NewPath =  'Old NPCs/' + 'NPCs from ' + Date + ' 1.xlsx'
    NewPath = os.path.join(ScriptDir, NewPath)
    i = 1
    while (MoveComplete == False):
        NameExistsAlready = os.path.isfile(NewPath)
        if (NameExistsAlready == True):
            ilen=len(str(i))
            i = i + 1
            cutoff=6+ilen
            NewPath = NewPath[:-cutoff] + ' ' + str(i) + '.xlsx'

        else:
            os.rename('New NPCs.xlsx', NewPath)
            break 


root=tk.Tk()
##########################################
#  Create tkinter variables   #
##########################################

##
# So tkinter runs loops weird and these variables need to be defined
# as tkinter variables.
# for strings use tk.StringVar()
# for integers use tk.IntVar()
# for others use Google
#
# To set a variable, say MyVar = tk.StringVar():
#   MyVar.set('Hello')
#
# To get the value from a variable
#   MyVar.get()
#   This returns the string 'Hello'
##

##
# These variables are the standard ones for the NPC
##
Name = tk.StringVar()
Age = tk.StringVar()
Gender = tk.StringVar()
Race = tk.StringVar()
VoiceSpeed = tk.StringVar()
VoiceQuality= tk.StringVar()
FaceDescription = tk.StringVar()
PhysicalDescription = tk.StringVar()
AccessoryDescription = tk.StringVar()
Profession = tk.StringVar()
CalmTrait = tk.StringVar()
StressedTrait = tk.StringVar()
Mood = tk.StringVar()
Reaction = tk.StringVar()
Motivation = tk.StringVar()
Rumor = tk.StringVar()
Notes = tk.StringVar()

##
# These are used in the pop up menus
##

# Color toggles
Color0 = tk.StringVar()
Color1 = tk.StringVar()
Color2 = tk.StringVar()

# Variables used to determine which panels are shown
ShowPresets = tk.IntVar()
ShowRandomNPC = tk.IntVar()
ShowName = tk.IntVar()
ShowAge = tk.IntVar()
ShowGender = tk.IntVar()
ShowRace = tk.IntVar()
ShowVoiceSpeed = tk.IntVar()
ShowVoiceQuality = tk.IntVar()
ShowFaceDescription = tk.IntVar()
ShowPhysicalDescription = tk.IntVar()
ShowAccessoryDescription = tk.IntVar()
ShowProfession = tk.IntVar()
ShowCalmTrait = tk.IntVar()
ShowStressedTrait = tk.IntVar()
ShowMood = tk.IntVar()
ShowReaction = tk.IntVar()
ShowMotivation = tk.IntVar()
ShowNotes = tk.IntVar()
ShowExport = tk.IntVar()

# Active preset variable, used to keep track of the large button
ActivePreset = tk.IntVar()

# Variables used to save the colors of the buttons for the presets
PresetColor1 = tk.StringVar()
PresetColor2 = tk.StringVar()
PresetColor3 = tk.StringVar()
PresetColor4 = tk.StringVar()
PresetColor5 = tk.StringVar()
PresetColor6 = tk.StringVar()
PresetColor7 = tk.StringVar()
PresetColor8 = tk.StringVar()
PresetColor9 = tk.StringVar()
PresetColor10 = tk.StringVar()

# Variables used to save the names of the presets
Preset1Var = tk.StringVar()
Preset2Var = tk.StringVar()
Preset3Var = tk.StringVar()
Preset4Var = tk.StringVar()
Preset5Var = tk.StringVar()
Preset6Var = tk.StringVar()
Preset7Var = tk.StringVar()
Preset8Var = tk.StringVar()
Preset9Var = tk.StringVar()
Preset10Var = tk.StringVar()

# Name Generator variables
HumanNameGen1Var = tk.IntVar()
HumanNameGen2Var = tk.IntVar()
HumanNameGen3Var = tk.IntVar()
HumanNameGen4Var = tk.IntVar()

# Age Variables
MinAge = tk.IntVar()
MaxAge = tk.IntVar()

# Gender Toggle variables
MaleVar = tk.IntVar()
FemaleVar = tk.IntVar()

# Demographics variables
HumansVar = tk.IntVar()
DwarvesVar = tk.IntVar()
ElvesVar = tk.IntVar()
HalflingsVar = tk.IntVar()
HalfElvesVar = tk.IntVar()
GnomesVar = tk.IntVar()
HalfOrcsVar = tk.IntVar()
DragonbornVar = tk.IntVar()
TieflingsVar = tk.IntVar()

# Face descriptive toggle variables
EyeVar = tk.IntVar()
EarsVar = tk.IntVar()
MouthVar = tk.IntVar()
NoseVar = tk.IntVar()
ChinOrJawVar = tk.IntVar()
HairVar = tk.IntVar()
OtherVar = tk.IntVar()

# Physical descriptive toggle variables
HeightVar = tk.IntVar()
BodyVar = tk.IntVar()
HandsVar = tk.IntVar()
ScarVar = tk.IntVar()

# Accessory description toggle variables
TattoosVar = tk.IntVar()
JeweleryVar = tk.IntVar()
ClothesVar = tk.IntVar()

# Calm trait toggle variables
CalmPositiveVar = tk.IntVar()
CalmNeutralVar = tk.IntVar()
CalmNegativeVar = tk.IntVar()

# Stressed trait toggle variables
StressedPositiveVar = tk.IntVar()
StressedNeutralVar = tk.IntVar()
StressedNegativeVar = tk.IntVar()

# Profession toggle variables
CommonerCraftsmenVar = tk.IntVar()
CommonerLaborerVar = tk.IntVar()
CommonerProfessionsVar = tk.IntVar()
FarmersVar = tk.IntVar()
MilitaryAndWarriorsVar = tk.IntVar()
BureaucratsVar = tk.IntVar()
ClergymenVar = tk.IntVar()
CriminalsVar = tk.IntVar()
AcademicsVar = tk.IntVar()
MagiciansVar = tk.IntVar()

# Mood toggle variables
HappyVar = tk.IntVar()
SadVar = tk.IntVar()
DisgustedVar = tk.IntVar()
AngryVar = tk.IntVar()
FearfulVar = tk.IntVar()
BadVar = tk.IntVar()
SurprisedVar = tk.IntVar()

# Reaction toggle variables
HostileReactionVar = tk.IntVar()
UnhappyReactionVar = tk.IntVar()
DisgruntledReactionVar = tk.IntVar()
IndifferentReactionVar = tk.IntVar()
PleasedReactionVar = tk.IntVar()
HappyReactionVar = tk.IntVar()

FriendlyReactionVar = tk.IntVar()

# Motivation toggle variables
OnTheRunMotivationVar = tk.IntVar()
VendettaMotivationVar = tk.IntVar()
InformationMotivationVar = tk.IntVar()
BuyingOrSellingMotivationVar = tk.IntVar()
LocalQuestMotivationVar = tk.IntVar()
QuestEnemyMotivationVar = tk.IntVar()
QuestTreasureMotivationVar = tk.IntVar()

# These functions are used to create a list of the current toggles in the
# description menus
def GetAll():
    AllCurrentVariables = [Color0.get(),Color1.get(),Color2.get(),
                HumanNameGen1Var.get(), HumanNameGen2Var.get(), HumanNameGen3Var.get(),HumanNameGen4Var.get(),
                MinAge.get(),MaxAge.get(),
                MaleVar.get(),FemaleVar.get(),
                HumansVar.get(),DwarvesVar.get(),ElvesVar.get(),HalflingsVar.get(),
                HalfElvesVar.get(),GnomesVar.get(),HalfOrcsVar.get(),DragonbornVar.get(),
                TieflingsVar.get(),
                EyeVar.get(),EarsVar.get(),MouthVar.get(),NoseVar.get(),ChinOrJawVar.get(),HairVar.get(),OtherVar.get(),
                HeightVar.get(),BodyVar.get(),HandsVar.get(),ScarVar.get(),
                TattoosVar.get(),JeweleryVar.get(),ClothesVar.get(),
                CalmPositiveVar.get(),CalmNeutralVar.get(),CalmNegativeVar.get(),
                StressedPositiveVar.get(),StressedNeutralVar.get(),StressedNegativeVar.get(),
                CommonerCraftsmenVar.get(),CommonerLaborerVar.get(),CommonerProfessionsVar.get(),
                FarmersVar.get(),MilitaryAndWarriorsVar.get(),BureaucratsVar.get(),ClergymenVar.get(),
                CriminalsVar.get(),AcademicsVar.get(),MagiciansVar.get(),
                HappyVar.get(),SadVar.get(),DisgustedVar.get(),AngryVar.get(),FearfulVar.get(),
                BadVar.get(),SurprisedVar.get(),
                HostileReactionVar.get(),UnhappyReactionVar.get(),DisgruntledReactionVar.get(),
                IndifferentReactionVar.get(),PleasedReactionVar.get(),HappyReactionVar.get(),FriendlyReactionVar.get(),
                OnTheRunMotivationVar.get(), VendettaMotivationVar.get(), InformationMotivationVar.get(),
                BuyingOrSellingMotivationVar.get(),LocalQuestMotivationVar.get(),
                QuestEnemyMotivationVar.get(),QuestTreasureMotivationVar.get()]
    return AllCurrentVariables
    
def GetDisplay():
    Display = [ShowPresets.get(), ShowRandomNPC.get(), ShowName.get(), ShowAge.get(), ShowGender.get(),
               ShowRace.get(), ShowVoiceSpeed.get(), ShowVoiceQuality.get(),
               ShowFaceDescription.get(), ShowPhysicalDescription.get(),
               ShowAccessoryDescription.get(), ShowProfession.get(),
               ShowCalmTrait.get(), ShowStressedTrait.get(), ShowMood.get(),
               ShowReaction.get(), ShowMotivation.get(), ShowNotes.get(), ShowExport.get()]
    return Display

def GetPresets():
    Presets = [Preset1Var.get(), Preset2Var.get(), Preset3Var.get(), Preset4Var.get(),Preset5Var.get(),
               Preset6Var.get(),Preset7Var.get(),Preset8Var.get(),Preset9Var.get(),Preset10Var.get()]
    return Presets

def GetName():
    Names = [HumanNameGen1Var.get(), HumanNameGen2Var.get(), HumanNameGen3Var.get(),
            HumanNameGen4Var.get()]
    return Names

def GetAges():
    Ages = [MinAge.get(),MaxAge.get()]
    return Ages

def GetRaces():
    Races = [HumansVar.get(),DwarvesVar.get(),ElvesVar.get(),HalflingsVar.get(),
    HalfElvesVar.get(),GnomesVar.get(),HalfOrcsVar.get(),DragonbornVar.get(),TieflingsVar.get()]
    return Races

def GetColors():
    Colors = [Color0.get(),Color1.get(),Color2.get(),PresetColor1.get(),PresetColor2.get(),
              PresetColor3.get(),PresetColor4.get(),PresetColor5.get(),
              PresetColor6.get(),PresetColor7.get(),PresetColor8.get(),
              PresetColor9.get(),PresetColor10.get()]
    return Colors

def GetGenderToggles():
    Toggles = [MaleVar.get(),FemaleVar.get()]
    return Toggles

def GetFaceToggles():
    Toggles = [EyeVar.get(),EarsVar.get(),MouthVar.get(),NoseVar.get(),
               ChinOrJawVar.get(),HairVar.get(),OtherVar.get()]
    return Toggles

def GetPhysicalToggles():
    Toggles = [HeightVar.get(),BodyVar.get(),HandsVar.get(),ScarVar.get()]
    return Toggles

def GetAccessoryToggles():
    Toggles = [TattoosVar.get(),JeweleryVar.get(),ClothesVar.get()]
    return Toggles

def GetCalmTraitToggles():
    Toggles = [CalmPositiveVar.get(),CalmNeutralVar.get(),CalmNegativeVar.get()]
    return Toggles

def GetStressedTraitToggles():
    Toggles = [StressedPositiveVar.get(),StressedNeutralVar.get(),StressedNegativeVar.get()]
    return Toggles

def GetProfessionToggles():
    Toggles = [CommonerCraftsmenVar.get(),CommonerLaborerVar.get(),CommonerProfessionsVar.get(),
               FarmersVar.get(),MilitaryAndWarriorsVar.get(),BureaucratsVar.get(),ClergymenVar.get(),
               CriminalsVar.get(),AcademicsVar.get(),MagiciansVar.get()]
    return Toggles

def GetMoodToggles():
    Toggles = [HappyVar.get(),SadVar.get(),DisgustedVar.get(),AngryVar.get(),FearfulVar.get(),
               BadVar.get(),SurprisedVar.get()]
    return Toggles

def GetReactionToggles():
    Toggles = [HostileReactionVar.get(),UnhappyReactionVar.get(),DisgruntledReactionVar.get(),
               IndifferentReactionVar.get(),PleasedReactionVar.get(),HappyReactionVar.get(),FriendlyReactionVar.get()]
    return Toggles

def GetMotivationToggles():
    Toggles = [OnTheRunMotivationVar.get(), VendettaMotivationVar.get(), InformationMotivationVar.get(),
               BuyingOrSellingMotivationVar.get(),LocalQuestMotivationVar.get(),
               QuestEnemyMotivationVar.get(),QuestTreasureMotivationVar.get()]
    return Toggles

#####
# Set the variables to the stored values from last time
# first read in the files that will be saved from last time
#
#####
DisplayPath = 'Tables/Toggles/Display.csv'
DisplayPath = os.path.join(ScriptDir, DisplayPath)
InitialDisplay = []
with open(DisplayPath) as f:
    reader = csv.reader(f)
    InitialDisplay = next(reader)

ActivePresetPath = 'Tables/Toggles/ActivePreset.csv'
ActivePresetPath = os.path.join(ScriptDir, ActivePresetPath)
InitialActivePreset = []
with open(ActivePresetPath) as f:
    reader = csv.reader(f)
    InitialActivePreset = next(reader)

ColorsPath = 'Tables/Toggles/Colors.csv'
ColorsPath = os.path.join(ScriptDir, ColorsPath)
InitialColors = []
with open(ColorsPath) as f:
    reader = csv.reader(f)
    InitialColors = next(reader)

PresetsPath = 'Tables/Presets/PresetNames.csv'
PresetsPath = os.path.join(ScriptDir, PresetsPath)
InitialPresets = []
with open(PresetsPath) as f:
    reader = csv.reader(f)
    InitialPresets = next(reader)

NamePath = 'Tables/Toggles/Name.csv'
NamePath = os.path.join(ScriptDir, NamePath)
InitialName = []
with open(NamePath) as f:
    reader = csv.reader(f)
    InitialName = next(reader)

AgePath = 'Tables/Toggles/Age.csv'
AgePath = os.path.join(ScriptDir, AgePath)
InitialAge = []
with open(AgePath) as f:
    reader = csv.reader(f)
    InitialAge = next(reader)

GenderPath = 'Tables/Toggles/Gender.csv'
GenderPath = os.path.join(ScriptDir, GenderPath)
InitialGender = []
with open(GenderPath) as f:
    reader = csv.reader(f)
    InitialGender = next(reader)

RacePath = 'Tables/Toggles/Race.csv'
RacePath = os.path.join(ScriptDir, RacePath)
InitialRace = []
with open(RacePath) as f:
    reader = csv.reader(f)
    InitialRace = next(reader)

FacePath = 'Tables/Toggles/Face.csv'
FacePath = os.path.join(ScriptDir, FacePath)
InitialFace = []
with open(FacePath) as f:
    reader = csv.reader(f)
    InitialFace = next(reader)

PhysicalPath = 'Tables/Toggles/Physical.csv'
PhysicalPath = os.path.join(ScriptDir, PhysicalPath)
InitialPhysical = []
with open(PhysicalPath) as f:
    reader = csv.reader(f)
    InitialPhysical = next(reader)

AccessoryPath = 'Tables/Toggles/Accessory.csv'
AccessoryPath = os.path.join(ScriptDir, AccessoryPath)
InitialAccessory = []
with open(AccessoryPath) as f:
    reader = csv.reader(f)
    InitialAccessory = next(reader)

CalmPath = 'Tables/Toggles/Calm.csv'
CalmPath = os.path.join(ScriptDir, CalmPath)
InitialCalm = []
with open(CalmPath) as f:
    reader = csv.reader(f)
    InitialCalm = next(reader)

StressedPath = 'Tables/Toggles/Stressed.csv'
StressedPath = os.path.join(ScriptDir, StressedPath)
InitialStressed = []
with open(StressedPath) as f:
    reader = csv.reader(f)
    InitialStressed = next(reader)

ProfessionPath = 'Tables/Toggles/Profession.csv'
ProfessionPath = os.path.join(ScriptDir, ProfessionPath)
InitialProfessions = []
with open(ProfessionPath) as f:
    reader = csv.reader(f)
    InitialProfession = next(reader)

MoodPath = 'Tables/Toggles/Mood.csv'
MoodPath = os.path.join(ScriptDir, MoodPath)
InitialMoods = []
with open(MoodPath) as f:
    reader = csv.reader(f)
    InitialMood = next(reader)

ReactionPath = 'Tables/Toggles/Reaction.csv'
ReactionPath = os.path.join(ScriptDir, ReactionPath)
InitialReactions = []
with open(ReactionPath) as f:
    reader = csv.reader(f)
    InitialReaction = next(reader)

MotivationPath = 'Tables/Toggles/Motivation.csv'
MotivationPath = os.path.join(ScriptDir, MotivationPath)
InitialMotivations = []
with open(MotivationPath) as f:
    reader = csv.reader(f)
    InitialMotivation = next(reader)

###
# Set all of the toggle variables to be what they
# were last time the program was run
###

ShowPresets.set(InitialDisplay[0])
ShowRandomNPC.set(InitialDisplay[1])
ShowName.set(InitialDisplay[2])
ShowAge.set(InitialDisplay[3])
ShowGender.set(InitialDisplay[4])
ShowRace.set(InitialDisplay[5])
ShowVoiceSpeed.set(InitialDisplay[6])
ShowVoiceQuality.set(InitialDisplay[7])
ShowFaceDescription.set(InitialDisplay[8])
ShowPhysicalDescription.set(InitialDisplay[9])
ShowAccessoryDescription.set(InitialDisplay[10])
ShowProfession.set(InitialDisplay[11])
ShowCalmTrait.set(InitialDisplay[12])
ShowStressedTrait.set(InitialDisplay[13])
ShowMood.set(InitialDisplay[14])
ShowReaction.set(InitialDisplay[15])
ShowMotivation.set(InitialDisplay[16])
ShowNotes.set(InitialDisplay[17])
ShowExport.set(InitialDisplay[18])

ActivePreset.set(InitialActivePreset[0])

Color0.set(InitialColors[0])
Color1.set(InitialColors[1])
Color2.set(InitialColors[2])
PresetColor1.set(InitialColors[3])
PresetColor2.set(InitialColors[4])
PresetColor3.set(InitialColors[5])
PresetColor4.set(InitialColors[6])
PresetColor5.set(InitialColors[7])
PresetColor6.set(InitialColors[8])
PresetColor7.set(InitialColors[9])
PresetColor8.set(InitialColors[10])
PresetColor9.set(InitialColors[11])
PresetColor10.set(InitialColors[12])

Preset1Var.set(InitialPresets[0])
Preset2Var.set(InitialPresets[1])
Preset3Var.set(InitialPresets[2])
Preset4Var.set(InitialPresets[3])
Preset5Var.set(InitialPresets[4])
Preset6Var.set(InitialPresets[5])
Preset7Var.set(InitialPresets[6])
Preset8Var.set(InitialPresets[7])
Preset9Var.set(InitialPresets[8])
Preset10Var.set(InitialPresets[9])

HumanNameGen1Var.set(int(InitialName[0]))
HumanNameGen2Var.set(int(InitialName[1]))
HumanNameGen3Var.set(int(InitialName[2]))
HumanNameGen4Var.set(int(InitialName[3]))

MinAge.set(InitialAge[0])
MaxAge.set(InitialAge[1])

MaleVar.set(int(InitialGender[0]))
FemaleVar.set(int(InitialGender[1]))

HumansVar.set(InitialRace[0])
DwarvesVar.set(InitialRace[1])
ElvesVar.set(InitialRace[2])
HalflingsVar.set(InitialRace[3])
HalfElvesVar.set(InitialRace[4])
GnomesVar.set(InitialRace[5])
HalfOrcsVar.set(InitialRace[6])
DragonbornVar.set(InitialRace[7])
TieflingsVar.set(InitialRace[8])

EyeVar.set(int(InitialFace[0]))
EarsVar.set(int(InitialFace[1]))
MouthVar.set(int(InitialFace[2]))
NoseVar.set(int(InitialFace[3]))
ChinOrJawVar.set(int(InitialFace[4]))
HairVar.set(int(InitialFace[5]))
OtherVar.set(int(InitialFace[6]))
    
EyeVar.set(int(InitialFace[0]))
EarsVar.set(int(InitialFace[1]))
MouthVar.set(int(InitialFace[2]))
NoseVar.set(int(InitialFace[3]))
ChinOrJawVar.set(int(InitialFace[4]))
HairVar.set(int(InitialFace[5]))
OtherVar.set(int(InitialFace[6]))

HeightVar.set(int(InitialPhysical[0]))
BodyVar.set(int(InitialPhysical[1]))
HandsVar.set(int(InitialPhysical[2]))
ScarVar.set(int(InitialPhysical[3]))

TattoosVar.set(int(InitialAccessory[0]))
JeweleryVar.set(int(InitialAccessory[1]))
ClothesVar.set(int(InitialAccessory[2]))

CalmPositiveVar.set(int(InitialCalm[0]))
CalmNeutralVar.set(int(InitialCalm[1]))
CalmNegativeVar.set(int(InitialCalm[2]))

StressedPositiveVar.set(int(InitialStressed[0]))
StressedNeutralVar.set(int(InitialStressed[1]))
StressedNegativeVar.set(int(InitialStressed[2]))

CommonerCraftsmenVar.set(int(InitialProfession[0]))
CommonerLaborerVar.set(int(InitialProfession[1]))
CommonerProfessionsVar.set(int(InitialProfession[2]))
FarmersVar.set(int(InitialProfession[3]))
MilitaryAndWarriorsVar.set(int(InitialProfession[4]))
BureaucratsVar.set(int(InitialProfession[5]))
ClergymenVar.set(int(InitialProfession[6]))
CriminalsVar.set(int(InitialProfession[7]))
AcademicsVar.set(int(InitialProfession[8]))
MagiciansVar.set(int(InitialProfession[9]))

HappyVar.set(int(InitialMood[0]))
SadVar.set(int(InitialMood[1]))
DisgustedVar.set(int(InitialMood[2]))
AngryVar.set(int(InitialMood[3]))
FearfulVar.set(int(InitialMood[4]))
BadVar.set(int(InitialMood[5]))
SurprisedVar.set(int(InitialMood[6]))

HostileReactionVar.set(int(InitialReaction[0]))
UnhappyReactionVar.set(int(InitialReaction[1]))
DisgruntledReactionVar.set(int(InitialReaction[2]))
IndifferentReactionVar.set(int(InitialReaction[3]))
PleasedReactionVar.set(int(InitialReaction[4]))
HappyReactionVar.set(int(InitialReaction[5]))
FriendlyReactionVar.set(int(InitialReaction[6]))

OnTheRunMotivationVar.set(int(InitialMotivation[0]))
VendettaMotivationVar.set(int(InitialMotivation[1]))
InformationMotivationVar.set(int(InitialMotivation[2]))
BuyingOrSellingMotivationVar.set(int(InitialMotivation[3]))
LocalQuestMotivationVar.set(int(InitialMotivation[4]))
QuestEnemyMotivationVar.set(int(InitialMotivation[5]))
QuestTreasureMotivationVar.set(int(InitialMotivation[6]))

##
# This variable n1 is created and immediately set to zero so that when the program
# runs initially it opens the excel file 'New NPCs.xlsx', and creates a blank list
# that will be used to store the names of exported NPCs
#
# n1 is iterated in the ExcelExportGUI() function
##
n1 = tk.IntVar()
n1.set(0)
if (n1.get() == 0):
    #Start the program by opening the excel sheet and making an empty list of names
    wb = xlsxwriter.Workbook('New NPCs.xlsx')
    NameList = []

###############################################
# Make functions that call the other functions#
###############################################


    
    
    
# The RC functions are what happens when the tk.Button is right clicked 
# that gives you options on what factors to choose from


Preset1Path = 'Tables/Presets/Preset1.csv'
Preset1Path = os.path.join(ScriptDir, Preset1Path)
Preset2Path = 'Tables/Presets/Preset2.csv'
Preset2Path = os.path.join(ScriptDir, Preset2Path)
Preset3Path = 'Tables/Presets/Preset3.csv'
Preset3Path = os.path.join(ScriptDir, Preset3Path)
Preset4Path = 'Tables/Presets/Preset4.csv'
Preset4Path = os.path.join(ScriptDir, Preset4Path)
Preset5Path = 'Tables/Presets/Preset5.csv'
Preset5Path = os.path.join(ScriptDir, Preset5Path)
Preset6Path = 'Tables/Presets/Preset6.csv'
Preset6Path = os.path.join(ScriptDir, Preset6Path)
Preset7Path = 'Tables/Presets/Preset7.csv'
Preset7Path = os.path.join(ScriptDir, Preset7Path)
Preset8Path = 'Tables/Presets/Preset8.csv'
Preset8Path = os.path.join(ScriptDir, Preset8Path)
Preset9Path = 'Tables/Presets/Preset9.csv'
Preset9Path = os.path.join(ScriptDir, Preset9Path)
Preset10Path = 'Tables/Presets/Preset10.csv'
Preset10Path = os.path.join(ScriptDir, Preset10Path)

def SetPreset(Preset):
    '''
    This takes a list of values and saves the current values them to the
    active variables in the program
    '''
    Color0.set(Preset[0])
    Color1.set(Preset[1])
    Color2.set(Preset[2])
    HumanNameGen1Var.set(int(Preset[3]))
    HumanNameGen2Var.set(int(Preset[4]))
    HumanNameGen3Var.set(int(Preset[5]))
    HumanNameGen4Var.set(int(Preset[6]))
    MinAge.set(int(Preset[7]))
    MaxAge.set(int(Preset[8]))
    MaleVar.set(int(Preset[9]))
    FemaleVar.set(int(Preset[10]))
    HumansVar.set(int(Preset[11]))
    DwarvesVar.set(int(Preset[12]))
    ElvesVar.set(int(Preset[13]))
    HalflingsVar.set(int(Preset[14]))
    HalfElvesVar.set(int(Preset[15]))
    GnomesVar.set(int(Preset[16]))
    HalfOrcsVar.set(int(Preset[17]))
    DragonbornVar.set(int(Preset[18]))
    TieflingsVar.set(int(Preset[19]))
    EyeVar.set(int(Preset[20]))
    EarsVar.set(int(Preset[21]))
    MouthVar.set(int(Preset[22]))
    NoseVar.set(int(Preset[23]))
    ChinOrJawVar.set(int(Preset[24]))
    HairVar.set(int(Preset[25]))
    OtherVar.set(int(Preset[26]))
    HeightVar.set(int(Preset[27]))
    BodyVar.set(int(Preset[28]))
    HandsVar.set(int(Preset[29]))
    ScarVar.set(int(Preset[30]))
    TattoosVar.set(int(Preset[31]))
    JeweleryVar.set(int(Preset[32]))
    ClothesVar.set(int(Preset[33]))
    CalmPositiveVar.set(int(Preset[34]))
    CalmNeutralVar.set(int(Preset[35]))
    CalmNegativeVar.set(int(Preset[36]))
    StressedPositiveVar.set(int(Preset[37]))
    StressedNeutralVar.set(int(Preset[38]))
    StressedNegativeVar.set(int(Preset[39]))
    CommonerCraftsmenVar.set(int(Preset[40]))
    CommonerLaborerVar.set(int(Preset[41]))
    CommonerProfessionsVar.set(int(Preset[42]))
    FarmersVar.set(int(Preset[43]))
    MilitaryAndWarriorsVar.set(int(Preset[44]))
    BureaucratsVar.set(int(Preset[45]))
    ClergymenVar.set(int(Preset[46]))
    CriminalsVar.set(int(Preset[47]))
    AcademicsVar.set(int(Preset[48]))
    MagiciansVar.set(int(Preset[49]))
    HappyVar.set(int(Preset[50]))
    SadVar.set(int(Preset[51]))
    DisgustedVar.set(int(Preset[52]))
    AngryVar.set(int(Preset[53]))
    FearfulVar.set(int(Preset[54]))
    BadVar.set(int(Preset[55]))
    SurprisedVar.set(int(Preset[56]))
    HostileReactionVar.set(int(Preset[57]))
    UnhappyReactionVar.set(int(Preset[58]))
    DisgruntledReactionVar.set(int(Preset[59]))
    IndifferentReactionVar.set(int(Preset[60]))
    PleasedReactionVar.set(int(Preset[61]))
    HappyReactionVar.set(int(Preset[62]))
    FriendlyReactionVar.set(int(Preset[63]))
    OnTheRunMotivationVar.set(int(Preset[64]))
    VendettaMotivationVar.set(int(Preset[65]))
    InformationMotivationVar.set(int(Preset[66]))
    BuyingOrSellingMotivationVar.set(int(Preset[67]))
    LocalQuestMotivationVar.set(int(Preset[68]))
    QuestEnemyMotivationVar.set(int(Preset[69]))
    QuestTreasureMotivationVar.set(int(Preset[70]))

# These programs are used to set the current values to the values saved
# as the presets currently
def SetPreset1():
    Preset1 = []
    with open(Preset1Path) as f:
        reader = csv.reader(f)
        Preset1 = next(reader)
    SetPreset(Preset1)
    SaveColors()
    AllGUI()
    ActivePreset.set(1)

def SetPreset2():
    Preset2 = []
    with open(Preset2Path) as f:
        reader = csv.reader(f)
        Preset2 = next(reader)
    SetPreset(Preset2)
    SaveColors()
    AllGUI()
    ActivePreset.set(2)
    
def SetPreset3():
    Preset3 = []
    with open(Preset3Path) as f:
        reader = csv.reader(f)
        Preset3 = next(reader)
    SetPreset(Preset3)
    SaveColors()
    AllGUI()
    ActivePreset.set(3)

def SetPreset4():
    Preset4 = []
    with open(Preset4Path) as f:
        reader = csv.reader(f)
        Preset4 = next(reader)
    SetPreset(Preset4)
    SaveColors()
    AllGUI()
    ActivePreset.set(4)

def SetPreset5():
    Preset5 = []
    with open(Preset5Path) as f:
        reader = csv.reader(f)
        Preset5 = next(reader)
    SetPreset(Preset5)
    SaveColors()
    AllGUI()
    ActivePreset.set(5)

def SetPreset6():
    Preset6 = []
    with open(Preset6Path) as f:
        reader = csv.reader(f)
        Preset6 = next(reader)
    SetPreset(Preset6)
    SaveColors()
    AllGUI()
    ActivePreset.set(6)

def SetPreset7():
    Preset7 = []
    with open(Preset7Path) as f:
        reader = csv.reader(f)
        Preset7 = next(reader)
    SetPreset(Preset7)
    SaveColors()
    AllGUI()
    ActivePreset.set(7)
 
def SetPreset8():
    Preset8 = []
    with open(Preset8Path) as f:
        reader = csv.reader(f)
        Preset8 = next(reader)
    SetPreset(Preset8)
    SaveColors()
    AllGUI()
    ActivePreset.set(8)

def SetPreset9():
    Preset9 = []
    with open(Preset9Path) as f:
        reader = csv.reader(f)
        Preset9 = next(reader)
    SetPreset(Preset9)
    SaveColors()
    AllGUI()
    ActivePreset.set(9)

def SetPreset10():
    Preset10 = []
    with open(Preset10Path) as f:
        reader = csv.reader(f)
        Preset10 = next(reader)
    SetPreset(Preset10)
    SaveColors()
    AllGUI()
    ActivePreset.set(10)

def SavePreset1():
    Preset1Button.config(bg=TempColor1.get())
    PresetColor1.set(TempColor1.get())
    AllToggles = GetAll()
    AllToggles[0] = TempColor0.get()
    AllToggles[1] = TempColor1.get()
    AllToggles[2] = TempColor2.get()
    if ActivePreset.get() == 1:
        Color0.set(TempColor0.get())
        Color1.set(TempColor1.get())
        Color2.set(TempColor2.get())
        SaveColors()
    with open(Preset1Path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(AllToggles)

def SavePreset2():
    Preset2Button.config(bg=TempColor1.get())
    PresetColor2.set(TempColor1.get())
    AllToggles = GetAll()
    AllToggles[0] = TempColor0.get()
    AllToggles[1] = TempColor1.get()
    AllToggles[2] = TempColor2.get()
    if ActivePreset.get() == 1:
        Color0.set(TempColor0.get())
        Color1.set(TempColor1.get())
        Color2.set(TempColor2.get())
        SaveColors()
    with open(Preset2Path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(AllToggles)

def SavePreset3():
    Preset3Button.config(bg=TempColor1.get())
    PresetColor3.set(TempColor1.get())
    AllToggles = GetAll()
    AllToggles[0] = TempColor0.get()
    AllToggles[1] = TempColor1.get()
    AllToggles[2] = TempColor2.get()
    if ActivePreset.get() == 1:
        Color0.set(TempColor0.get())
        Color1.set(TempColor1.get())
        Color2.set(TempColor2.get())
        SaveColors()
    with open(Preset3Path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(AllToggles)
        
def SavePreset4():
    Preset4Button.config(bg=TempColor1.get())
    PresetColor4.set(TempColor1.get())
    AllToggles = GetAll()
    AllToggles[0] = TempColor0.get()
    AllToggles[1] = TempColor1.get()
    AllToggles[2] = TempColor2.get()
    if ActivePreset.get() == 1:
        Color0.set(TempColor0.get())
        Color1.set(TempColor1.get())
        Color2.set(TempColor2.get())
        SaveColors()
    with open(Preset4Path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(AllToggles)  
        
def SavePreset5():
    Preset5Button.config(bg=TempColor1.get())
    PresetColor5.set(TempColor1.get())
    AllToggles = GetAll()
    AllToggles[0] = TempColor0.get()
    AllToggles[1] = TempColor1.get()
    AllToggles[2] = TempColor2.get()
    if ActivePreset.get() == 1:
        Color0.set(TempColor0.get())
        Color1.set(TempColor1.get())
        Color2.set(TempColor2.get())
        SaveColors()
    with open(Preset5Path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(AllToggles)  

def SavePreset6():
    Preset6Button.config(bg=TempColor1.get())
    PresetColor6.set(TempColor1.get())
    AllToggles = GetAll()
    AllToggles[0] = TempColor0.get()
    AllToggles[1] = TempColor1.get()
    AllToggles[2] = TempColor2.get()
    if ActivePreset.get() == 1:
        Color0.set(TempColor0.get())
        Color1.set(TempColor1.get())
        Color2.set(TempColor2.get())
        SaveColors()
    with open(Preset6Path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(AllToggles)  
        
def SavePreset7():
    Preset7Button.config(bg=TempColor1.get())
    PresetColor7.set(TempColor1.get())
    AllToggles = GetAll()
    AllToggles[0] = TempColor0.get()
    AllToggles[1] = TempColor1.get()
    AllToggles[2] = TempColor2.get()
    if ActivePreset.get() == 1:
        Color0.set(TempColor0.get())
        Color1.set(TempColor1.get())
        Color2.set(TempColor2.get())
        SaveColors()
    with open(Preset7Path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(AllToggles)  

def SavePreset8():
    Preset8Button.config(bg=TempColor1.get())
    PresetColor8.set(TempColor1.get())
    AllToggles = GetAll()
    AllToggles[0] = TempColor0.get()
    AllToggles[1] = TempColor1.get()
    AllToggles[2] = TempColor2.get()
    if ActivePreset.get() == 1:
        Color0.set(TempColor0.get())
        Color1.set(TempColor1.get())
        Color2.set(TempColor2.get())
        SaveColors()
    with open(Preset8Path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(AllToggles)  
        
def SavePreset9():
    Preset9Button.config(bg=TempColor1.get())
    PresetColor9.set(TempColor1.get())
    AllToggles = GetAll()
    AllToggles[0] = TempColor0.get()
    AllToggles[1] = TempColor1.get()
    AllToggles[2] = TempColor2.get()
    if ActivePreset.get() == 1:
        Color0.set(TempColor0.get())
        Color1.set(TempColor1.get())
        Color2.set(TempColor2.get())
        SaveColors()
    with open(Preset9Path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(AllToggles)

def SavePreset10():
    Preset10Button.config(bg=TempColor1.get())
    PresetColor10.set(TempColor1.get())
    AllToggles = GetAll()
    AllToggles[0] = TempColor0.get()
    AllToggles[1] = TempColor1.get()
    AllToggles[2] = TempColor2.get()
    if ActivePreset.get() == 1:
        Color0.set(TempColor0.get())
        Color1.set(TempColor1.get())
        Color2.set(TempColor2.get())
        SaveColors()
    with open(Preset10Path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(AllToggles)


# When the tk.Button is right clicked these menus pop up and you can change
# the name and save the currently selected values to be reloaded later
# or during the game.

TempColor0 = tk.StringVar()
TempColor1 = tk.StringVar()
TempColor2 = tk.StringVar()
        
def Preset1RC(event):
    top = tk.Toplevel(root)
    top.title('Preset 1')
    PresetLabel = tk.Label(top, text='Preset name:', width=10)
    PresetLabel.grid(row=0, column=0)
    Preset1Entry = tk.Entry(top, textvariable = Preset1Var, width=20)
    Preset1Entry.grid(row=0, column=1)
    
    def CheckTempColors():
        # This function is used when the check colors tk.Button is pressed
        # it'll show what the colors chosen would look like from the labels
        Color0Label.config(bg = TempColor0.get())
        Color1Label.config(bg = TempColor1.get())
        Color2Label.config(bg = TempColor2.get())
    
    def SaveTempColors():
        # This function is used to save the temporary colors over the old colors
        # and update the colors shown on the GUI
        CheckTempColors()
        Preset1[0] = TempColor0.get()
        Preset1[1] = TempColor1.get()
        Preset1[2] = TempColor2.get()
        Preset1Button.config(bg=TempColor1.get())
        
        # This saves the color for the preset button on the main GUI
        PresetColor1.set(TempColor1.get())
        Colors = GetColors()
        with open(ColorsPath, "w") as f:
            writer = csv.writer(f)
            writer.writerow(Colors)
            
        if ActivePreset.get() == 1:
            Color0.set(TempColor0.get())
            Color1.set(TempColor1.get())
            Color2.set(TempColor2.get())
            SaveColors()
        with open(Preset1Path, "w") as f:
            writer = csv.writer(f)
            writer.writerow(Preset1)
        
    # Get the values for the current preset so that the colors can be overwritten
    # should you want them to be different
    Preset1 = []
    with open(Preset1Path) as f:
        reader = csv.reader(f)
        Preset1 = next(reader)
        
    TempColor0.set(Preset1[0])
    TempColor1.set(Preset1[1])
    TempColor2.set(Preset1[2])
    
    # Build the color menu inside the pop up menu
    Color0Label = tk.Label(top,bg = TempColor0.get(), width=10)
    Color1Label = tk.Label(top,bg = TempColor1.get(), width=10)   
    Color2Label = tk.Label(top,bg = TempColor2.get(), width=10)
    Color0Entry = tk.Entry(top, text='Color 1', textvariable = TempColor0, width=20)
    Color1Entry = tk.Entry(top, text='Color 2', textvariable = TempColor1, width=20)
    Color2Entry = tk.Entry(top, text='Color 3', textvariable = TempColor2, width=20)
    Color0Entry.config(textvariable = TempColor0)
    Color1Entry.config(textvariable = TempColor1)
    Color2Entry.config(textvariable = TempColor2)
    
    # Create the buttons that let you check colors or save just the colors
    CheckColorsButton = tk.Button(top, text = 'Check colors', bg = TempColor0.get(),
                                  command = CheckTempColors, width=10)
    SaveColorsButton = tk.Button(top, text = 'Save colors', bg = TempColor0.get(),
                                 command = SaveTempColors, width=20)

    # Place the different widgets
    Color0Label.grid(row = 1, column = 0)
    Color1Label.grid(row = 2, column = 0)
    Color2Label.grid(row = 3, column = 0)
    
    Color0Entry.grid(row = 1, column = 1)
    Color1Entry.grid(row = 2, column = 1)
    Color2Entry.grid(row = 3, column = 1)
    
    CheckColorsButton.grid(row = 4, column=0)
    SaveColorsButton.grid(row=4, column=1)
    
    # Create and place the button that saves all settings
    PresetSaveButton = tk.Button(top, text = 'Save all current settings', width=31,
                              bg = TempColor0.get(),justify=tk.CENTER,command = SavePreset1)
    PresetSaveButton.grid(row=5, columnspan=2)
    
    top.grid()
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" % (x, y))

def Preset2RC(event):
    top = tk.Toplevel(root)
    top.title('Preset 2')
    PresetLabel = tk.Label(top, text='Preset name:', width=10)
    PresetLabel.grid(row=0, column=0)
    Preset2Entry = tk.Entry(top, textvariable = Preset2Var, width=20)
    Preset2Entry.grid(row=0, column=1)
    
    def CheckTempColors():
        # This function is used when the check colors tk.Button is pressed
        # it'll show what the colors chosen would look like from the labels
        Color0Label.config(bg = TempColor0.get())
        Color1Label.config(bg = TempColor1.get())
        Color2Label.config(bg = TempColor2.get())
    
    def SaveTempColors():
        # This function is used to save the temporary colors over the old colors
        # and update the colors shown on the GUI
        CheckTempColors()
        Preset2[0] = TempColor0.get()
        Preset2[1] = TempColor1.get()
        Preset2[2] = TempColor2.get()
        Preset2Button.config(bg=TempColor1.get())
        
        # This saves the color for the preset button on the main GUI
        PresetColor2.set(TempColor1.get())
        Colors = GetColors()
        with open(ColorsPath, "w") as f:
            writer = csv.writer(f)
            writer.writerow(Colors)
            
        if ActivePreset.get() == 2:
            Color0.set(TempColor0.get())
            Color1.set(TempColor1.get())
            Color2.set(TempColor2.get())
            SaveColors()
        with open(Preset2Path, "w") as f:
            writer = csv.writer(f)
            writer.writerow(Preset2)
        
    # Get the values for the current preset so that the colors can be overwritten
    # should you want them to be different
    Preset2 = []
    with open(Preset2Path) as f:
        reader = csv.reader(f)
        Preset2 = next(reader)
        
    TempColor0.set(Preset2[0])
    TempColor1.set(Preset2[1])
    TempColor2.set(Preset2[2])
    
    # Build the color menu inside the pop up menu
    Color0Label = tk.Label(top,bg = TempColor0.get(), width=10)
    Color1Label = tk.Label(top,bg = TempColor1.get(), width=10)   
    Color2Label = tk.Label(top,bg = TempColor2.get(), width=10)
    Color0Entry = tk.Entry(top, text='Color 1', textvariable = TempColor0, width=20)
    Color1Entry = tk.Entry(top, text='Color 2', textvariable = TempColor1, width=20)
    Color2Entry = tk.Entry(top, text='Color 3', textvariable = TempColor2, width=20)
    Color0Entry.config(textvariable = TempColor0)
    Color1Entry.config(textvariable = TempColor1)
    Color2Entry.config(textvariable = TempColor2)
    
    # Create the buttons that let you check colors or save just the colors
    CheckColorsButton = tk.Button(top, text = 'Check colors', bg = TempColor0.get(),
                                  command = CheckTempColors, width=10)
    SaveColorsButton = tk.Button(top, text = 'Save colors', bg = TempColor0.get(),
                                 command = SaveTempColors, width=20)

    # Place the different widgets
    Color0Label.grid(row = 1, column = 0)
    Color1Label.grid(row = 2, column = 0)
    Color2Label.grid(row = 3, column = 0)
    
    Color0Entry.grid(row = 1, column = 1)
    Color1Entry.grid(row = 2, column = 1)
    Color2Entry.grid(row = 3, column = 1)
    
    CheckColorsButton.grid(row = 4, column=0)
    SaveColorsButton.grid(row=4, column=1)
    
    # Create and place the button that saves all settings
    PresetSaveButton = tk.Button(top, text = 'Save all current settings', width=31,
                              bg = TempColor0.get(),justify=tk.CENTER,command = SavePreset2)
    PresetSaveButton.grid(row=5, columnspan=2)
    
    top.grid()
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" % (x, y))

def Preset3RC(event):
    top = tk.Toplevel(root)
    top.title('Preset 3')
    PresetLabel = tk.Label(top, text='Preset name:', width=10)
    PresetLabel.grid(row=0, column=0)
    Preset3Entry = tk.Entry(top, textvariable = Preset3Var, width=20)
    Preset3Entry.grid(row=0, column=1)
    
    def CheckTempColors():
        # This function is used when the check colors tk.Button is pressed
        # it'll show what the colors chosen would look like from the labels
        Color0Label.config(bg = TempColor0.get())
        Color1Label.config(bg = TempColor1.get())
        Color2Label.config(bg = TempColor2.get())
    
    def SaveTempColors():
        # This function is used to save the temporary colors over the old colors
        # and update the colors shown on the GUI
        CheckTempColors()
        Preset3[0] = TempColor0.get()
        Preset3[1] = TempColor1.get()
        Preset3[2] = TempColor2.get()
        Preset3Button.config(bg=TempColor1.get())
        
        # This saves the color for the preset button on the main GUI
        PresetColor3.set(TempColor1.get())
        Colors = GetColors()
        with open(ColorsPath, "w") as f:
            writer = csv.writer(f)
            writer.writerow(Colors)
            
        if ActivePreset.get() == 3:
            Color0.set(TempColor0.get())
            Color1.set(TempColor1.get())
            Color2.set(TempColor2.get())
            SaveColors()
        with open(Preset3Path, "w") as f:
            writer = csv.writer(f)
            writer.writerow(Preset3)
        
    # Get the values for the current preset so that the colors can be overwritten
    # should you want them to be different
    Preset3 = []
    with open(Preset3Path) as f:
        reader = csv.reader(f)
        Preset3 = next(reader)
        
    TempColor0.set(Preset3[0])
    TempColor1.set(Preset3[1])
    TempColor2.set(Preset3[2])
    
    # Build the color menu inside the pop up menu
    Color0Label = tk.Label(top,bg = TempColor0.get(), width=10)
    Color1Label = tk.Label(top,bg = TempColor1.get(), width=10)   
    Color2Label = tk.Label(top,bg = TempColor2.get(), width=10)
    Color0Entry = tk.Entry(top, text='Color 1', textvariable = TempColor0, width=20)
    Color1Entry = tk.Entry(top, text='Color 2', textvariable = TempColor1, width=20)
    Color2Entry = tk.Entry(top, text='Color 3', textvariable = TempColor2, width=20)
    Color0Entry.config(textvariable = TempColor0)
    Color1Entry.config(textvariable = TempColor1)
    Color2Entry.config(textvariable = TempColor2)
    
    # Create the buttons that let you check colors or save just the colors
    CheckColorsButton = tk.Button(top, text = 'Check colors', bg = TempColor0.get(),
                                  command = CheckTempColors, width=10)
    SaveColorsButton = tk.Button(top, text = 'Save colors', bg = TempColor0.get(),
                                 command = SaveTempColors, width=20)

    # Place the different widgets
    Color0Label.grid(row = 1, column = 0)
    Color1Label.grid(row = 2, column = 0)
    Color2Label.grid(row = 3, column = 0)
    
    Color0Entry.grid(row = 1, column = 1)
    Color1Entry.grid(row = 2, column = 1)
    Color2Entry.grid(row = 3, column = 1)
    
    CheckColorsButton.grid(row = 4, column=0)
    SaveColorsButton.grid(row=4, column=1)
    
    # Create and place the button that saves all settings
    PresetSaveButton = tk.Button(top, text = 'Save all current settings', width=31,
                              bg = TempColor0.get(),justify=tk.CENTER,command = SavePreset3)
    PresetSaveButton.grid(row=5, columnspan=2)
    
    top.grid()
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" % (x, y))
    
def Preset4RC(event):
    top = tk.Toplevel(root)
    top.title('Preset 4')
    PresetLabel = tk.Label(top, text='Preset name:', width=10)
    PresetLabel.grid(row=0, column=0)
    Preset4Entry = tk.Entry(top, textvariable = Preset4Var, width=20)
    Preset4Entry.grid(row=0, column=1)
    
    def CheckTempColors():
        # This function is used when the check colors tk.Button is pressed
        # it'll show what the colors chosen would look like from the labels
        Color0Label.config(bg = TempColor0.get())
        Color1Label.config(bg = TempColor1.get())
        Color2Label.config(bg = TempColor2.get())
    
    def SaveTempColors():
        # This function is used to save the temporary colors over the old colors
        # and update the colors shown on the GUI
        CheckTempColors()
        Preset4[0] = TempColor0.get()
        Preset4[1] = TempColor1.get()
        Preset4[2] = TempColor2.get()
        Preset4Button.config(bg=TempColor1.get())
        
        # This saves the color for the preset button on the main GUI
        PresetColor4.set(TempColor1.get())
        Colors = GetColors()
        with open(ColorsPath, "w") as f:
            writer = csv.writer(f)
            writer.writerow(Colors)
            
        if ActivePreset.get() == 4:
            Color0.set(TempColor0.get())
            Color1.set(TempColor1.get())
            Color2.set(TempColor2.get())
            SaveColors()
        with open(Preset4Path, "w") as f:
            writer = csv.writer(f)
            writer.writerow(Preset4)
        
    # Get the values for the current preset so that the colors can be overwritten
    # should you want them to be different
    Preset4 = []
    with open(Preset4Path) as f:
        reader = csv.reader(f)
        Preset4 = next(reader)
        
    TempColor0.set(Preset4[0])
    TempColor1.set(Preset4[1])
    TempColor2.set(Preset4[2])
    
    # Build the color menu inside the pop up menu
    Color0Label = tk.Label(top,bg = TempColor0.get(), width=10)
    Color1Label = tk.Label(top,bg = TempColor1.get(), width=10)   
    Color2Label = tk.Label(top,bg = TempColor2.get(), width=10)
    Color0Entry = tk.Entry(top, text='Color 1', textvariable = TempColor0, width=20)
    Color1Entry = tk.Entry(top, text='Color 2', textvariable = TempColor1, width=20)
    Color2Entry = tk.Entry(top, text='Color 3', textvariable = TempColor2, width=20)
    Color0Entry.config(textvariable = TempColor0)
    Color1Entry.config(textvariable = TempColor1)
    Color2Entry.config(textvariable = TempColor2)
    
    # Create the buttons that let you check colors or save just the colors
    CheckColorsButton = tk.Button(top, text = 'Check colors', bg = TempColor0.get(),
                                  command = CheckTempColors, width=10)
    SaveColorsButton = tk.Button(top, text = 'Save colors', bg = TempColor0.get(),
                                 command = SaveTempColors, width=20)

    # Place the different widgets
    Color0Label.grid(row = 1, column = 0)
    Color1Label.grid(row = 2, column = 0)
    Color2Label.grid(row = 3, column = 0)
    
    Color0Entry.grid(row = 1, column = 1)
    Color1Entry.grid(row = 2, column = 1)
    Color2Entry.grid(row = 3, column = 1)
    
    CheckColorsButton.grid(row = 4, column=0)
    SaveColorsButton.grid(row=4, column=1)
    
    # Create and place the button that saves all settings
    PresetSaveButton = tk.Button(top, text = 'Save all current settings', width=31,
                              bg = TempColor0.get(),justify=tk.CENTER,command = SavePreset4)
    PresetSaveButton.grid(row=5, columnspan=2)
    
    top.grid()
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" % (x, y))
    
def Preset5RC(event):
    top = tk.Toplevel(root)
    top.title('Preset 5')
    PresetLabel = tk.Label(top, text='Preset name:', width=10)
    PresetLabel.grid(row=0, column=0)
    Preset5Entry = tk.Entry(top, textvariable = Preset5Var, width=20)
    Preset5Entry.grid(row=0, column=1)
    
    def CheckTempColors():
        # This function is used when the check colors tk.Button is pressed
        # it'll show what the colors chosen would look like from the labels
        Color0Label.config(bg = TempColor0.get())
        Color1Label.config(bg = TempColor1.get())
        Color2Label.config(bg = TempColor2.get())
    
    def SaveTempColors():
        # This function is used to save the temporary colors over the old colors
        # and update the colors shown on the GUI
        CheckTempColors()
        Preset5[0] = TempColor0.get()
        Preset5[1] = TempColor1.get()
        Preset5[2] = TempColor2.get()
        Preset5Button.config(bg=TempColor1.get())
        
        # This saves the color for the preset button on the main GUI
        PresetColor5.set(TempColor1.get())
        Colors = GetColors()
        with open(ColorsPath, "w") as f:
            writer = csv.writer(f)
            writer.writerow(Colors)
            
        if ActivePreset.get() == 5:
            Color0.set(TempColor0.get())
            Color1.set(TempColor1.get())
            Color2.set(TempColor2.get())
            SaveColors()
        with open(Preset5Path, "w") as f:
            writer = csv.writer(f)
            writer.writerow(Preset5)
        
    # Get the values for the current preset so that the colors can be overwritten
    # should you want them to be different
    Preset5 = []
    with open(Preset5Path) as f:
        reader = csv.reader(f)
        Preset5 = next(reader)
        
    TempColor0.set(Preset5[0])
    TempColor1.set(Preset5[1])
    TempColor2.set(Preset5[2])
    
    # Build the color menu inside the pop up menu
    Color0Label = tk.Label(top,bg = TempColor0.get(), width=10)
    Color1Label = tk.Label(top,bg = TempColor1.get(), width=10)   
    Color2Label = tk.Label(top,bg = TempColor2.get(), width=10)
    Color0Entry = tk.Entry(top, text='Color 1', textvariable = TempColor0, width=20)
    Color1Entry = tk.Entry(top, text='Color 2', textvariable = TempColor1, width=20)
    Color2Entry = tk.Entry(top, text='Color 3', textvariable = TempColor2, width=20)
    Color0Entry.config(textvariable = TempColor0)
    Color1Entry.config(textvariable = TempColor1)
    Color2Entry.config(textvariable = TempColor2)
    
    # Create the buttons that let you check colors or save just the colors
    CheckColorsButton = tk.Button(top, text = 'Check colors', bg = TempColor0.get(),
                                  command = CheckTempColors, width=10)
    SaveColorsButton = tk.Button(top, text = 'Save colors', bg = TempColor0.get(),
                                 command = SaveTempColors, width=20)

    # Place the different widgets
    Color0Label.grid(row = 1, column = 0)
    Color1Label.grid(row = 2, column = 0)
    Color2Label.grid(row = 3, column = 0)
    
    Color0Entry.grid(row = 1, column = 1)
    Color1Entry.grid(row = 2, column = 1)
    Color2Entry.grid(row = 3, column = 1)
    
    CheckColorsButton.grid(row = 4, column=0)
    SaveColorsButton.grid(row=4, column=1)
    
    # Create and place the button that saves all settings
    PresetSaveButton = tk.Button(top, text = 'Save all current settings', width=31,
                              bg = TempColor0.get(),justify=tk.CENTER,command = SavePreset5)
    PresetSaveButton.grid(row=5, columnspan=2)
    
    top.grid()
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" % (x, y))

def Preset6RC(event):
    top = tk.Toplevel(root)
    top.title('Preset 6')
    PresetLabel = tk.Label(top, text='Preset name:', width=10)
    PresetLabel.grid(row=0, column=0)
    Preset6Entry = tk.Entry(top, textvariable = Preset6Var, width=20)
    Preset6Entry.grid(row=0, column=1)
    
    def CheckTempColors():
        # This function is used when the check colors tk.Button is pressed
        # it'll show what the colors chosen would look like from the labels
        Color0Label.config(bg = TempColor0.get())
        Color1Label.config(bg = TempColor1.get())
        Color2Label.config(bg = TempColor2.get())
    
    def SaveTempColors():
        # This function is used to save the temporary colors over the old colors
        # and update the colors shown on the GUI
        CheckTempColors()
        Preset6[0] = TempColor0.get()
        Preset6[1] = TempColor1.get()
        Preset6[2] = TempColor2.get()
        Preset6Button.config(bg=TempColor1.get())
        
        # This saves the color for the preset button on the main GUI
        PresetColor6.set(TempColor1.get())
        Colors = GetColors()
        with open(ColorsPath, "w") as f:
            writer = csv.writer(f)
            writer.writerow(Colors)
            
        if ActivePreset.get() == 6:
            Color0.set(TempColor0.get())
            Color1.set(TempColor1.get())
            Color2.set(TempColor2.get())
            SaveColors()
        with open(Preset6Path, "w") as f:
            writer = csv.writer(f)
            writer.writerow(Preset6)
        
    # Get the values for the current preset so that the colors can be overwritten
    # should you want them to be different
    Preset6 = []
    with open(Preset6Path) as f:
        reader = csv.reader(f)
        Preset6 = next(reader)
        
    TempColor0.set(Preset6[0])
    TempColor1.set(Preset6[1])
    TempColor2.set(Preset6[2])
    
    # Build the color menu inside the pop up menu
    Color0Label = tk.Label(top,bg = TempColor0.get(), width=10)
    Color1Label = tk.Label(top,bg = TempColor1.get(), width=10)   
    Color2Label = tk.Label(top,bg = TempColor2.get(), width=10)
    Color0Entry = tk.Entry(top, text='Color 1', textvariable = TempColor0, width=20)
    Color1Entry = tk.Entry(top, text='Color 2', textvariable = TempColor1, width=20)
    Color2Entry = tk.Entry(top, text='Color 3', textvariable = TempColor2, width=20)
    Color0Entry.config(textvariable = TempColor0)
    Color1Entry.config(textvariable = TempColor1)
    Color2Entry.config(textvariable = TempColor2)
    
    # Create the buttons that let you check colors or save just the colors
    CheckColorsButton = tk.Button(top, text = 'Check colors', bg = TempColor0.get(),
                                  command = CheckTempColors, width=10)
    SaveColorsButton = tk.Button(top, text = 'Save colors', bg = TempColor0.get(),
                                 command = SaveTempColors, width=20)

    # Place the different widgets
    Color0Label.grid(row = 1, column = 0)
    Color1Label.grid(row = 2, column = 0)
    Color2Label.grid(row = 3, column = 0)
    
    Color0Entry.grid(row = 1, column = 1)
    Color1Entry.grid(row = 2, column = 1)
    Color2Entry.grid(row = 3, column = 1)
    
    CheckColorsButton.grid(row = 4, column=0)
    SaveColorsButton.grid(row=4, column=1)
    
    # Create and place the button that saves all settings
    PresetSaveButton = tk.Button(top, text = 'Save all current settings', width=31,
                              bg = TempColor0.get(),justify=tk.CENTER,command = SavePreset6)
    PresetSaveButton.grid(row=5, columnspan=2)
    
    top.grid()
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" % (x, y))
    
def Preset7RC(event):
    top = tk.Toplevel(root)
    top.title('Preset 7')
    PresetLabel = tk.Label(top, text='Preset name:', width=10)
    PresetLabel.grid(row=0, column=0)
    Preset7Entry = tk.Entry(top, textvariable = Preset7Var, width=20)
    Preset7Entry.grid(row=0, column=1)
    
    def CheckTempColors():
        # This function is used when the check colors tk.Button is pressed
        # it'll show what the colors chosen would look like from the labels
        Color0Label.config(bg = TempColor0.get())
        Color1Label.config(bg = TempColor1.get())
        Color2Label.config(bg = TempColor2.get())
    
    def SaveTempColors():
        # This function is used to save the temporary colors over the old colors
        # and update the colors shown on the GUI
        CheckTempColors()
        Preset7[0] = TempColor0.get()
        Preset7[1] = TempColor1.get()
        Preset7[2] = TempColor2.get()
        Preset7Button.config(bg=TempColor1.get())
        
        # This saves the color for the preset button on the main GUI
        PresetColor7.set(TempColor1.get())
        Colors = GetColors()
        with open(ColorsPath, "w") as f:
            writer = csv.writer(f)
            writer.writerow(Colors)
            
        if ActivePreset.get() == 7:
            Color0.set(TempColor0.get())
            Color1.set(TempColor1.get())
            Color2.set(TempColor2.get())
            SaveColors()
        with open(Preset7Path, "w") as f:
            writer = csv.writer(f)
            writer.writerow(Preset7)
        
    # Get the values for the current preset so that the colors can be overwritten
    # should you want them to be different
    Preset7 = []
    with open(Preset7Path) as f:
        reader = csv.reader(f)
        Preset7 = next(reader)
        
    TempColor0.set(Preset7[0])
    TempColor1.set(Preset7[1])
    TempColor2.set(Preset7[2])
    
    # Build the color menu inside the pop up menu
    Color0Label = tk.Label(top,bg = TempColor0.get(), width=10)
    Color1Label = tk.Label(top,bg = TempColor1.get(), width=10)   
    Color2Label = tk.Label(top,bg = TempColor2.get(), width=10)
    Color0Entry = tk.Entry(top, text='Color 1', textvariable = TempColor0, width=20)
    Color1Entry = tk.Entry(top, text='Color 2', textvariable = TempColor1, width=20)
    Color2Entry = tk.Entry(top, text='Color 3', textvariable = TempColor2, width=20)
    Color0Entry.config(textvariable = TempColor0)
    Color1Entry.config(textvariable = TempColor1)
    Color2Entry.config(textvariable = TempColor2)
    
    # Create the buttons that let you check colors or save just the colors
    CheckColorsButton = tk.Button(top, text = 'Check colors', bg = TempColor0.get(),
                                  command = CheckTempColors, width=10)
    SaveColorsButton = tk.Button(top, text = 'Save colors', bg = TempColor0.get(),
                                 command = SaveTempColors, width=20)

    # Place the different widgets
    Color0Label.grid(row = 1, column = 0)
    Color1Label.grid(row = 2, column = 0)
    Color2Label.grid(row = 3, column = 0)
    
    Color0Entry.grid(row = 1, column = 1)
    Color1Entry.grid(row = 2, column = 1)
    Color2Entry.grid(row = 3, column = 1)
    
    CheckColorsButton.grid(row = 4, column=0)
    SaveColorsButton.grid(row=4, column=1)
    
    # Create and place the button that saves all settings
    PresetSaveButton = tk.Button(top, text = 'Save all current settings', width=31,
                              bg = TempColor0.get(),justify=tk.CENTER,command = SavePreset7)
    PresetSaveButton.grid(row=5, columnspan=2)
    
    top.grid()
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" % (x, y))

def Preset8RC(event):
    top = tk.Toplevel(root)
    top.title('Preset 8')
    PresetLabel = tk.Label(top, text='Preset name:', width=10)
    PresetLabel.grid(row=0, column=0)
    Preset8Entry = tk.Entry(top, textvariable = Preset8Var, width=20)
    Preset8Entry.grid(row=0, column=1)
    
    def CheckTempColors():
        # This function is used when the check colors tk.Button is pressed
        # it'll show what the colors chosen would look like from the labels
        Color0Label.config(bg = TempColor0.get())
        Color1Label.config(bg = TempColor1.get())
        Color2Label.config(bg = TempColor2.get())
    
    def SaveTempColors():
        # This function is used to save the temporary colors over the old colors
        # and update the colors shown on the GUI
        CheckTempColors()
        Preset8[0] = TempColor0.get()
        Preset8[1] = TempColor1.get()
        Preset8[2] = TempColor2.get()
        Preset8Button.config(bg=TempColor1.get())
        
        # This saves the color for the preset button on the main GUI
        PresetColor8.set(TempColor1.get())
        Colors = GetColors()
        with open(ColorsPath, "w") as f:
            writer = csv.writer(f)
            writer.writerow(Colors)
            
        if ActivePreset.get() == 8:
            Color0.set(TempColor0.get())
            Color1.set(TempColor1.get())
            Color2.set(TempColor2.get())
            SaveColors()
        with open(Preset8Path, "w") as f:
            writer = csv.writer(f)
            writer.writerow(Preset8)
        
    # Get the values for the current preset so that the colors can be overwritten
    # should you want them to be different
    Preset8 = []
    with open(Preset8Path) as f:
        reader = csv.reader(f)
        Preset8 = next(reader)
        
    TempColor0.set(Preset8[0])
    TempColor1.set(Preset8[1])
    TempColor2.set(Preset8[2])
    
    # Build the color menu inside the pop up menu
    Color0Label = tk.Label(top,bg = TempColor0.get(), width=10)
    Color1Label = tk.Label(top,bg = TempColor1.get(), width=10)   
    Color2Label = tk.Label(top,bg = TempColor2.get(), width=10)
    Color0Entry = tk.Entry(top, text='Color 1', textvariable = TempColor0, width=20)
    Color1Entry = tk.Entry(top, text='Color 2', textvariable = TempColor1, width=20)
    Color2Entry = tk.Entry(top, text='Color 3', textvariable = TempColor2, width=20)
    Color0Entry.config(textvariable = TempColor0)
    Color1Entry.config(textvariable = TempColor1)
    Color2Entry.config(textvariable = TempColor2)
    
    # Create the buttons that let you check colors or save just the colors
    CheckColorsButton = tk.Button(top, text = 'Check colors', bg = TempColor0.get(),
                                  command = CheckTempColors, width=10)
    SaveColorsButton = tk.Button(top, text = 'Save colors', bg = TempColor0.get(),
                                 command = SaveTempColors, width=20)

    # Place the different widgets
    Color0Label.grid(row = 1, column = 0)
    Color1Label.grid(row = 2, column = 0)
    Color2Label.grid(row = 3, column = 0)
    
    Color0Entry.grid(row = 1, column = 1)
    Color1Entry.grid(row = 2, column = 1)
    Color2Entry.grid(row = 3, column = 1)
    
    CheckColorsButton.grid(row = 4, column=0)
    SaveColorsButton.grid(row=4, column=1)
    
    # Create and place the button that saves all settings
    PresetSaveButton = tk.Button(top, text = 'Save all current settings', width=31,
                              bg = TempColor0.get(),justify=tk.CENTER,command = SavePreset8)
    PresetSaveButton.grid(row=5, columnspan=2)
    
    top.grid()
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" % (x, y))
    
def Preset9RC(event):
    top = tk.Toplevel(root)
    top.title('Preset 9')
    PresetLabel = tk.Label(top, text='Preset name:', width=10)
    PresetLabel.grid(row=0, column=0)
    Preset9Entry = tk.Entry(top, textvariable = Preset9Var, width=20)
    Preset9Entry.grid(row=0, column=1)
    
    def CheckTempColors():
        # This function is used when the check colors tk.Button is pressed
        # it'll show what the colors chosen would look like from the labels
        Color0Label.config(bg = TempColor0.get())
        Color1Label.config(bg = TempColor1.get())
        Color2Label.config(bg = TempColor2.get())
    
    def SaveTempColors():
        # This function is used to save the temporary colors over the old colors
        # and update the colors shown on the GUI
        CheckTempColors()
        Preset9[0] = TempColor0.get()
        Preset9[1] = TempColor1.get()
        Preset9[2] = TempColor2.get()
        Preset9Button.config(bg=TempColor1.get())
        
        # This saves the color for the preset button on the main GUI
        PresetColor9.set(TempColor1.get())
        Colors = GetColors()
        with open(ColorsPath, "w") as f:
            writer = csv.writer(f)
            writer.writerow(Colors)
            
        if ActivePreset.get() == 9:
            Color0.set(TempColor0.get())
            Color1.set(TempColor1.get())
            Color2.set(TempColor2.get())
            SaveColors()
        with open(Preset9Path, "w") as f:
            writer = csv.writer(f)
            writer.writerow(Preset9)
        
    # Get the values for the current preset so that the colors can be overwritten
    # should you want them to be different
    Preset9 = []
    with open(Preset9Path) as f:
        reader = csv.reader(f)
        Preset9 = next(reader)
        
    TempColor0.set(Preset9[0])
    TempColor1.set(Preset9[1])
    TempColor2.set(Preset9[2])
    
    # Build the color menu inside the pop up menu
    Color0Label = tk.Label(top,bg = TempColor0.get(), width=10)
    Color1Label = tk.Label(top,bg = TempColor1.get(), width=10)   
    Color2Label = tk.Label(top,bg = TempColor2.get(), width=10)
    Color0Entry = tk.Entry(top, text='Color 1', textvariable = TempColor0, width=20)
    Color1Entry = tk.Entry(top, text='Color 2', textvariable = TempColor1, width=20)
    Color2Entry = tk.Entry(top, text='Color 3', textvariable = TempColor2, width=20)
    Color0Entry.config(textvariable = TempColor0)
    Color1Entry.config(textvariable = TempColor1)
    Color2Entry.config(textvariable = TempColor2)
    
    # Create the buttons that let you check colors or save just the colors
    CheckColorsButton = tk.Button(top, text = 'Check colors', bg = TempColor0.get(),
                                  command = CheckTempColors, width=10)
    SaveColorsButton = tk.Button(top, text = 'Save colors', bg = TempColor0.get(),
                                 command = SaveTempColors, width=20)

    # Place the different widgets
    Color0Label.grid(row = 1, column = 0)
    Color1Label.grid(row = 2, column = 0)
    Color2Label.grid(row = 3, column = 0)
    
    Color0Entry.grid(row = 1, column = 1)
    Color1Entry.grid(row = 2, column = 1)
    Color2Entry.grid(row = 3, column = 1)
    
    CheckColorsButton.grid(row = 4, column=0)
    SaveColorsButton.grid(row=4, column=1)
    
    # Create and place the button that saves all settings
    PresetSaveButton = tk.Button(top, text = 'Save all current settings', width=31,
                              bg = TempColor0.get(),justify=tk.CENTER,command = SavePreset9)
    PresetSaveButton.grid(row=5, columnspan=2)
    
    top.grid()
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" % (x, y))

def Preset10RC(event):
    top = tk.Toplevel(root)
    top.title('Preset 10')
    PresetLabel = tk.Label(top, text='Preset name:', width=10)
    PresetLabel.grid(row=0, column=0)
    Preset10Entry = tk.Entry(top, textvariable = Preset10Var, width=20)
    Preset10Entry.grid(row=0, column=1)
    
    def CheckTempColors():
        # This function is used when the check colors tk.Button is pressed
        # it'll show what the colors chosen would look like from the labels
        Color0Label.config(bg = TempColor0.get())
        Color1Label.config(bg = TempColor1.get())
        Color2Label.config(bg = TempColor2.get())
    
    def SaveTempColors():
        # This function is used to save the temporary colors over the old colors
        # and update the colors shown on the GUI
        CheckTempColors()
        Preset10[0] = TempColor0.get()
        Preset10[1] = TempColor1.get()
        Preset10[2] = TempColor2.get()
        Preset10Button.config(bg=TempColor1.get())
        
        # This saves the color for the preset button on the main GUI
        PresetColor10.set(TempColor1.get())
        Colors = GetColors()
        with open(ColorsPath, "w") as f:
            writer = csv.writer(f)
            writer.writerow(Colors)
            
        if ActivePreset.get() == 10:
            Color0.set(TempColor0.get())
            Color1.set(TempColor1.get())
            Color2.set(TempColor2.get())
            SaveColors()
        with open(Preset10Path, "w") as f:
            writer = csv.writer(f)
            writer.writerow(Preset10)
        
    # Get the values for the current preset so that the colors can be overwritten
    # should you want them to be different
    Preset10 = []
    with open(Preset10Path) as f:
        reader = csv.reader(f)
        Preset10 = next(reader)
        
    TempColor0.set(Preset10[0])
    TempColor1.set(Preset10[1])
    TempColor2.set(Preset10[2])
    
    # Build the color menu inside the pop up menu
    Color0Label = tk.Label(top,bg = TempColor0.get(), width=10)
    Color1Label = tk.Label(top,bg = TempColor1.get(), width=10)   
    Color2Label = tk.Label(top,bg = TempColor2.get(), width=10)
    Color0Entry = tk.Entry(top, text='Color 1', textvariable = TempColor0, width=20)
    Color1Entry = tk.Entry(top, text='Color 2', textvariable = TempColor1, width=20)
    Color2Entry = tk.Entry(top, text='Color 3', textvariable = TempColor2, width=20)
    Color0Entry.config(textvariable = TempColor0)
    Color1Entry.config(textvariable = TempColor1)
    Color2Entry.config(textvariable = TempColor2)
    
    # Create the buttons that let you check colors or save just the colors
    CheckColorsButton = tk.Button(top, text = 'Check colors', bg = TempColor0.get(),
                                  command = CheckTempColors, width=10)
    SaveColorsButton = tk.Button(top, text = 'Save colors', bg = TempColor0.get(),
                                 command = SaveTempColors, width=20)

    # Place the different widgets
    Color0Label.grid(row = 1, column = 0)
    Color1Label.grid(row = 2, column = 0)
    Color2Label.grid(row = 3, column = 0)
    
    Color0Entry.grid(row = 1, column = 1)
    Color1Entry.grid(row = 2, column = 1)
    Color2Entry.grid(row = 3, column = 1)
    
    CheckColorsButton.grid(row = 4, column=0)
    SaveColorsButton.grid(row=4, column=1)
    
    # Create and place the button that saves all settings
    PresetSaveButton = tk.Button(top, text = 'Save all current settings', width=31,
                              bg = TempColor0.get(),justify=tk.CENTER,command = SavePreset10)
    PresetSaveButton.grid(row=5, columnspan=2)
    
    top.grid()
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" % (x, y))

# This sets the tk.Toplevel window relative to the
# root/main window

def NameRC(event):
    top = tk.Toplevel(root)
    top.title('Name generator menu')
    
    frame = tk.Frame(top)
    FirstBox = tk.Checkbutton(frame, text='First Human name generator', variable = HumanNameGen1Var)
    FirstBox.pack()
    SecondBox = tk.Checkbutton(frame, text='Second Human name generator', variable = HumanNameGen2Var)
    SecondBox.pack()
    ThirdBox = tk.Checkbutton(frame, text='Third Human name generator', variable = HumanNameGen3Var)
    ThirdBox.pack()
    FourthBox = tk.Checkbutton(frame, text='Fourth Human name generator', variable = HumanNameGen4Var)
    FourthBox.pack()
    frame.pack()
    # This sets the tk.Toplevel window relative to the
    # root/main window
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" % (x, y))
    

def AgeRC(event):
    
    def DefaultAge():
        # This is used to reset to the typical age ranges
        MinAge.set(1)
        MaxAge.set(100)
        
    top = tk.Toplevel(root)
    top.title('Age Menu')
    
    DefaultAgesButton = tk.Button(top, text = 'Default ages', command = DefaultAge, width = 20)

    
    RelativeMinLabel = tk.Label(top, text = 'Relative min', width=10)
    RelativeMaxLabel = tk.Label(top, text = 'Relative max', width=10)
    RelativeMinEntry = tk.Entry(top, textvariable = MinAge, width=10)
    RelativeMaxEntry = tk.Entry(top, textvariable = MaxAge, width=10)
    
    DefaultAgesButton.grid(row = 0, columnspan = 2)
    
    RelativeMinLabel.grid(row = 1, column = 0)
    RelativeMaxLabel.grid(row = 2, column = 0)

    RelativeMinEntry.grid(row = 1, column = 1)
    RelativeMaxEntry.grid(row = 2, column = 1)
    
    top.grid()
    # This sets the tk.Toplevel window relative to the
    # root/main window
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" % (x, y))
    
    def CheckAges():
        if (MinAge.get() <= MaxAge.get() and MinAge.get() >= 0):
            top.destroy()
        else:
            tk.Toplevel = tk.Toplevel()
            WarningLabel = tk.Label(tk.Toplevel, text = 'Yeah, no.')
            WarningLabel.pack()  
            tk.Toplevel.after(750,tk.Toplevel.destroy)
    top.protocol("WM_DELETE_WINDOW",CheckAges)

def GenderRC(event):
    top = tk.Toplevel(root)
    top.title('Genders')
    frame = tk.Frame(top)
    MaleBox = tk.Checkbutton(frame, text='Male', variable = MaleVar)
    MaleBox.pack()
    FemaleBox = tk.Checkbutton(frame, text='Female', variable = FemaleVar)
    FemaleBox.pack()
    frame.pack()
    # This sets the tk.Toplevel window relative to the
    # root/main window
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" % (x, y))

def RaceRC(event):
    '''
    This function opens up a window that lets you specify the demographic
    information of the location you are in.  It draws the information
    from an excel sheet in the tables section, it works fast enough for 
    me to not want to change it
    '''
    top = tk.Toplevel(root)
    
    RacePath = 'Tables/Toggles/Race.csv'
    RacePath = os.path.join(ScriptDir, RacePath)
    
    SumVal = tk.IntVar()
    def Sum():        
        SumVal.set(HumansVar.get()+DwarvesVar.get()+ElvesVar.get()\
        +HalflingsVar.get()+HalfElvesVar.get()+GnomesVar.get()\
        +HalfOrcsVar.get()+DragonbornVar.get()+TieflingsVar.get())
        
    def SaveDemos():
        Races = GetRaces()
        with open(RacePath, "w") as f:
            writer = csv.writer(f)
            writer.writerow(Races)
            
        Sum()
        if (SumVal.get() != 100):
            tk.Toplevel = tk.Toplevel()
            WarningLabel = tk.Label(tk.Toplevel, text = 'Not equal to 100')
            WarningLabel.pack()  
            tk.Toplevel.after(750,tk.Toplevel.destroy)
        else:
            top.destroy()
    
    def AllZero():
        HumansVar.set(0)
        DwarvesVar.set(0)
        ElvesVar.set(0)
        HalflingsVar.set(0)
        HalfElvesVar.set(0)
        GnomesVar.set(0)
        HalfOrcsVar.set(0)
        DragonbornVar.set(0)
        TieflingsVar.set(0)
    
    
    def Defaults():
        HumansVar.set(63)
        DwarvesVar.set(10)
        ElvesVar.set(10)
        HalflingsVar.set(5)
        HalfElvesVar.set(5)
        GnomesVar.set(3)
        HalfOrcsVar.set(2)
        DragonbornVar.set(1)
        TieflingsVar.set(1)
    
    def HumansOnly():
        AllZero()
        HumansVar.set(100)
        SaveDemos()
        top.after(500,top.destroy)
    
    def DwarvesOnly():
        AllZero()
        DwarvesVar.set(100)
        SaveDemos()
        top.after(500,top.destroy)
        
    def ElvesOnly():
        AllZero()
        ElvesVar.set(100)
        SaveDemos()
        top.after(500,top.destroy)
        
    def HalflingsOnly():
        AllZero()
        HalflingsVar.set(100)
        SaveDemos()
        top.after(500,top.destroy)
        
    def HalfElvesOnly():
        AllZero()
        HalfElvesVar.set(100)
        SaveDemos()
        top.after(500,top.destroy)
        
    def GnomesOnly():
        AllZero()
        GnomesVar.set(100)
        SaveDemos()
        top.after(500,top.destroy)
        
    def HalfOrcsOnly():
        AllZero()
        HalfOrcsVar.set(100)
        SaveDemos()
        top.after(500,top.destroy)
        
    def DragonbornOnly():
        AllZero()
        DragonbornVar.set(100)
        SaveDemos()
        top.after(500,top.destroy)
        
    def TieflingsOnly():
        AllZero()
        TieflingsVar.set(100)
        SaveDemos()
        top.after(500,top.destroy)
        
    # This block creates the tk.Buttons and entries
    DefaultsButton = tk.Button(top,text = 'Set to default percentages', command = Defaults)
    HumansEntry = tk.Entry(top,width=10,textvariable = HumansVar)
    HumansButton = tk.Button(top, text = 'Humans: ',width=11,anchor=tk.E,command = HumansOnly)
    DwarvesEntry = tk.Entry(top,width=10,textvariable = DwarvesVar)
    DwarvesButton = tk.Button(top, text = 'Dwarves: ',width=11,anchor=tk.E,command = DwarvesOnly)
    ElvesEntry = tk.Entry(top,width=10,textvariable = ElvesVar)
    ElvesButton = tk.Button(top, text = 'Elves: ',width=11,anchor=tk.E,command = ElvesOnly)
    HalflingsEntry = tk.Entry(top,width=10,textvariable = HalflingsVar)
    HalflingsButton = tk.Button(top, text = 'Halflings: ',width=11,anchor=tk.E,command = HalflingsOnly)
    HalfElvesEntry = tk.Entry(top,width=10,textvariable = HalfElvesVar)
    HalfElvesButton = tk.Button(top, text = 'Half-Elves: ',width=11,anchor=tk.E,command = HalfElvesOnly)
    GnomesEntry = tk.Entry(top,width=10,textvariable = GnomesVar)
    GnomesButton = tk.Button(top, text = 'Gnomes: ',width=11,anchor=tk.E,command = GnomesOnly)
    HalfOrcsEntry = tk.Entry(top,width=10,textvariable = HalfOrcsVar)
    HalfOrcsButton = tk.Button(top, text = 'HalfOrcs: ',width=11,anchor=tk.E,command = HalfOrcsOnly)
    DragonbornEntry = tk.Entry(top,width=10,textvariable = DragonbornVar)
    DragonbornButton = tk.Button(top, text = 'Dragonborn: ',width=11,anchor=tk.E,command = DragonbornOnly)
    TieflingsEntry = tk.Entry(top,width=10,textvariable = TieflingsVar)
    TieflingsButton = tk.Button(top, text = 'Tieflings: ',width=11,anchor=tk.E,command = TieflingsOnly)
    
    # Sum here is run first and then the tk.Button and label are made
    # so that it has an inital value
    Sum()
    SumButton = tk.Button(top, text = 'Sum the values', command = Sum,width=11)
    SumLabel = tk.Label(top, textvariable = SumVal,anchor=tk.W,width=9)
    
    # This sets the tk.Toplevel window relative to the
    # root/main window
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" % (x, y))
    
    # This block places the tk.Buttons and entries where I want them to be
#    DefaultsButton.grid(row = 0, columnspan =2)
    HumansButton.grid(row = 1, column = 0)
    HumansEntry.grid(row = 1, column = 1)
    DwarvesButton.grid(row = 2, column = 0)
    DwarvesEntry.grid(row = 2, column = 1)
    ElvesButton.grid(row = 3, column = 0)
    ElvesEntry.grid(row = 3, column = 1)
    HalflingsButton.grid(row = 4, column = 0)
    HalflingsEntry.grid(row = 4, column = 1)
    HalfElvesButton.grid(row = 5, column = 0)
    HalfElvesEntry.grid(row = 5, column = 1)
    GnomesButton.grid(row = 6, column = 0)
    GnomesEntry.grid(row = 6, column = 1)
    HalfOrcsButton.grid(row = 7, column = 0)
    HalfOrcsEntry.grid(row = 7, column = 1)
    DragonbornButton.grid(row = 8, column = 0)
    DragonbornEntry.grid(row = 8, column = 1)
    TieflingsButton.grid(row = 9, column = 0)
    TieflingsEntry.grid(row = 9, column = 1)
    SumButton.grid(row=10,column=0)
    SumLabel.grid(row=10,column=1)
    top.grid_columnconfigure(1,weight=2)
    top.grid()
    
    # This makes it so that when the window is closed the 
    # current demographics are saved
    top.protocol("WM_DELETE_WINDOW",SaveDemos)

def FaceDescriptionRC(event):
    top = tk.Toplevel(root)
    top.title('Face Descriptions')
    frame = tk.Frame(top)
    EyeBox = tk.Checkbutton(frame, text='Eye', variable = EyeVar)
    EyeBox.pack()
    EarsBox = tk.Checkbutton(frame, text='Ears', variable = EarsVar)
    EarsBox.pack()
    MouthBox = tk.Checkbutton(frame, text='Mouth', variable = MouthVar)
    MouthBox.pack()
    NoseBox = tk.Checkbutton(frame, text='Nose', variable = NoseVar)
    NoseBox.pack()
    ChinOrJawBox = tk.Checkbutton(frame, text='Chin/Jaw', variable = ChinOrJawVar)
    ChinOrJawBox.pack()
    HairBox = tk.Checkbutton(frame, text='Hair', variable = HairVar)
    HairBox.pack()
    OtherBox = tk.Checkbutton(frame, text='Other', variable = OtherVar)
    OtherBox.pack()
    frame.pack()
    # This sets the tk.Toplevel window relative to the
    # root/main window
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" % (x, y))
    
def PhysicalDescriptionRC(event):
    top = tk.Toplevel(root)
    top.title('Physical Descriptions')
    frame = tk.Frame(top)
    HairBox = tk.Checkbutton(frame, text='Hair', variable = HairVar)
    HairBox.pack()
    BodyBox = tk.Checkbutton(frame, text='Body', variable = BodyVar)
    BodyBox.pack()
    HandsBox = tk.Checkbutton(frame, text='Hands', variable = HandsVar)
    HandsBox.pack()
    ScarBox = tk.Checkbutton(frame, text='Scar', variable = ScarVar)
    ScarBox.pack()
    frame.pack()
    # This sets the tk.Toplevel window relative to the
    # root/main window
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" % (x, y))

def AccessoryDescriptionRC(event):
    top = tk.Toplevel(root)
    top.title('Accessory Descriptions')
    frame = tk.Frame(top)
    tattooBox = tk.Checkbutton(frame, text='Tattoos', variable = TattoosVar)
    tattooBox.pack()
    jeweleryBox = tk.Checkbutton(frame, text='Jewelery', variable = JeweleryVar)
    jeweleryBox.pack()
    clothesBox = tk.Checkbutton(frame, text='Clothes', variable = ClothesVar)
    clothesBox.pack()
    frame.pack()
    # This sets the tk.Toplevel window relative to the
    # root/main window
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" % (x, y))

def CalmTraitRC(event):
    top = tk.Toplevel(root)
    top.title('Calm Traits')
    frame = tk.Frame(top)
    positiveBox = tk.Checkbutton(frame, text='Positive', variable = CalmPositiveVar)
    positiveBox.pack()
    neutralBox = tk.Checkbutton(frame, text='Neutral', variable = CalmNeutralVar)
    neutralBox.pack()
    negativeBox = tk.Checkbutton(frame, text='Negative', variable = CalmNegativeVar)
    negativeBox.pack()
    frame.pack()
    # This sets the tk.Toplevel window relative to the
    # root/main window
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" % (x, y))

def StressedTraitRC(event):
    top = tk.Toplevel(root)
    top.title('Stressed Traits')
    frame = tk.Frame(top)
    positiveBox = tk.Checkbutton(frame, text='Positive', variable = StressedPositiveVar)
    positiveBox.pack()
    neutralBox = tk.Checkbutton(frame, text='Neutral', variable = StressedNeutralVar)
    neutralBox.pack()
    negativeBox = tk.Checkbutton(frame, text='Negative', variable = StressedNegativeVar)
    negativeBox.pack()
    frame.pack()
    # This sets the tk.Toplevel window relative to the
    # root/main window
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" % (x, y))

def ProfessionRC(event):
    top = tk.Toplevel(root)
    top.title('Professions')
    frame = tk.Frame(top)
    CommonerCraftsmenBox = tk.Checkbutton(frame, text='Commoner Craftsmen', variable = CommonerCraftsmenVar)
    CommonerCraftsmenBox.pack()
    CommonerLaborerBox = tk.Checkbutton(frame, text='Commoner Laborer', variable = CommonerLaborerVar)
    CommonerLaborerBox.pack()
    CommonerProfessionsBox = tk.Checkbutton(frame, text='Commoner Professions', variable = CommonerProfessionsVar)
    CommonerProfessionsBox.pack()
    FarmersBox = tk.Checkbutton(frame, text='Farmers', variable = FarmersVar)
    FarmersBox.pack()
    MilitaryAndWarriorsBox = tk.Checkbutton(frame, text='Military and warriors', variable = MilitaryAndWarriorsVar)
    MilitaryAndWarriorsBox.pack()
    BureaucratsBox = tk.Checkbutton(frame, text='Bureaucrats', variable = BureaucratsVar)
    BureaucratsBox.pack()
    ClergymenBox = tk.Checkbutton(frame, text='Clergymen', variable = ClergymenVar)
    ClergymenBox.pack()
    CriminalsBox = tk.Checkbutton(frame, text='Criminals', variable = CriminalsVar)
    CriminalsBox.pack()
    AcademicsBox = tk.Checkbutton(frame, text='Academics', variable = AcademicsVar)
    AcademicsBox.pack()
    MagiciansBox = tk.Checkbutton(frame, text='Magicians', variable = MagiciansVar)
    MagiciansBox.pack()
    frame.pack()
    # This sets the tk.Toplevel window relative to the
    # root/main window
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" % (x, y))

def MoodRC(event):
    top = tk.Toplevel(root)
    top.title('Moods')
    frame = tk.Frame(top)
    HappyBox = tk.Checkbutton(frame, text='Happy', variable = HappyVar)
    HappyBox.pack()
    SadBox = tk.Checkbutton(frame, text='Sad', variable = SadVar)
    SadBox.pack()
    DisgustedBox = tk.Checkbutton(frame, text='Disgusted', variable = DisgustedVar)
    DisgustedBox.pack()
    AngryBox = tk.Checkbutton(frame, text='Angry', variable = AngryVar)
    AngryBox.pack()
    FearfulBox = tk.Checkbutton(frame, text='Fearful', variable = FearfulVar)
    FearfulBox.pack()
    BadBox = tk.Checkbutton(frame, text='Bad', variable = BadVar)
    BadBox.pack()
    SurprisedBox = tk.Checkbutton(frame, text='Surprised', variable = SurprisedVar)
    SurprisedBox.pack()
    frame.pack()
    # This sets the tk.Toplevel window relative to the
    # root/main window
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" % (x, y))

def ReactionRC(event):
    top = tk.Toplevel(root)
    top.title('Reactions')
    frame = tk.Frame(top)
    HappyBox = tk.Checkbutton(frame, text='Hostile', variable = HostileReactionVar)
    HappyBox.pack()
    SadBox = tk.Checkbutton(frame, text='Unhappy', variable = UnhappyReactionVar)
    SadBox.pack()
    DisgustedBox = tk.Checkbutton(frame, text='Disgruntled', variable = DisgruntledReactionVar)
    DisgustedBox.pack()
    AngryBox = tk.Checkbutton(frame, text='Indifferent', variable = IndifferentReactionVar)
    AngryBox.pack()
    FearfulBox = tk.Checkbutton(frame, text='Pleased', variable = PleasedReactionVar)
    FearfulBox.pack()
    BadBox = tk.Checkbutton(frame, text='Happy', variable = HappyReactionVar)
    BadBox.pack()
    SurprisedBox = tk.Checkbutton(frame, text='Friendly', variable = FriendlyReactionVar)
    SurprisedBox.pack()
    frame.pack()
    # This sets the tk.Toplevel window relative to the
    # root/main window
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" % (x, y))

def MotivationRC(event):
    top = tk.Toplevel(root)
    top.title('Motivations')
    frame = tk.Frame(top)
    HappyBox = tk.Checkbutton(frame, text='On the run', variable = OnTheRunMotivationVar)
    HappyBox.pack()
    SadBox = tk.Checkbutton(frame, text='Vendetta', variable = VendettaMotivationVar)
    SadBox.pack()
    DisgustedBox = tk.Checkbutton(frame, text='Local, personal, or item information', variable = InformationMotivationVar)
    DisgustedBox.pack()
    AngryBox = tk.Checkbutton(frame, text='Buying or selling', variable = BuyingOrSellingMotivationVar)
    AngryBox.pack()
    FearfulBox = tk.Checkbutton(frame, text='Local quest', variable = LocalQuestMotivationVar)
    FearfulBox.pack()
    BadBox = tk.Checkbutton(frame, text='Quest for enemy', variable = QuestEnemyMotivationVar)
    BadBox.pack()
    SurprisedBox = tk.Checkbutton(frame, text='Quest for treasure', variable = QuestTreasureMotivationVar)
    SurprisedBox.pack()
    frame.pack()
    # This sets the tk.Toplevel window relative to the
    # root/main window
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" % (x, y))

def SaveToggles():
    '''
    Get the current toggles and save them so that next time the 
    program is loaded they will still be there
    '''
    Display = GetDisplay()
    Presets = GetPresets()
    Names = GetName()
    Ages = GetAges()
    GenderToggles = GetGenderToggles()
    Races = GetRaces()
    FaceToggles = GetFaceToggles()
    PhysicalToggles = GetPhysicalToggles()
    AccessoryToggles = GetAccessoryToggles()
    CalmTraitToggles = GetCalmTraitToggles()
    StressedTraitToggles = GetStressedTraitToggles()
    ProfessionToggles = GetProfessionToggles()
    MoodToggles = GetMoodToggles()
    ReactionToggles = GetReactionToggles()
    MotivationToggles = GetMotivationToggles()
    with open(DisplayPath, "w") as f:
        writer = csv.writer(f)
        writer.writerow(Display)
    with open(ActivePresetPath, "w") as f:
        writer = csv.writer(f)
        writer.writerow([ActivePreset.get()])
    with open(PresetsPath, "w") as f:
        writer = csv.writer(f)
        writer.writerow(Presets)
    with open(NamePath, "w") as f:
        writer = csv.writer(f)
        writer.writerow(Names)
    with open(AgePath, "w") as f:
        writer = csv.writer(f)
        writer.writerow(Ages)
    with open(GenderPath, "w") as f:
        writer = csv.writer(f)
        writer.writerow(GenderToggles)
    with open(RacePath, "w") as f:
        writer = csv.writer(f)
        writer.writerow(Races)
    with open(FacePath, "w") as f:
        writer = csv.writer(f)
        writer.writerow(FaceToggles)
    with open(PhysicalPath, "w") as f:
        writer = csv.writer(f)
        writer.writerow(PhysicalToggles)    
    with open(AccessoryPath, "w") as f:
        writer = csv.writer(f)
        writer.writerow(AccessoryToggles)
    with open(CalmPath, "w") as f:
        writer = csv.writer(f)
        writer.writerow(CalmTraitToggles)
    with open(StressedPath, "w") as f:
        writer = csv.writer(f)
        writer.writerow(StressedTraitToggles)
    with open(ProfessionPath, "w") as f:
        writer = csv.writer(f)
        writer.writerow(ProfessionToggles)
    with open(MoodPath, "w") as f:
        writer = csv.writer(f)
        writer.writerow(MoodToggles)
    with open(ReactionPath, "w") as f:
        writer = csv.writer(f)
        writer.writerow(ReactionToggles)
    with open(MotivationPath, "w") as f:
        writer = csv.writer(f)
        writer.writerow(MotivationToggles)

def SaveColors():
        '''
        This is used to update all of the colors and then save them to the
        csv file that they are read from when the application is opened
        '''
        NameFrame.config(bg = Color1.get())
        AgeFrame.config(bg = Color1.get())
        GenderFrame.config(bg = Color1.get())
        RaceFrame.config(bg = Color1.get())
        FaceDescriptionFrame.config(bg = Color2.get())
        PhysicalDescriptionFrame.config(bg = Color2.get())
        AccessoryDescriptionFrame.config(bg = Color2.get())
        VoiceSpeedFrame.config(bg = Color1.get())
        VoiceQualityFrame.config(bg = Color1.get())
        ProfessionFrame.config(bg = Color2.get())
        CalmTraitFrame.config(bg = Color1.get())
        StressedTraitFrame.config(bg = Color1.get())
        MoodFrame.config(bg = Color2.get())
        ReactionFrame.config(bg = Color2.get())
        MotivationFrame.config(bg = Color1.get())
        NotesFrame.config(bg = Color2.get())
        
        ColorButton.config(bg = Color0.get())
        AllButton.config(bg = Color0.get())
        NameButton.config(bg = Color1.get())
        AgeButton.config(bg = Color1.get())
        GenderButton.config(bg = Color1.get())
        RaceButton.config(bg = Color1.get())
        FaceDescriptionButton.config(bg = Color2.get())
        PhysicalDescriptionButton.config(bg = Color2.get())
        AccessoryDescriptionButton.config(bg = Color2.get())
        VoiceSpeedButton.config(bg = Color1.get())
        VoiceQualityButton.config(bg = Color1.get())
        ProfessionButton.config(bg = Color2.get())
        CalmTraitButton.config(bg = Color1.get())
        StressedTraitButton.config(bg = Color1.get())
        MoodButton.config(bg = Color2.get())
        ReactionButton.config(bg = Color2.get())
        MotivationButton.config(bg = Color1.get())
        NotesButton.config(bg = Color2.get())
        ExcelExportButton.config(bg = Color0.get())
        
        NameEntry.config(bg = Color1.get())
        AgeEntry.config(bg = Color1.get())
        GenderEntry.config(bg = Color1.get())
        RaceEntry.config(bg = Color1.get())
        FaceDescriptionEntry.config(bg = Color2.get())
        PhysicalDescriptionEntry.config(bg = Color2.get())
        AccessoryDescriptionEntry.config(bg = Color2.get())
        VoiceSpeedEntry.config(bg = Color1.get())
        VoiceQualityEntry.config(bg = Color1.get())
        ProfessionEntry.config(bg = Color2.get())
        CalmTraitEntry.config(bg = Color1.get())
        StressedTraitEntry.config(bg = Color1.get())
        MoodEntry.config(bg = Color2.get())
        ReactionEntry.config(bg = Color2.get())
        MotivationEntry.config(bg = Color1.get())
        NotesEntry.config(bg = Color2.get())
        
        Colors = GetColors()
        with open(ColorsPath, "w") as f:
            writer = csv.writer(f)
            writer.writerow(Colors)
        

def ColorGUI():
    '''
    This is a pop up menu that lets the user choose what colors they want to 
    use.  Like if you want an evil person set it to reds or some shit.
    '''
        
    def CheckColors():
        # This function is used when the check colors tk.Button is pressed
        # it'll show what the colors chosen would look like from the labels
        Color0Label.config(bg = Color0.get())
        Color1Label.config(bg = Color1.get())
        Color2Label.config(bg = Color2.get())
    
    top = tk.Toplevel(root)
    top.title('Color Menu')
    
    Color0Label = tk.Label(top,bg = Color0.get(), width=10)
    Color1Label = tk.Label(top,bg = Color1.get(), width=10)   
    Color2Label = tk.Label(top,bg = Color2.get(), width=10)
    Color0Entry = tk.Entry(top, text='Color 1', textvariable = Color0, width=10)
    Color1Entry = tk.Entry(top, text='Color 2', textvariable = Color1, width=10)
    Color2Entry = tk.Entry(top, text='Color 3', textvariable = Color2, width=10)
    Color0Entry.config(textvariable = Color0)
    Color1Entry.config(textvariable = Color1)
    Color2Entry.config(textvariable = Color2)
    
    CheckColorsButton = tk.Button(top, text = 'Check colors', bg = Color0.get(), command = CheckColors, width=22)
#    DefaultGreenButton.grid(row = 5, column = 0)
#    DefaultRedButton.grid(row = 5, column = 1)
    
    Color0Label.grid(row = 1, column = 0)
    Color1Label.grid(row = 2, column = 0)
    Color2Label.grid(row = 3, column = 0)
    
    Color0Entry.grid(row = 1, column = 1)
    Color1Entry.grid(row = 2, column = 1)
    Color2Entry.grid(row = 3, column = 1)
    
    CheckColorsButton.grid(row = 4, columnspan = 2)
    
    top.grid()
    # This sets the tk.Toplevel window relative to the
    # root/main window
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" % (x, y))
    
    def SaveColorsInMenu():
        SaveColors()
        top.destroy()
    
            
    top.protocol("WM_DELETE_WINDOW",SaveColorsInMenu)

def AllGUI(): 
    ###########################################################################
    # This creates an entire new NPC
    # Order is Gender -> Race -> Name -> Age -> Everything else
    # As long as Race and Gender come before the Age and Name it should work
    # 
    # This Race and Gender need to come first because:
    #   Age is race dependent
    #   Name is race and gender dependent
    ###########################################################################
    GenderGUI()
    RaceGUI()
    NameGUI()
    AgeGUI()
    FaceDescriptionGUI()
    PhysicalDescriptionGUI()
    AccessoryDescriptionGUI()
    VoiceSpeedGUI()
    VoiceQualityGUI()
    ProfessionGUI()
    CalmTraitGUI()
    StressedTraitGUI()
    MoodGUI()
    ReactionGUI()
    MotivationGUI()
    RumorGUI()

def NameGUI():
    # Calls function NameGen() from the GenratorFunctions.py file to set Name
    # Depends on: Race, Gender
    Toggles = GetName()
    Name.set(NameGen(Race.get(),Gender.get(),Toggles))
    
def AgeGUI():
    # Calls function AgeGen() to set Age
    # Depends on: Race
    
    Age.set(str(AgeGen(Race.get(),MinAge.get(),MaxAge.get()))+' years old')

def GenderGUI(): 
    # Calls function GenderGen() to set Gender
    # Depends on: 
    Toggles = GetGenderToggles()
    Gender.set(GenderGen(Toggles))

def ToggleGenderGUI(event):
    # This toggles between male and female because there's no
    # point in changing something with two values randomly
    # Depends on:  nothing   
    if (Gender.get() == 'Male'):
        Gender.set('Female')
    else:
        Gender.set('Male')
    
def RaceGUI():
    # Calls function RaceGen() to set Race
    # Depends on: 
    Races = GetRaces()
    Race.set(RaceGen(Races))
    
def FaceDescriptionGUI():
    # Calls function FaceDescriptionGen() to set FaceDescription
    # Depends on: 
    Toggles = GetFaceToggles()
    FaceDescription.set(FaceDescriptionGen(Toggles))
    
def PhysicalDescriptionGUI():
    # Calls function PhyscialDescriptionGen() to set (hyscialDescription
    # Depends on: 
    Toggles = GetPhysicalToggles()
    PhysicalDescription.set(PhyscialDescriptionGen(Toggles))
    
def AccessoryDescriptionGUI():
    # Calls function AccessoryDescriptionGen() to set AccessoryDescription
    # Depends on:
    Toggles = GetAccessoryToggles()
    AccessoryDescription.set(AccessoryDescriptionGen(Toggles))
    
def VoiceSpeedGUI():
    # Calls function VoiceSpeedGen() to set VoiceSpeed
    # Depends on:
    VoiceSpeed.set(VoiceSpeedGen())
    
def VoiceQualityGUI():
    # Calls function VoiceQualityGen() to set VoiceQuality
    # Depends on:
    VoiceQuality.set(VoiceQualityGen())
    
def ProfessionGUI():
    # Calls function ProfessionGen() to set Profession
    # Depends on:
    Toggles = GetProfessionToggles()
    Profession.set(ProfessionGen(Toggles))
    
def CalmTraitGUI():
    # Calls function CalmTraitGen() to set CalmTrait
    # Depends on:
    Toggles = GetCalmTraitToggles()
    CalmTrait.set(CalmTraitGen(Toggles))
    
def StressedTraitGUI():
    # Calls function StressedTraitGen() to set StressedTrait
    # Depends on:
    Toggles = GetStressedTraitToggles()
    StressedTrait.set(StressedTraitGen(Toggles))
    
def MoodGUI():
    # Calls function MoodGen() to set Mood
    # Depends on:
    Toggles = GetMoodToggles()
    Mood.set(MoodGen(Toggles))
    
def ReactionGUI():
    # Calls function ReactionGen() to set Reaction
    # Depends on:
    Toggles = GetReactionToggles()
    ReactionInitial = ReactionGen(Toggles)
    GenderTemp = Gender.get()
    if (GenderTemp == 'Male'):
        Pronoun = 'He'
        Pronoun2 = 'His'
        Pronoun3 = 'Him'
    elif(GenderTemp == 'Female'):
        Pronoun = 'She'
        Pronoun2 = 'Her'
        Pronoun3 = 'Her'
    if ('The NPC\'s' in ReactionInitial):
        ReactionInitial = ReactionInitial.replace('The NPC\'s',Pronoun2)
    if ('the NPC\'s' in ReactionInitial):
        ReactionInitial = ReactionInitial.replace('the NPC\'s',Pronoun2.lower())
    if ('The NPC' in ReactionInitial):
        ReactionInitial = ReactionInitial.replace('The NPC',Pronoun)
    if ('the NPC' in ReactionInitial):
        ReactionInitial = ReactionInitial.replace('the NPC',Pronoun.lower())
    if ('He/she' in ReactionInitial):
        ReactionInitial = ReactionInitial.replace('He/she',Pronoun)
    if ('he/she' in ReactionInitial):
        ReactionInitial = ReactionInitial.replace('he/she',Pronoun.lower())
    if ('His/her' in ReactionInitial):
        ReactionInitial = ReactionInitial.replace('His/her',Pronoun2)
    if ('his/her' in ReactionInitial):
        ReactionInitial = ReactionInitial.replace('his/her',Pronoun2.lower())
    if ('Him/her' in ReactionInitial):
        ReactionInitial = ReactionInitial.replace('Him/her',Pronoun3)
    if ('him/her' in ReactionInitial):
        ReactionInitial = ReactionInitial.replace('him/her',Pronoun3.lower())
    Reaction.set(ReactionInitial)
    ReactionEntry.delete(1.0,tk.END)
    ReactionEntry.insert(tk.END,Reaction.get())

def MotivationGUI():
    # Calls function MotivationGen() to set Motivation
    # Depends on:
    Toggles = GetMotivationToggles()
    MotivationInitial = MotivationGen(Toggles)
    GenderTemp = Gender.get()
    if (GenderTemp == 'Male'):
        Pronoun = 'He'
        Pronoun2 = 'His'
        Pronoun3 = 'Him'
    elif(GenderTemp == 'Female'):
        Pronoun = 'She'
        Pronoun2 = 'Her'
        Pronoun3 = 'Her'
    if ('The NPC\'s' in MotivationInitial):
        MotivationInitial = MotivationInitial.replace('The NPC\'s',Pronoun2)
    if ('the NPC\'s' in MotivationInitial):
        MotivationInitial = MotivationInitial.replace('the NPC\'s',Pronoun2.lower())
    if ('The NPC' in MotivationInitial):
        MotivationInitial = MotivationInitial.replace('The NPC',Pronoun)
    if ('the NPC' in MotivationInitial):
        MotivationInitial = MotivationInitial.replace('the NPC',Pronoun.lower())
    if ('He/she' in MotivationInitial):
        MotivationInitial = MotivationInitial.replace('He/she',Pronoun)
    if ('he/she' in MotivationInitial):
        MotivationInitial = MotivationInitial.replace('he/she',Pronoun.lower())
    if ('His/her' in MotivationInitial):
        MotivationInitial = MotivationInitial.replace('His/her',Pronoun2)
    if ('his/her' in MotivationInitial):
        MotivationInitial = MotivationInitial.replace('his/her',Pronoun2.lower())
    if ('Him/her' in MotivationInitial):
        MotivationInitial = MotivationInitial.replace('Him/her',Pronoun3)
    if ('him/her' in MotivationInitial):
        MotivationInitial = MotivationInitial.replace('him/her',Pronoun3.lower())
    Motivation.set(MotivationInitial)
    MotivationEntry.delete(1.0,tk.END)
    MotivationEntry.insert(tk.END,Motivation.get())

def RumorGUI():
    # Calls function RumorGen() to set Rumor
    # Depends on:
    Rumor.set(RumorGen())
    
def Save(): 
    #Saves the excel sheet when the window is closed
    SaveToggles()
    wb.close()
    root.destroy()

def ExcelExportGUI():
    ##
    # These dumb variables are defined to be passed into the ExcelWrite2 function
    # I didn't have something like Name.get() work for me, so we're rolling
    # with this stupid workaround. You're welcome future Corey
    #   --- Past Corey
    #  
    #   I hate you
    #   --- Future Corey
    ##
     
    Namexl = Name.get()
    Agexl = Age.get()
    Genderxl = Gender.get()
    Racexl = Race.get()
    FaceDescriptionxl = FaceDescription.get()
    PhysicalDescriptionxl = PhysicalDescription.get()
    AccessoryDescriptionxl = AccessoryDescription.get()
    VoiceSpeedxl = VoiceSpeed.get()
    VoiceQualityxl = VoiceQuality.get()
    Professionxl = Profession.get()
    CalmTraitxl = CalmTrait.get()
    StressedTraitxl = StressedTrait.get()
    Moodxl = Mood.get()
    Reactionxl = ReactionEntry.get('1.0', tk.END)
    Motivationxl = MotivationEntry.get('1.0', tk.END)
    Notesxl = NotesEntry.get('1.0', tk.END)
    n1xl = n1.get()
    
    
    ##
    # The ExcelWrite2 function with all of the current variables
    # it returns the name of the NPC which is then stored at the end of NameList
    #
    # Note that if an NPC with the same name is exported twice there will be a
    # number corresponding to which version of that NPC was exported in their Name
    ##
    CurrentName = ExcelWrite(NameList,n1xl,wb,Namexl,Agexl,Genderxl,Racexl,\
                              FaceDescriptionxl,PhysicalDescriptionxl,\
                              AccessoryDescriptionxl,VoiceSpeedxl,VoiceQualityxl,\
                              Professionxl,CalmTraitxl,StressedTraitxl,Moodxl,\
                              Reactionxl,Motivationxl,Notesxl,Color1.get(),Color2.get())
    NameList.append(CurrentName)
    n1.set(n1.get() + 1)

def FieldsGUI():
    top = tk.Toplevel(root)
    top.title('Fields')
    frame = tk.Frame(top)
    ShowPresetsBox = tk.Checkbutton(frame, text='Display Presets', variable=ShowPresets,
                                    width=23, anchor=tk.W, command=PresetFrameUpdate)
    ShowRandomNPCBox = tk.Checkbutton(frame, text='Display Random NPC Button', variable=ShowRandomNPC,
                                  width=23, anchor=tk.W, command=RandomNPCFrameUpdate)
    ShowNameBox = tk.Checkbutton(frame, text='Display Name', variable=ShowName,
                                 width=23, anchor=tk.W, command=NameFrameUpdate)
    ShowAgeBox = tk.Checkbutton(frame, text='Display Age', variable=ShowAge,
                                width=23, anchor=tk.W, command=AgeFrameUpdate)
    ShowGenderBox = tk.Checkbutton(frame, text='Display Gender', variable=ShowGender,
                                   width=23, anchor=tk.W, command=GenderFrameUpdate)
    ShowRaceBox = tk.Checkbutton(frame, text='Display Race', variable=ShowRace,
                                 width=23, anchor=tk.W, command=RaceFrameUpdate)
    ShowFaceDescriptionBox = tk.Checkbutton(frame, text='Display Face Description', variable=ShowFaceDescription,
                                            width=23, anchor=tk.W, command=FaceDescriptionFrameUpdate)
    ShowPhysicalDescriptionBox = tk.Checkbutton(frame, text='Display Physical Description', variable=ShowPhysicalDescription,
                                                width=23, anchor=tk.W, command=PhysicalDescriptionFrameUpdate)
    ShowAccessoryDescriptionBox = tk.Checkbutton(frame, text='Display Accessory Description', variable=ShowAccessoryDescription,
                                                 width=23, anchor=tk.W, command=AccessoryDescriptionFrameUpdate)
    ShowVoiceSpeedBox = tk.Checkbutton(frame, text='Display Voice Speed', variable=ShowVoiceSpeed,
                                       width=23, anchor=tk.W, command=VoiceSpeedFrameUpdate)
    ShowVoiceQualityBox = tk.Checkbutton(frame, text='Display Voice Quality', variable=ShowVoiceQuality,
                                         width=23, anchor=tk.W, command=VoiceQualityFrameUpdate)
    ShowProfessionBox = tk.Checkbutton(frame, text='Display Profession', variable=ShowProfession,
                                       width=23, anchor=tk.W, command=ProfessionFrameUpdate)
    ShowCalmTraitBox = tk.Checkbutton(frame, text='Display Calm Trait', variable=ShowCalmTrait,
                                      width=23, anchor=tk.W, command=CalmTraitFrameUpdate)
    ShowStressedTraitBox = tk.Checkbutton(frame, text='Display Stressed Trait', variable=ShowStressedTrait,
                                          width=23, anchor=tk.W, command=StressedTraitFrameUpdate)
    ShowMoodBox = tk.Checkbutton(frame, text='Display Mood', variable=ShowMood,
                                 width=23, anchor=tk.W, command=MoodFrameUpdate)
    ShowReactionBox = tk.Checkbutton(frame, text='Display Reaction', variable=ShowReaction,
                                     width=23, anchor=tk.W, command=ReactionFrameUpdate)
    ShowMotivationBox = tk.Checkbutton(frame, text='Display Motivation', variable=ShowMotivation,
                                       width=23, anchor=tk.W, command=MotivationFrameUpdate)
    ShowNotesBox = tk.Checkbutton(frame, text='Display Notes', variable=ShowNotes,
                                  width=23, anchor=tk.W, command=NotesFrameUpdate)
    ShowExportBox = tk.Checkbutton(frame, text='Display Export Button', variable=ShowExport,
                                  width=23, anchor=tk.W, command=ExportFrameUpdate)
    
    ShowPresetsBox.grid(row=1)
    ShowRandomNPCBox.grid(row=2)
    ShowNameBox.grid(row=3)
    ShowAgeBox.grid(row=4)
    ShowGenderBox.grid(row=5)
    ShowRaceBox.grid(row=6)
    ShowFaceDescriptionBox.grid(row=7)
    ShowPhysicalDescriptionBox.grid(row=8)
    ShowAccessoryDescriptionBox.grid(row=9)
    ShowVoiceSpeedBox.grid(row=10)
    ShowVoiceQualityBox.grid(row=11)
    ShowProfessionBox.grid(row=12)
    ShowCalmTraitBox.grid(row=13)
    ShowStressedTraitBox.grid(row=14)
    ShowMoodBox.grid(row=15)
    ShowReactionBox.grid(row=16)
    ShowMotivationBox.grid(row=17)
    ShowNotesBox.grid(row=18)
    ShowExportBox.grid(row=19)
    frame.grid()
    # This sets the tk.Toplevel window relative to the
    # root/main window
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" % (x, y))

def PresetFrameUpdate():
    if ShowPresets.get()==1:
        PresetFrame.grid(row=0, column = 0, sticky = tk.W)
    else:
        PresetFrame.grid_forget()

def RandomNPCFrameUpdate():
    if ShowRandomNPC.get()==1:
        RandomNPCFrame.grid(row=2, column = 0, sticky = tk.W)
    else:
        RandomNPCFrame.grid_forget()

def NameFrameUpdate():
    if ShowName.get()==1:
        NameFrame.grid(row=3, column = 0, sticky = tk.W)
    else:
        NameFrame.grid_forget()

def AgeFrameUpdate():
    if ShowAge.get()==1:
        AgeFrame.grid(row=4, column = 0, sticky = tk.W)
    else:
        AgeFrame.grid_forget()
        
def GenderFrameUpdate():
    if ShowGender.get()==1:
        GenderFrame.grid(row=5, column = 0, sticky = tk.W)
    else:
        GenderFrame.grid_forget()
        
def RaceFrameUpdate():
    if ShowRace.get()==1:
        RaceFrame.grid(row=6, column = 0, sticky = tk.W)
    else:
        RaceFrame.grid_forget()

def FaceDescriptionFrameUpdate():
    if ShowFaceDescription.get()==1:
        FaceDescriptionFrame.grid(row=7, column = 0, sticky = tk.W)
    else:
        FaceDescriptionFrame.grid_forget()

def PhysicalDescriptionFrameUpdate():
    if ShowPhysicalDescription.get()==1:
        PhysicalDescriptionFrame.grid(row=8, column = 0, sticky = tk.W)
    else:
        PhysicalDescriptionFrame.grid_forget()

def AccessoryDescriptionFrameUpdate():
    if ShowAccessoryDescription.get()==1:
        AccessoryDescriptionFrame.grid(row=9, column = 0, sticky = tk.W)
    else:
        AccessoryDescriptionFrame.grid_forget()
        
def VoiceSpeedFrameUpdate():
    if ShowVoiceSpeed.get()==1:
        VoiceSpeedFrame.grid(row=10, column = 0, sticky = tk.W)
    else:
        VoiceSpeedFrame.grid_forget()
        
def VoiceQualityFrameUpdate():
    if ShowVoiceQuality.get()==1:
        VoiceQualityFrame.grid(row=11, column = 0, sticky = tk.W)
    else:
        VoiceQualityFrame.grid_forget()
        
def ProfessionFrameUpdate():
    if ShowProfession.get()==1:
        ProfessionFrame.grid(row=12, column = 0, sticky = tk.W)
    else:
        ProfessionFrame.grid_forget()
        
def CalmTraitFrameUpdate():
    if ShowCalmTrait.get()==1:
        CalmTraitFrame.grid(row=13, column = 0, sticky = tk.W)
    else:
        CalmTraitFrame.grid_forget()
        
def StressedTraitFrameUpdate():
    if ShowStressedTrait.get()==1:
        StressedTraitFrame.grid(row=14, column = 0, sticky = tk.W)
    else:
        StressedTraitFrame.grid_forget()
        
def MoodFrameUpdate():
    if ShowMood.get()==1:
        MoodFrame.grid(row=15, column = 0, sticky = tk.W)
    else:
        MoodFrame.grid_forget()
        
def ReactionFrameUpdate():
    if ShowReaction.get()==1:
        ReactionFrame.grid(row=16, column = 0, sticky = tk.W)
    else:
        ReactionFrame.grid_forget()
        
def MotivationFrameUpdate():
    if ShowMotivation.get()==1:
        MotivationFrame.grid(row=17, column = 0, sticky = tk.W)
    else:
        MotivationFrame.grid_forget()
        
def NotesFrameUpdate():
    if ShowNotes.get()==1:
        NotesFrame.grid(row=18, column = 0, sticky = tk.W)
    else:
        NotesFrame.grid_forget()

def ExportFrameUpdate():
    if ShowExport.get()==1:
        ExportFrame.grid(row=19, column = 0, sticky = tk.W)
    else:
        ExportFrame.grid_forget()

def UpdateAllFrames():
    PresetFrameUpdate()
    RandomNPCFrameUpdate()
    NameFrameUpdate()
    AgeFrameUpdate()
    GenderFrameUpdate()
    RaceFrameUpdate()
    FaceDescriptionFrameUpdate()
    PhysicalDescriptionFrameUpdate()
    AccessoryDescriptionFrameUpdate()
    VoiceSpeedFrameUpdate()
    VoiceQualityFrameUpdate()
    ProfessionFrameUpdate()
    CalmTraitFrameUpdate()
    StressedTraitFrameUpdate()
    MoodFrameUpdate()
    ReactionFrameUpdate()
    MotivationFrameUpdate()
    NotesFrameUpdate()
    ExportFrameUpdate()

##########################################
#          Create the menu               #
##########################################

# Create the basic menu
menubar = tk.Menu(root)

# A menu that lets you choose which
displaymenu = tk.Menu(menubar, tearoff=0)
displaymenu.add_command(label='Choose Colors', command=ColorGUI)
displaymenu.add_command(label='Name', command=NameGUI)
displaymenu.add_command(label='Fields', command=FieldsGUI)
menubar.add_cascade(label='Display', menu=displaymenu)

#Display the menu
root.config(menu=menubar)


##########################################
#          Create the tk.Frames          #
##########################################

PresetFrame = tk.Frame(width=60, height=10, bg=Color1.get())
RandomNPCFrame = tk.Frame(width=60, height=10, bg=Color1.get())
NameFrame = tk.Frame(width=60, height=10, bg=Color1.get())
AgeFrame = tk.Frame(width=60, height=10, bg=Color1.get())
GenderFrame = tk.Frame(width=60, height=10, bg=Color1.get())
RaceFrame = tk.Frame(width=60, height=10, bg=Color1.get())
FaceDescriptionFrame = tk.Frame(width=60, height=10, bg=Color2.get())
PhysicalDescriptionFrame = tk.Frame(width=60, height=10, bg=Color2.get())
AccessoryDescriptionFrame = tk.Frame(width=60, height=10, bg=Color2.get())
VoiceSpeedFrame = tk.Frame(width=60, height=10, bg=Color1.get())
VoiceQualityFrame = tk.Frame(width=60, height=10, bg=Color1.get())
ProfessionFrame = tk.Frame(width=60, height=10, bg=Color2.get())
CalmTraitFrame = tk.Frame(width=60, height=10, bg=Color1.get())
StressedTraitFrame = tk.Frame(width=60, height=10, bg=Color1.get())
MoodFrame = tk.Frame(width=60, height=10, bg=Color2.get())
ReactionFrame = tk.Frame(width=60, height=10, bg=Color2.get())
MotivationFrame = tk.Frame(width=60, height=10, bg=Color1.get())
NotesFrame = tk.Frame(width=60, height=10, bg=Color2.get())
ExportFrame = tk.Frame(width=60, height=10, bg=Color2.get())

##########################################
#          Create the tk.Buttons         #
##########################################

#
#You should know what tk.Buttons are Corey, I'm not gonna do this all for you
#
Preset1Button = tk.Button(PresetFrame, textvariable = Preset1Var, wraplength = 75, command = SetPreset1,
                   width = 11, height = 3, bg=PresetColor1.get())
Preset2Button = tk.Button(PresetFrame, textvariable = Preset2Var, wraplength = 75, command = SetPreset2,
                   width = 11, height = 3, bg=PresetColor2.get())
Preset3Button = tk.Button(PresetFrame, textvariable = Preset3Var, wraplength = 75, command = SetPreset3,
                   width = 11, height = 3, bg=PresetColor3.get())
Preset4Button = tk.Button(PresetFrame, textvariable = Preset4Var, wraplength = 75, command = SetPreset4,
                   width = 11, height = 3, bg=PresetColor4.get())
Preset5Button = tk.Button(PresetFrame, textvariable = Preset5Var, wraplength = 75, command = SetPreset5,
                   width = 11, height = 3, bg=PresetColor5.get())
Preset6Button = tk.Button(PresetFrame, textvariable = Preset6Var, wraplength = 75, command = SetPreset6,
                   width = 11, height = 3, bg=PresetColor6.get())
Preset7Button = tk.Button(PresetFrame, textvariable = Preset7Var, wraplength = 75, command = SetPreset7,
                   width = 11, height = 3, bg=PresetColor7.get())
Preset8Button = tk.Button(PresetFrame, textvariable = Preset8Var, wraplength = 75, command = SetPreset8,
                   width = 11, height = 3, bg=PresetColor8.get())
Preset9Button = tk.Button(PresetFrame, textvariable = Preset9Var, wraplength = 75, command = SetPreset9,
                   width = 11, height = 3, bg=PresetColor9.get())
Preset10Button = tk.Button(PresetFrame, textvariable = Preset10Var, wraplength = 75, command = SetPreset10,
                   width = 11, height = 3, bg=PresetColor10.get())

ColorButton = tk.Button(RandomNPCFrame,text="Color Menu",bg = Color0.get(),command=ColorGUI,height=3,width=10)
AllButton = tk.Button(RandomNPCFrame,text="Generate a random NPC",bg = Color0.get(),command=AllGUI,height=3,width=61)
NameButton = tk.Button(NameFrame,text="Name", bg = Color1.get(),command=NameGUI,height=1,width=10)
AgeButton = tk.Button(AgeFrame,text="Age", bg = Color1.get(),command=AgeGUI,height=1,width=10)
GenderButton = tk.Button(GenderFrame,text="Gender", bg = Color1.get(),command=GenderGUI,height=1,width=10)
RaceButton = tk.Button(RaceFrame,text="Race", bg = Color1.get(),command=RaceGUI,height=1,width=10)
FaceDescriptionButton = tk.Button(FaceDescriptionFrame,text="Face", bg = Color2.get(),command=FaceDescriptionGUI,height=1,width=10)
PhysicalDescriptionButton = tk.Button(PhysicalDescriptionFrame,text="Body", bg = Color2.get(),command=PhysicalDescriptionGUI,height=1,width=10)
AccessoryDescriptionButton = tk.Button(AccessoryDescriptionFrame,text="Accessory", bg = Color2.get(),command=AccessoryDescriptionGUI,height=1,width=10)
VoiceSpeedButton = tk.Button(VoiceSpeedFrame,text="Voice Speed", bg = Color1.get(),command=VoiceSpeedGUI,height=1,width=10)
VoiceQualityButton = tk.Button(VoiceQualityFrame,text="Voice Quality", bg = Color1.get(),command=VoiceQualityGUI,height=1,width=10)
ProfessionButton = tk.Button(ProfessionFrame,text="Profession", bg = Color2.get(),command=ProfessionGUI,height=1,width=10)
CalmTraitButton = tk.Button(CalmTraitFrame,text="Calm Trait", bg = Color1.get(),command=CalmTraitGUI,height=1,width=10)
StressedTraitButton = tk.Button(StressedTraitFrame,text="Stressed Trait", bg = Color1.get(),command=StressedTraitGUI,height=1,width=10)
MoodButton = tk.Button(MoodFrame,text="Mood", bg = Color2.get(),command=MoodGUI,height=1,width=10)
ReactionButton = tk.Button(ReactionFrame,text="Reaction", bg = Color2.get(),command=ReactionGUI,height=5,width=10)
MotivationButton = tk.Button(MotivationFrame,text="Motivation", bg = Color1.get(),command=MotivationGUI,height=4,width=10)
NotesButton = tk.Button(NotesFrame, text='Session Notes', bg=Color2.get(), height=4, width=10)
#RumorButton = tk.Button(root,text="Rumor", bg = '#e2efd9',command=RumorGUI,height=8,width=11)

ExcelExportButton = tk.Button(ExportFrame,bg = Color0.get(),text="Export to excel. Only exports when this window is closed.",command=ExcelExportGUI,height=3,width=61)

NameButton.bind("<Button-3>", NameRC)
AgeButton.bind("<Button-3>", AgeRC)
GenderButton.bind("<Button-2>", ToggleGenderGUI)
GenderButton.bind("<Button-3>", GenderRC)
RaceButton.bind("<Button-3>", RaceRC)
FaceDescriptionButton.bind("<Button-3>", FaceDescriptionRC)
PhysicalDescriptionButton.bind("<Button-3>", PhysicalDescriptionRC)
AccessoryDescriptionButton.bind("<Button-3>", AccessoryDescriptionRC)
CalmTraitButton.bind("<Button-3>", CalmTraitRC)
StressedTraitButton.bind("<Button-3>", StressedTraitRC)
ProfessionButton.bind("<Button-3>", ProfessionRC)
MoodButton.bind("<Button-3>", MoodRC)
ReactionButton.bind("<Button-3>", ReactionRC)
MotivationButton.bind("<Button-3>", MotivationRC)

##########################################
#          Create the tk.Labels          #
##########################################

#
#These are the text things, called labels in tkinter because reasons
#

#NameLabel = tk.Label(root,anchor=tk.W, textvariable = Name,width=53, bg = Color1.get())
#AgeLabel = tk.Label(AgeFrame,anchor=tk.W, textvariable = str(Age),width=53, bg = Color1.get())
#GenderLabel = tk.Label(GenderFrame,anchor=tk.W, textvariable = Gender,width=53, bg = Color1.get())
#RaceLabel = tk.Label(RaceFrame,anchor=tk.W, textvariable = Race,width=53, bg = Color1.get())
#FaceDescriptionLabel = tk.Label(FaceDescriptionFrame,anchor=tk.W, textvariable = FaceDescription, width=53, bg = Color2.get())
#PhysicalDescriptionLabel = tk.Label(PhysicalDescriptionFrame,anchor=tk.W, textvariable = PhysicalDescription, width=53, bg = Color2.get())
#AccessoryDescriptionLabel = tk.Label(AccessoryDescriptionFrame,anchor=tk.W, textvariable = AccessoryDescription, width=53, bg = Color2.get())
#VoiceSpeedLabel = tk.Label(VoiceSpeedFrame,anchor=tk.W, textvariable = VoiceSpeed,width=53, bg = Color1.get())
#VoiceQualityLabel = tk.Label(VoiceQualityFrame,anchor=tk.W, textvariable = VoiceQuality,width=53, bg = Color1.get())
#ProfessionLabel = tk.Label(ProfessionFrame,anchor=tk.W, textvariable = Profession,width=53, bg = Color2.get())
#CalmTraitLabel = tk.Label(CalmTraitFrame,anchor=tk.W, textvariable = CalmTrait,width=53, bg = Color1.get())
#StressedTraitLabel = tk.Label(StressedTraitFrame,anchor=tk.W, textvariable = StressedTrait,width=53, bg = Color1.get())
#MoodLabel = tk.Label(MoodFrame,anchor=tk.W, textvariable = Mood,width=53, bg = Color2.get())
#ReactionLabel = tk.Label(ReactionFrame,anchor=tk.W, textvariable = Reaction,width=53,height=5,wraplength = 355,justify=tk.LEFT, bg = Color2.get())
#MotivationLabel = tk.Label(MotivationFrame,anchor=tk.W, textvariable = Motivation,width=53,height=4,wraplength = 355,justify=tk.LEFT, bg = Color1.get())
#RumorLabel = tk.Label(root,anchor=W, textvariable = Rumor,width=53,height=8,wraplength = 355,justify=LEFT, bg = '#c5e0b3')

##########################################
#          Create the entry things       #
##########################################
NameEntry = tk.Entry(NameFrame, textvariable = Name, width=59, bg = Color1.get(), bd=0)
AgeEntry = tk.Entry(AgeFrame, textvariable = str(Age), width=59, bg = Color1.get(), bd=0)
GenderEntry = tk.Entry(GenderFrame, textvariable = Gender, width=59, bg = Color1.get(), bd=0)
RaceEntry = tk.Entry(RaceFrame, textvariable = Race, width=59, bg = Color1.get(), bd=0)
FaceDescriptionEntry = tk.Entry(FaceDescriptionFrame, textvariable = FaceDescription, width=59, bg = Color2.get(), bd=0)
PhysicalDescriptionEntry = tk.Entry(PhysicalDescriptionFrame, textvariable = PhysicalDescription, width=59, bg = Color2.get(), bd=0)
AccessoryDescriptionEntry = tk.Entry(AccessoryDescriptionFrame, textvariable = AccessoryDescription, width=59, bg = Color2.get(), bd=0)
VoiceSpeedEntry = tk.Entry(VoiceSpeedFrame, textvariable = VoiceSpeed, width=59, bg = Color1.get(), bd=0)
VoiceQualityEntry = tk.Entry(VoiceQualityFrame, textvariable = VoiceQuality, width=59, bg = Color1.get(), bd=0)
ProfessionEntry = tk.Entry(ProfessionFrame, textvariable = Profession, width=59, bg = Color2.get(), bd=0)
CalmTraitEntry = tk.Entry(CalmTraitFrame, textvariable = CalmTrait, width=59, bg = Color1.get(), bd=0)
StressedTraitEntry = tk.Entry(StressedTraitFrame, textvariable = StressedTrait, width=59, bg = Color1.get(), bd=0)
MoodEntry = tk.Entry(MoodFrame, textvariable = Mood, width=59, bg = Color2.get(), bd=0)

# These two are Text regions because they need to be multiple lines
ReactionEntry = tk.Text(ReactionFrame, width=59, wrap=tk.WORD, height=4, bg = Color2.get(), bd=0)
MotivationEntry = tk.Text(MotivationFrame, width=59, wrap=tk.WORD, height=4, bg = Color1.get(), bd=0)
NotesEntry = tk.Text(NotesFrame, width=59, wrap=tk.WORD, height=4, bg = Color2.get(), bd=0)

 
ReactionEntry.configure(font=('Segoe UI', 9))
MotivationEntry.configure(font=('Segoe UI', 9))
NotesEntry.configure(font=('Segoe UI', 9))
#MotivationEntry.insert(tk.INSERT,'Test')

##########################################
#          Place everything              #
##########################################

# Because I want it to look like a grid we have this thing
# looks pretty fucking stupid right now but w/e

# Check to see which frames should be displayed
Preset1Button.grid(row = 0, column = 0, sticky = tk.W)
Preset2Button.grid(row = 0, column = 1, sticky = tk.W)
Preset3Button.grid(row = 0, column = 2, sticky = tk.W)
Preset4Button.grid(row = 0, column = 3, sticky = tk.W)
Preset5Button.grid(row = 0, column = 4, sticky = tk.W)
Preset6Button.grid(row = 1, column = 0, sticky = tk.W)
Preset7Button.grid(row = 1, column = 1, sticky = tk.W)
Preset8Button.grid(row = 1, column = 2, sticky = tk.W)
Preset9Button.grid(row = 1, column = 3, sticky = tk.W)
Preset10Button.grid(row = 1, column = 4, sticky = tk.W)

Preset1Button.bind("<Button-3>", Preset1RC)
Preset2Button.bind("<Button-3>", Preset2RC)
Preset3Button.bind("<Button-3>", Preset3RC)
Preset4Button.bind("<Button-3>", Preset4RC)
Preset5Button.bind("<Button-3>", Preset5RC)
Preset6Button.bind("<Button-3>", Preset6RC)
Preset7Button.bind("<Button-3>", Preset7RC)
Preset8Button.bind("<Button-3>", Preset8RC)
Preset9Button.bind("<Button-3>", Preset9RC)
Preset10Button.bind("<Button-3>", Preset10RC)

UpdateAllFrames()

#PresetFrame.grid(row=0, column=0, sticky = tk.W)
#TopButtonFrame.grid(row=1, column=0, sticky = tk.W)
#NameFrame.grid(row=3, column = 0, sticky = tk.W)
#AgeFrame.grid(row=4, column = 0, sticky = tk.W)
#GenderFrame.grid(row=5, column = 0, columnspan=4,sticky = tk.W)
#RaceFrame.grid(row=6, column = 0, columnspan=4,sticky = tk.W)
#FaceDescriptionFrame.grid(row=7, column = 0, columnspan=4,sticky = tk.W)
#PhysicalDescriptionFrame.grid(row=8, column = 0, columnspan=4,sticky = tk.W)
#AccessoryDescriptionFrame.grid(row=9, column = 0, columnspan=4,sticky = tk.W)
#VoiceSpeedFrame.grid(row=10, column = 0, columnspan=4,sticky = tk.W)
#VoiceQualityFrame.grid(row=11, column = 0, columnspan=4,sticky = tk.W)
#ProfessionFrame.grid(row=12, column = 0, columnspan=4,sticky = tk.W)
#CalmTraitFrame.grid(row=13, column = 0, columnspan=4,sticky = tk.W)
#StressedTraitFrame.grid(row=14, column = 0, columnspan=4,sticky = tk.W)
#MoodFrame.grid(row=15, column = 0, columnspan=4,sticky = tk.W)
#ReactionFrame.grid(row=16, column = 0, columnspan=4,sticky = tk.W)
#MotivationFrame.grid(row=17, column = 0, columnspan=4,sticky = tk.W)
#NotesFrame.grid(row=18, column=0, columnspan=4, sticky=tk.W)


#RandomNPCFrame.grid(row=1, column=0, sticky = tk.W)
AllButton.grid(row=2, column=0, sticky = tk.W)
#ColorButton.grid(row=2, column=0, sticky = tk.W)

NameButton.grid(row=3, column=0, sticky = tk.E)
NameEntry.grid(row=3, column=1, columnspan=1, sticky = tk.W)
AgeButton.grid(row=4, column=0, sticky = tk.E)
AgeEntry.grid(row=4, column=1, sticky = tk.W)
GenderButton.grid(row=5, column=0, sticky = tk.E)
GenderEntry.grid(row=5, column=1, sticky = tk.W)
RaceButton.grid(row=6, column=0, sticky = tk.E)
RaceEntry.grid(row=6, column=1, sticky = tk.W)
FaceDescriptionButton.grid(row=7, column=0, sticky = tk.E)
FaceDescriptionEntry.grid(row=7, column=1, sticky = tk.W)
PhysicalDescriptionButton.grid(row=8, column=0, sticky = tk.E)
PhysicalDescriptionEntry.grid(row=8, column=1, sticky = tk.W)
AccessoryDescriptionButton.grid(row=9, column=0, sticky = tk.E)
AccessoryDescriptionEntry.grid(row=9, column=1, sticky = tk.W)
VoiceSpeedButton.grid(row=10, column=0, sticky = tk.E)
VoiceSpeedEntry.grid(row=10, column=1, sticky = tk.W)
VoiceQualityButton.grid(row=11, column=0, sticky = tk.E)
VoiceQualityEntry.grid(row=11, column=1, sticky = tk.W)
ProfessionButton.grid(row=12, column=0, sticky = tk.E)
ProfessionEntry.grid(row=12, column=1, sticky = tk.W)
CalmTraitButton.grid(row=13, column=0, sticky = tk.E)
CalmTraitEntry.grid(row=13, column=1, sticky = tk.W)
StressedTraitButton.grid(row=14, column=0, sticky = tk.E)
StressedTraitEntry.grid(row=14, column=1 ,sticky = tk.W)
MoodButton.grid(row=15, column=0, sticky = tk.E)
MoodEntry.grid(row=15, column=1, sticky = tk.W)
ReactionButton.grid(row=16, column=0, sticky = tk.E)
ReactionEntry.grid(row=16, column=1, sticky = tk.W)
MotivationButton.grid(row=17, column=0, sticky = tk.E)
MotivationEntry.grid(row=17, column=1, sticky = tk.W)
NotesButton.grid(row=18, column=0, sticky=tk.E)
NotesEntry.grid(row=18, column=1, sticky=tk.W)
#RumorButton.grid(row=16, column=0,sticky = E)
#RumorLabel.grid(row=16, column=1,sticky = W)

ExcelExportButton.grid(row=19, columnspan=5, sticky=tk.W)

#root.minsize(width=444, height=607)
#root.maxsize(width=444, height=607)
root.grid_columnconfigure(1,weight=1)
root.grid()
root.wm_title('OmnipotentSpoon\'s NPCs Generator')
AllGUI()

root.protocol("WM_DELETE_WINDOW",Save)
root.mainloop()