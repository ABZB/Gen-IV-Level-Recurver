import io
import string
import math
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import binascii
import os
import time

trainer_scale_array_hgss = [13,4,4,5,19,14,16,4,27,12,100,11,11,46,74,27,48,8,100,8,13,19,9,17,9,8,8,69,7,20,22,46,32,30,52,69,26,67,24,100,70,21,6,24,24,21,4,72,8,7,6,6,6,6,6,8,8,77,65,8,10,14,100,14,14,14,12,12,12,19,19,16,26,16,16,16,16,16,70,16,20,23,68,68,27,27,100,100,21,28,28,28,28,28,28,28,28,28,28,10,11,69,60,60,100,100,100,48,44,51,51,51,69,60,60,44,51,21,51,21,48,40,34,47,47,44,44,28,34,40,40,40,70,34,67,68,47,100,75,72,100,14,48,48,48,48,49,70,69,69,49,76,76,49,10,29,29,51,29,53,53,53,53,53,100,100,100,100,100,100,100,40,40,100,21,21,21,18,67,100,18,18,68,18,45,45,45,45,45,45,45,45,45,100,45,45,45,45,45,45,33,33,33,33,33,33,100,100,33,33,26,26,26,26,26,46,26,46,46,46,100,46,46,46,100,100,46,46,100,62,51,60,18,69,75,75,75,75,75,75,75,75,75,58,58,58,58,72,4,48,29,79,73,70,60,64,68,62,80,82,81,100,23,71,4,13,23,71,13,23,47,71,100,14,14,8,8,48,4,4,22,22,46,75,76,76,76,47,47,6,79,100,78,78,100,77,70,70,76,66,67,67,75,100,100,100,100,73,63,63,63,67,66,66,66,65,65,74,9,65,65,65,34,34,47,64,76,67,70,70,67,69,69,14,49,64,60,100,75,100,100,100,100,100,100,64,100,65,65,66,66,75,46,64,64,64,69,65,65,16,70,76,33,63,63,70,60,62,62,79,79,100,78,77,100,100,70,74,74,65,65,67,8,9,19,20,12,16,24,9,18,18,18,100,17,60,23,23,75,23,26,40,40,46,47,47,47,47,14,23,69,60,69,75,62,64,28,58,70,65,65,75,75,75,75,75,75,75,75,18,18,17,17,23,23,18,18,24,24,26,26,100,100,60,60,75,47,47,16,47,48,48,49,16,16,69,69,69,69,5,5,8,8,23,23,40,40,45,45,45,46,46,100,100,100,100,100,46,47,45,45,45,45,45,47,12,47,46,101,101,101,65,21,21,3,3,3,29,45,52,52,52,18,100,17,100,23,100,26,4,100,5,16,100,8,100,34,8,100,14,100,40,10,100,14,100,16,23,100,40,100,100,4,27,27,34,16,51,16,75,75,20,20,20,76,76,74,74,74,74,74,74,63,63,65,65,65,65,65,65,65,65,65,66,66,66,66,66,67,67,67,66,66,66,66,66,66,66,66,78,78,78,78,78,78,75,78,78,77,77,77,77,77,77,77,77,77,61,61,61,11,75,49,69,48,48,60,47,69,24,18,47,18,18,18,14,14,14,16,16,16,72,72,72,72,72,72,66,66,66,66,66,66,66,66,66,67,67,67,67,67,67,67,67,67,66,66,66,66,66,66,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,75,75,75,75,75,26,26,26,45,70,70,70,20,20,81,81,81,81,73,79,79,79,80,80,80,80,80,80,75,68,75,75,75,100,100,58,100,100,100,46,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,31,32,32,32,32,100,100,100,100,100]


trainer_min_level_array_hgss = [21,5,5,7,27,21,22,6,40,21,0,17,17,52,96,40,56,17,0,16,21,27,17,24,17,17,17,63,16,27,38,50,42,41,58,63,40,92,39,0,64,38,8,39,39,38,6,95,17,16,8,8,8,8,8,17,17,98,91,17,17,21,0,21,21,21,21,21,21,27,27,22,40,22,22,22,22,22,64,22,31,39,93,93,40,40,0,0,38,41,41,41,41,41,41,41,41,41,41,17,17,63,62,62,0,0,0,56,47,58,58,58,63,62,62,47,58,38,58,38,56,45,43,56,56,47,47,41,43,45,45,45,64,43,92,93,56,0,81,95,0,21,56,56,56,56,56,64,63,63,56,98,98,56,17,41,41,58,41,60,60,60,60,60,0,0,0,0,0,0,0,45,45,0,38,38,38,25,92,0,25,25,93,25,50,50,50,50,50,50,50,50,50,0,50,50,50,50,50,50,49,49,49,49,49,49,0,0,49,49,40,40,40,40,40,52,40,52,52,52,0,52,52,52,0,0,52,52,0,89,58,62,25,63,81,81,81,81,81,81,81,81,81,65,65,65,65,95,6,56,41,99,96,64,62,90,93,89,0,0,0,0,34,64,5,21,34,64,21,34,52,64,0,21,21,17,17,56,6,6,34,34,52,81,81,81,81,52,52,8,99,0,99,99,0,98,64,64,98,91,92,92,81,0,0,0,0,96,89,89,89,92,91,91,91,91,91,96,17,91,91,91,43,43,56,90,98,92,64,64,92,63,63,21,56,90,62,0,81,0,0,0,0,0,0,90,0,91,91,91,91,81,52,90,90,90,63,91,91,22,64,98,49,89,89,64,62,89,89,99,99,0,99,98,0,0,64,96,96,91,91,92,17,17,27,31,21,22,39,17,25,25,52,0,24,62,39,39,81,39,40,45,45,52,56,56,56,56,21,39,63,62,63,81,89,90,41,65,64,91,91,81,81,81,81,81,81,81,81,25,25,24,24,39,39,25,25,39,39,40,40,0,0,62,62,81,56,56,22,56,56,56,56,22,22,63,63,63,63,7,7,17,17,39,39,45,45,50,50,50,52,52,0,0,0,0,0,50,52,50,50,50,50,50,52,17,52,50,100,100,100,91,38,38,5,5,5,41,50,59,59,59,25,0,24,0,39,0,40,6,0,7,22,0,17,0,43,17,0,21,0,45,17,0,21,0,22,39,0,45,0,0,6,40,40,43,22,58,22,81,81,31,31,31,98,98,96,96,96,96,96,96,89,89,91,91,91,91,91,91,91,91,91,91,91,91,91,91,92,92,92,91,91,91,91,91,91,91,91,99,99,99,99,99,99,81,99,99,98,98,98,98,98,98,98,98,98,88,88,88,17,81,56,63,56,56,62,56,63,39,25,56,25,25,25,21,21,21,22,22,22,95,95,95,95,95,95,91,91,91,91,91,91,91,91,91,92,92,92,92,92,92,92,92,92,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,81,81,81,81,81,40,40,40,50,64,64,64,31,31,0,0,0,0,96,99,99,99,0,0,0,0,0,0,81,93,81,81,81,0,100,65,100,100,100,50,0,0,0,0,0,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,42,42,42,42,42,100,100,100,100,100]


evolve_array_hgss = [0,2,3,3,5,6,6,8,9,9,11,12,12,14,15,15,17,18,18,20,20,22,22,24,24,25,26,28,28,30,31,31,33,34,34,36,36,38,38,40,40,42,169,45,182,45,47,47,49,49,51,51,53,53,55,55,57,57,59,59,62,186,62,64,65,65,67,68,68,70,71,71,73,73,75,76,76,78,78,80,80,82,462,83,85,85,87,87,89,89,91,91,93,94,94,208,97,97,99,99,101,101,103,103,105,105,106,107,463,110,110,112,464,242,465,115,117,230,119,119,121,121,122,123,124,466,467,127,128,130,130,131,132,133,134,135,136,233,139,139,141,141,142,143,144,145,146,148,149,149,150,151,153,154,154,156,157,157,159,160,160,162,162,164,164,166,166,168,168,169,171,171,25,35,39,176,468,178,178,180,181,181,182,184,184,185,186,188,189,189,424,192,192,469,195,195,196,197,430,199,429,201,202,203,205,205,206,472,208,210,210,211,212,213,214,461,217,217,219,219,221,473,222,224,224,225,226,227,229,229,230,232,232,474,234,235,237,237,124,125,126,241,242,243,244,245,247,248,248,249,250,251,253,254,254,256,257,257,259,260,260,262,262,264,264,266,267,267,269,269,271,272,272,274,275,275,277,277,279,279,281,282,282,284,284,286,286,288,289,289,291,291,292,294,295,295,297,297,183,476,301,301,302,303,305,306,306,308,308,310,310,311,312,313,314,407,317,317,319,319,321,321,323,323,324,326,326,327,329,330,330,332,332,334,334,335,336,337,338,340,340,342,342,344,344,346,346,348,348,350,350,351,352,354,354,356,477,357,358,359,202,362,362,364,365,365,367,367,368,369,370,372,373,373,375,376,376,377,378,379,380,381,382,383,384,385,386,388,389,389,391,392,392,394,395,395,397,398,398,400,400,402,402,404,405,405,315,407,409,409,411,411,413,413,414,416,416,417,419,419,421,421,423,423,424,426,426,428,428,429,430,432,432,358,435,435,437,437,185,122,113,441,442,444,445,445,143,448,448,450,450,452,452,454,454,455,457,457,226,460,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507]

evolve_level_barrier_array_hgss = [0,16,32,0,16,36,0,16,36,0,7,10,0,7,10,0,18,36,0,20,0,20,0,22,0,0,0,22,0,16,21,0,16,21,0,5,0,5,0,5,0,22,27,21,26,0,24,0,31,0,26,0,28,0,33,0,28,0,5,0,25,30,0,16,21,0,28,33,0,21,26,0,30,0,25,30,0,40,0,37,0,30,35,0,31,0,34,0,38,0,5,0,25,30,0,5,26,0,28,0,30,0,5,0,28,0,0,0,5,35,0,42,47,52,57,0,32,37,33,0,5,0,0,0,0,5,10,0,0,20,0,0,0,0,0,0,0,30,40,0,40,0,0,0,0,0,0,30,55,0,0,0,16,32,0,14,36,0,18,30,0,15,0,20,0,18,0,22,0,0,27,0,10,10,10,10,30,25,0,15,30,0,0,18,0,0,0,18,27,0,40,5,0,5,40,0,0,0,40,0,40,0,0,0,31,0,0,40,0,23,0,0,0,0,0,30,30,0,38,0,33,38,0,25,0,0,0,0,24,0,0,25,0,40,0,0,20,0,30,30,30,0,0,0,0,0,30,55,0,0,0,0,16,36,0,16,36,0,16,36,0,18,0,20,0,7,10,0,10,0,14,19,0,14,19,0,22,0,25,0,20,30,0,22,0,23,0,18,36,0,20,0,0,20,40,0,24,0,15,30,20,0,0,0,32,42,0,37,0,26,0,0,0,0,0,36,26,0,30,0,40,0,33,0,0,32,0,0,35,45,0,32,0,35,0,0,0,0,0,30,0,30,0,36,0,40,0,40,0,5,0,0,0,37,0,37,42,0,0,0,15,42,0,32,44,0,5,0,0,0,0,30,50,0,20,45,0,0,0,0,0,0,0,0,0,0,0,18,32,0,14,36,0,16,36,0,14,34,0,15,0,10,0,15,30,0,10,0,30,0,30,0,20,0,0,21,0,0,26,0,25,0,30,0,0,28,0,5,0,0,0,38,0,10,34,0,33,0,10,10,10,0,0,24,48,0,30,35,0,34,0,40,0,37,0,0,31,0,30,40,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

type_array = [['bug',10,11,12,13,14,15,46,47,48,49,123,127,165,166,167,168,193,204,205,212,213,214,265,266,267,268,269,283,284,290,291,292,313,314,347,348,401,402,412,413,414,415,416,451,469,499,500],['dark',197,198,215,228,229,248,261,262,274,275,302,318,319,332,342,359,430,434,435,442,452,461,491],['dragon',147,148,149,230,329,330,334,371,372,373,380,381,384,443,444,445,483,484,487,501],['electric',25,26,81,82,100,101,125,135,145,170,171,172,179,180,181,239,243,309,310,311,312,403,404,405,417,462,466,479,503,504,505,506,507],['fighting',56,57,62,66,67,68,106,107,214,236,237,256,257,286,296,297,307,308,391,392,447,448,453,454,475],['fire',4,5,6,37,38,58,59,77,78,126,136,146,155,156,157,218,219,228,229,240,244,250,255,256,257,322,323,324,390,391,392,467,485],['flying',6,12,16,17,18,21,22,41,42,83,84,85,123,130,142,144,145,146,149,163,164,165,166,169,176,177,178,187,188,189,193,198,207,225,226,227,249,250,267,276,277,278,279,284,291,333,334,357,373,384,396,397,398,414,415,416,425,426,430,441,458,468,469,472,502],['ghost',92,93,94,200,292,302,353,354,355,356,425,426,429,442,477,478,479,487,501,503,504,505,506,507],['grass',1,2,3,43,44,45,46,47,69,70,71,102,103,114,152,153,154,182,187,188,189,191,192,251,252,253,254,270,271,272,273,274,275,285,286,315,331,332,345,346,357,387,388,389,406,407,413,420,421,455,459,460,465,470,492,499,500,502],['ground',27,28,31,34,50,51,74,75,76,95,104,105,111,112,194,195,207,208,220,221,231,232,246,247,259,260,290,322,323,328,329,330,339,340,343,344,383,389,423,443,444,445,449,450,464,472,473],['ice',87,91,124,131,144,215,220,221,225,238,361,362,363,364,365,378,459,460,461,471,473,478],['normal',16,17,18,19,20,21,22,39,40,52,53,83,84,85,108,113,115,128,132,133,137,143,161,162,163,164,174,190,203,206,216,217,233,234,235,241,242,263,264,276,277,287,288,289,293,294,295,298,300,301,327,333,335,351,352,396,397,398,399,400,424,427,428,431,432,440,441,446,463,474,486,493],['poison',1,2,3,13,14,15,23,24,29,30,31,32,33,34,41,42,43,44,45,48,49,69,70,71,72,73,88,89,92,93,94,109,110,167,168,169,211,269,315,316,317,336,406,407,434,435,451,452,453,454],['psychic',63,64,65,79,80,96,97,102,103,121,122,124,150,151,177,178,196,199,201,202,203,238,249,251,280,281,282,307,308,325,326,337,338,343,344,358,360,374,375,376,380,381,385,386,433,436,437,439,475,480,481,482,488,496,497,498],['rock',74,75,76,95,111,112,138,139,140,141,142,185,213,219,222,246,247,248,299,304,305,306,337,338,345,346,347,348,369,377,408,409,410,411,438,464,476],['steel',81,82,205,208,212,227,303,304,305,306,374,375,376,379,385,395,410,411,436,437,448,462,476,483,485],['water',7,8,9,54,55,60,61,62,72,73,79,80,86,87,90,91,98,99,116,117,118,119,120,121,129,130,131,134,138,139,140,141,158,159,160,170,171,183,184,186,194,195,199,211,222,223,224,226,230,245,258,259,260,270,271,272,278,279,283,318,319,320,321,339,340,341,342,349,350,363,364,365,366,367,368,369,370,382,393,394,395,400,418,419,422,423,456,457,458,484,489,490]]


static_trainer_classes = [23,66,67,70,72,75,74,73,76,87,112,89,88,86,98,103,104,105,107,106,108,110,109]


def evolve_poke(index_number):
	return(evolve_array_hgss[index_number])
	
def calc(trdata, trpoke):
	
	trainer_array = []
	pokemon_array = []
	
	#current integer byte-offset for TRdata
	#TRdata, start from 0x1758 = 5976
	pointer_data = 5976
	trainer_number = 0
	#will have bump at the trainer number location
	trainer_bump = []
	
	
	#parse trdata
	while True:
		#If the trainer class is always static or event (Rival, Elite 4, Gym Leaders, and Red), change to double battle, except for the data for the double battle against Claire and Lance alongside the Rival.
		if((trdata[pointer_data + 1] in static_trainer_classes) and trainer_number < 730 and trdata[pointer_data + 3] > 1):
			if(trdata[pointer_data + 16] & 2 == 0):
				trdata[pointer_data + 16] += 2
		
		
		skip_number = 8
		
		#get the "has items/has moves" booleans
		extra_space_bool = trdata[pointer_data]
		
		#if moves
		if(extra_space_bool & 1 == 1):
			skip_number += 8
		#if items
		if(extra_space_bool & 2 == 2):
			skip_number += 2
		
		#get # of Pokemon, which is the 3rd hex pair on
		number_pokemon = trdata[pointer_data + 3] & 7
		
		#write as many skips as the trainer has Pokemon
		pokemon_count = 0
		while True:
			#fix for Bugsy (third Pokemon has an extra byte for some reason)
			#if((trainer_number == 20 and pokemon_count == 2) or (trainer_number == 31 and pokemon_count == 2) or (trainer_number == 32 and pokemon_count == 2) or (trainer_number == 159 and pokemon_count == 0) or (trainer_number == 160 and pokemon_count == 0)):
				#skip_number += 2
				#print("fix")
			trainer_array.append([trainer_number, skip_number])
			pokemon_count += 1
			if(pokemon_count == number_pokemon):
				break
		
		trainer_bump.append([0])
		
		trainer_number += 1
		pointer_data += 20
		
		if(trainer_number == 737):
			break
			
	
	#offset initial for trpoke = 174E = 5966
	pointer_poke = 5966
	pokemon_count = 0
	total_pokemon = len(trainer_array)
	
	edit_array = []
	
	#pull all the levels:
	while True:
		
		level = trpoke[pointer_poke]
		
		if(level == 0 or level > 100):
			level1 = trpoke[pointer_poke+2]
			level2 = trpoke[pointer_poke-2]
			print("trying", level1, level2)
			
			if((level1 == 0 or level1 > 100) and (level2 == 0 or level2 > 100)):
				print("cannot fix")
				print("problem at trainer", 1+trainer_array[pokemon_count][0], "getting value", level, "at", pointer_poke)
			#two ahead is good but two behind is not
			elif((level1 > 0 and level1 <= 100) and (level2 == 0 or level2 > 100)):
				print("two ahead good", level1, "replacing", level, "at trainer", 1+trainer_array[pokemon_count][0], "address", pointer_poke)
				level = level1
				pointer_poke += 2
			#two behind is good but two ahead is not
			elif((level1 == 0 or level1 > 100) and (level2 > 0 and level2 <= 100)):
				print("two behind good", level1, "replacing", level, "at trainer", 1+trainer_array[pokemon_count][0], "address", pointer_poke)
				level = level2
				pointer_poke -= 2
			#both good
			else:
				print("Both make sense, check manually", level1, level2, "error value", level, "at trainer", 1+trainer_array[pokemon_count][0], "address", pointer_poke)
				level = min(level1, level2)
		
		#level at address pokemon_count
		edit_array.append([level, pointer_poke])
		
		
		#add index number to trainer_bump array
		trainer_bump[trainer_array[pokemon_count][0]].append(trpoke[pointer_poke+2] + trpoke[pointer_poke+3]*256)
		
		#if this is the last Pokemon, break
		if(pokemon_count + 1 >= total_pokemon):
			break
		else:
			#move to the next pokemon
			pointer_poke += trainer_array[pokemon_count][1]
			#increment the pokemon count
			pokemon_count += 1
	
	
	
	#initial scaling of all Pokemon
	pokemon_count = 0
	while True:
	
		level = edit_array[pokemon_count][0]
		
		#scales level, taking into account the order in which that trainer is encountered in-game. 
		try:
		
			mult = trainer_scale_array_hgss[trainer_array[pokemon_count][0]]
			mult /= 100
			mult += 1
			new_level = round(mult*level)
			
			if(new_level == level):
				new_level += 1
			
			#ensures that the level is at least the minimum level
			while True:
				if(new_level + trainer_bump[trainer_array[pokemon_count][0]][0] < trainer_min_level_array_hgss[trainer_array[pokemon_count][0]]):
					trainer_bump[trainer_array[pokemon_count][0]][0] += 1
				else:
					break
			#print("Trainer number", trainer_array[pokemon_count][0], "Bumped by", trainer_bump[trainer_array[pokemon_count][0]])
				
			level = min(new_level, 100)
			
		except:
			print("exception")
			level = 100
		
		edit_array[pokemon_count][0] = level
		
		#if this is the last Pokemon, break
		if(pokemon_count + 1 >= total_pokemon):
			break
		else:
			#increment the pokemon count
			pokemon_count += 1
		
	
		
	#add to each trainer to satisfy min level, evolve if needed, then write back to array
	pokemon_count = 0
	while True:
	
		pointer_poke = edit_array[pokemon_count][1]
		level = min(edit_array[pokemon_count][0] + trainer_bump[trainer_array[pokemon_count][0]][0], 100)
		
		print(trainer_array[pokemon_count][0], trainer_bump[trainer_array[pokemon_count][0]][0], level)
		
		if(False):
			#makes trainer's teams more diverse. If they have multiples of the same Pokemon on their team, it bumps the second copy to a different Pokemon that shares one of its types.
			#only do this once per trainer, by checking if the current Pokemon is from a different trainer than the last. If the try fails, it is the first trainer, who has only unique Pokemon anyway
			try:
				if(trainer_array[pokemon_count][0] != trainer_array[pokemon_count - 1][0]):
					temp_list = []
					for j in range(len(trainer_bump[trainer_array[pokemon_count][0]])):
						if j > 0:
							temp_list.append(trainer_bump[trainer_array[pokemon_count][0]][j])
					
					count_team = len(temp_list)
					
					for i in range(count_team):
						for j in range(count_team):
							if(i != j and temp_list[i] == temp_list[j]):
								if(temp_list[i] == temp_list[j]):
									type_iter = 0
									temp = temp_list[j]
									while True:
										#get the index of this Pokemon in the type
										try:
											new_index = type_array[type_iter].index(temp_list[j]) + 1
											#grab next Pokemon that has that type
											try:
												new_dex = type_array[type_iter][new_index]
											#out of range, loop around
											except:
												new_index = 1
												new_dex = type_array[type_iter][new_index]
											
											#otherwise, set the new dex number as current team member and iterate again
											if(new_dex in temp_list or (new_dex - temp)**2 <= 4):
												temp_list[j] = new_dex
											#ensure no duplicates and no same evolutionary line
											else:
												trainer_bump[trainer_array[pokemon_count][0]][j + 1] = new_dex
												break
										#Pokemon does not have this type
										except:
											type_iter += 1
									print("Index", temp, "now", temp_list[j])
					#write back to trpoke. "edit_array[pokemon_count + i][1]" gives current until the last pokemon this trainer has (adding 0,1,...5)
					for i in range(count_team):
						if(trainer_bump[trainer_array[pokemon_count][0]][i + 1] > 256):
							trpoke[edit_array[pokemon_count + i][1] + 3] = 1
							trainer_bump[trainer_array[pokemon_count][0]][i + 1] -= 256
						else:
							#write 0 to the high digit
							trpoke[edit_array[pokemon_count + i][1] + 3] = 0
						#low digit
						trpoke[edit_array[pokemon_count + i][1] + 2] = trainer_bump[trainer_array[pokemon_count][0]][i + 1]

			except:
				print("Major Error in Index Number Handling")
		
		#evolve the Pokemon if it is above the level it evolves at (or set value for other kinds of evolutions)
		#get index number
		low_digits = trpoke[pointer_poke + 2]
		high_digits = trpoke[pointer_poke + 3]*256
		
		index_number = low_digits + high_digits
		
		new_number = index_number
		
		#get the level that Pokemon should be evolved above. recurse in case a non-evolved pokemon is high enough to evolve twice
		while True:
			#get the level this Pokemon should evolve by
			try:
				evolve_level = evolve_level_barrier_array_hgss[new_number]
			except:
				print("Error at", trainer_array[pokemon_count][0] + 1)
				break
				
			#if it's high enough, grab the index number of the next stage
			if(level >= evolve_level):
				new_number = evolve_array_hgss[new_number]
			else:
				break
			if(new_number == evolve_array_hgss[new_number]):
				break
		
		#write new index number if different
		if(new_number != index_number):
			# as max in gen IV is 507, this is either 0x00 or 0x01. Only need to write either 0 or 1 
			if(new_number > 256):
				trpoke[pointer_poke + 3] = 1
				new_number -= 256
			else:
				#write 0 to the high digit
				trpoke[pointer_poke + 3] = 0
			#low digit
			trpoke[pointer_poke + 2] = new_number
					

		#write level back to the byte
		trpoke[pointer_poke] = level
		#if this is the last Pokemon, break
		if(pokemon_count + 1 >= total_pokemon):
			break
		else:
			#increment the pokemon count
			pokemon_count += 1
	return(trdata, trpoke)

#takes in bytearray, saves bytes to file
def save_binary_file(data, file_name, path):
	
	output_path = asksaveasfilename(initialdir = path,  defaultextension = "", initialfile = file_name)
	
	output_binary = bytes(data)
	
	with open(output_path, 'wb') as f:
		f.write(output_binary)

		
#write backup of the file to be modified to local directory
def save_backup(data, name):
	try:
		current_directory = os.getcsd()
		file_name = os.path.join(current_directory, 'backup', name, '.',time.strftime("%y/%m/%d %H:%M"),'.bak')
		with open(file_name, 'wb') as f:
			f.write(output_binary)
	except:
		print("Could not save backup")

		
def get_files():

	#for HGSS, trdata is a055, trpoke is a056
	
	#get hex file locations:
	root = Tk()
	root.update()
	trdata_location = askopenfilename(filetypes = (("Select a/0/5/5", "*.*"), ("All Files", "*.*")))
	trpoke_location = askopenfilename(filetypes = (("Select a/0/5/6", "*.*"), ("All Files", "*.*")))
	root.destroy()
	
	
	trdata = bytearray()
	trpoke = bytearray()
	
	#get the data
	with open(trdata_location, 'rb') as f:
		trdata_bin = f.read()
	
	with open(trpoke_location, 'rb') as f:
		trpoke_bin = f.read()
	
	save_backup(trpoke_bin, 6)

	
	#convert the binary data into bytearrays. each index is one hex-pair
	trdata = bytearray(trdata_bin)
	trpoke = bytearray(trpoke_bin)
	
	return(trdata, trpoke, trpoke_location)
	
def main():
	#get the data files and the output path
	trdata, trpoke, output_path = get_files()
	
	trdata, trpoke = calc(trdata, trpoke)
	
	#seperates the file name (always a single character from HGSS on) from path
	file_name = output_path[-1]
	output_path = output_path[:-1]
	
	save_binary_file(trdata, '5', output_path)
	save_binary_file(trpoke, '6', output_path)
		
		
main()
