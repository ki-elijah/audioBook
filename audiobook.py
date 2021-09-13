import PyPDF2

pdfReader = PyPDF2.PdfFileReader(
    open('The life of A W Tozer  In Pursuit of God.pdf', 'rb'))

import pyttsx3

speaker = pyttsx3.init()
for pagenum in range(pdfReader.numPages):
    text = pdfReader.getPage(pagenum).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()

speaker.save_to_file(text, 'book.mp3')
speaker.runAndWait()
