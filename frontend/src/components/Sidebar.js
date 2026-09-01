import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
import { LayoutDashboard, GraduationCap, BookOpen, CalendarCheck, Award, DollarSign, Briefcase, Home, Bus, FileText, Cpu, ShieldCheck, Building2, Package, Layers } from "lucide-react";
export const Sidebar = ({ activeTab, setActiveTab }) => {
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
    return (_jsxs("aside", { className: "w-64 bg-slate-900 text-slate-300 flex flex-col shrink-0 border-r border-slate-800 min-h-[calc(100vh-45px)]", children: [_jsxs("div", { className: "p-4 border-b border-slate-800 flex items-center space-x-3", children: [_jsx("div", { className: "w-8 h-8 rounded bg-sky-600 flex items-center justify-center font-bold text-white", children: "ERP" }), _jsxs("div", { children: [_jsx("h2", { className: "font-bold text-sm text-white", children: "Apex Enterprise" }), _jsx("p", { className: "text-[11px] text-sky-400", children: "School & College ERP" })] })] }), _jsx("div", { className: "flex-1 overflow-y-auto py-3 px-2 space-y-1", children: menuItems.map((item) => {
                    const Icon = item.icon;
                    const isActive = activeTab === item.id;
                    return (_jsxs("button", { onClick: () => setActiveTab(item.id), className: `w-full flex items-center space-x-3 px-3 py-2 rounded-lg text-xs font-medium transition ${isActive ? "bg-sky-600 text-white font-semibold" : "text-slate-400 hover:text-white hover:bg-slate-800"}`, children: [_jsx(Icon, { className: `w-4 h-4 ${isActive ? "text-white" : "text-slate-400"}` }), _jsx("span", { children: item.label })] }, item.id));
                }) }), _jsx("div", { className: "p-3 border-t border-slate-800 text-[11px] text-slate-400 bg-slate-950/40", children: _jsxs("div", { className: "flex items-center justify-between", children: [_jsx("span", { children: "Version 1.0.0 (37 Phases)" }), _jsx("span", { className: "w-2 h-2 rounded-full bg-emerald-500 animate-pulse" })] }) })] }));
};
