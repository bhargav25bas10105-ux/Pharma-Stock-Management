import datetime as dt
from collections import defaultdict

INV, SALES = [], []
REORDER, CUR = 10, '₹'

def i_get(name):
    """Find item by name."""
    return next((i for i in INV if i['name'].lower() == name.lower()), None)

def i_list():
    """Display inventory with alerts."""
    if not INV: return print("\n[INFO] Inventory empty.")
    print("\n--- Inventory ---")
    print(f"| {'Name':<20} | {'Qty':<4} | {'Price':<6} | {'Expiry':<10} | {'Alert'}")
    print("-" * 62)
    today = dt.date.today()
    for i in INV:
        alert, exp = "", i.get('expiryDate', 'N/A')
        try:
            exp_date = dt.datetime.strptime(exp, '%Y-%m-%d').date()
            if exp_date <= today: alert = "!!EXPIRED!!"
            elif (exp_date - today).days <= 90: alert = "Exp Soon"
        except ValueError: alert = "!!BAD DATE!!"
        A = alert or (i['quantity'] <= REORDER and "LOW") or ""
        print(f"| {i['name'][:20]:<20} | {i['quantity']:<4} | {CUR}{i['price']:<5.2f} | {exp:<10} | {A:<10}")

def i_add_upd(mode):
    """Add new item or update price/qty."""
    print(f"\n--- {mode} Item ---")
    name = input("Name: ").strip(); i = i_get(name)
    if mode == 'ADD':
        if i: return print("[ERR] Exists. Use UPDATE.")
        try:
            data = {'name': name, 'expiryDate': input("Expiry (Y-M-D): ").strip(),
                    'price': float(input("Price: ")), 'quantity': int(input("Quantity: "))}
            dt.datetime.strptime(data['expiryDate'], '%Y-%m-%d'); INV.append(data); print(f"[OK] Added {name}.")
        except: print("[ERR] Invalid input.")
    elif mode == 'UPDATE':
        if not i: return print("[ERR] Not Found.")
        if (p := input(f"New Price ({i['price']:.2f}): ").strip()): i['price'] = float(p)
        if (q := input(f"New Stock ({i['quantity']}): ").strip()): i['quantity'] = int(q)
        print(f"[OK] Updated {name}.")

def s_process():
    """Handle interactive sales and generate log."""
    cart, available = [], [i for i in INV if i['quantity'] > 0]
    if not available: return print("[INFO] No stock.")
    print("\n--- Sale --- (F: finish)"); total = 0.0
    while True:
        name = input("Item Name (F/C): ").strip()
        if name in ('F', 'C', ''): break
        i = i_get(name);
        if not i or i['quantity'] == 0: continue
        try: qty = int(input(f"Qty ({i['quantity']}): "))
        except: continue
        if 0 < qty <= i['quantity']:
            sub = qty * i['price']; total += sub
            cart.append({'name': i['name'], 'qty': qty, 'price': i['price']}); i['quantity'] -= qty
        else: print(f"[ERR] Invalid Qty.")

    if not cart: return print("Sale cancelled.")
    SALES.append({'items': cart, 'total': total, 'time': dt.datetime.now()})
    print("\n" + "="*30 + f"\n    INVOICE (Total: {CUR}{total:.2f})\n" + "="*30)

def s_report():
    """Generate daily and monthly reports."""
    if not SALES: return print("\n[INFO] No sales.")
    today, d_tot, m_tot = dt.date.today(), 0.0, 0.0
    m_y = (today.year, today.month)
    for s in SALES:
        date, items = s['time'].date(), s['items']
        is_d, is_m = date == today, (date.year, date.month) == m_y
        for i in items:
            if is_d: d_tot += i['qty'] * i['price']
            if is_m: m_tot += i['qty'] * i['price']
            
    print("\n" + "="*30 + "\n    SALES REPORT")
    print(f"--- DAILY ({today.strftime('%Y-%m-%d')}) Revenue: {CUR}{d_tot:.2f} ---")
    print(f"--- MONTHLY ({today.strftime('%B %Y')}) Revenue: {CUR}{m_tot:.2f} ---")
    print("="*30)

def i_del(name):
    """Delete item by name."""
    i = i_get(name)
    if i: INV.remove(i); print(f"[OK] Deleted {name}.")
    else: print(f"[ERR] '{name}' not found.")

def main():
    INV.extend([{'name': 'Para 500', 'expiryDate': '2026-10-30', 'price': 15.00, 'quantity': 150},
                {'name': 'Amox 250', 'expiryDate': '2024-01-15', 'price': 52.50, 'quantity': 5}])
    yesterday = dt.datetime.now() - dt.timedelta(days=1)
    SALES.append({'items': [{'name': 'Para 500', 'qty': 5, 'price': 15.00}], 'total': 75.00, 'time': yesterday})

    actions = {'1': i_list, '2': lambda: i_add_upd('ADD'), '3': lambda: i_add_upd('UPDATE'),
               '4': lambda: i_del(input("Del Name: ")), '5': s_process, '7': s_report}
    
    while True:
        print("\nPHARMA MANAGER\n1: View | 2: Add | 3: Update | 4: Del | 5: Sale | 7: Report | 8: Exit")
        choice = input("Choice: ")
        if choice == '8': print("Exiting."); break
        actions.get(choice, lambda: print("[ERR] Invalid."))()
        input("ENTER...")

if __name__ == '__main__':
    main()