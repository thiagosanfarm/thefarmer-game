
#loop infinito
while True:
	#rodar cada linha
	for i in range(get_world_size()):
		#rodar cada coluna 
		for j in range(get_world_size()):
			#plantar cenoura
			if get_ground_type() == Grounds.Soil:
				plant(Entities.Carrot)
			if not can_harvest():
				move(North)
			if can_harvest():
				harvest()
				if get_ground_type() != Grounds.Soil: 
					till()
				plant(Entities.Carrot)
			if get_water() < 0.2:
				use_item(Items.Water)
			move(North)
		move(East)

		
	
		
		

	
