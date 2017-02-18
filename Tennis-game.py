class player:
	def __init__(self,point,game,setc,it,ball,serve):
		self.point=point
		self.game=game
		self.setc=setc
		self.it=it
		self.ball=ball
		self.serve=serve
	def point(self):
		self.point=self.point+1
class set(player):
	def pointgain(self):
		self.it+=1
		self.point=point[self.it]
		#print self.point
	def r_setc(self):
		return self.setc

	def r_point(self):
		return self.point

	def r_serve(self):
		return self.serve

	def r_it(self):
		return self.it

	def r_game(self):
		return self.game

	def r_ball(self):
		return self.ball

	def ch_setc(self):
		self.setc+=1

	def ch_game(self):
		self.game+=1

	def ch_point(self):
		self.it+=1
		self.point=point[self.it]

	def a_point(self):
		self.point=point[self.it]

	def ch_serve(self):
		#print "changing serve"
		if self.serve==1:
			self.serve=0
		else:
	       		self.serve=1

	def  ch_ball(self):
		if self.ball==1:
			self.ball=0
		else:
			self.ball=1

	def res_point(self):
		self.point=0

	def res_it(self):
		self.it=0

	def res_ball(self):
		self.ball=self.serve

	def ch_it(self):
		self.it+=1

	def dec_it(self):
		self.it=self.it-1
		
	def res_game(self):
		self.game=0
			
def winset(p1,p2):
	if p1.r_game()==6 and p2.r_game()<=4:
		#print "p1 =6"
		p1.ch_setc()
		p1.res_point()
		p2.res_point()
		p1.res_game()
		p2.res_game()
		return 1
	elif p1.r_game()>=7 and p1.r_game()-p2.r_game()>=2:
		#print "p1>7"
		p1.ch_setc()
		p1.res_point()
		p2.res_point()
		p1.ch_serve()
		p2.ch_serve()
		p1.res_game()
		p2.res_game()
		return 1
	elif p2.r_game()>=7 and p2.r_game()-p1.r_game()>=2:
		#print "p2>7"
		p2.ch_setc()
		p1.res_point()
		p2.res_point()
		p1.ch_serve()
		p2.ch_serve()
		p1.res_game()
		p2.res_game()
		return 2
	elif p2.game==6 and p1.game<=4:
		#print "p2 =6"
		p2.ch_setc()
		p1.res_point()
		p2.res_point()
		p1.ch_serve()
		p2.ch_serve()
		p1.res_game()
		p2.res_game()
		return 2
	else:
		return 0
f=0
def wingame(p1,p2,flag):
	#print p1.point,',',p2.point
	if p1.r_point() == '50' and p2.point <= '40':
		#print "player 1 won game"
		p1.res_point()
		p1.res_it()
		p2.res_point
		p2.res_it()
		p1.ch_game()
		p1.ch_serve()
		p2.ch_serve()
		p1.res_ball()
		p2.res_ball()
		#global f
		f=0
		return 1
	elif p2.r_point() == '50' and p1.r_point() < '40':
		#print "player 2 won game"
		p1.res_point()
		p1.res_it()
		p2.res_point()
		p2.res_it()
		p2.ch_game()
		p1.ch_serve()
		p2.ch_serve()
		#global f
		p1.res_ball()
		p2.res_ball()
		f=0
		return 2
	elif p1.r_point()=='40' and p2.r_point()=='40':
		if flag==0:
			p1.ch_it()
			p1.ch_it()
			p1.a_point()
			p2.ch_it()
			p2.ch_it()
			p2.a_point()
		#global f
		f=1
	elif p1.r_point()=='70' and p2.r_point()=='70':
		#print "dec"
		p1.dec_it()
		p1.a_point()
		p2.dec_it()
		p2.a_point()
		#global f
		f=0
	elif p1.r_point()=='80' and p2.r_point()=='60':
		p1.res_point()
		p1.res_it()
		p2.res_point()
		p2.res_it()
		p1.ch_game()
		#global f
		p1.ch_serve()
		p2.ch_serve()
		p1.res_ball()
		p2.res_ball()
		f=0
		return 1
	elif p2.r_point()=='80' and p1.r_point()=='60':
		p1.res_point()
		p1.res_it()
		p2.res_point()
		p2.res_it()
		p2.res_point()
		p2.ch_game()
		#global f
		f=0
		p1.ch_serve()
		p2.ch_serve()
		p1.res_ball()
		p2.res_ball()
		return 2
	else:
		#print "no one won"
		return 0
point=['0','15','30','40','50','60','70','80','90']
fault=0
i=1
p1=set(0,0,0,0,1,1)
p2=set(0,0,0,0,0,0)
import sys
file = sys.argv[1]
fi= open(file,'r')
for line in fi:
	words=line.split(' ')
	print "Iteration:",i 
	#print "Player:",words[1]
	#print "before back"
	#sys.stdout.softspace=0
	#print ':',words[1]
	#print "ball 1 = ",p1.r_ball()
	#print "ball 2 = ",p2.r_ball()
	if words[1]=="Serve\n":
		print "Serve" 
		if p1.r_ball()==1:
			#print "changing ball from 1"
			p2.ch_ball()
			p1.ch_ball()
		else:
			#print "changing ball from 2"
			p2.ch_ball()
			p1.ch_ball()
	if words[1]=="Fault\n":
		print "Fault"
		if p1.ball==1:
			p2.ch_ball()
			p1.ch_ball()
			p1.ch_point()
		else: 
			p2.ch_ball()
			p1.ch_ball()
			p2.ch_point()
	if words[1]=="Backhand\n":
		print "Backhand"
		p2.ch_ball()
		p1.ch_ball()
	if words[1]=="Forehand\n":
		print "FRONT"
		p2.ch_ball()
		p1.ch_ball()
	if words[1]=="PointLost-SameSide\n":
		print "PointLost-SameSide"
		if p1.r_ball()==1:
			p1.pointgain()
			p1.res_ball()		
			p2.res_ball()
		else:
			p2.pointgain()
			p1.res_ball()		
			p2.res_ball()
	if words[1]=="PointLost-Out\n":
		print "PointLost-Out"
		if p1.r_ball()==1:
			p1.pointgain()
			p1.res_ball()		
			p2.res_ball()
		else:
			p2.pointgain()
			p1.res_ball()		
			p2.res_ball()
	if words[1]=="PointLost-CouldNotReach\n":
		print "PointLost-CouldNotReach"
		if p1.r_ball()==1:
			p1.pointgain()
			p1.res_ball()		
			p2.res_ball()
		else:
			p2.pointgain()
			p1.res_ball()		
			p2.res_ball()
	if words[1]=="Ace\n":
		print "Ace"
		if p1.r_serve()==1:
			p1.pointgain()
			#print "ace pointgain 1 it:",p1.it
			p1.res_ball()
			p2.res_ball()
		else:
			p2.pointgain()
			#print "ace pointgain 2 it:",p2.it
			p1.res_ball()
			p2.res_ball()
			
	#print "flag:",f
	#print "1 = ",p1.r_point()
	#print "2 = ",p2.r_point()
	#print "p1.ball before:",p1.r_ball()
	#print "p2.ball before:",p2.r_ball()
	wingame(p1,p2,f)
	winset(p1,p2)
	if p1.r_point()=='40' and p2.r_point()=='40':
		print "P1 score: DUECE"
		print "P2 score: DUECE"
	elif p1.r_point()=='60' and p2.r_point()=='60':
		print "P1 score: DUECE"
		print "P2 score: DUECE"
	elif p1.r_point()=='70' and p2.r_point()=='60':
		print "P1 score: Advantage"
		print "P2 score: "
	elif p1.r_point()=='60' and p2.r_point()=='70':
		print "P1 score: "
		print "P2 score: Advantage"
	else:
		print "P1 score:",p1.r_point() 
		print "P2 score:", p2.r_point()
	print "P1 win game:",p1.r_game()
	print "P2 win game:", p2.r_game()
	print "P1 win set:", p1.r_setc()
	print "P2 win set:", p2.r_setc()
	#print "p1.ball:",p1.r_ball()
	#print "p2.ball:",p2.r_ball()
	#print "faults are",fault
	#print "p1.it:",p1.it
	#print "p2.it:",p2.it
	print "\n"
	i+=1
