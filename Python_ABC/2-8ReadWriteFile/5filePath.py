from pathlib import Path

p = Path('.')
# print(p.cwd())

# q = Path('./Jeanette.txt')
# q = p / 'Jeanette.txt'
q = p.joinpath('Jeanette.txt')
# print(q.stem)
# print(q.name)
# print(q.cwd())
# print(q.exists())
# print(q.is_dir())
# print(q.is_file())


# with q.open() as f:
# 	print(f.read())

# print([x for x in p.iterdir() if x.is_dir()])
for f in [x for x in p.iterdir() if x.is_dir()]:
	print(f.name)


# for f in p.glob('**/*.py'):
# 	print(f.name)
#
for f in p.glob('*.py'):
	print(f.name)
#
# for f in p.glob('*/*.py'):
# 	print(f.name)

# p.joinpath('temp').mkdir(mode=0o777, exist_ok=True)

# source = Path('./quote1.txt')
# source.open('w').write('There is no discovery without risk and what you risk reveals what you value.')
# target = Path('quote2.txt')
# source.rename(target)
# target = Path('./temp/quote3.txt')
# source.rename(target)



