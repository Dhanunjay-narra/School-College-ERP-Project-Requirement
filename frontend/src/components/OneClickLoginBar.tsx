import React from "react";
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
};
