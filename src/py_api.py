import dvc.api

with dvc.api.open(
    'get-started/data.xml',
    repo='https://github.com/iterative/dataset-registry',encoding="utf8") as f:
  lines = f.readlines()
  print (lines[:2])