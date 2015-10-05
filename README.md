# RecSysOrd
Modul for recording videos from recognition.

- seznam zásuvných modulů:
	a) SimpleCV
	b) OpenCV
	c) numpy

- vstup: povel k zahájení, či ukončení (simulace tlačítka nahraj a přestaň nahrávat)
- vystup: složka s názvem ve formátu YYYY-MM-DD, která bude obsahovat videa s názvem ve formátu video_HH-MM-SS_čísloKamery.avi

Celý modul bude fungovat následujícím způsobem:
	a) v ČAS dostane povel k zaznamenání kamery ČÍSLO
	b) v domovské adresáři systému vytvoří do složky záznamy složku reprezentující okamžik, do které se bude/ou zaznamenávat videa
	c) v ČAS2 dostane povel k ukončení zaznamenávání kamery ČÍSLO

Videa budou zaznamenávaná ve formátu .avi bez zvuku...