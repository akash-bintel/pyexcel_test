import xlsxwriter

if __name__ == '__main__':

    students =(
        ["Shyam", 90, 87, 32],
        ["Meera", 89, 76,94],
        ["Rakesh", 88, 91, 93],
    )

    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook('data/demo.xlsx')
    worksheet = workbook.add_worksheet("student")

    for row in range(len(students)):
        for col in range(len(students[row])):
            worksheet.write(row, col, students[row][col])

    for row in range(len(students[0])-1):
        worksheet.write(row, len(students)+1, f'=SUM(B{row+1}:D{row+1})')

    workbook.close()