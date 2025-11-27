"""
Constantes para días festivos colombianos.
"""

# Festivos fijos (nunca se mueven)
FIXED_HOLIDAYS = {
    (1, 1): "Año Nuevo (New Year's Day)",
    (5, 1): "Día del Trabajo (Labour Day)",
    (7, 20): "Día de la Independencia (Independence Day)",
    (8, 7): "Batalla de Boyacá (Battle of Boyacá)",
    (12, 8): "Inmaculada Concepción (Immaculate Conception)",
    (12, 25): "Navidad (Christmas Day)",
}

# Festivos que se mueven al lunes siguiente (Ley Emiliani)
MOVABLE_TO_MONDAY = {
    (1, 6): "Epifanía (Epiphany)",
    (3, 19): "Día de San José (St. Joseph's Day)",
    (6, 29): "San Pedro y San Pablo (St. Peter and St. Paul)",
    (8, 15): "Asunción de la Virgen (Assumption of Mary)",
    (10, 12): "Día de la Raza (Columbus Day)",
    (11, 1): "Todos los Santos (All Saints' Day)",
    (11, 11): "Independencia de Cartagena (Independence of Cartagena)",
}
