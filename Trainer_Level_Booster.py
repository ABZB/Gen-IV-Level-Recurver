import io
import string
import math
from tkinter import *
from tkinter.filedialog import askopenfilename
import binascii
import os
import time

trainer_scale_array_hgss = [12,3,3,5,18,14,16,4,23,12,100,11,11,46,74,23,48,8,100,7,12,18,9,17,9,8,100,70,7,18,20,45,26,25,51,70,22,67,21,100,100,100,6,21,21,20,4,72,8,7,6,6,6,6,6,8,8,77,65,8,10,14,100,14,14,14,12,12,12,18,18,16,22,16,16,16,16,16,100,16,19,21,68,68,23,23,100,100,20,24,24,24,24,24,24,24,24,24,24,10,11,70,60,60,100,100,100,48,44,51,51,51,70,60,60,44,51,100,51,100,48,31,29,47,47,44,44,100,29,31,31,31,100,29,67,68,47,100,75,72,100,14,48,48,48,48,49,70,69,69,49,76,76,49,10,25,25,100,25,100,100,100,100,100,100,100,100,100,100,100,100,31,31,100,100,100,100,17,67,100,17,17,68,17,45,45,45,45,45,45,45,45,45,100,45,45,45,45,45,45,100,100,100,100,100,100,100,100,100,100,22,22,22,22,22,46,22,46,46,46,100,46,46,46,100,100,46,46,100,62,100,60,46,69,75,100,100,75,75,100,100,75,100,58,58,58,58,72,4,48,25,79,73,70,60,64,68,62,80,82,81,100,20,100,3,12,20,100,12,20,58,100,100,14,14,100,100,48,4,4,100,20,46,100,100,100,100,58,58,6,79,100,78,78,100,77,70,70,76,66,67,67,100,100,100,100,100,73,63,63,63,67,66,66,66,65,65,74,9,65,65,65,29,29,47,64,76,67,70,70,67,69,69,14,49,64,60,100,100,100,100,100,100,100,100,64,100,65,65,66,66,100,46,100,100,64,69,65,65,16,70,76,100,63,63,70,100,62,62,79,79,100,78,77,100,100,70,74,74,65,65,67,8,9,100,19,12,16,21,9,46,46,46,100,17,60,21,21,75,21,22,31,31,46,47,47,47,47,14,21,70,60,70,100,62,64,100,58,70,65,65,100,100,75,75,75,100,100,100,17,17,17,17,21,21,17,17,21,21,22,22,100,100,60,60,100,47,47,16,47,48,48,49,16,16,70,70,70,70,5,5,8,8,21,21,31,31,45,45,45,46,46,100,100,100,100,100,45,46,45,45,45,45,45,46,11,46,45,100,100,100,65,20,20,3,3,3,25,45,52,52,52,17,100,17,100,21,100,22,4,100,5,16,100,8,100,29,100,100,14,100,31,10,100,14,100,16,21,100,31,100,100,100,100,100,100,100,100,100,100,100,100,100,100,76,76,74,74,74,74,74,74,63,63,65,65,65,65,65,65,65,65,65,66,66,66,66,66,67,67,67,66,66,66,66,66,66,66,66,78,78,78,78,78,78,100,78,78,77,77,77,77,77,77,77,77,77,61,61,61,11,100,49,70,48,48,60,47,70,21,17,47,17,17,17,14,14,14,16,16,16,72,72,72,72,72,72,66,66,66,66,66,66,66,66,66,67,67,67,67,67,67,67,67,67,66,66,66,66,66,66,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,100,100,100,100,100,22,22,22,45,70,70,70,19,19,81,81,81,81,73,79,79,79,80,80,80,80,80,80,75,100,75,75,75,100,100,58,100,100,100,45,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,26,27,27,27,27,100,100,100,100,100]

evolve_array_hgss = [0,3,3,3,6,6,6,9,9,9,12,12,12,15,15,15,18,18,18,20,20,22,22,24,24,26,26,28,28,31,31,31,34,34,34,36,36,38,38,40,40,169,169,45,45,45,47,47,49,49,51,51,53,53,55,55,57,57,59,59,62,62,62,65,65,65,68,68,68,71,71,71,73,73,76,76,76,78,78,80,80,462,462,83,85,85,87,87,89,89,91,91,94,94,94,208,97,97,99,99,101,101,103,103,105,105,106,107,463,110,110,464,464,242,465,115,230,230,119,119,121,121,122,123,124,466,467,127,128,130,130,131,132,134,134,135,136,474,139,139,141,141,142,143,144,145,146,149,149,149,150,151,154,154,154,157,157,157,160,160,160,162,162,164,164,166,166,168,168,169,171,171,25,36,40,468,468,178,178,181,181,181,182,184,184,185,186,189,189,189,424,192,192,469,195,195,196,197,430,199,429,201,202,203,205,205,206,472,208,210,210,211,212,213,214,461,217,217,219,219,473,473,222,224,224,225,226,227,229,229,230,232,232,233,234,235,237,237,124,466,467,241,242,243,244,245,248,248,248,249,250,251,254,254,254,257,257,257,260,260,260,262,262,264,264,267,267,267,269,269,272,272,272,275,275,275,277,277,279,279,282,282,282,284,284,286,286,289,289,289,291,291,292,295,295,295,297,297,184,476,301,301,302,303,306,306,306,308,308,310,310,311,312,313,314,407,317,317,319,319,321,321,323,323,324,326,326,327,330,330,330,332,332,334,334,335,336,337,338,339,340,341,342,344,344,346,346,348,348,350,350,351,352,354,354,477,477,357,358,359,202,362,362,365,365,365,367,367,368,369,370,373,373,373,376,376,376,377,378,379,380,381,382,383,384,385,386,389,389,389,392,392,392,395,395,395,398,398,398,400,400,402,402,405,405,405,407,407,409,409,411,411,413,413,414,416,416,417,419,419,421,421,423,423,424,426,426,428,428,429,430,432,432,358,435,435,437,437,185,122,242,441,442,445,445,445,143,448,448,450,450,452,452,454,454,455,457,457,226,460,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507]



def evolve_poke(index_number):
	return(evolve_array_hgss[index_number])
	
def calc(trdata, trpoke):
	
	trainer_array = []
	pokemon_array = []
	
	#current integer byte-offset for TRdata
	#TRdata, start from 0x1758 = 5976
	pointer_data = 5976
	trainer_number = 0
	trainer_number_array = [0]
	
	
	#parse trdata
	while True:
		skip_number = 6 + 2
	
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
		trainer_number_array.append(number_pokemon)
		while True:
			trainer_array.append([trainer_number, skip_number])
			pokemon_count += 1
			if(pokemon_count == number_pokemon):
				break
	
		trainer_number += 1
		pointer_data += 20
		
		if(trainer_number == 737):
			break
			
	
	#offset initial for trpoke = 174E = 5966
	pointer_poke = 5966
	pokemon_count = 0
	total_pokemon = len(trainer_array)
	
	
	while True:

	
		
		level = trpoke[pointer_poke]
		
		#in HGSS there is exactly one trainer who causes this exception - the one with Seals on her balls, I think.
		if(level == 0 or level > 100):
			print("problem at trainer ", trainer_array[pokemon_count][0])
			pointer_poke -= 2
			level = trpoke[pointer_poke]
			print("trying", level)
		
		#scales level, taking into account the order in which that trainer is encountered in-game. 
		try:
		
			mult = trainer_scale_array_hgss[trainer_array[pokemon_count][0]]
			mult /= 100
			mult += 1
			mult *= level
			
			level = round(mult)
			
			level = min(level, 100)
			
		except:
			print("exception")
			level = min(level * 2, 100)
		
		

		#write level back to the byte
		trpoke[pointer_poke] = level
		
		
		#if level is greater than the chosen value, fully evolve the Pokemon
		if(level >= 40):
			low_digits = trpoke[pointer_poke + 2]
			
			high_digits = trpoke[pointer_poke + 3]*256
			
			index_number = low_digits + high_digits
			
			#get FE index #, if any
			new_number = evolve_poke(index_number)
			#write new index number
			# as max in gen IV is 507, this is either 0x00 or 0x01. Only need to write either 0 or 1 
			if(new_number > 256):
				trpoke[pointer_poke + 3] = 1
				new_number -= 256
			else:
				#write 0 to the high digit
				trpoke[pointer_poke + 3] = 0
				#1's place
				trpoke[pointer_poke + 2] = new_number
						
			
		#if this is the last Pokemon, break
		if(pokemon_count + 1 >= total_pokemon):
			break
		
		else:
			#move to the next pokemon
			pointer_poke += trainer_array[pokemon_count][1]
			#increment the pokemon count
			pokemon_count += 1
	return(trpoke)

#takes in bytearray, saves bytes to file
def save_binary_file(data, file_name, path):
	
	output_path = asksaveasfilename(initialdir = path,  defaultextension = ".txt", initialfile = file_name)
	
	output_binary = bytes(data)
	
	with open(output_path, 'wb') as f:
		f.write(output_binary)

		
		#write backup of the file to be modified to local directory
def save_backup(data, name):
	try:
		current_directory = os.getcsd()
		file_name = os.path.join(current_directory, 'backup', name, '.',time.strftime("%y/%m/%d %H:%M"),.bak)
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
	
	trpoke = calc()
	
	#seperates the file name (always a single character from HGSS on) from path
	file_name = output_path[-1]
	output_path = output_path[:-1]
	
	save_binary_file(trpoke, file_name, output_path)
		
		
main()