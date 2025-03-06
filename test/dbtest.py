from tools.dbmanager import add_table, add_expense, get_expenses, mod_expense, del_expense, sum_expenses, sum_expenses_month

def run_tests():
    print("\n=== INICIANDO PRUEBAS ===\n")

    # 1️⃣ CREAR TABLA
    print("[1] Creando la tabla...")
    add_table()

    # 2️⃣ INSERTAR GASTOS
    print("\n[2] Insertando gastos...")
    add_expense("Café", 3.50, "Alimentos")
    add_expense("Cena en restaurante", 25.00, "Comida", "2024-03-05 20:00:00")
    add_expense("Netflix", 15.00, "Entretenimiento")

    # 3️⃣ CONSULTAR GASTOS
    print("\n[3] Mostrando gastos actuales en la DB:")
    expenses = get_expenses()
    for e in expenses:
        print(e)

    # 4️⃣ MODIFICAR UN GASTO (Modificar id=1)
    if expenses:
        first_id = expenses[0]['id']
        print(f"\n[4] Modificando el gasto con ID {first_id}...")
        mod_expense(first_id, "Café grande", 4.50)

    # 5️⃣ CONSULTAR GASTOS NUEVAMENTE
    print("\n[5] Mostrando gastos después de la modificación:")
    expenses = get_expenses()
    for e in expenses:
        print(e)

    # 6️⃣ ELIMINAR UN GASTO (Eliminar id=3 si existe)
    if len(expenses) > 2:
        third_id = expenses[2]['id']
        print(f"\n[6] Eliminando el gasto con ID {third_id}...")
        del_expense(third_id)

    # 7️⃣ CONSULTAR GASTOS NUEVAMENTE
    print("\n[7] Mostrando gastos después de eliminar uno:")
    expenses = get_expenses()
    for e in expenses:
        print(e)

    # 8️⃣ SUMAR TODOS LOS GASTOS
    total = sum_expenses()
    print(f"\n[8] Total de gastos en la base de datos: {total:.2f}")

    # 9️⃣ SUMAR GASTOS DE MARZO 2024
    total_marzo_2024 = sum_expenses_month(2024, 3)
    print(f"\n[9] Total de gastos en marzo 2024: {total_marzo_2024:.2f}")

    print("\n=== PRUEBAS COMPLETADAS ===")

if __name__ == "__main__":
    run_tests()