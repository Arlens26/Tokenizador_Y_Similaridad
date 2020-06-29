from tkinter import *
###### Libraria sentence piece para words, subwords
import sentencepiece as spm

# Entrenamiento de palabras
spm.SentencePieceTrainer.train('--input=tweets_clean.txt --model_prefix=m_word --model_type=word --vocab_size=2000')
sp_word = spm.SentencePieceProcessor()
sp_word.load('m_word.model')

# Entrenamiendo de subpalabras
spm.SentencePieceTrainer.train('--input=tweets_clean.txt --model_prefix=m_user --user_defined_symbols=<sep>,<cls> --vocab_size=2000')
sp_user = spm.SentencePieceProcessor()
sp_user.load('m_user.model')

window = Tk()
window.geometry("800x600")
# No se puede cambiar tamaño ventana
window.resizable(False,False)
window.title("Tokenizador de Tweet")


main_title = Label(window, text="Tokenizador", font=("Cambria Bold",24), bg="#6973FF", fg="white", width="42", height="0")
main_title.pack()
#main_title.grid(column=0, row=0)

#tweet = StringVar()

input_tweet = Text(window, height=25, width=45)
input_tweet.place(x=30, y=60)
#input_tweet.grid(column=0, row=1)

out_tweet = Text(window, height=25, width=45)
out_tweet.place(x=400, y=60)
#out_tweet.grid(column=1, row=1)

def word():
	text_tweet = input_tweet.get("1.0","end-1c")
	word = sp_word.encode_as_pieces(text_tweet)		
	out_tweet.insert(INSERT, word)	
	#out_tweet.configure(text=text_tweet)

def subword():
	text_tweet = input_tweet.get("1.0","end-1c")
	subword = sp_user.encode_as_pieces(text_tweet)
	sp_user.piece_to_id('<sep>')
	sp_user.piece_to_id('<cls>')
	sp_user.decode_ids([3])
	sp_user.decode_ids([4])
	out_tweet.insert(INSERT, str(subword))

def clear():
	input_tweet.delete("1.0","end-1c")
	out_tweet.delete("1.0","end-1c")


btn_word = Button(window, text="Word", bg="#4056FF", command=word)
btn_word.place(x=180, y=500)
#btn.grid(column=0, row=2)

btn_subword = Button(window, text="Subword", bg="#4056FF", command=subword)
btn_subword.place(x=250, y=500)

btn_clear = Button(window, text="Clear", bg="#4056FF", command=clear)
btn_clear.place(x=350, y=500)

window.mainloop()