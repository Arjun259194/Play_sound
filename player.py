from asyncio import sleep
from playsound import playsound

file = input('Enter sound file location with file\n>')
opened_file = open(file)
file_dir = opened_file.name
opened_file.close()

file_name = file_dir.split('/')[-1].split('.')[0]

print(f'playing {file_name} ...')

playsound(file)
