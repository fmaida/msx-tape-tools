from .generico import BloccoDati
from ..intestazioni import Intestazioni
from ..wav import Esportazione


class FileAscii(BloccoDati):

	intestazione = b"\xea" * 10

	# --=-=--------------------------------------------------------------------------=-=--

	def esporta(self, p_file: Esportazione):

		p_file.inserisci_sincronismo(2000)  # Tre secondi

		intestazione = Intestazioni.blocco_file_ascii + self.titolo.ljust(6, " ").encode("ascii")

		for elemento in intestazione:
			p_file.inserisci_byte(elemento)

		p_file.inserisci_silenzio(750)

		p_file.inserisci_sincronismo(1000)  # Tre/quarti di secondo

		ind = 0
		continua = True
		temp = ""
		print(len(self.dati))
		while continua:
			stringa = self.dati[ind:ind+8]
			if stringa == Intestazioni.blocco_intestazione:
				p_file.inserisci_silenzio(500)
				p_file.inserisci_sincronismo(1000)
				ind += 8
			else:
				if ind < (len(self.dati) - 1):
					a = self.dati[ind:ind+1]
					b = ord(a)
					temp += a.decode("ascii")
					p_file.inserisci_byte(b)
				else:
					p_file.inserisci_byte(26)
					temp += "[FINE]"
					continua = False
				ind += 1
		print(temp)
		print(len(temp) - len("[FINE]"))
