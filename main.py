import services
import argparse
from modules import circle_function
	
@circle_function
def main(number: int):
	try:
		services.zarubas_service(number)
		services.youla_service(number)
		services.yandex_service(number)
		services.ivi_service(number)
		services.kontur_service(number)
		services.vkusvill_service(number)
		services.x5id_service(number)
		services.medtochka_service(number)
		services.magnit_service(number)
		services.cg_service(number)
		services.smotr_service(number)
		services.zdapteka_service(number)
		services.youdo_service(number)
	except Exception as Error:	
		pass

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--number', '-n',
		action='store',
		dest='number',
		help='send number, example: 9000000000')
	args = parser.parse_args()
	main(args.number)
		
