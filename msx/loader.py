class Loader:

	# loader 8kb (C) Alexey Podrezov
	# loader 16/32kb (C) Edison Antonio Pires de Moraes

	# Ricordati che quando importi i file ASM devi eliminare i primi sette bytes
	# i primi 7 bytes = 0xFE + 2 x Indirizzo partenza + 2 x Indirizzo fine
	# + 2 x Indirizzo esecuzione

	binari_16k_4000h = b':\xff\xff/\xe6\xf0G\x0f\x0f\xb02\xff\xff' \
					   b'\xcd8\x01G\x0f\x0f\xb0\xcd;\x01!\x00\x90\x11\x00@\x01\x00@\xed\xb0:{' \
					   b'\xfe\xfe\xc9(\x0b\xfd*G\xf3\xdd!)@\xcd\x1c\x00*\x02@\xe9'

	binari_16k_8000h = b'\xf3!\x00\x90\x11\x00\x80\x01\x00@\xed\xb0:{' \
					   b'\xfe\xfe\xc9(\x0b\xfd*G\xf3\xdd!)@\xcd\x1c\x00*\x02\x80\xe9'

	binari_32k_4000h = b'\xf3:\xff\xff/28\xd0\xe6\xf0G\x0f\x0f\xb02' \
					   b'\xff\xff\xcd8\x0127\xd0G\x0f\x0f\xb0\xcd;\x01!\x00\x90\x11\x00@\x01' \
					   b'\x00@\xed\xb0:7\xd0\xcd;\x01:8\xd02\xff\xff\xfb\xc9\x00\x00'

	binari_32k_8000h = b'\xf3:\xff\xff/\xe6\xf0G\x0f\x0f\xb02\xff' \
					   b'\xff\xcd8\x01G\x0f\x0f\xb0\xcd;\x01!\x00\x90\x11\x00\x80\x01\x00' \
					   b'@\xed\xb0:{\xfe\xfe\xc9(\x0b\xfd*{\xfe\xdd!)@\xcd\x1c\x00*\x02@\xe9'


	binari_8k_4000h = bytes([243, 58, 255, 255, 47, 245, 230, 240, 71,
							 7, 7, 7, 7, 176, 50, 255, 255, 219, 168,
							 245, 230, 240, 71, 7, 7, 7, 7, 176, 211,
							 168, 33, 0, 160, 17, 0, 0, 1, 0, 32, 237,
							 176, 33, 0, 0, 17, 0, 32, 1, 0, 160, 237,
							 176, 241, 211, 168, 241, 50, 255, 255, 199])
