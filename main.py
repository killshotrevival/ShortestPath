import pygame
from support import *
import time
#import tracemalloc

"""tracemalloc.start()
my_complex_analysis_method()
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
tracemalloc.stop()"""

#from pympler import muppy, summary
"""
all_objects = muppy.get_objects()
sum1 = summary.summarize(all_objects)"""




if __name__=='__main__':
	
	#tracemalloc.start()
	pygame.init()


	window_width = 1200
	window_height = 600
	top_bar_line_width = 4
	clock = pygame.time.Clock()
	start_assign = False
	finish_assign = False
	objects_assign = False
	box_created = False
	path_found = False
	path_through_box = False
	textfont = 'showcardgothic' #'tempussansitc'
	status = 'None'
	total_distance = 0
	start_button_string = '/* Click at a point to place the start flag */'
	finish_button_string = '/* Click at a point to place the finish flag */ '
	object_button_string = '/* Click at two points to create an object */ '
	clear_button_string = '/* Clearing whole screen */ '
	distance_button_string = '/* Click on multiple points to calculate the total distance travelled */ '
	quit_string = '/* press "q" to quit the process */'
	box_button_string = '/* Click on two diagonal points to create a solid object */'







	display_window = window(window_width,window_height,'Shortest Path')
	colour = color()

	display = display_window.create_window()

	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				#tracemalloc.stop()
				#summary.print_(sum1)
				pygame.quit
				quit()

		#current, peak = tracemalloc.get_traced_memory()
		#print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
		#all_objects = muppy.get_objects()
		#um1 = summary.summarize(all_objects)

		display.fill(colour.Color('whitesmoke'))

		#top bar
		pygame.draw.line(display,colour.Color('black'),(0,70),(1200,70),top_bar_line_width)

		#button__init__(msg, button_x, button_y, button_width, button_height, inactive_color, active_color, textfont, text_size, text_color action)
		start_button = button('SP',50, 12, 50, 50,colour.Color('black'),colour.Color('start_button_active'),
									 textfont,25, colour.Color('white'), colour.Color('black') )
		finish_button = button('FP',120, 12, 50, 50,colour.Color('black'),colour.Color('start_button_active'),
									 textfont,25, colour.Color('white'), colour.Color('black'))
		object_button = button('Object',190, 12, 130, 50,colour.Color('black'),colour.Color('start_button_active'),
									 textfont,25, colour.Color('white'), colour.Color('black') )
		box_button = 	button('Box',340, 12, 60, 50,colour.Color('black'),colour.Color('start_button_active'),
									 textfont,25, colour.Color('white'), colour.Color('black') )
		clear_button = button('Clear',420, 12, 130, 50,colour.Color('black'),colour.Color('start_button_active'),
									 textfont,25, colour.Color('white'), colour.Color('black'))
		startdis_button = button('Start',570, 12, 110, 50,colour.Color('black'),colour.Color('start_button_active'),
									 textfont,25, colour.Color('white'), colour.Color('black'))
		selector_button = button('Distance',700, 12, 150, 50,colour.Color('black'),colour.Color('start_button_active'),
									 textfont,25, colour.Color('white'), colour.Color('black'))
		
#################################################### Start Object ##########################################################################		
		sb = start_button.draw(display)
		if sb:
			while True:
				clicked = False
				for event in pygame.event.get():
					if event.type==pygame.MOUSEBUTTONDOWN:
						if event.button==1:
							mouse = pygame.mouse.get_pos()
							clicked = True
					elif event.type == pygame.QUIT:
						pygame.quit
						quit()

				msg1 = message(start_button_string, 20, 96, window_width//2,colour.Color('info'),'microsoftnewtailue' )
				m = msg1.message_display(display,1)
				pygame.display.update(m)

				if clicked:
					break
			#start.__init__(self,x,y,radius,color)
			if mouse[1]<=70:
				y=90 #70+20
			else:
				y=mouse[1]
			start_object = start_end(mouse[0],y,15,colour.Color('green'), colour.Color('grey'))
			start_assign = True

#################################################### Finish Object ##########################################################################		

		fb = finish_button.draw(display)
		if fb:
			while True:
				clicked = False
				for event in pygame.event.get():
					if event.type==pygame.MOUSEBUTTONDOWN:
						if event.button==1:
							mouse = pygame.mouse.get_pos()
							clicked = True
					elif event.type == pygame.QUIT:
						pygame.quit
						quit()
				if clicked:
					break
				msg1 = message(finish_button_string, 20, 96, window_width//2,colour.Color('info'),'microsoftnewtailue' )
				m = msg1.message_display(display,1)
				pygame.display.update(m)

			#start.__init__(self,x,y,radius,color)
			if mouse[1]<=70:
				y =90 #70+20
			else:
				y=mouse[1]
			finish_object = start_end(mouse[0],y,15,colour.Color('green'), colour.Color('grey'))
			finish_assign = True

#################################################### Line Object ##########################################################################		


		ob = object_button.draw(display)
		if ob :
			while True:
				clicked = False
				for event in pygame.event.get():
					if event.type==pygame.MOUSEBUTTONDOWN:
						if event.button==1:
							mouse = pygame.mouse.get_pos()
							clicked = True
					elif event.type == pygame.QUIT:
						pygame.quit
						quit()
				if clicked:
					break
				msg1 = message(object_button_string, 20, 96, window_width//2,colour.Color('info'),'microsoftnewtailue' )
				m = msg1.message_display(display,1)
				pygame.display.update(m)
			if mouse[1]<=70:
				y =73
			else:
				y=mouse[1]		
			first = (mouse[0],y)

			while True:
				clicked = False
				for event in pygame.event.get():
					if event.type==pygame.MOUSEBUTTONDOWN:
						if event.button==1:
							mouse = pygame.mouse.get_pos()
							clicked = True
					elif event.type == pygame.QUIT:
						pygame.quit
						quit()
				if clicked:
					break
				msg1 = message(object_button_string, 20, 96, window_width//2,colour.Color('info'),'microsoftnewtailue' )
				m = msg1.message_display(display,1)
				pygame.display.update(m)
			if mouse[1]<=70:
				y =73
			else:
				y=mouse[1]
			second = (mouse[0],y)

			#objects.__init__(self, first_point, sec_point, color , width)
			objects_object = objects(first,second,colour.Color('black'), 3)
			objects_assign = True

#################################################### Box Object ##########################################################################		

		bb = box_button.draw(display)
		if bb:
			while True:
				clicked2 = False
				box_cord = [0,0]
				box_width = 0
				box_height = 0
				for event in pygame.event.get():
					if event.type==pygame.QUIT:
						pygame.quit
						quit()
					elif event.type == pygame.MOUSEBUTTONDOWN:
						if event.button == 1:
							box_first = pygame.mouse.get_pos()

							while True:
								clicked = False

								for event2 in pygame.event.get():
									if event2.type == pygame.MOUSEBUTTONDOWN:
										if event2.button ==1:
											box_sec = pygame.mouse.get_pos()
											# box__init__(self, first_tuple, sec_tuple, color) 
											clicked = True
											clicked2 = True
								b1 = pygame.draw.rect(display,colour.Color('whitesmoke'),(box_cord[0],box_cord[1],box_width,box_height))
								#print('box_cord',box_cord)
								#b1 = pygame.draw.rect(display,(255,0,0),(100,100,100,100))
								#print('clear')

								box_sec = pygame.mouse.get_pos()

								if box_first[0]<box_sec[0] and box_first[1]>box_sec[1]:
									box_cord = [box_first[0],box_sec[1]]

								elif box_first[0]<box_sec[0] and box_first[1]<box_sec[1]:
									box_cord = [box_first[0],box_first[1]]

								elif box_first[0]>box_sec[0] and box_first[1]>box_sec[1]:
									box_cord = [box_sec[0],box_sec[1]]

								elif box_first[0]>box_sec[0] and box_first[1]<box_sec[1]:
									box_cord = [box_sec[0],box_first[1]]

								if box_cord[1]<=70:
									box_cord[1] = 75

								box_width = abs(box_first[0]-box_sec[0])
								box_height = abs(box_first[1]-box_sec[1])

								b = pygame.draw.rect(display,(0,0,0),(box_cord[0],box_cord[1],box_width,box_height))
								pygame.display.update([b,b1])

								if clicked:
									break
				if clicked2:
					box_object = box(box_cord,[box_cord[0]+box_width, box_cord[1]+box_height],colour.Color('black'))
					box_created = True
					break
				msg1 = message(box_button_string, 20, 96, window_width//2,colour.Color('info'),'microsoftnewtailue' )
				m = msg1.message_display(display,1)
				pygame.display.update(m)




#################################################### Clear Object ##########################################################################		


		cb = clear_button.draw(display)
		if cb:
			if objects_assign:
				objects_object.clear_object()
			start_assign = False
			finish_assign = False
			objects_assign = False
			path_found = False
			path_through_box = False
			status ='None'
			if path_found:
				shortest_path.final_list.clear()
			if box_created:
				box_object.box_obj.clear()
			msg1 = message(start_button_string, 20, 96, window_width//2,colour.Color('info'),'microsoftnewtailue' )
			m = msg1.message_display(display,1)
			pygame.display.update(m)
			time.sleep(1)
			continue

#################################################### Start Calculating Object ##########################################################################		

		sdb = startdis_button.draw(display)
		if sdb:
			#main_path__init__(self,startpoint,endpoint,objects,color, width)
			shortest_path = main_path((start_object.x,start_object.y),(finish_object.x,finish_object.y),(255,0,0),4)
			#print('Object created')
			shortest_path.final_list.append(shortest_path.startpoint)
			#if box_created:
			shortest_path.find2(shortest_path.startpoint,shortest_path.endpoint, box.box_obj, objects.obj)
			path_through_box = True
			shortest_path.final_list.append(shortest_path.endpoint)


#################################################### Distance Object ##########################################################################		

		sb = selector_button.draw(display)
		if sb:
			while True:
				clicked = False
				for event in pygame.event.get():
					if event.type==pygame.QUIT:
						pygame.quit
						quit()
					elif event.type == pygame.MOUSEBUTTONDOWN:
						if event.button == 1:
							mouse = pygame.mouse.get_pos()
							diss = distance_travelled(mouse)
							total = diss.draw()
							#print('total', total)
							#m2= pygame.Rect(35,80,100,100)
							m1 = pygame.draw.rect(display,colour.Color('whitesmoke'),(900,15,180,45))
							#pygame.display.update(m)

							msg = message(str(total), 15, 35,1001 ,colour.Color('black'), 'copperplategothic' )
							m = msg.message_display(display,1)
							pygame.display.update([m1,m])
							
					elif event.type ==pygame.KEYDOWN:
						if event.key == pygame.K_q:
							distance_travelled.dis_list.clear()
							clicked = True
				if clicked:
					break
				msg1 = message(distance_button_string, 15, 96, window_width//2,colour.Color('info'),'microsoftnewtailue' )
				m1 = msg1.message_display(display,1)
				#pygame.display.update(m)

				msg1 = message(quit_string, 15, 110, window_width//2,colour.Color('info'),'microsoftnewtailue' )
				m = msg1.message_display(display,1)
				pygame.display.update([m1,m])
		
#################################################### Displaying All Objects ##########################################################################		


		if start_assign:
			start_object.draw(display)

		if finish_assign:
			finish_object.draw(display)

		if objects_assign:
			objects_object.draw(display)
		if box_created:
			box_object.draw(display)
		if path_through_box:
			shortest_path.draw(display)

#################################################### Displaying total distance traveled box ##########################################################################		

		#empty_rect.__init__(self,x,y,z,w,width,color)
		distance_display = empty_rect((870,12),(1132,12),(1132,62),(870,62),3,colour.Color('black'))
		distance_display.draw(display)

		msg = message('Distance traveled', 15, 35,1000 ,colour.Color('black'), 'copperplategothic' )
		msg.message_display(display)

		

		pygame.display.update()

		clock.tick(60)
