from auxiliar_functions import sen_cos_tg
from auxiliar_functions import percentage
from auxiliar_functions import uniform_motion

total_distance = sen_cos_tg.cateto_adjacente_tangente(1, 1000) * 2
final_distance = percentage.remove_percentage(20, total_distance)
picture_time = uniform_motion.time(final_distance, 0, 50)

print(f'Result = {picture_time}s')
