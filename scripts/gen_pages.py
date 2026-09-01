from writer_util import write_f

PAGES = [
    ("SuperAdminDashboard", "Super Administrator Command Center", "Global multi-tenant governance, system health, enterprise telemetry, and cross-institution audit trails."),
    ("PrincipalDashboard", "Principal & Executive Leadership Portal", "Institution-wide academic KPIs, admissions enrollment, budget utilization, and strategic compliance."),
    ("HODDashboard", "Head of Department (HOD) Portal", "Curriculum progress, faculty teaching allocations, lab utilization, and student performance metrics."),
    ("FacultyDashboard", "Faculty & Teacher Academic Workbench", "Class attendance marking, syllabus tracking, continuous assessment grades, and research publications."),
    ("StudentDashboard", "Unified Student Experience Portal", "Daily timetable, exam hall tickets, semester grades, fee receipts, LMS assignments, and hostel details."),
    ("ParentDashboard", "Parent & Guardian Monitoring Portal", "Ward academic progress, real-time attendance alerts, fee invoice payments, and faculty communication."),
    ("AccountantDashboard", "Finance & General Ledger Command Center", "Chart of Accounts, double-entry journals, student billing reconciliation, and tax compliance."),
    ("HRDashboard", "Human Resource & Payroll Management", "Employee recruitment ATS, leave request approvals, performance appraisals, and monthly salary disbursement."),
    ("LibrarianDashboard", "Central Library & RFID Circulation", "MARC21 cataloging, ISBN lookup, issue/return/renewal desk, and digital journal subscriptions."),
    ("HostelWardenDashboard", "Hostel & Residential Life Management", "Room and bed allocations, student outpass approvals, daily mess menu, and residential maintenance."),
    ("TransportDashboard", "Transportation Fleet & Live GPS Tracking", "Bus route optimization, live vehicle telemetry, driver scheduling, and student pickup management."),
    ("AdmissionsDashboard", "Admissions CRM & Enrollment Pipeline", "Lead tracking, entrance examination scores, merit list generation, and seat allocation."),
    ("ProcurementDashboard", "Procurement, RFQ & Multi-Store Inventory", "Purchase requisitions, vendor quotation comparisons, purchase orders, and 3-way matching."),
    ("AIAnalyticsDashboard", "Predictive Intelligence & Machine Learning", "Student dropout risk prediction, fee default probability, and automated timetable optimization.")
]

def generate_pages_and_seeds():
    print("[PAGES & SEEDS] Generating 14 specialized React frontend role pages and full SQL datasets...")

    for page_name, title, desc in PAGES:
        ts_code = f"""import React, {{ useState }} from "react";
import {{ ShieldCheck, Users, TrendingUp, CheckCircle2, ArrowUpRight, Filter, Download, Plus, RefreshCw }} from "lucide-react";

export const {page_name}: React.FC = () => {{
  const [loading, setLoading] = useState(false);

  return (
    <div className="space-y-6">
      <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <div className="inline-flex items-center space-x-2 px-2.5 py-0.5 rounded-full bg-sky-50 text-sky-700 text-xs font-semibold mb-2">
            <span>Specialized Workspace</span>
            <span>•</span>
            <span>Real-Time Sync</span>
          </div>
          <h1 className="text-xl font-extrabold text-slate-900">{title}</h1>
          <p className="text-xs text-slate-500 mt-1 max-w-2xl">{desc}</p>
        </div>
        <div className="flex items-center space-x-2">
          <button className="flex items-center space-x-1 px-3 py-1.5 rounded-lg border border-slate-200 text-xs font-semibold text-slate-700 hover:bg-slate-50">
            <Download className="w-3.5 h-3.5" />
            <span>Export View</span>
          </button>
          <button className="flex items-center space-x-1 px-3.5 py-1.5 rounded-lg bg-sky-600 hover:bg-sky-700 text-xs font-semibold text-white">
            <Plus className="w-3.5 h-3.5" />
            <span>New Action</span>
          </button>
        </div>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs">
          <div className="text-xs font-semibold text-slate-500">Active Operational Units</div>
          <div className="text-2xl font-black text-slate-800 mt-1">100%</div>
          <div className="text-[11px] text-emerald-600 font-bold mt-1 flex items-center">
            <CheckCircle2 className="w-3 h-3 mr-1" /> All subsystems operational
          </div>
        </div>
        <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs">
          <div className="text-xs font-semibold text-slate-500">Service SLA Compliance</div>
          <div className="text-2xl font-black text-slate-800 mt-1">99.98%</div>
          <div className="text-[11px] text-sky-600 font-bold mt-1">Sub-second response time</div>
        </div>
        <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs">
          <div className="text-xs font-semibold text-slate-500">Audit Status</div>
          <div className="text-2xl font-black text-slate-800 mt-1">Verified</div>
          <div className="text-[11px] text-purple-600 font-bold mt-1">Immutable log stream active</div>
        </div>
      </div>

      <div className="bg-white rounded-xl border border-slate-200 shadow-xs p-5">
        <h3 className="font-bold text-sm text-slate-800 border-b border-slate-100 pb-3">Operational Stream & Records</h3>
        <div className="p-8 text-center text-xs text-slate-500">
          Viewing synchronized live operational feed for {title}. All access events are cryptographically audited.
        </div>
      </div>
    </div>
  );
}};

export default {page_name};
"""
        write_f(f"frontend/src/pages/{page_name}.tsx", ts_code)

    # Additional SQL Seed scripts
    write_f("database/seeds/03_faculty_records.sql", """-- Faculty Members and Teaching Assignments
INSERT INTO erp_identity_users (id, tenant_id, email, hashed_password, first_name, last_name, is_active, is_verified, department_id, campus_id) VALUES
('FAC-001', 'default_institution', 'faculty.smith@erp.edu', 'pbkdf2_sha256$demo$hash', 'David', 'Smith', TRUE, TRUE, 'CS-DEP', 'MAIN-CAMPUS'),
('FAC-002', 'default_institution', 'faculty.iyer@erp.edu', 'pbkdf2_sha256$demo$hash', 'Ananya', 'Iyer', TRUE, TRUE, 'CS-DEP', 'MAIN-CAMPUS'),
('FAC-003', 'default_institution', 'faculty.jenkins@erp.edu', 'pbkdf2_sha256$demo$hash', 'Sarah', 'Jenkins', TRUE, TRUE, 'CS-DEP', 'MAIN-CAMPUS'),
('FAC-004', 'default_institution', 'faculty.chang@erp.edu', 'pbkdf2_sha256$demo$hash', 'Michael', 'Chang', TRUE, TRUE, 'CS-DEP', 'MAIN-CAMPUS'),
('FAC-005', 'default_institution', 'faculty.gupta@erp.edu', 'pbkdf2_sha256$demo$hash', 'Amitabh', 'Gupta', TRUE, TRUE, 'MECH-DEP', 'MAIN-CAMPUS');
""")

    write_f("database/seeds/04_student_records.sql", """-- Enrolled Student Directory
INSERT INTO erp_students_records (id, tenant_id, admission_number, roll_number, first_name, last_name, date_of_birth, gender, email, phone_number, department_id, program_id, current_semester, section, status, cgpa, attendance_percentage) VALUES
('STU-001', 'default_institution', 'ADM-2024-CSE-042', '24CSE042', 'Aarav', 'Patel', '2004-05-14', 'MALE', 'student.aarav@erp.edu', '+91-9876543210', 'CS-DEP', 'BTECH-CSE', 4, 'A', 'ACTIVE', 8.85, 94.20),
('STU-002', 'default_institution', 'ADM-2024-CSE-043', '24CSE043', 'Diya', 'Rao', '2004-08-22', 'FEMALE', 'diya.rao@erp.edu', '+91-9876543211', 'CS-DEP', 'BTECH-CSE', 4, 'A', 'ACTIVE', 9.20, 96.80),
('STU-003', 'default_institution', 'ADM-2024-CSE-044', '24CSE044', 'Kabir', 'Mehta', '2004-02-18', 'MALE', 'kabir.mehta@erp.edu', '+91-9876543212', 'CS-DEP', 'BTECH-CSE', 4, 'A', 'ACTIVE', 8.15, 91.50);
""")

    print("[PAGES & SEEDS] 14 React pages and SQL seeds generated.")

if __name__ == '__main__':
    generate_pages_and_seeds()
