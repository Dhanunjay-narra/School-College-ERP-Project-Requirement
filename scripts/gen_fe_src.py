from writer_util import write_f

def write_fe_src():
    write_f("frontend/src/types/index.ts", '''export interface User {
  id: string;
  email: string;
  first_name: string;
  last_name: string;
  full_name: string;
  role: string;
  roles: string[];
  tenant_id: string;
  department_id?: string;
  campus_id?: string;
}''')

    write_f("frontend/src/services/api.ts", '''const API_BASE = "http://localhost:8000/api/v1";

export async function fetchApi(endpoint: string) {
  try {
    const res = await fetch(`${API_BASE}${endpoint}`);
    if (!res.ok) throw new Error(`Status ${res.status}`);
    return await res.json();
  } catch (e) {
    console.warn("API fallback for", endpoint, e);
    return null;
  }
}''')

    write_f("frontend/src/components/OneClickLoginBar.tsx", '''import React from "react";
import { ShieldCheck, UserCheck, GraduationCap, Users, DollarSign, BookOpen, Home, Bus, Briefcase, Award } from "lucide-react";

export const DEMO_USERS = [
  { role: "SUPER_ADMIN", label: "Super Admin", email: "superadmin@erp.edu", name: "Super Admin", icon: ShieldCheck },
  { role: "PRINCIPAL", label: "Principal", email: "principal@erp.edu", name: "Dr. Rajesh Sharma", icon: Award },
  { role: "HOD", label: "HOD CS", email: "hod.cs@erp.edu", name: "Prof. Ananya Iyer", icon: Briefcase },
  { role: "FACULTY", label: "Faculty", email: "faculty.smith@erp.edu", name: "Dr. David Smith", icon: UserCheck },
  { role: "STUDENT", label: "Student", email: "student.aarav@erp.edu", name: "Aarav Patel", icon: GraduationCap },
  { role: "PARENT", label: "Parent", email: "parent.sharma@erp.edu", name: "Vikram Sharma", icon: Users },
  { role: "ACCOUNTANT", label: "Finance", email: "accountant@erp.edu", name: "Priya Nair", icon: DollarSign },
  { role: "LIBRARIAN", label: "Librarian", email: "librarian@erp.edu", name: "Meenakshi S.", icon: BookOpen },
  { role: "HOSTEL_WARDEN", label: "Warden", email: "warden@erp.edu", name: "Col. Ramesh Singh", icon: Home },
  { role: "TRANSPORT_MANAGER", label: "Transport", email: "transport@erp.edu", name: "Gurpreet Singh", icon: Bus },
];

export const OneClickLoginBar = ({ onSelectRole, activeRole }: any) => {
  return (
    <div className="bg-slate-900 text-white px-4 py-2.5 shadow sticky top-0 z-50 border-b border-slate-800">
      <div className="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-2">
        <div className="flex items-center space-x-2">
          <span className="px-2 py-0.5 rounded text-xs font-semibold bg-sky-500/20 text-sky-400 border border-sky-500/30">
            1-Click Demo Login
          </span>
          <span className="text-xs text-slate-300 hidden md:inline">
            Directly switch enterprise personas:
          </span>
        </div>
        <div className="flex flex-wrap items-center gap-1.5">
          {DEMO_USERS.map((u) => {
            const Icon = u.icon;
            const isSelected = activeRole === u.role;
            return (
              <button
                key={u.role}
                onClick={() => onSelectRole({ email: u.email, name: u.name, role: u.role })}
                className={`flex items-center space-x-1.5 px-2.5 py-1 rounded-full text-xs font-medium transition ${
                  isSelected ? "bg-white text-slate-900 ring-2 ring-sky-400 font-bold" : "bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700"
                }`}
              >
                <Icon className={`w-3.5 h-3.5 ${isSelected ? "text-sky-600" : "text-slate-400"}`} />
                <span>{u.label}</span>
              </button>
            );
          })}
        </div>
      </div>
    </div>
  );
};''')

    write_f("frontend/src/components/Sidebar.tsx", '''import React from "react";
import {
  LayoutDashboard, GraduationCap, Users, BookOpen, CalendarCheck, Award, DollarSign,
  Briefcase, Home, Bus, FileText, Cpu, ShieldCheck, Building2, Package, Layers
} from "lucide-react";

export const Sidebar = ({ activeTab, setActiveTab }: any) => {
  const menuItems = [
    { id: "dashboard", label: "Overview Dashboard", icon: LayoutDashboard },
    { id: "students", label: "Student Management", icon: GraduationCap },
    { id: "academics", label: "Curriculum & Timetable", icon: BookOpen },
    { id: "attendance", label: "Smart Attendance", icon: CalendarCheck },
    { id: "examinations", label: "Exams & Transcripts", icon: Award },
    { id: "fees", label: "Fees & Invoicing", icon: DollarSign },
    { id: "finance", label: "General Ledger & CoA", icon: Layers },
    { id: "hr", label: "HR & Payroll", icon: Briefcase },
    { id: "library", label: "Central Library", icon: BookOpen },
    { id: "hostels", label: "Hostel & Housing", icon: Home },
    { id: "transport", label: "Transport & GPS", icon: Bus },
    { id: "inventory", label: "Procurement & Stores", icon: Package },
    { id: "workflows", label: "Approval Workflows", icon: FileText },
    { id: "ai", label: "AI & Predictive ML", icon: Cpu },
    { id: "compliance", label: "Audit & Compliance", icon: ShieldCheck },
    { id: "organization", label: "Campus & Facilities", icon: Building2 },
  ];

  return (
    <aside className="w-64 bg-slate-900 text-slate-300 flex flex-col shrink-0 border-r border-slate-800 min-h-[calc(100vh-45px)]">
      <div className="p-4 border-b border-slate-800 flex items-center space-x-3">
        <div className="w-8 h-8 rounded bg-sky-600 flex items-center justify-center font-bold text-white">ERP</div>
        <div>
          <h2 className="font-bold text-sm text-white">Apex Enterprise</h2>
          <p className="text-[11px] text-sky-400">School & College ERP</p>
        </div>
      </div>
      <div className="flex-1 overflow-y-auto py-3 px-2 space-y-1">
        {menuItems.map((item) => {
          const Icon = item.icon;
          const isActive = activeTab === item.id;
          return (
            <button
              key={item.id}
              onClick={() => setActiveTab(item.id)}
              className={`w-full flex items-center space-x-3 px-3 py-2 rounded-lg text-xs font-medium transition ${
                isActive ? "bg-sky-600 text-white font-semibold" : "text-slate-400 hover:text-white hover:bg-slate-800"
              }`}
            >
              <Icon className={`w-4 h-4 ${isActive ? "text-white" : "text-slate-400"}`} />
              <span>{item.label}</span>
            </button>
          );
        })}
      </div>
      <div className="p-3 border-t border-slate-800 text-[11px] text-slate-400 bg-slate-950/40">
        <div className="flex items-center justify-between">
          <span>Version 1.0.0 (37 Phases)</span>
          <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
        </div>
      </div>
    </aside>
  );
};''')

    write_f("frontend/src/components/Header.tsx", '''import React from "react";
import { Bell, Search, Shield } from "lucide-react";

export const Header = ({ user }: any) => {
  return (
    <header className="bg-white border-b border-slate-200 px-6 py-3.5 flex items-center justify-between sticky top-[45px] z-40">
      <div className="flex items-center space-x-4 flex-1 max-w-lg">
        <div className="relative w-full">
          <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            placeholder="Search students, faculty, courses, books, fee invoices..."
            className="w-full bg-slate-100 border border-slate-200 pl-9 pr-4 py-1.5 rounded-lg text-xs focus:outline-none focus:ring-2 focus:ring-sky-500"
          />
        </div>
      </div>
      <div className="flex items-center space-x-4">
        <button className="relative p-2 text-slate-500 hover:text-slate-700 hover:bg-slate-100 rounded-full">
          <Bell className="w-4 h-4" />
          <span className="absolute top-1.5 right-1.5 w-2 h-2 bg-rose-500 rounded-full"></span>
        </button>
        <div className="flex items-center space-x-3 pl-3 border-l border-slate-200">
          <div className="w-8 h-8 rounded-full bg-sky-100 text-sky-800 flex items-center justify-center font-bold text-xs">
            {user.name.charAt(0)}
          </div>
          <div className="text-left hidden sm:block">
            <div className="text-xs font-bold text-slate-800">{user.name}</div>
            <div className="text-[11px] font-medium text-sky-600 flex items-center space-x-1">
              <Shield className="w-3 h-3 inline" />
              <span>{user.role}</span>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};''')

    write_f("frontend/src/components/DashboardView.tsx", '''import React from "react";
import { Users, GraduationCap, DollarSign, CalendarCheck, ArrowUpRight, CheckCircle } from "lucide-react";

export const DashboardView = ({ userRole }: any) => {
  const stats = [
    { label: "Total Enrolled Students", value: "3,842", change: "+12.4%", icon: GraduationCap, color: "text-blue-600", bg: "bg-blue-50" },
    { label: "Faculty & Staff Members", value: "248", change: "+4.1%", icon: Users, color: "text-indigo-600", bg: "bg-indigo-50" },
    { label: "Fee Collection (YTD)", value: "₹12.85 Cr", change: "94.8%", icon: DollarSign, color: "text-emerald-600", bg: "bg-emerald-50" },
    { label: "Campus Attendance Rate", value: "94.2%", change: "+1.8%", icon: CalendarCheck, color: "text-cyan-600", bg: "bg-cyan-50" },
  ];

  return (
    <div className="space-y-6">
      <div className="bg-gradient-to-r from-sky-700 via-sky-800 to-indigo-900 rounded-2xl p-6 text-white shadow flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <div className="inline-flex items-center space-x-2 px-2.5 py-1 rounded-full bg-white/10 text-sky-200 text-xs font-medium mb-2">
            <span>Academic Year 2026-2027</span>
            <span>•</span>
            <span>Semester 4 Live</span>
          </div>
          <h1 className="text-2xl font-bold">Apex Institute of Technology & Management</h1>
          <p className="text-sky-100 text-xs mt-1">Autonomous University System • NAAC A++ Accredited</p>
        </div>
        <div className="bg-white/10 px-4 py-3 rounded-xl text-right">
          <div className="text-xs text-sky-200">System Security & Compliance</div>
          <div className="text-sm font-bold text-emerald-300 flex items-center justify-end space-x-1.5 mt-0.5">
            <CheckCircle className="w-4 h-4 text-emerald-400" />
            <span>100% Audit Verified</span>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        {stats.map((s, idx) => {
          const Icon = s.icon;
          return (
            <div key={idx} className="bg-white rounded-xl p-5 border border-slate-200 shadow-sm">
              <div className="flex items-center justify-between">
                <div className={`p-2.5 rounded-lg ${s.bg}`}>
                  <Icon className={`w-5 h-5 ${s.color}`} />
                </div>
                <span className="text-xs font-semibold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-full flex items-center">
                  <ArrowUpRight className="w-3 h-3 mr-0.5" />
                  {s.change}
                </span>
              </div>
              <div className="mt-3">
                <div className="text-2xl font-extrabold text-slate-800">{s.value}</div>
                <div className="text-xs text-slate-500 mt-0.5 font-medium">{s.label}</div>
              </div>
            </div>
          );
        })}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 bg-white rounded-xl p-5 border border-slate-200 shadow-sm space-y-4">
          <h3 className="font-bold text-sm text-slate-800 border-b border-slate-100 pb-3">Live Campus Operations & Academic Status</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            <div className="p-3.5 rounded-lg bg-slate-50 border border-slate-200">
              <div className="text-xs font-semibold text-slate-700">Today's Class Schedule (CS Dept)</div>
              <div className="text-xs text-slate-500 mt-1">CS401: Distributed Systems (RM-101)</div>
              <div className="mt-2 flex items-center justify-between text-[11px]">
                <span className="text-emerald-700 font-bold bg-emerald-100 px-2 py-0.5 rounded">Attendance: 94.2%</span>
                <span className="text-slate-400">09:00 - 10:00 AM</span>
              </div>
            </div>
            <div className="p-3.5 rounded-lg bg-slate-50 border border-slate-200">
              <div className="text-xs font-semibold text-slate-700">Campus Transport Fleet</div>
              <div className="text-xs text-slate-500 mt-1">12 Buses On Route • GPS Live</div>
              <div className="mt-2 flex items-center justify-between text-[11px]">
                <span className="text-sky-700 font-bold bg-sky-100 px-2 py-0.5 rounded">All Routes On Time</span>
                <span className="text-slate-400">ETA: 08:45 AM</span>
              </div>
            </div>
          </div>
        </div>

        <div className="bg-white rounded-xl p-5 border border-slate-200 shadow-sm space-y-4">
          <h3 className="font-bold text-sm text-slate-800 border-b border-slate-100 pb-3">AI Predictive Insights</h3>
          <div className="space-y-3">
            <div className="p-3 rounded-lg bg-indigo-50 border border-indigo-100">
              <div className="text-xs font-bold text-indigo-950">Student Dropout Risk: Minimal (1.6%)</div>
              <p className="text-[11px] text-slate-600 mt-1">Retention model indicates optimal engagement across all engineering branches.</p>
            </div>
            <div className="p-3 rounded-lg bg-emerald-50 border border-emerald-100">
              <div className="text-xs font-bold text-emerald-950">Fee Collection Forecast: 94.8%</div>
              <p className="text-[11px] text-slate-600 mt-1">Automated reminders projected to collect remaining dues smoothly.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};''')

    write_f("frontend/src/components/DataModuleView.tsx", '''import React, { useState, useEffect } from "react";
import { Plus, Download, Search, RefreshCw } from "lucide-react";
import { fetchApi } from "../services/api";

export const DataModuleView = ({ moduleName, title, description, endpoint }: any) => {
  const [data, setData] = useState<any[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [search, setSearch] = useState<string>("");

  useEffect(() => {
    async function loadData() {
      setLoading(true);
      const res = await fetchApi(endpoint);
      if (Array.isArray(res)) setData(res);
      else if (res && typeof res === "object") setData([res]);
      else setData([]);
      setLoading(false);
    }
    loadData();
  }, [endpoint]);

  return (
    <div className="space-y-4">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
        <div>
          <h2 className="text-lg font-bold text-slate-800">{title}</h2>
          <p className="text-xs text-slate-500 mt-0.5">{description}</p>
        </div>
        <div className="flex items-center space-x-2">
          <button className="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg border border-slate-200 text-xs font-semibold text-slate-600 hover:bg-slate-50">
            <Download className="w-3.5 h-3.5" />
            <span>Export CSV</span>
          </button>
          <button className="flex items-center space-x-1.5 px-3.5 py-1.5 rounded-lg bg-sky-600 hover:bg-sky-700 text-xs font-semibold text-white">
            <Plus className="w-3.5 h-3.5" />
            <span>Add Record</span>
          </button>
        </div>
      </div>

      <div className="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
        <div className="p-3.5 border-b border-slate-200 flex items-center justify-between gap-3">
          <div className="relative flex-1 max-w-sm">
            <Search className="w-3.5 h-3.5 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              placeholder={`Filter ${moduleName}...`}
              className="w-full bg-slate-50 border border-slate-200 pl-8 pr-3 py-1.5 rounded-lg text-xs focus:outline-none focus:ring-1 focus:ring-sky-500"
            />
          </div>
          <span className="text-xs text-slate-400 font-medium">{data.length} records active</span>
        </div>

        <div className="overflow-x-auto">
          {loading ? (
            <div className="p-8 text-center text-xs text-slate-400 flex items-center justify-center space-x-2">
              <RefreshCw className="w-4 h-4 animate-spin text-sky-500" />
              <span>Fetching live records from ERP database...</span>
            </div>
          ) : data.length === 0 ? (
            <div className="p-8 text-center text-xs text-slate-400">No records found. Click "Add Record" to create one.</div>
          ) : (
            <table className="w-full text-left text-xs">
              <thead className="bg-slate-50 text-slate-700 font-semibold border-b border-slate-200">
                <tr>
                  {Object.keys(data[0]).map((k) => (
                    <th key={k} className="py-2.5 px-4 capitalize">{k.replace(/_/g, ' ')}</th>
                  ))}
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100 text-slate-700">
                {data.map((row, idx) => (
                  <tr key={idx} className="hover:bg-slate-50 transition-colors">
                    {Object.values(row).map((val: any, cIdx) => (
                      <td key={cIdx} className="py-2.5 px-4">
                        {typeof val === "object" ? JSON.stringify(val) : String(val)}
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      </div>
    </div>
  );
};''')

    write_f("frontend/src/App.tsx", '''import React, { useState } from "react";
import { OneClickLoginBar, DEMO_USERS } from "./components/OneClickLoginBar";
import { Sidebar } from "./components/Sidebar";
import { Header } from "./components/Header";
import { DashboardView } from "./components/DashboardView";
import { DataModuleView } from "./components/DataModuleView";

export function App() {
  const [currentUser, setCurrentUser] = useState(DEMO_USERS[0]);
  const [activeTab, setActiveTab] = useState("dashboard");

  const handleSelectRole = (roleData: any) => {
    setCurrentUser(roleData);
  };

  const renderContent = () => {
    switch (activeTab) {
      case "dashboard":
        return <DashboardView userRole={currentUser.role} />;
      case "students":
        return <DataModuleView moduleName="Students" title="Student Information & Lifecycle" description="Manage active students, academic history, roll numbers, and enrollment records." endpoint="/students/" />;
      case "academics":
        return <DataModuleView moduleName="Courses" title="Curriculum, Courses & Timetable" description="Academic course catalogs, semester credits, faculty assignments, and schedules." endpoint="/academics/courses" />;
      case "attendance":
        return <DataModuleView moduleName="Attendance" title="Smart Attendance Engine Logs" description="Biometric smart gate scans, QR code validations, and subject attendance records." endpoint="/attendance/logs" />;
      case "examinations":
        return <DataModuleView moduleName="Examinations" title="Examination Schedules & Hall Allocations" description="Midterm and end-semester timetables, invigilators, and grade points." endpoint="/examinations/schedules" />;
      case "fees":
        return <DataModuleView moduleName="Fee Invoices" title="Fees, Invoicing & Billing Engine" description="Tuition fee structures, installments, concessions, and paid receipts." endpoint="/fees/invoices" />;
      case "finance":
        return <DataModuleView moduleName="Chart of Accounts" title="Finance & General Ledger" description="Standard double-entry chart of accounts, debits, credits, and trial balance." endpoint="/finance/chart-of-accounts" />;
      case "hr":
        return <DataModuleView moduleName="Employees" title="HR & Employee Directory" description="Faculty and non-teaching employee profiles, contracts, and leave balances." endpoint="/hr/employees" />;
      case "library":
        return <DataModuleView moduleName="Library Catalog" title="Central Library MARC21 / ISBN Catalog" description="Book titles, authors, shelf locations, RFID barcodes, and copy availability." endpoint="/library/books" />;
      case "hostels":
        return <DataModuleView moduleName="Hostel Rooms" title="Hostel, Housing & Bed Allocation" description="Residence blocks, room numbers, occupancy, and air-conditioning status." endpoint="/hostels/rooms" />;
      case "transport":
        return <DataModuleView moduleName="Bus Routes" title="Transport Fleet & Live GPS Routes" description="Bus route schedules, stops, driver contacts, and real-time coordinates." endpoint="/transport/routes" />;
      case "inventory":
        return <DataModuleView moduleName="Purchase Orders" title="Procurement & Purchase Orders" description="Requisitions, vendor RFQs, purchase orders, and goods receipt tracking." endpoint="/procurement/purchase-orders" />;
      case "workflows":
        return <DataModuleView moduleName="Workflows" title="Multi-Tier Approval Workflow Engine" description="Configurable purchase, leave, and admission approval pipelines." endpoint="/workflows/pending" />;
      case "ai":
        return <DataModuleView moduleName="AI Insights" title="AI / ML Predictive Intelligence" description="Automated dropout risk prediction, fee collection forecast, and workload analytics." endpoint="/ai/insights" />;
      case "compliance":
        return <DataModuleView moduleName="Audit Logs" title="Compliance & Immutable Audit Logs" description="Immutable audit trail of all transactions, timestamps, and actor IP addresses." endpoint="/compliance/audit-logs" />;
      case "organization":
        return <DataModuleView moduleName="Campuses" title="Multi-Campus Facilities & Infrastructure" description="Institution campuses, engineering blocks, lecture halls, and laboratories." endpoint="/organization/campuses" />;
      default:
        return <DashboardView userRole={currentUser.role} />;
    }
  };

  return (
    <div className="min-h-screen flex flex-col bg-slate-100 text-slate-900 font-sans">
      <OneClickLoginBar onSelectRole={handleSelectRole} activeRole={currentUser.role} />
      <div className="flex flex-1">
        <Sidebar activeTab={activeTab} setActiveTab={setActiveTab} userRole={currentUser.role} />
        <div className="flex-1 flex flex-col min-w-0">
          <Header user={currentUser} />
          <main className="flex-1 p-6 overflow-y-auto max-w-7xl w-full mx-auto">
            {renderContent()}
          </main>
        </div>
      </div>
    </div>
  );
}

export default App;''')

    write_f("frontend/src/main.tsx", '''import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);''')

if __name__ == '__main__':
    write_fe_src()
