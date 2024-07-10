from odoo import models
from odoo.exceptions import ValidationError
from datetime import datetime

class ClassXlsxReport(models.AbstractModel):
    _name = 'report.nti_training_academic.class_xlsx_report'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, classes):
        sh_dashboard = workbook.add_worksheet('Dashboard')
        sh_mahasiswa = workbook.add_worksheet('Mahasiswa')
        sh_jadwal = workbook.add_worksheet('Jadwal')
        
        title_header = workbook.add_format({'font_size': 16, 'align': 'center', 'valign': 'vcenter', 'bold': True})
        text_style = workbook.add_format({'font_size': 10, 'border': 1, 'align': 'center', 'valign': 'vcenter', 'text_wrap': True})
        text_left = workbook.add_format({'font_size': 10, 'border': 1, 'align': 'left', 'valign': 'vcenter', 'text_wrap': True})
        header = workbook.add_format({'font_size': 10, 'border': 1, 'align': 'center', 'valign': 'vcenter', 'text_wrap': True, 'bold': True})

        # SHEET DASHBOARD
        sh_dashboard.merge_range('B2:C2', 'Dashboard Report Kelas', title_header)
        sh_dashboard.set_column('B:C', 20)
        
        sh_dashboard.write(2, 1, 'Total Kelas', header)
        sh_dashboard.write(3, 1, 'Nama Kelas', header)
        sh_dashboard.write(4, 1, 'Tanggal', header)
        sh_dashboard.write(5, 1, 'Dosen', header)
        sh_dashboard.write(6, 1, 'Jumlah Mahasiswa', header)
        
        sh_dashboard.write(2, 2, len(classes), text_style) 
        sh_dashboard.write(3, 2, classes[0].name, text_style)
        sh_dashboard.write(4, 2, classes[0].date.strftime('%d/%m/%Y'), text_style)
        sh_dashboard.write(5, 2, classes[0].user_id.name, text_style)
        sh_dashboard.write(6, 2, len(classes[0].student_ids), text_style)

        # SHEET MAHASISWA
            
        sh_mahasiswa.merge_range('B2:F2', 'Report Mahasiswa', title_header)
        sh_mahasiswa.set_column('B:F', 20)
        sh_mahasiswa.write(2, 1, 'Nama Mahasiswa', header)
        sh_mahasiswa.write(2, 2, 'Phone', header)
        sh_mahasiswa.write(2, 3, 'Email', header)
        sh_mahasiswa.write(2, 4, 'Tanggal Lahir', header)
        sh_mahasiswa.write(2, 5, 'Alamat', header)
        
        row = 3
        for student in classes[0].student_ids:
            sh_mahasiswa.write(row, 1, student.name, text_left)
            sh_mahasiswa.write(row, 2, student.phone, text_left)
            sh_mahasiswa.write(row, 3, student.email, text_left)
            sh_mahasiswa.write(row, 4, student.birthday.strftime('%d/%m/%Y') if student.birthday else '', text_left)
            sh_mahasiswa.write(row, 5, student.street, text_left)
            row += 1
        
        # SHEET JADWAL
        
        sh_jadwal.merge_range('B2:F2', 'Report Jadwal', title_header)
        sh_jadwal.set_column('B:F', 20)
        sh_jadwal.write(2, 1, 'Nama Mata Kuliah', header)
        sh_jadwal.write(2, 2, 'Code', header)
        sh_jadwal.write(2, 3, 'Dosen', header)
        sh_jadwal.write(2, 4, 'Start Hour', header)
        sh_jadwal.write(2, 5, 'End Hour', header)
        
        row = 3
        for subject_line in classes[0].subject_line_ids:
            sh_jadwal.write(row, 1, subject_line.subject_id.name, text_left)
            sh_jadwal.write(row, 2, subject_line.subject_id.code, text_left)
            sh_jadwal.write(row, 3, subject_line.lecturer_id.name, text_left)
            sh_jadwal.write(row, 4, self.float_to_time(subject_line.start_hour), text_left)
            sh_jadwal.write(row, 5, self.float_to_time(subject_line.end_hour), text_left)
            row += 1
    

    def float_to_time(self, float_val):
        hours, remainder = divmod(float_val * 60, 60)
        return "%02d:%02d" % (int(hours), int(remainder))
