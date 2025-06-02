from typing import  Tuple
import re
import json


def check(
	U: float,
	widthInput: float,
	widthOutput: float,
	sideTriangle: float,
	lenCone: float,
	widthBase: float,
	ten: float,
	coneT: float,
	minSize: float,
	maxSize: float,
) -> Tuple[bool, str]:
	if U <= 0 or widthInput <= 0 or widthOutput <= 0 or sideTriangle <= 0 or lenCone <= 0 or widthBase <= 0 or ten <0 or coneT <0:
		return False, "Все значения должны быть >0"

	if widthInput >= widthOutput:
		return False,"wI должно быть < wo"
	if ten >= lenCone:
		return False,"bt должно быть < L"
	if coneT >= widthInput / 2:
		return False,"coneT слишком велико"
	if widthBase > widthOutput:
		return False, "Ширина выступа wb не может превышать внешнюю ширину wo"
	if ten + coneT > lenCone:
		return False, "Сумма bt и ct не может превышать длину L"
	if sideTriangle >= lenCone:
		return False, "t должно быть меньше L"

	result = {
		"heightS": str(widthInput),
		"heightB": str(widthOutput),
		"triangle": str(sideTriangle),
		"widthL": str(lenCone),
		"widthR": str(widthBase),
		"distanceToTriangle": str(ten),
		"angle": "11",
		"gap": str(coneT),
		"minSize": str(minSize),
		"maxSize": str(maxSize),
	}

	with open('data.json', 'w') as file:
		json.dump(result, file, indent=4)
	change_inlet_velocity(U)
	return True, "Параметры корректны. Запуск расчёта..."


def change_inlet_velocity(new_x_velocity: float = 1, file_path: str = "0/U"):
	"""Изменяет значение скорости на входе (inlet) в файле U OpenFOAM"""
	with open(file_path, 'r') as file:
		content = file.read()

	# Ищем и заменяем значение скорости в inlet
	pattern = r'(inlet\s*\{[^}]*value\s*uniform\s*\()(\d+\.?\d*)(\s+0\s+0\);)'
	replacement = fr'\g<1>{new_x_velocity}\g<3>'
	new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

	with open(file_path, 'w') as file:
		file.write(new_content)
