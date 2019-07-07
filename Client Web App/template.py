
import sqlite3
def connect():

    conn = sqlite3.connect("./onyx.db")
    cur = conn.cursor()

    return conn, cur


def select_all_info():
    cost1=[]
    area1=[]
	conn, cur = connect()
	#cur.execute('select * from ngo')

	#data = cur.fetchall()

	cur.execute("select image_path from ngo where area=? ",(area,))
	data=cur.fetchall()
	
	cur.execute("select area from survey where area=?",(area,))
    data1=cur.fetchall()

    for r in data1:
    	for r1 in data:
    		if r==r1 or r1-r<=200:
    			cur.execute("select cost from ngo where cost=?",(cost,))
    			p=cur.fetchall()
    			cur.execute("select budget from survey where budget=?",(budget,))
    			p1=cur.fetchall()
    			for q in p1:
    				for q1 in p:
    					if q==q1 or q1-q<=10000:
                            cur.execute("select image_path,cost,area from ngo where q1==q")
                            fin=cur.fetcahll()
                            for r in fin:
								print(r)

								return fin
    conn.commit()
	conn.close()