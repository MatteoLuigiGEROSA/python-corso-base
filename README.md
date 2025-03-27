# CFP Terragni di Meda - Linguaggio PYTHON, Corso Base

Se desideri fare qualche esperimento in autonomia con questo materiale sul tuo Personal Computer, devi prima scaricarlo mediante **Git** (programma *git-client*), invocando apposito comando `git clone <GIT-REPO-ADDR>` - ti basterà seguire i semplici passi qui di seguito descritti.

Ma se sei già esperto, allora ti basta questo: <br>
<br> `git clone https://github.com/MatteoLuigiGEROSA/python-corso-base.git` <br>

Subito dopo, per lanciare i programmi Python che avrai scaricato, ti servirà aver installato il pacchetto [Python per Windows](https://www.python.org/ftp/python/3.13.2/python-3.13.2-amd64.exe) ed eventualmente configurare un *VenV*, ovvero un *Python virtual-environment* (o *Ambiente virtuale Python*): in fondo a questo documento sono appositamente state inserite alcune brevi istruzioni per poter costruire facilmente ed utilizzare un tuo nuovo *venv*.

<br>

Per installare **Git** su Windows:

1. Apri il browser e vai sul link: https://git-scm.com/download/win
2. Il download inizierà automaticamente.
3. Esegui il file scaricato per installare Git.
4. Durante l'installazione puoi lasciare tutte le opzioni predefinite (consigliato).
5. Al termine, clicca su **Finish**.

<br>

Per scaricare questo materiale (repository **PythonCorsoBase**):

1. Dopo l’installazione di Git, clicca su **Start** (oppure premi il tasto Windows).
2. Cerca e apri **Git Bash**, per lanciare Git
3. Si aprirà una finestra simile a un terminale, ed in effetti questo è proprio un teminale *bash* su Windows, recante **MINGW64** nel titolo, vicino ad un'icona colorata a forma di diamante
4. Spostati nella cartella dove vuoi scaricare i file del corso <br>
   Esempio: <br>
   per spostarti nella cartella Windows `C:\Users\NomeUtente\Documents\PythonCorsoBase`, utilizza uno dei due comandi seguenti:<br>
   * in stile *bash*: `cd /c/Users/NomeUtente/Documents/PythonCorsoBase` <br>
   * in stile *MS-DOS*: `cd C:\Users\NomeUtente\Documents\PythonCorsoBase` <br>
5. Esegui il comando per *clonare* (cioé: scaricare in locale) il repository dal web-site di **GitHub**: <br>
   `git clone https://github.com/MatteoLuigiGEROSA/python-corso-base.git`
6. Dopo qualche secondo, vedrai una nuova cartella con il nome `python-corso-base`: essa **è la tua copia locale personale** del *git-repo* `python-corso-base` (cioé: del repository Git `python-corso-base`)
7. Ora puoi entrare nella cartella **python-corso-base** e navigare tra i file del git-repo omonimo: <br>
`cd python-corso-base`
8. Per aggiornare il contenuto di codesto tuo repository locale, dovrai *pullare* (!!!) invocando `git pull` dall'interno di tale directory...

<br>

Se desideri **imparare di più su Git**, qui c'è la copia elettronica gratuita del manuale, che puoi scaricare: <br>
https://git-scm.com/book

<br>

(Facoltativo) **Collegare con un Python Virtual Environment (VenV):**

Se hai già creato un virtual-environment, ad esempio chiamato *venv_lezione_01*, puoi attivarlo con: <br>
`.\venv_lezione_01\Scripts\activate`

Oppure, se devi ancora crearlo, potrai farlo mediante l'apposito comando Python che segue:
```
python -m venv venv_lezione_01
.\venv_lezione_01\Scripts\activate
```

<br>

**Ora finalmente puoi davvero iniziare a lavorare sugli esercizi del Corso di Python !!! <br> HAPPY CODING !!! :-)**

