#char_array= ['b','i','r','d']
#a=''.join(char_array)
#print(a)

class CaesarCipher():
	''' Replace each character with (i+r)%26th alphabet'''
	def __init__(self,shift):
			encoder=[None]*26
			decoder=[None]*26
			for k in range(26):
				encoder[k]=chr(ord('A')+((shift+k)%26))
				decoder[k]=chr(ord('A')+((k-shift)%26))
			self._forward=''.join(encoder)
			self._backward=''.join(decoder)
	def encrypt(self,message):
		return self._transform(message,self._forward)
	def decrypt(self,secret):
		return self._transform(secret,self._backward)

	def _transform(self,original,code):
		msg=list(original)
		for k in range(len(msg)):
			if msg[k].isupper():
				j=ord(msg[k])-ord('A')
				msg[k]=code[j]

		return ''.join(msg)

if __name__== '__main__':
	cipher=CaesarCipher(5)
	message= "Hey, I AM READY . MEET ME NEAR THE HOSTEL"
	coded=cipher.encrypt(message)
	print("Secret : ",coded)
	answer=cipher.decrypt(coded)
	print("message : ",answer)

