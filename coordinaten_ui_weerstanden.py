# canvas coordinaten
canvas_x = 0 
canvas_grote_x = 1300
canvas_x_end = canvas_x + canvas_grote_x
canvas_y = 0
canvas_grote_y = 700
canvas_y_end = canvas_y + canvas_grote_y

knop_grote_y = 25
# reset_knop,plus_knop,min_knop
reset_knop_y = (canvas_y_end - 4*knop_grote_y)/2
reset_knop_x = canvas_x_end + 20
reset_knop_size_y = knop_grote_y
reset_knop_size_x = 90
reset_knop_y_end = reset_knop_y + reset_knop_size_y
reset_knop_x_end = reset_knop_x + reset_knop_size_x

plus_knop_y = (canvas_y_end - 4*knop_grote_y)/2 + knop_grote_y
plus_knop_x = canvas_x_end + 20
plus_knop_size_y = knop_grote_y
plus_knop_size_x = 90/2
plus_knop_y_end = plus_knop_y + plus_knop_size_y
plus_knop_x_end = plus_knop_x + plus_knop_size_x

min_knop_y = (canvas_y_end - 4*knop_grote_y)/2 + knop_grote_y
min_knop_x = canvas_x_end + 20 + 90/2
min_knop_size_y = knop_grote_y
min_knop_size_x = 90/2
min_knop_y_end = min_knop_y + min_knop_size_y
min_knop_x_end = min_knop_x + min_knop_size_x

serie_knop_y = (canvas_y_end - 4*knop_grote_y)/2 + 2*knop_grote_y
serie_knop_x = canvas_x_end + 20
serie_knop_size_y = knop_grote_y
serie_knop_size_x = 90/2
serie_knop_y_end = plus_knop_y + serie_knop_size_y
serie_knop_x_end = plus_knop_x + serie_knop_size_x

parralel_knop_y = (canvas_y_end - 4*knop_grote_y)/2 + 2*knop_grote_y
parralel_knop_x = canvas_x_end + 20 + 90/2
parralel_knop_size_y = knop_grote_y
parralel_knop_size_x = 90/2
parralel_knop_y_end = min_knop_y + parralel_knop_size_y
parralel_knop_x_end = min_knop_x + parralel_knop_size_x


# BRON:




bron_input_box_x = canvas_x_end + 20 
bron_input_box_eind_x = bron_input_box_x + 200
bron_input_box_y = 700
bron_input_box_eind_y = bron_input_box_y + 75
bron_input_breete_x = 200
bron_input_breete_y = 75 + 35
bron_inputvelden_grote_y =  bron_input_breete_y/3

bron_R_input_x = bron_input_box_x  + 50
bron_R_input_eind_x = bron_input_box_eind_x
bron_R_input_y = bron_input_box_y + 10
bron_R_input_eind_y = bron_input_box_y + bron_inputvelden_grote_y 

bron_U_input_x = bron_input_box_x  + 50
bron_U_input_eind = bron_input_box_eind_x 
bron_U_input_y = bron_input_box_y + bron_inputvelden_grote_y + 10
bron_U_input_eind_y = bron_input_box_y + 2 * bron_inputvelden_grote_y

bron_I_input_x = bron_input_box_x + 50
bron_I_input_eind = bron_input_box_eind_x
bron_I_input_y = bron_input_box_y + 2 * bron_inputvelden_grote_y + 10
bron_I_input_eind_y = bron_input_box_y + 3 * bron_inputvelden_grote_y

bron_R_text_x = bron_input_box_x + 20
bron_R_text_y = bron_R_input_y

bron_U_text_x = bron_input_box_x + 20
bron_U_text_y = bron_U_input_y

bron_I_text_x = bron_input_box_x + 20
bron_I_text_y = bron_I_input_y



    
#input boxes
input_box_x = canvas_x_end + 20 
input_box_eind_x = input_box_x + 200
input_box_y = 100
input_box_eind_y = input_box_y + 75
input_breete_x = 200
input_breete_y = 75 + 35

inputvelden_grote_y =  input_breete_y/3
R_input_x = input_box_x  + 50
R_input_eind_x = input_box_eind_x
R_input_y = input_box_y + 10
R_input_eind_y = input_box_y + inputvelden_grote_y 

U_input_x = input_box_x  + 50
U_input_eind = input_box_eind_x 
U_input_y = input_box_y + inputvelden_grote_y + 10
U_input_eind_y = input_box_y + 2 * inputvelden_grote_y

I_input_x = input_box_x + 50
I_input_eind = input_box_eind_x
I_input_y = input_box_y + 2 * inputvelden_grote_y + 10
I_input_eind_y = input_box_y + 3 * inputvelden_grote_y

R_text_x = input_box_x + 20
R_text_y = R_input_y

U_text_x = input_box_x + 20
U_text_y = U_input_y

I_text_x = input_box_x + 20
I_text_y = I_input_y

binden_x = canvas_grote_x / 2
binden_y = canvas_grote_y 