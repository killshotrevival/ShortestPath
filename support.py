import pygame
import math
import time

pygame.init()

class window:
	def __init__(self, width, height, name):
		self.window_width = width
		self.window_height = height
		self.name = name

	def create_window(self):
		#display = pygame.display.set_mode((self.window_width,self.window_height))
		pygame.display.set_caption(self.name)
		#pygame.display.set_caption('Chris-Cross')

		return pygame.display.set_mode((self.window_width,self.window_height))




class color:
	colors = {
	'red': (255,0,0),
	'black': (0,0,0),
	'white': (255,255,255),
	'green' : (0,255,0),
	'blue' : (0,0,255),
	'grey' : (119,136,1,53),
	'burlywood' : (222,184,135),
	'whitesmoke' : (245,245,245),
	'azure' : (240,255,255),
	'light_yellow' : (255,255,51),
	'start_button_active' : (222, 222, 220),
	'info' : (195, 193, 193)
	}

	def Color(self,string):
		return self.colors[string]


class button:
	def __init__(self,msg, button_x, button_y, button_width, button_height, inactive_color, active_color, textfont, text_size, inactive_text_color, active_text_color): #action):
		self.msg = msg
		self.x = button_x
		self.y = button_y
		self.width = button_width
		self.height = button_height
		self.inactive_color = inactive_color
		self.active_color = active_color
		#self.action = action
		self.text_font = textfont
		self.text_size = text_size
		self.inactive_text_color = inactive_text_color
		self.active_text_color = active_text_color


	def draw(self,gameDisplay):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		if self.x+self.width>mouse[0]>self.x and self.y+self.height>mouse[1]>self.y:
			pygame.draw.rect(gameDisplay,self.active_color,(self.x, self.y, self.width, self.height))
			msg = message(self.msg, self.text_size, int((self.y+(self.height/2))), int((self.x+(self.width/2))), self.active_text_color, self.text_font)
			msg.message_display(gameDisplay)
			if click[0]==1:
				#action()
				return True
		else:
			pygame.draw.rect(gameDisplay,self.inactive_color,(self.x, self.y, self.width, self.height))

			msg = message(self.msg, self.text_size, int((self.y+(self.height/2))), int((self.x+(self.width/2))), self.inactive_text_color, self.text_font)

			msg.message_display(gameDisplay)


class message:
	def __init__(self,text, size, x,y , color, font):
		self.text = text
		self.size = size
		self.x = x
		self.y = y
		self.color = color
		self.font = font


	def text_objects(self,text_font):
		#font = pygame.font.Font('freesansbold.ttf', 32) 
		text_surface = text_font.render(self.text, True, self.color)
		return text_surface, text_surface.get_rect()


	def text_prop(self):
		return pygame.font.SysFont(self.font,self.size)


	def message_display(self, gameDisplay, alone=None):
		text_font = self.text_prop()
		text_surface,text_rect = self.text_objects(text_font)
		text_rect.center = (self.y,self.x)
		gameDisplay.blit(text_surface,text_rect)
		if alone:
			return text_rect


class empty_rect:
	def __init__(self,x,y,z,w,width,color):
		self.x = x
		self.y = y
		self.z = z
		self.w = w
		self.width = width
		self.color = color

	def draw(self,gameDisplay):
		pygame.draw.line(gameDisplay, self.color, self.x,self.y,self.width)
		pygame.draw.line(gameDisplay, self.color, self.y,self.z,self.width)
		pygame.draw.line(gameDisplay, self.color, self.z,self.w,self.width)
		pygame.draw.line(gameDisplay, self.color, self.w,self.x,self.width)
		



class start_end:
	def __init__(self,x,y,radius,color,inner_color):	
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.inner_color = inner_color
	def draw(self,display):
		pygame.draw.circle(display,self.color, (self.x,self.y),self.radius)
		#print('Inside draw')
		pygame.draw.circle(display,self.inner_color,(self.x,self.y),self.radius-9)



class objects:
	obj = []
	def __init__(self, first_point, sec_point, color , width):
		#self.first_point = first_point
		#self.sec_point = sec_point
		#self.color = color
		#self. width = width
		objects.obj.append((first_point,sec_point,color,width))

	def draw(self,display):
		for s in objects.obj:
			pygame.draw.line(display, s[2], s[0], s[1], s[3])
	def clear_object(self):
		objects.obj.clear()


class box:
	box_obj = []
	def __init__(self, first_tuple, sec_tuple, color):
		box.box_obj.append((first_tuple,sec_tuple,color))

	def draw(self,display):
		for s in box.box_obj:
			#print('s',s)
			box_sec = s[1]
			box_first = s[0]

			pygame.draw.rect(display,(0,0,0),(box_first[0],box_first[1],box_sec[0]-box_first[0],box_sec[1]-box_first[1]))

	def clear_object(self):
		objects.obj.clear()


class main_path:
	def __init__(self,startpoint,endpoint,color, width):
		self.startpoint = startpoint
		self.endpoint = endpoint
		self.color = color
		self.width = width
		self.final_list = []

		

	def dist(self,A,B):
		return math.sqrt(((B[1]-A[1])**2)+((B[0]-A[0])**2))

	def equ_solver(self,tuple1,tuple2):
		x = (tuple2[1]-tuple1[1])/(tuple1[0]-tuple2[0])
		y = (tuple1[0]*x)+tuple1[1]
		return (x,y)

	def equi_solver_evolved(self,line_1,line_2):
		if (line_1[1][0]-line_1[0][0])==0 and line_2[1][0]-line_2[0][0]!=0:
			x=line_1[1][0]
			m2 = (line_2[1][1]-line_2[0][1])/(line_2[1][0]-line_2[0][0])
			b2 = line_2[0][1]-(line_2[0][0]*m2)
			y = (m2*x)+b2

			return(x,y)

		if line_2[1][0]-line_2[0][0]==0 and line_1[1][0]-line_1[0][0]!=0:
			x = line_2[1][0]
			m1 = (line_1[1][1]-line_1[0][1])/(line_1[1][0]-line_1[0][0])
			b1 = line_1[0][1]-(line_1[0][0]*m1)
			y = (m1*x)+b1

			return(x,y)

		if line_2[1][0]-line_2[0][0]!=0 and line_1[1][0]-line_1[0][0]!=0:
            #print('Not Equal')
			m1 = (line_1[1][1]-line_1[0][1])/(line_1[1][0]-line_1[0][0])
			m2 = (line_2[1][1]-line_2[0][1])/(line_2[1][0]-line_2[0][0])
			a1 = m1
			b1 = line_1[0][1]-(line_1[0][0]*m1)

			a2 = m2
			b2 = line_2[0][1]-(line_2[0][0]*m2)

            #equ_solver(tuple1,tuple2)
			return self.equ_solver((a1,b1),(a2,b2))


	def satisfy(self,line_cord1, line_cord2, tuple1, line_cord11, line_cord12):
		if min(line_cord1[0],line_cord2[0])<tuple1[0]<max(line_cord2[0],line_cord1[0]) and min(line_cord1[1],line_cord2[1])<tuple1[1]<max(line_cord2[1],line_cord1[1]):
			if min(line_cord11[0],line_cord12[0])<tuple1[0]<max(line_cord12[0],line_cord11[0]) and min(line_cord11[1],line_cord12[1])<tuple1[1]<max(line_cord12[1],line_cord11[1]):
				return True
		else:
			return False

	def lies_on_line(self,temp_,tuple1):
		crossed = []
		for line in temp_:
			line_cord1 = line[0]
			line_cord2 = line[1]
			if min(line_cord1[0],line_cord2[0])<=tuple1[0]<=max(line_cord2[0],line_cord1[0]) and min(line_cord1[1],line_cord2[1])<=tuple1[1]<=max(line_cord2[1],line_cord1[1]):
				crossed.append(line[0])
				crossed.append(line[1])
		return crossed

	def satisfy_evolved(self,line_cord1, line_cord2, tuple1, line_cord11, line_cord12):
		if line_cord11[0]==line_cord12[0]==tuple1[0]:
			if min(line_cord1[1],line_cord2[1])<tuple1[1]<max(line_cord2[1],line_cord1[1]):
				if min(line_cord11[1],line_cord12[1])<tuple1[1]<max(line_cord12[1],line_cord11[1]):
					return True
		elif min(line_cord1[0],line_cord2[0])<tuple1[0]<max(line_cord2[0],line_cord1[0]) and min(line_cord1[1],line_cord2[1])<tuple1[1]<max(line_cord2[1],line_cord1[1]):
			if min(line_cord11[0],line_cord12[0])<tuple1[0]<max(line_cord12[0],line_cord11[0]) and min(line_cord11[1],line_cord12[1])<tuple1[1]<max(line_cord12[1],line_cord11[1]):
				return True

		return False

	def find2(self,point,endpoint, box_objects, line_objects):
		_obj = self.all_objects(point,endpoint, box_objects, line_objects)
		#print('final_list',self.final_list)
		#print('obj',_obj)
		if _obj:
			if _obj[3]==1:
				x = _obj[0][0]
				y = _obj[0][1]
				z = _obj[2][0]
				w = _obj[2][1]
				temp_ = [[[x,y],[x,w]],[[x,y],[z,y]],[[x,w],[z,w]],[[z,y],[z,w]]]
				crossed = self.lies_on_line(temp_,point)
				#print('crossed',crossed)
				if len(crossed)!=0:
					#print('crossed',crossed)
					temp_dis = 1200
					temp_point = []
					for i in crossed:
						dis = self.dist(i,endpoint)
						if dis<temp_dis:
							temp_dis=dis
							temp_point = i
					self.final_list.append(temp_point)
				else:
					x_mid = x+(z-x)/2
					y_mid = y+(w-y)/2
					line2 = [(x_mid,y_mid),point]
					#print('line2',line2)
					for line in temp_:
						crossing_point = self.equi_solver_evolved(line2,line)
						#print('line',line)
						#print('crossing_point',crossing_point)
						if self.satisfy_evolved(line2[0],line2[1],crossing_point,line[0],line[1]):
							#print('line[0]',line[0])
							#print('line[1]',line[1])
							dis0 = self.dist(point,line[0])
							dis1 = self.dist(point,line[1])

							temp_point = line[1] if dis1<dis0 else line[0]

							self.final_list.append(temp_point)

				self.find2(temp_point,endpoint,box_objects,line_objects)

			elif _obj[3]==0:
				line = [_obj[0],_obj[2]]
				dis0 = self.dist(point,line[0])
				dis1 = self.dist(point,line[1])
				temp_point = line[1] if dis1<=dis0 else line[0]
				#print('Temp execute',temp_point)
				self.final_list.append(temp_point)
			self.find2(temp_point,endpoint,box_objects,line_objects)



	def all_objects(self,point,end_point, box_objects, line_objects):
		objects = []

		for obj in box_objects:
			x = obj[0][0]
			y = obj[0][1]
			z = obj[1][0]
			w = obj[1][1]

			x_mid = x+(z-x)/2
			y_mid = y+(w-y)/2

			tuple1 = self.equi_solver_evolved([(x,y),(z,w)],[point,end_point])
			tuple2 = self.equi_solver_evolved([(z,y),(x,w)],[point,end_point])

			if self.satisfy_evolved((x,y),(z,w),tuple1,point,end_point) or self.satisfy_evolved((z,y),(x,w),tuple2,point,end_point):
				distance = self.dist(point,(x_mid,y_mid))
				objects.append([obj[0],distance,obj[1],1])
		for obj in line_objects:
			tuple1 = self.equi_solver_evolved((obj[0],obj[1]),[point,end_point])
			if self.satisfy_evolved(obj[0],obj[1],tuple1,point,end_point):
				x = obj[0][0]
				y = obj[0][1]
				z = obj[1][0]
				w = obj[1][1]

				x_mid = x+(z-x)/2
				y_mid = y+(w-y)/2
				distance = self.dist(point,(x_mid,y_mid))
				objects.append([obj[0],distance,obj[1],0])
		objects.sort(key=lambda x:x[1])
		if len(objects)!=0:
			return objects[0]
		else:
			return False



	def draw(self,display):
		#print('Inside draw', self.final_list)
		i = 0
		final_l = []
		while i<len(self.final_list)-1:
			if self.final_list[i] not in final_l:
				final_l.append(self.final_list[i])
				pygame.draw.line(display,self.color,self.final_list[i],self.final_list[i+1],self.width)
			i+=1
		pygame.draw.line(display,self.color,self.final_list[i-1],self.final_list[i],self.width)


class distance_travelled:
	dis_list = []
	def __init__(self,point):
		distance_travelled.dis_list.append(point)
		self.total=0

	def dist(self,A,B):
		return math.sqrt(((B[1]-A[1])**2)+((B[0]-A[0])**2))

	def draw(self):
		i = 0
		while i<len(distance_travelled.dis_list)-1:
			self.total+=self.dist(distance_travelled.dis_list[i],distance_travelled.dis_list[i+1])
			i+=1
		return round(self.total,2)
