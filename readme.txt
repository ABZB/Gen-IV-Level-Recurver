Section I: Purpose

	This program increases the level curve of enemy trainers.

	It currently works for the following games:

	HeartGold
	Soulsilver

	I plan to extend its functionality to at least Black2/White2.

	I do not plan to extend it to work with games from Generation VI onward, as tools to do so for those games already exist.

Section II: Description of edits

	HGSS:

	* Level curve rescaled so the Elite 4 is roughly at the level it is in Generation I games, and Kanto trainers scale from there through level 100 (Kanto Gym Leaders will be leveled in the 90s).

	* All trainer's Pokemon that are level 40 or higher are evolved to their final form (Pokemon with multiple evolutionary branches will evolve into the one with the lowest Pokedex number).


Section III: Instructions

	1) Decompress the NDS file using an appropriate tool.

	2) Run Trainer Level Booster

	3) Select the appropriate generation, if this feature has been added.

	4) Select the appropriate files as instructed:

			* HGSS: root/a/0/5/5 (TRdata) then root/a/0/5/6 (TRpoke)

	5) A timestamped backup of the file that will be edited will be saved to the /backup subfolder.
	
	6) A prompt will appear to save the edited file.
	
	7) Rebuild the NDS file.
	
Section IV: Be aware of the following:

	1) If your trdata or trpoke were edited in a way that changes the offset of the first trainer or Pokemon, the program will (probably) run, but the output will not be good. As this program does not alter any offsets, try running this before applying any other patches, if possible.
	2) I have not as of yet playtested this, please let me know if there are any trainers or areas where the level jump more or less than they should.