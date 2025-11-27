# Colombian Holidays

Una librería Python para verificar días festivos en Colombia, incluyendo soporte para la Ley Emiliani (Ley 51 de 1983) y reconocimiento automático de domingos como días festivos.

## Características

- ✅ Verifica si hoy es festivo
- ✅ Verifica si cualquier fecha es festivo
- ✅ Todos los domingos son reconocidos como festivos
- ✅ Soporte completo para la Ley Emiliani
- ✅ Cálculo automático de festivos basados en Pascua
- ✅ 18 festivos oficiales de Colombia

## Instalación

```bash
pip install colombian-holidays
```

## Uso Rápido

```python
from colombian_holidays import is_today_holiday, get_today_holiday_name

# Verificar si hoy es festivo
if is_today_holiday():
    print(f"Hoy es festivo: {get_today_holiday_name()}")
else:
    print("Hoy no es festivo")
```

## Ejemplos

### Verificar una fecha específica

```python
from datetime import datetime
from colombian_holidays import is_holiday, get_holiday_name

fecha = datetime(2025, 12, 25)
if is_holiday(fecha):
    print(f"Es festivo: {get_holiday_name(fecha)}")
```

### Listar todos los festivos del año

```python
from colombian_holidays import list_holidays

festivos_2025 = list_holidays(2025)
for (mes, dia), nombre in sorted(festivos_2025.items()):
    print(f"{mes:02d}/{dia:02d}: {nombre}")
```

### Uso avanzado con la clase

```python
from datetime import datetime
from colombian_holidays import ColombianHolidays

checker = ColombianHolidays()

# Verificar múltiples fechas
fechas = [
    datetime(2025, 1, 1),
    datetime(2025, 7, 20),
    datetime(2025, 12, 25),
]

for fecha in fechas:
    if checker.is_holiday(fecha):
        print(f"{fecha}: {checker.get_holiday_name(fecha)}")
```

## Festivos Incluidos

### Festivos Fijos
- Año Nuevo (1 de enero)
- Día del Trabajo (1 de mayo)
- Día de la Independencia (20 de julio)
- Batalla de Boyacá (7 de agosto)
- Inmaculada Concepción (8 de diciembre)
- Navidad (25 de diciembre)

### Festivos Móviles (Ley Emiliani)
- Epifanía
- San José
- San Pedro y San Pablo
- Asunción de la Virgen
- Día de la Raza
- Todos los Santos
- Independencia de Cartagena

### Festivos basados en Pascua
- Jueves Santo
- Viernes Santo
- Ascensión del Señor
- Corpus Christi
- Sagrado Corazón

## API Reference

### Funciones principales

- `is_today_holiday()`: Verifica si hoy es festivo
- `get_today_holiday_name()`: Obtiene el nombre del festivo de hoy
- `is_holiday(date)`: Verifica si una fecha es festivo
- `get_holiday_name(date)`: Obtiene el nombre del festivo de una fecha
- `list_holidays(year)`: Lista todos los festivos de un año

### Clase ColombianHolidays

```python
checker = ColombianHolidays(date=None)
checker.is_holiday(date=None)
checker.get_holiday_name(date=None)
checker.get_all_holidays(year)
```

## Licencia

MIT License

## Contribuciones

Las contribuciones son bienvenidas. Por favor abre un issue o pull request en GitHub.