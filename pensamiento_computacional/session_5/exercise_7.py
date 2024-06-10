# 7. Se quiere guardar la información de un grupo de maratonistas. 
# Se necesita guardar su nombre, DNI, y todas las maratones que corrió, de la cual a su vez se quiere tener el nombre de cada una, el año, el
# puesto en que salió el maratonista, y el tiempo que tardó en terminarla.

# a. Crear el diccionario que represente esta situación.

# AYUDA: Queremos guardar muchos maratonistas, y a su vez, muchas maratones para cada
# maratonista, entonces ¿Qué tipo de dato debería ser el campo que guarda todas las
# maratones? ¿Y qué tipo de dato es la maratón en sí?

# b. Teniendo una lista de diccionarios de maratonistas, ordenarlos alfabéticamente.
# c. Ordenar las maratones de cada maratonista según el tiempo que tardó en completar cada una
# de forma ascendente.

marathoners = [
  {
    "name": "Gebrselassie",
    "lastname": "Tesfay",
	"dni": 123456,
    "marathons": [
      {
        "year": 2008,
        "position": 1,
        "time": "02:05:27"
      },
      {
        "year": 2001,
        "position": 1,
        "time": "02:04:55"
      },
      {
        "year": 1998,
        "position": 1,
        "time": "02:04:26"
      }
    ]
  },
  {
    "name": "Brigid",
    "lastname": "Kosgei",
	"dni": 132124,
    "marathons": [
      {
        "year": 2021,
        "position": 1,
        "time": "02:17:41"
      },
      {
        "year": 2019,
        "position": 1,
        "time": "02:24:11"
      },
      {
        "year": 2016,
        "position": 1,
        "time": "02:14:04"
      }
    ]
  },
  {
    "name": "Paula",
    "lastname": "Radcliffe",
	"dni": 542312,
    "marathons": [
      {
        "year": 2003,
        "position": 1,
        "time": "02:23:29"
      },
      {
        "year": 2000,
        "position": 2,
        "time": "02:15:25"
      }
    ]
  },
  {
    "name": "Eliud",
    "lastname": "Kipchoge",
	"dni": 875643,
    "marathons": [
      {
        "year": 2023,
        "position": 1,
        "time": "02:02:38"
      },
      {
        "year": 2022,
        "position": 1,
        "time": "02:01:39"
      },
      {
        "year": 2018,
        "position": 1,
        "time": "02:01:09"
      }
    ]
  },
]

def convertTimeToSeconds(time_string):
	hours, minutes, seconds = map(int, str(time_string).split(":")) # Remember that a string is an iterable.
	return hours * 3600 + minutes * 60 + seconds

def sortMarathoners():
	marathoners.sort(key = lambda marathoner : marathoner["name"])

	for marathoner in marathoners:
     	# marathoner["marathons"].sort(key=lambda marathon: convertTimeToSeconds(marathon["time"])) #not recomended because marathoner["marathons"] is type any
		marathoner["marathons"] = sorted(marathoner["marathons"],key = lambda marathon : convertTimeToSeconds(marathon["time"])) #the sorted method return a new list
  
		# marathons: list = marathoner["marathons"] #alternative 2 with types to avoid "any" 
		# marathons.sort(key = lambda marathon : convertTimeToSeconds(marathon["time"]))
  
	for marathoner in marathoners:
		print(f"\n {marathoner["name"]}")
		for marathon in marathoner["marathons"]:
			print(marathon["time"])

    

sortMarathoners()  
