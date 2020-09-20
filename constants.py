"""Common constants/mappings used throughout analysis"""

FILE_URLS = [
    'https://cdn.touringplans.com/datasets/touringplans_data_dictionary.xlsx',
    'https://cdn.touringplans.com/datasets/metadata.csv',
    'https://cdn.touringplans.com/datasets/entities.csv',
    'https://cdn.touringplans.com/datasets/alien_saucers.csv',
    'https://cdn.touringplans.com/datasets/flight_of_passage.csv',
    'https://cdn.touringplans.com/datasets/dinosaur.csv',
    'https://cdn.touringplans.com/datasets/expedition_everest.csv',
    'https://cdn.touringplans.com/datasets/kilimanjaro_safaris.csv',
    'https://cdn.touringplans.com/datasets/navi_river.csv',
    'https://cdn.touringplans.com/datasets/pirates_of_caribbean.csv',
    'https://cdn.touringplans.com/datasets/rock_n_rollercoaster.csv',
    'https://cdn.touringplans.com/datasets/7_dwarfs_train.csv',
    'https://cdn.touringplans.com/datasets/slinky_dog.csv',
    'https://cdn.touringplans.com/datasets/soarin.csv',
    'https://cdn.touringplans.com/datasets/spaceship_earth.csv',
    'https://cdn.touringplans.com/datasets/splash_mountain.csv',
    'https://cdn.touringplans.com/datasets/toy_story_mania.csv',
]

ATTRACTION_FILE_TO_CODES = {
    # Mapping of attraction file to code, transcribed from entities.csv
    'alien_saucers.csv': 'HS104',
    'flight_of_passage.csv': 'AK86',
    'dinosaur.csv': 'AK18',
    'expedition_everest.csv': 'AK11',
    'kilimanjaro_safaris.csv': 'AK07',
    'navi_river.csv': 'AK85',
    'pirates_of_caribbean.csv': 'DL40',
    'rock_n_rollercoaster.csv': 'HS12',
    '7_dwarfs_train.csv': 'MK141',
    'slinky_dog.csv': 'HS103',
    'soarin.csv': 'CA09',
    'spaceship_earth.csv': 'EP02',
    'splash_mountain.csv': 'MK04',
    'toy_story_mania.csv': 'CA30',
}
