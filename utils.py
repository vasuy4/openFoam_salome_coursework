from typing import  Tuple

def check(
	U: float,
	widthInput: float,
	widthOutput: float,
	sideTriangle: float,
	lenCone: float,
	widthBase: float,
	ten: float,
	coneT: float,
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


	return True, "Параметры корректны. Запуск расчёта..."
