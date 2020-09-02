from google_images_download import google_images_download

# BC_native_plants = [
#     'Aster',
#     'Aquilegia formosa',
#     # 'Sedum spathulifolium',
#     # 'Delphinium menziesii',
#     # 'Rosa nutkana',
#     # 'Physocarpus capitatus'
#     # 'Sambucus racemosa',
#     # 'Gaultheria shallon',
#     # 'Arbutus menziesii',
#     # 'Cornus Eddie\'s White Wonder',
#     # 'Sorbus aucuparia',
#     # 'Acer circinatum'
# ]

response = google_images_download.googleimagesdownload()

arguments = {"keywords": "Polar bears,baloons,Beaches", "limit": 20, "print_urls": True}

paths = response.download(arguments)

print(paths)
