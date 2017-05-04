# curl -O -L ftp://ftp.cyrusimap.org/cyrus-sasl/cyrus-sasl-2.1.26.tar.gz
# tar xzf cyrus-sasl-2.1.26.tar.gz
# cd cyrus-sasl-2.1.26
# sudo ./configure && sudo make install
 
# sudo pip install sasl
# sudo pip install pyhive
# sudo pip install pycrypto

import sys
from pyhive import hive
from Crypto.Cipher import AES
import base64


encrypter = AES.new('<16 char key>', AES.MODE_CBC, '<16 char IV>')

conn = hive.Connection(host = "<host>", port = 10000, username = "<user>")

cursor = conn.cursor()
cursor.execute("Select * from <table>")

inserter = conn.cursor()

for result in cursor.fetchall():
	print('id is ' + str(result[0]))
	encrypted_ssn = encrypter.encrypt(result[1]+'xxxxx') #padding
	print(encrypted_ssn)
	print('^ encrypted ssn')
	encoded = base64.b64encode(encrypted_ssn)
	print(encoded)
	print('^ encoded encrypted ssn')
	ins_statement = "Insert into table <table> values (" + str( result[0]) + " ,'" + encoded + "')"
        inserter.execute(ins_statement) 
