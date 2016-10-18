def song_decoder(song,rm):
	song = song.split(rm)
	new_song = ''
	for i in song:
		if i == '':continue
		new_song = new_song + ' ' + i
	return new_song.strip()

song = raw_input('mixed song:')
rm = raw_input('the thing need to remove:')
print song_decoder(song,rm)
