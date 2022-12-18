import services
import argparse

def main(number: int):#number: int, cirlces:int
	try:
		services.youla_service(number)
		services.yandex_service(number)
		services.ivi_service(number)
		services.kontur_service(number)
		services.vkusvill_service(number)
		services.premier_one_service(number)
		services.x5id_service(number)
		services.medtochka_service(number)
		services.lenta_service(number)
		services.magnit_service(number)
		services.cg_service(number)
	except:	
		pass

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--number', '-n',
		action='store',
		dest='number',
		help='send number, example: 9000000000')
	parser.add_argument('--circle', '-c',
		action='store',
		dest='circles',
		help='send circle, example: 10')
	args = parser.parse_args()
	main(args.number)#args.number, args.circles
		
