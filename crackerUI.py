

from Tkinter import *

from tkFileDialog import askopenfilename, asksaveasfilename
from crackerFunctions import *

def load_button_handler():
    '''
    This is a simple function to read the contents of a text file
    and display them in a text widget.
    :return: Nothing is returned.
    '''
    try:
        filePath = askopenfilename()
        with open(filePath,'r') as file:
            encryptedTextStr = file.read()
            txtEncrypted.delete(0.0, END)
            txtEncrypted.insert(0.0,encryptedTextStr)
    except:
        print('The user cancelled.')

def save_button_handler():
    '''
    This is a simple function to write the contents of the decrypted
    text to a file if desired.
    :return: Nothing is returned.
    '''
    try:
        filePath = asksaveasfilename()
        with open(filePath, 'w') as file:
            plainTextToWrite = txtCracked.get(0.0, END)
            file.write(plainTextToWrite)
    except:
        print 'The user cancelled.'

def code_button_handler():
    '''
    This button handler takes care of the first half of the decryption process
    by calling all the relevant functions from the functions file.
    :return:
    '''
    cipherString = txtEncrypted.get('1.0','end-1c') # Get the encrypted text
    tlc = findThreeLetterCombos(cipherString) # Find the three letter combos
    intervalsList = findIntervals(tlc, cipherString) # Find the intervals and factors
    keysAndLengths = findKeyLength(intervalsList) # Estimate the likely key length

    keyAnalysis.deiconify() # Display the key length selection window

    radioPointer = 0
    while radioPointer < len(keysAndLengths):

        hashStr = ''
        for i in range(keysAndLengths[radioPointer][1]):
            hashStr = hashStr + '#'
        theText = str(keysAndLengths[radioPointer][0]) + ' : ' + str(hashStr)
        radios[radioPointer].config(text=theText, value=keysAndLengths[radioPointer][0])
        radioPointer += 1
    rdValue.set(keysAndLengths[0][0]) # Set the first radio button to ON

def doReturn():
    '''
    This is the second half of the decryptio process and is called when the user returns
    the likely key length they wish to try
    :return:
    '''
    keyAnalysis.withdraw()
    likelyKeyLength = rdValue.get()
    cipherText = txtEncrypted.get(0.0, END)

    substrings = divideCiphertext(cipherText, likelyKeyLength)
    keyword = retrieveKeyword(substrings)

    txtKeyword.delete(0, END)
    txtKeyword.insert(0, keyword)

    plainTextString = doDecrypt(cipherText, keyword)
    txtCracked.delete(0.0, END)
    txtCracked.insert(0.0, plainTextString)




main = Tk()
main.geometry('600x500')
main.title('Vigenere Cipher Cracker v2.0')

lbSpace1 = Label(main, text='     ').grid(row=0, column=0)

txtEncrypted = Text(main, width=75, height=12)
txtEncrypted.grid(row=1, column=1, columnspan=5)
txtEncrypted.config(wrap=WORD)
txtEncrypted.focus_set()

lbKeyword = Label(main, text='Keyword').grid(row=2, column=1)

txtKeyword = Entry(main)
txtKeyword.grid(row=2, column=2)

pbLoad = Button(main, text='Load', command=load_button_handler)
pbLoad.grid(row=2, column=3)

pbRotate = Button(main, text='Decrypt', command=code_button_handler)
pbRotate.grid(row=2, column=4)

pbSave = Button(main, text='Save', command=save_button_handler)
pbSave.grid(row=2, column=5)

txtCracked = Text(main, width=75, height=12)
txtCracked.grid(row=3, column=1, columnspan=5)
txtCracked.config(wrap=WORD)

keyAnalysis = Toplevel()
keyAnalysis.geometry('600x400+800+0')
keyAnalysis.title('Key length analysis')

lbspace2 = Label(keyAnalysis, text='     ').grid(row=0, column=0)

rdValue = IntVar()

radios = []
for i in range(10):
    radios.append(Radiobutton(keyAnalysis, variable=rdValue))

for i in range(10):
    radios[i].grid(row=i, column=1, sticky='W')

pbReturn = Button(keyAnalysis, text='Return', command=doReturn)
pbReturn.grid(row=12, column=1)


keyAnalysis.withdraw()
mainloop()