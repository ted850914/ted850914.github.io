#python 2.7.14
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import random
import base64
from Tkinter import *

def generate_key():
	# generate random number
	random_generator = Random.new().read
	# RSA generator
	rsa = RSA.generate(1024, random_generator)

	# generate public & private key
	private_key = rsa.exportKey()
	public_key = rsa.publickey().exportKey()

	return private_key, public_key

def encrypt(key, message):
	rsakey = RSA.importKey(key)
   	cipher = Cipher_pkcs1_v1_5.new(rsakey)
	len_message = len(message)	
	cipher_text = ""
	if len_message < 117: 
   		cipher_text = cipher.encrypt(message)
	else:
		offset = 0
		while len_message - offset > 0:
			if len_message - offset > 117:
				cipher_text += cipher.encrypt(message[offset:offset+117])
			else:
				cipher_text += cipher.encrypt(message[offset:])
			offset += 117
   	return base64.b64encode(cipher_text)

def decrypt(key, encrypt_text):
	rsakey = RSA.importKey(key)
   	cipher = Cipher_pkcs1_v1_5.new(rsakey)
	encrypt_text = base64.b64decode(encrypt_text)
	len_text = len(encrypt_text)
	text = ""
	if len_text < 128:
   		text = cipher.decrypt(encrypt_text, 1)
	else:
		offset = 0
		while len_text - offset > 0:
			if len_text - offset > 128:
				text += cipher.decrypt(encrypt_text[offset:offset+128], 1)
			else:
				text += cipher.decrypt(encrypt_text[offset:], 1)
			offset += 128
   	return text

def signature(key, message):
	rsakey = RSA.importKey(key)
	signer = Signature_pkcs1_v1_5.new(rsakey)
	digest = SHA.new()
	digest.update(message)
	sign = signer.sign(digest)
	signature = base64.b64encode(sign)
	return signature

def verify(key, signature, message):
	rsakey = RSA.importKey(key)
	verifier = Signature_pkcs1_v1_5.new(rsakey)
	digest = SHA.new()
	digest.update(message)
	is_verify = verifier.verify(digest, base64.b64decode(signature))
	
	return is_verify

#init
Ted_private, Ted_public = generate_key()
Karen_private, Karen_public = generate_key()

#step1 Ted send Ted_enonce to Karen
def step1():
	global Ted_enonce, Ted_nonce
	Ted_nonce = random.randint(0,65535)
	Ted_enonce = encrypt(Ted_public, str(Ted_nonce))
	Ted_et3.delete(0,END)
	Ted_et3.insert(END, Ted_nonce)
	Ted_et4.delete(0,END)
	Ted_et4.insert(END, Ted_enonce)
	Karen_et3.delete(0,END)
	Karen_et3.insert(END, Ted_enonce)

#step2 Karen send Ted_enonce & Karen_enonce to KDC
def step2():
	global Karen_enonce, Karen_nonce
	Karen_nonce = random.randint(0,65535)
	Karen_enonce = encrypt(Karen_public, str(Karen_nonce))
	Karen_et4.delete(0,END)
	Karen_et4.insert(END, Karen_nonce)
	Karen_et5.delete(0,END)
	Karen_et5.insert(END, Karen_enonce)
	KDC_et5.delete(0,END)
	KDC_et5.insert(END, Ted_enonce)
	KDC_et6.delete(0,END)
	KDC_et6.insert(END, Karen_enonce)

#step3 KDC send (Ks & Ted_enonce & signature) to Ted, send (Ks & Karen_enonce & signature) Karen
def step3():
	global Ted_dnonce, Karen_dnonce, Session_private, Session_public, Ted_encrypt_text, Ted_signature, Karen_encrypt_text, Karen_signature
	Ted_dnonce = decrypt(Ted_private, Ted_enonce)
	Karen_dnonce = decrypt(Karen_private, Karen_enonce)
	Session_private, Session_public = generate_key()
	Ted_encrypt_text = encrypt(Ted_public, Session_private + ":" + Session_public + ":" + Ted_dnonce)
	Ted_signature = signature(Ted_private, Session_private + ":" + Session_public + ":" + Ted_dnonce)
	Karen_encrypt_text = encrypt(Karen_public, Session_private + ":" + Session_public + ":" + Karen_dnonce)
	Karen_signature = signature(Karen_private, Session_private + ":" + Session_public + ":" + Karen_dnonce)
	KDC_et7.delete(0,END)
	KDC_et7.insert(END, Ted_dnonce)
	KDC_et8.delete(0,END)
	KDC_et8.insert(END, Karen_dnonce)
	KDC_et9.delete(0,END)
	KDC_et9.insert(END, Session_private)
	KDC_et10.delete(0,END)
	KDC_et10.insert(END, Session_public)
	KDC_et11.delete(0,END)
	KDC_et11.insert(END, Ted_signature)
	KDC_et12.delete(0,END)
	KDC_et12.insert(END, Karen_signature)

#step4 Ted & Karen decrypt the message from KDC, verify the message and nonce, use Ks to communicate with each other
def step4():
	global Ted_message, Ted_verify, Ted_Session_private, Ted_Session_public, Ted_Session_nonce
	Ted_message = decrypt(Ted_private, Ted_encrypt_text)
	Ted_verify = verify(Ted_public, Ted_signature, Ted_message)
	Ted_Session_private = Ted_message.split(":")[0]
	Ted_Session_public = Ted_message.split(":")[1]
	Ted_Session_nonce = Ted_message.split(":")[2]
	Ted_et5.delete(0,END)
	Ted_et5.insert(END, Ted_Session_nonce)
	Ted_et6.delete(0,END)
	Ted_et6.insert(END, Ted_signature)
	Ted_et7.delete(0,END)
	Ted_et7.insert(END, Ted_Session_private)
	Ted_et8.delete(0,END)
	Ted_et8.insert(END, Ted_Session_public)
	Ted_et9.delete(0,END)
	Ted_et9.insert(END, Ted_verify)

def step4_2():
	global Karen_message, Karen_verify, Karen_Session_private, Karen_Session_public, Karen_Session_nonce
	Karen_message = decrypt(Karen_private, Karen_encrypt_text)
	Karen_verify = verify(Karen_public, Karen_signature, Karen_message)
	Karen_Session_private = Karen_message.split(":")[0]
	Karen_Session_public = Karen_message.split(":")[1]
	Karen_Session_nonce = Karen_message.split(":")[2]
	Karen_et6.delete(0,END)
	Karen_et6.insert(END, Karen_Session_nonce)
	Karen_et7.delete(0,END)
	Karen_et7.insert(END, Karen_signature)
	Karen_et8.delete(0,END)
	Karen_et8.insert(END, Karen_Session_private)
	Karen_et9.delete(0,END)
	Karen_et9.insert(END, Karen_Session_public)
	Karen_et10.delete(0,END)
	Karen_et10.insert(END, Karen_verify)

def show():
	global Ted_nonce
	print(Ted_nonce)

Ted_win = Tk()
Ted_win.title("Ted")
Ted_win.geometry("400x600")

Ted_lb1 = Label(Ted_win, text="private key", font=('Microsoft JhengHei', 10))
Ted_lb1.pack()
Ted_et1 = Entry(Ted_win, font=('Microsoft JhengHei', 10), width=40)
Ted_et1.insert(END, Ted_private)
Ted_et1.pack()

Ted_lb2 = Label(Ted_win, text="public key", font=('Microsoft JhengHei', 10))
Ted_lb2.pack()
Ted_et2 = Entry(Ted_win, font=('Microsoft JhengHei', 10), width=40)
Ted_et2.insert(END, Ted_public)
Ted_et2.pack()

Ted_lb3 = Label(Ted_win, text="nonce", font=('Microsoft JhengHei', 10))
Ted_lb3.pack()
Ted_et3 = Entry(Ted_win, font=('Microsoft JhengHei', 10), width=40)
Ted_et3.pack()

Ted_lb4 = Label(Ted_win, text="enonce", font=('Microsoft JhengHei', 10))
Ted_lb4.pack()
Ted_et4 = Entry(Ted_win, font=('Microsoft JhengHei', 10), width=40)
Ted_et4.pack()

Ted_lb5 = Label(Ted_win, text="dnonce", font=('Microsoft JhengHei', 10))
Ted_lb5.pack()
Ted_et5 = Entry(Ted_win, font=('Microsoft JhengHei', 10), width=40)
Ted_et5.pack()

Ted_lb6 = Label(Ted_win, text="signature", font=('Microsoft JhengHei', 10))
Ted_lb6.pack()
Ted_et6 = Entry(Ted_win, font=('Microsoft JhengHei', 10), width=40)
Ted_et6.pack()

Ted_lb7 = Label(Ted_win, text="Session private key", font=('Microsoft JhengHei', 10))
Ted_lb7.pack()
Ted_et7 = Entry(Ted_win, font=('Microsoft JhengHei', 10), width=40)
Ted_et7.pack()

Ted_lb8 = Label(Ted_win, text="Session public key", font=('Microsoft JhengHei', 10))
Ted_lb8.pack()
Ted_et8 = Entry(Ted_win, font=('Microsoft JhengHei', 10), width=40)
Ted_et8.pack()

Ted_lb9 = Label(Ted_win, text="verify", font=('Microsoft JhengHei', 10))
Ted_lb9.pack()
Ted_et9 = Entry(Ted_win, font=('Microsoft JhengHei', 10), width=40)
Ted_et9.pack()

Ted_bt1 = Button(Ted_win, text="send request", command=step1)
Ted_bt1.pack()
Ted_bt2 = Button(Ted_win, text="verify", command=step4)
Ted_bt2.pack()


Karen_win = Tk()
Karen_win.title("Karen")
Karen_win.geometry("400x600")

Karen_lb1 = Label(Karen_win, text="private key", font=('Microsoft JhengHei', 10))
Karen_lb1.pack()
Karen_et1 = Entry(Karen_win, font=('Microsoft JhengHei', 10), width=40)
Karen_et1.insert(END, Karen_private)
Karen_et1.pack()

Karen_lb2 = Label(Karen_win, text="public key", font=('Microsoft JhengHei', 10))
Karen_lb2.pack()
Karen_et2 = Entry(Karen_win, font=('Microsoft JhengHei', 10), width=40)
Karen_et2.insert(END, Karen_public)
Karen_et2.pack()

Karen_lb3 = Label(Karen_win, text="Ted_enonce", font=('Microsoft JhengHei', 10))
Karen_lb3.pack()
Karen_et3 = Entry(Karen_win, font=('Microsoft JhengHei', 10), width=40)
Karen_et3.pack()

Karen_lb4 = Label(Karen_win, text="nonce", font=('Microsoft JhengHei', 10))
Karen_lb4.pack()
Karen_et4 = Entry(Karen_win, font=('Microsoft JhengHei', 10), width=40)
Karen_et4.pack()

Karen_lb5 = Label(Karen_win, text="enonce", font=('Microsoft JhengHei', 10))
Karen_lb5.pack()
Karen_et5 = Entry(Karen_win, font=('Microsoft JhengHei', 10), width=40)
Karen_et5.pack()

Karen_lb6 = Label(Karen_win, text="dnonce", font=('Microsoft JhengHei', 10))
Karen_lb6.pack()
Karen_et6 = Entry(Karen_win, font=('Microsoft JhengHei', 10), width=40)
Karen_et6.pack()

Karen_lb7 = Label(Karen_win, text="signatrue", font=('Microsoft JhengHei', 10))
Karen_lb7.pack()
Karen_et7 = Entry(Karen_win, font=('Microsoft JhengHei', 10), width=40)
Karen_et7.pack()

Karen_lb8 = Label(Karen_win, text="Session private key", font=('Microsoft JhengHei', 10))
Karen_lb8.pack()
Karen_et8 = Entry(Karen_win, font=('Microsoft JhengHei', 10), width=40)
Karen_et8.pack()

Karen_lb9 = Label(Karen_win, text="Session public key", font=('Microsoft JhengHei', 10))
Karen_lb9.pack()
Karen_et9 = Entry(Karen_win, font=('Microsoft JhengHei', 10), width=40)
Karen_et9.pack()

Karen_lb10 = Label(Karen_win, text="verify", font=('Microsoft JhengHei', 10))
Karen_lb10.pack()
Karen_et10 = Entry(Karen_win, font=('Microsoft JhengHei', 10), width=40)
Karen_et10.pack()

Karen_bt1 = Button(Karen_win, text="send request", command=step2)
Karen_bt1.pack()
Karen_bt2 = Button(Karen_win, text="verify", command=step4_2)
Karen_bt2.pack()


KDC_win = Tk()
KDC_win.title("KDC")
KDC_win.geometry("400x600")

KDC_lb1 = Label(KDC_win, text="Ted private key", font=('Microsoft JhengHei', 10))
KDC_lb1.pack()
KDC_et1 = Entry(KDC_win, font=('Microsoft JhengHei', 10), width=40)
KDC_et1.insert(END, Ted_private)
KDC_et1.pack()

KDC_lb2 = Label(KDC_win, text="Ted public key", font=('Microsoft JhengHei', 10))
KDC_lb2.pack()
KDC_et2 = Entry(KDC_win, font=('Microsoft JhengHei', 10), width=40)
KDC_et2.insert(END, Ted_public)
KDC_et2.pack()

KDC_lb3 = Label(KDC_win, text="Karen private key", font=('Microsoft JhengHei', 10))
KDC_lb3.pack()
KDC_et3 = Entry(KDC_win, font=('Microsoft JhengHei', 10), width=40)
KDC_et3.insert(END, Karen_private)
KDC_et3.pack()

KDC_lb4 = Label(KDC_win, text="Karen public key", font=('Microsoft JhengHei', 10))
KDC_lb4.pack()
KDC_et4 = Entry(KDC_win, font=('Microsoft JhengHei', 10), width=40)
KDC_et4.insert(END, Karen_public)
KDC_et4.pack()

KDC_lb5 = Label(KDC_win, text="Ted_enonce", font=('Microsoft JhengHei', 10))
KDC_lb5.pack()
KDC_et5 = Entry(KDC_win, font=('Microsoft JhengHei', 10), width=40)
KDC_et5.pack()

KDC_lb6 = Label(KDC_win, text="Karen_enonce", font=('Microsoft JhengHei', 10))
KDC_lb6.pack()
KDC_et6 = Entry(KDC_win, font=('Microsoft JhengHei', 10), width=40)
KDC_et6.pack()

KDC_lb7 = Label(KDC_win, text="Ted_nonce", font=('Microsoft JhengHei', 10))
KDC_lb7.pack()
KDC_et7 = Entry(KDC_win, font=('Microsoft JhengHei', 10), width=40)
KDC_et7.pack()

KDC_lb8 = Label(KDC_win, text="Karen_nonce", font=('Microsoft JhengHei', 10))
KDC_lb8.pack()
KDC_et8 = Entry(KDC_win, font=('Microsoft JhengHei', 10), width=40)
KDC_et8.pack()

KDC_lb9 = Label(KDC_win, text="Session private key", font=('Microsoft JhengHei', 10))
KDC_lb9.pack()
KDC_et9 = Entry(KDC_win, font=('Microsoft JhengHei', 10), width=40)
KDC_et9.pack()

KDC_lb10 = Label(KDC_win, text="Session public key", font=('Microsoft JhengHei', 10))
KDC_lb10.pack()
KDC_et10 = Entry(KDC_win, font=('Microsoft JhengHei', 10), width=40)
KDC_et10.pack()

KDC_lb11 = Label(KDC_win, text="Ted signature", font=('Microsoft JhengHei', 10))
KDC_lb11.pack()
KDC_et11 = Entry(KDC_win, font=('Microsoft JhengHei', 10), width=40)
KDC_et11.pack()

KDC_lb12 = Label(KDC_win, text="Karen signature", font=('Microsoft JhengHei', 10))
KDC_lb12.pack()
KDC_et12 = Entry(KDC_win, font=('Microsoft JhengHei', 10), width=40)
KDC_et12.pack()

KDC_bt1 = Button(KDC_win, text="send response", command=step3)
KDC_bt1.pack()

Ted_win.mainloop()
#Karen_win.mainloop()

