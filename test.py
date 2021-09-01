
from pyTigerDriver import GSQL_Client


tgCl =GSQL_Client(server_ip="127.0.0.1",gsPort="14240", restpp="9000"
                 , username="tigergraph", password="tigergraph",debug=True
                 , version="3.1.0"
                  ,cacert="/home/med/.gsql/my-cert.txt")



print("################ GSQL  ##################")



res = tgCl.query('''
CREATE QUERY ttss () FOR GRAPH Test {
print "it works";
}
INSTALL QUERY ALL
''',graph="Test")
print(res)

