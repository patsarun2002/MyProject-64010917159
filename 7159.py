def calculate_personal_income_tax(income, expenses, deductions):
  """
  คำนวณภาษีเงินได้บุคคลธรรมดา

  Args:
      income: รายได้
      expenses: ค่าใช้จ่าย
      deductions: ค่าลดหย่อน

  Returns:
      ภาษีเงินได้บุคคลธรรมดาที่ต้องชำระ
  """

  # หารายได้สุทธิ
  net_income = income - expenses

  # หารายได้เสียภาษี
  taxable_income = net_income - deductions

  # คำนวณภาษี
  tax = 0
  for bracket, rate in TAX_BRACKETS:
    if taxable_income <= bracket:
      tax += taxable_income * rate
      break
    else:
      tax += bracket * rate
      taxable_income -= bracket

  # คืนค่าภาษี
  return tax

# ตัวอย่างการใช้งาน
income = 1000000
expenses = 500000
deductions = 60000

tax = calculate_personal_income_tax(income, expenses, deductions)

print("ภาษีเงินได้บุคคลธรรมดาที่ต้องชำระ:", tax)